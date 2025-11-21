# Rescue Plan — Mission Intents and Gen Docs to Main (Gen24)

BLUF
- Enumerate divergent branches, identify mission intents and Gen* docs that are not in main, verify they meet guards, then merge or re-house to archive with provenance.
- Prefer scripted, idempotent steps and append receipts for every material action.

## Scope
- Targets
  - hfo_mission_intent/YYYY-MM-DD/* (non-archive)
  - hfo_gem/gen_*/**/*.md, **/*.yml (notably gen_21, gen_23, gen_24)
  - AGENTS.md, ops/dual_repo/* if divergent
- Non-targets
  - temp/, .ipynb_checkpoints/, large binaries

## Preconditions and guardrails
- Mission intent precondition: ≥3 clarification passes for same date; else set hallucination_flag and move to archive/.
- Single-active-per-timeframe (day): duplicates moved to archive/ and flagged.
- Chunk limit ≤200 lines per write; no placeholders; append-only blackboard receipts.

## Steps (scriptable)
1) Enumerate branches
   - Local: git branch --list
   - Remote: git branch -r | sed 's#origin/##'
2) For each candidate branch B
   - Diff paths against main for targets above
   - Collect changed/added files and compute simple metadata (lines, sha256, date in path)
3) Validate mission intents
   - Check date bucket, required keys, clarification_pass_refs count and existence
   - If invalid: move to hfo_mission_intent/archive/<same-date>/ with hallucination_flag: true note
4) Stage rescue into a staging branch
   - Create rescue/<date>-<shortid> from main
   - Copy validated files into place preserving paths
   - Add provenance header at top of each rescued doc (branch, commit, sha, date)
5) Verify
   - If runs are included, ensure latest attempt_* per lane has core artifacts (perception/react/engage/yield)
   - Run quorum_plus on the run directory; confirm PASS
   - Lint JSON/JSONL and Mermaid
6) Merge to main via PR
   - Include Verify checklist, quorum+ summary if relevant, and receipts.

## Data model for provenance header
- YAML front-matter block at top of rescued docs (md/yml):
  - rescued_from_branch: <name>
  - rescued_from_commit: <sha>
  - rescued_at: <ISO 8601 Z>
  - original_path: <path-in-branch>
  - checksum_sha256: <hex>

## Minimal helper commands (optional)
- List missing in main (example target: mission intents on a date):
  - git ls-tree -r --name-only <branch> -- hfo_mission_intent/2025-10-*/ | grep -v archive/
  - git ls-tree -r --name-only main -- hfo_mission_intent/2025-10-*/ | grep -v archive/
  - comm -23 <(list-branch | sort) <(list-main | sort)
- Compute sha256 for a path:
  - sha256sum <file> | cut -d' ' -f1

## Receipts
- Per stage append receipts to hfo_blackboard/obsidian_synapse_blackboard.jsonl with evidence_refs to file paths and sha256.
- Example summary: "Rescued 4 intents and 2 gen docs from feature/x into rescue/2025-11-06-ab12; 1 intent archived for precondition fail."

## Harvest pointers (if runs present)
- Index: hfo_crew_ai_swarm_results/YYYY-MM-DD/run-<ts>/RESCUE_INDEX.jsonl
- Summary: hfo_crew_ai_swarm_results/YYYY-MM-DD/run-<ts>/RESCUED_SUMMARY.md

## Rollback
- If Verify fails or policy trips: revert the staging branch, shrink scope, fix provenance, and re-run.

## Next steps
- Implement scripts/tools/rescue_scan.py to generate a candidate list with validations and checksums.
- Wire into CI: comment with a rescue report on PRs that propose mission intent/doc changes from non-main.
