import unittest
import shutil
import os
from buds.hfo_gem_gen_59.memory.database import IronLedger
from buds.hfo_gem_gen_59.blood.schema import MemoryItem
from buds.hfo_gem_gen_59.brain.assimilator import Assimilator
from buds.hfo_gem_gen_59.brain.bridger_oracle import BridgerOracle

class TestBridgerOracle(unittest.TestCase):
    def setUp(self):
        self.test_db_path = "buds/hfo_gem_gen_59/tests/temp_oracle_memory.db"
        self.test_lancedb_path = "buds/hfo_gem_gen_59/tests/temp_oracle_lancedb"
        
        if os.path.exists(self.test_db_path):
            os.remove(self.test_db_path)
        if os.path.exists(self.test_lancedb_path):
            shutil.rmtree(self.test_lancedb_path)

    def tearDown(self):
        if os.path.exists(self.test_db_path):
            os.remove(self.test_db_path)
        if os.path.exists(self.test_lancedb_path):
            shutil.rmtree(self.test_lancedb_path)

    def test_oracle_retrieval(self):
        # 1. Seed Data
        assimilator = Assimilator(db_path=self.test_db_path, lancedb_path=self.test_lancedb_path)
        
        docs = [
            ("The Swarmlord is the apex commander.", "bio/swarmlord.md"),
            ("Disruptors are the red team adversaries.", "bio/disruptor.md"),
            ("The Hive Mind connects all creatures.", "bio/hive_mind.md")
        ]
        
        for content, path in docs:
            item = MemoryItem(source_path=path, content=content, generation=59, category="bio")
            assimilator.ledger.insert(item)
            
        # 2. Assimilate
        assimilator.run_sync_cycle()
        
        # 3. Ask Oracle
        oracle = BridgerOracle(lancedb_path=self.test_lancedb_path)
        
        # Query 1: Swarmlord
        results = oracle.ask("Who is the commander?")
        self.assertTrue(len(results) > 0)
        self.assertIn("Swarmlord", results[0]['text'])
        
        # Query 2: Disruptors
        results = oracle.ask("Who is the adversary?")
        self.assertTrue(len(results) > 0)
        self.assertIn("Disruptors", results[0]['text'])
        
        print("✅ Test Passed: Bridger Oracle retrieved correct memories.")

if __name__ == '__main__':
    unittest.main()
