"""
---
holon:
  id: hfo-91b45699
  type: unknown
  file: check_fitness.py
  status: active
---
"""
import sys
import os
from buds.hfo_gem_gen_63.carapace.guard_knowledge_structure import KnowledgeStructureGuard

def main():
    # Point to the Bud Root (hfo_gem_gen_63)
    bud_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    print(f"🛡️  Running Evo-Devo Fitness Function on: {bud_root}")
    
    guard = KnowledgeStructureGuard(bud_root)
    errors = guard.validate()
    
    if errors:
        print(f"❌ Fitness Check FAILED ({len(errors)} Violations):")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("✅ Fitness Check PASSED (System is Healthy)")
        sys.exit(0)

if __name__ == "__main__":
    main()
