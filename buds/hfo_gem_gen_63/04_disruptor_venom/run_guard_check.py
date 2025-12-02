import sys
import os
from buds.hfo_gem_gen_63.carapace.guard_knowledge_structure import KnowledgeStructureGuard

def main():
    root_path = os.path.abspath("buds/hfo_gem_gen_63/brain")
    print(f"🛡️  Running Knowledge Structure Guard on: {root_path}")
    
    guard = KnowledgeStructureGuard(root_path)
    errors = guard.validate()
    
    if errors:
        print(f"❌ Found {len(errors)} Violations:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("✅ Structure is Valid (HFO Second Brain Compliant)")
        sys.exit(0)

if __name__ == "__main__":
    main()
