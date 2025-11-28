import unittest
import shutil
import os
from pathlib import Path
from buds.hfo_gem_gen_59.memory.database import IronLedger
from buds.hfo_gem_gen_59.blood.schema import MemoryItem
from buds.hfo_gem_gen_59.brain.assimilator import Assimilator

class TestAssimilator(unittest.TestCase):
    def setUp(self):
        # Use a temporary DB path
        self.test_db_path = "buds/hfo_gem_gen_59/tests/temp_memory.db"
        self.test_lancedb_path = "buds/hfo_gem_gen_59/tests/temp_lancedb"
        
        # Clean up previous runs
        if os.path.exists(self.test_db_path):
            os.remove(self.test_db_path)
        if os.path.exists(self.test_lancedb_path):
            shutil.rmtree(self.test_lancedb_path)

        # Initialize components with test paths
        # Note: We need to patch the paths in the classes or pass them in __init__
        # Since I didn't make paths configurable in Assimilator __init__, I'll patch them or just rely on the classes using defaults if I can't change them easily.
        # Wait, I made them configurable in IronLedger and VectorMirror, but Assimilator instantiates them with defaults.
        # I should update Assimilator to accept paths or instances.
        pass

    def tearDown(self):
        # Cleanup
        if os.path.exists(self.test_db_path):
            os.remove(self.test_db_path)
        if os.path.exists(self.test_lancedb_path):
            shutil.rmtree(self.test_lancedb_path)

    def test_full_pipeline(self):
        # 1. Setup Custom Assimilator
        assimilator = Assimilator(db_path=self.test_db_path, lancedb_path=self.test_lancedb_path)
        
        # Insert a memory item
        item = MemoryItem(
            source_path="test/doc1.md",
            content="The Swarmlord directs the hive fleet.",
            generation=59,
            category="test"
        )
        assimilator.ledger.insert(item)
        
        # Verify it's unvectorized
        unvec = assimilator.ledger.get_unvectorized_items()
        self.assertEqual(len(unvec), 1)
        
        # 2. Run Assimilator Sync
        assimilator.run_sync_cycle()
        
        # 3. Verify it's now vectorized in SQLite
        unvec_after = assimilator.ledger.get_unvectorized_items()
        self.assertEqual(len(unvec_after), 0)
        
        # 4. Verify it's in LanceDB
        # We need to search for it
        # Get embedding for query
        query_vec = assimilator.motor.embed(["Swarmlord"])[0]
        results = assimilator.mirror.search(query_vec, limit=1)
        
        self.assertFalse(results.empty)
        self.assertEqual(results.iloc[0]['text'], "The Swarmlord directs the hive fleet.")
        print("✅ Test Passed: Pipeline synced successfully.")

if __name__ == '__main__':
    unittest.main()
