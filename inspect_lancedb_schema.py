
import lancedb
import os
import sys

# Fix for OMP Error
os.environ["KMP_DUPLICATE_LIB_OK"] = "True"

DB_PATH = "buds/hfo_gem_gen_63/06_assimilator_memory/lancedb"

try:
    db = lancedb.connect(DB_PATH)
    print(f"📂 Tables: {db.table_names()}")
    
    for t_name in db.table_names():
        tbl = db.open_table(t_name)
        print(f"\n--- Table: {t_name} ---")
        print(f"Schema: {tbl.schema}")
        
        # Try to peek at data to see vector length
        df = tbl.head(1).to_pandas()
        if not df.empty and 'vector' in df.columns:
            vec = df.iloc[0]['vector']
            print(f"Vector Dim: {len(vec)}")
        else:
            print("No vector column or empty table.")

except Exception as e:
    print(f"❌ Error: {e}")
