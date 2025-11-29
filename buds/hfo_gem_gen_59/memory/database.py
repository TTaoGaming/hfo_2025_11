import sqlite3
import json
import logging
from pathlib import Path
from typing import Optional, List
from ..blood.schema import MemoryItem, Level0Artifact, Level1Artifact, Level2Artifact

# Setup Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ScribeDB")

class IronLedger:
    """
    The Iron Ledger (SQLite).
    A portable, single-file, ACID-compliant database.
    It stores the 'Truth' of the repository.
    """
    def __init__(self, db_path: str = "buds/hfo_gem_gen_59/memory/hfo_gen_59_memory.db"):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_db()

    def _init_db(self):
        """Initialize the schema. Idempotent."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # The Memory Table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS memory_items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                source_path TEXT UNIQUE NOT NULL,
                content TEXT NOT NULL,
                content_hash TEXT NOT NULL,
                generation INTEGER NOT NULL,
                category TEXT NOT NULL,
                tags TEXT,  -- JSON list
                vectorized BOOLEAN DEFAULT 0,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Migration: Add vectorized column if it doesn't exist
        try:
            cursor.execute("ALTER TABLE memory_items ADD COLUMN vectorized BOOLEAN DEFAULT 0")
        except sqlite3.OperationalError:
            pass # Column likely exists

        # The Level 0 Artifacts (8 PREY Agents)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS level0_artifacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                source_hash TEXT NOT NULL,
                agent_id INTEGER NOT NULL,
                model_used TEXT NOT NULL,
                pillars_json TEXT NOT NULL, -- Stores the 8 pillars as JSON
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(source_hash) REFERENCES memory_items(content_hash)
            )
        """)

        # The Level 1 Artifacts (Byzantine Quorum)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS level1_artifacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                source_hash TEXT NOT NULL,
                consensus_score REAL,
                synthesis TEXT NOT NULL,
                resolved_conflicts TEXT, -- JSON list
                model_used TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(source_hash) REFERENCES memory_items(content_hash)
            )
        """)
        
        # The Vector Pointer Table (Future Proofing)
        # We don't store vectors here, we just link to them.
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS vector_refs (
                memory_id INTEGER,
                vector_id TEXT,
                store_type TEXT,
                FOREIGN KEY(memory_id) REFERENCES memory_items(id)
            )
        """)
        
        conn.commit()
        conn.close()

    def insert(self, item: MemoryItem) -> int:
        """
        Insert a validated MemoryItem.
        Returns the Row ID.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        try:
            # Ensure hash is computed
            if not item.content_hash:
                item.compute_hash()

            cursor.execute("""
                INSERT OR REPLACE INTO memory_items 
                (source_path, content, content_hash, generation, category, tags, timestamp)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                item.source_path,
                item.content,
                item.content_hash,
                item.generation,
                item.category,
                json.dumps(item.tags),
                item.timestamp.isoformat()
            ))
            
            row_id = cursor.lastrowid
            conn.commit()
            logger.info(f"✅ Scribed: {item.source_path} (Gen {item.generation})")
            return row_id
            
        except Exception as e:
            logger.error(f"❌ Scribe Failed: {e}")
            conn.rollback()
            raise
        finally:
            conn.close()

    def insert_level0(self, artifact: Level0Artifact) -> int:
        """
        Insert a Level 0 Artifact from a PREY Agent.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Serialize the 8 pillars
        pillars_data = {
            "ontos": artifact.ontos.model_dump(),
            "logos": artifact.logos.model_dump(),
            "telos": artifact.telos.model_dump(),
            "chronos": artifact.chronos.model_dump(),
            "pathos": artifact.pathos.model_dump(),
            "ethos": artifact.ethos.model_dump(),
            "topos": artifact.topos.model_dump(),
            "nomos": artifact.nomos.model_dump(),
        }
        
        try:
            cursor.execute("""
                INSERT INTO level0_artifacts 
                (source_hash, agent_id, model_used, pillars_json, timestamp)
                VALUES (?, ?, ?, ?, ?)
            """, (
                artifact.source_hash,
                artifact.agent_id,
                artifact.model_used,
                json.dumps(pillars_data),
                artifact.timestamp.isoformat()
            ))
            
            row_id = cursor.lastrowid
            conn.commit()
            logger.info(f"🕷️ Agent {artifact.agent_id} filed comprehensive artifact.")
            return row_id
            
        except Exception as e:
            logger.error(f"❌ Level 0 Insert Failed: {e}")
            conn.rollback()
            raise
        finally:
            conn.close()

    def insert_level1(self, artifact: Level1Artifact) -> int:
        """
        Insert a Level 1 Artifact (Quorum Result).
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        try:
            cursor.execute("""
                INSERT INTO level1_artifacts 
                (source_hash, consensus_score, synthesis, resolved_conflicts, model_used, timestamp)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                artifact.source_hash,
                artifact.consensus_score,
                artifact.synthesis,
                json.dumps(artifact.resolved_conflicts),
                artifact.model_used,
                artifact.timestamp.isoformat()
            ))
            
            row_id = cursor.lastrowid
            conn.commit()
            logger.info(f"🦅 Quorum Reached! Level 1 Artifact minted (Score: {artifact.consensus_score}).")
            return row_id
            
        except Exception as e:
            logger.error(f"❌ Level 1 Insert Failed: {e}")
            conn.rollback()
            raise
        finally:
            conn.close()

    def insert_level2(self, artifact: Level2Artifact) -> int:
        """
        Insert a Level 2 Artifact (Recursive Reduction).
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        try:
            # Ensure table exists (Migration on the fly)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS level2_artifacts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    source_hash TEXT NOT NULL,
                    synthesis TEXT NOT NULL,
                    constituent_hashes TEXT NOT NULL, -- JSON list
                    model_used TEXT NOT NULL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY(source_hash) REFERENCES memory_items(content_hash)
                )
            """)

            cursor.execute("""
                INSERT INTO level2_artifacts 
                (source_hash, synthesis, constituent_hashes, model_used, timestamp)
                VALUES (?, ?, ?, ?, ?)
            """, (
                artifact.source_hash,
                artifact.synthesis,
                json.dumps(artifact.constituent_hashes),
                artifact.model_used,
                artifact.timestamp.isoformat()
            ))
            
            row_id = cursor.lastrowid
            conn.commit()
            logger.info(f"🪐 Fractal Synthesis! Level 2 Artifact minted.")
            return row_id
            
        except Exception as e:
            logger.error(f"❌ Level 2 Insert Failed: {e}")
            conn.rollback()
            raise
        finally:
            conn.close()

    def get_level0_artifacts(self, source_hash: str) -> List[tuple]:
        """Retrieve all Level 0 artifacts for a given source hash."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM level0_artifacts WHERE source_hash = ?", (source_hash,))
        rows = cursor.fetchall()
        conn.close()
        return rows

    def get_unvectorized_items(self, limit: int = 100) -> List[tuple]:
        """
        Get items that haven't been vectorized yet.
        Returns list of (id, content, source_path, category).
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, content, source_path, category 
            FROM memory_items 
            WHERE vectorized = 0 
            LIMIT ?
        """, (limit,))
        rows = cursor.fetchall()
        conn.close()
        return rows

    def mark_vectorized(self, memory_id: int):
        """Mark an item as vectorized."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("UPDATE memory_items SET vectorized = 1 WHERE id = ?", (memory_id,))
        conn.commit()
        conn.close()

    def reset_vectorized_flags(self):
        """
        PHOENIX PROTOCOL: Reset all vectorized flags to 0.
        This forces the Assimilator to re-process everything.
        Used when the VectorDB is wiped or corrupted.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("UPDATE memory_items SET vectorized = 0")
        rows = cursor.rowcount
        conn.commit()
        conn.close()
        logger.warning(f"🔥 PHOENIX PROTOCOL: Reset {rows} items to unvectorized state.")
        return rows

    def get_stats(self) -> dict:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT generation, COUNT(*) FROM memory_items GROUP BY generation")
        stats = dict(cursor.fetchall())
        conn.close()
        return stats

    def is_processed(self, content_hash: str) -> bool:
        """Check if a content hash already exists in the ledger."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM memory_items WHERE content_hash = ?", (content_hash,))
        exists = cursor.fetchone() is not None
        conn.close()
        return exists
