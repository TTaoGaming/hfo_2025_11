---
hexagon:
  ontos:
    id: 4f72fc90-68fb-481a-a845-0cd2d000e9a6
    type: md
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T11:07:35.873748Z'
    generation: 51
  topos:
    address: eyes/archive/hfo_gem/gen_22/gen_22_swarmlord_chat.md
    links: []
  telos:
    viral_factor: 0.0
    meme: gen_22_swarmlord_chat.md
---
# Gen22 — Swarmlord Chat (Repo-as-Chat)

BLUF: Use the repo itself as the chat surface. Author from phone via GitHub Mobile, write to a daily Markdown file with wake word “Obsidian ”, and let an always-on bridge on your machine run PREY lanes, append blackboard receipts, and mirror to DuckDB. This keeps safety, receipts, and model allowlist intact while giving you mobile control.

## What “repo-as-chat” means

- Chat surface: `swarmlord_chat/Swarmlord_of_Webs_Chat_YYYY-MM-DD.md` (daily file). Lines starting with “Obsidian ” are user intents.
- Bridge: a small always-on process pulls new repo edits, reads the daily file, filters triggers, and routes intents to runners.
- Orchestrators: existing Crew AI pilot and ARC swarm runners execute PREY lanes in parallel, with receipts and spans.
- Evidence: all material actions write to the blackboard JSONL and DuckDB mirrors for audit and stigmergy.

## Current assets (already in this repo)

- Chat watcher: `scripts/swarmlord/chat_log_watcher.py` (start-of-line wake word, bot recursion guard, JSONL + DuckDB mirrors).
- Blackboard receipts: `hfo_blackboard/obsidian_synapse_blackboard.jsonl` (append-only JSONL with evidence_refs).
- DuckDB mirror: `swarmlord_chat/swarmlord.duckdb` with tables `chats`, `inbox`.
- Crew AI pilot: `scripts/crew_ai/runner_unified.py` with PREY lanes, receipts, and allowlisted models via OpenRouter.
- ARC swarm: `scripts/crew_ai/arc_swarm_runner.py` and one-click `scripts/crew_ai/auto_arc_limit50.sh`.
- Trace analysis: `scripts/crew_ai/analyze_traces.py` to verify parallelism.

## Mobile workflow (GitHub Mobile or Telegram)

- Edit the day’s Markdown chat file from your phone; begin commands with the wake word.
- Examples
  - obsidian plan day
  - obsidian work on gesture controls
  - obsidian clean fifteen
  - obsidian arc fifty
- Wake word normalization (2025-11-02): start-of-line `obsidian` (case-insensitive) followed by optional space/colon/EOF.
- Replies are appended by the bridge and must not begin with the wake word (recursion guard). The bridge mirrors chats to `swarmlord_chat/chat.jsonl` and to DuckDB.

### Telegram bridge (optional)

- Authoritative IO: Telegram is authoritative by default — the Chat Log Watcher neither mirrors replies nor launches consults for Telegram‑originated messages (`SWARM_TELEGRAM_AUTHORITATIVE=1`).
- Minimal bot: `scripts/swarmlord/telegram_bot.py` (long polling) logs inbox events and launches consults.
- Mature bot (optional): `scripts/swarmlord/telegram_bot_ptb.py` using python‑telegram‑bot; enable via `SWARM_TELEGRAM_PTB=1`.
- Idempotency: message‑id based dedupe; old re‑deliveries are ignored. Offline gating limits “LLM offline” notices to once per 5 minutes per chat.
- Path alignment: both bot and watcher point to the same chat file. In dual‑repo mode, set `SWARM_PRIVATE_ROOT` and they will use `<private>/SWARMLORD_CHATLOG.md`.
- Start (local): `ops/dual_repo/run_bridge.sh` (starts bot + watcher + mirror). Use `make swarmlord-restart` to normalize with pre‑clean.

## Always-on bridge (expected behavior)

- Runs continuously on a home server, laptop-on-dock, or a small VPS.
- Watches or periodically pulls the repo (or consumes webhooks) and tails the daily chat file.
- On each trigger line:
  - Parse intent → map to a handler (pilot, ARC sanity, planner, or state update).
  - Execute PREY under bounded Engage (allowlisted models, token caps, retry-on-empty as needed).
  - Append receipts with evidence_refs (paths to artifacts, spans, reports).
  - Write a human reply to the chat file (≤200 lines per write) and mirror to DuckDB and Telegram (if configured).

## Active chat file (private root)

- Single entry point recommended: `<SWARM_PRIVATE_ROOT>/SWARMLORD_CHATLOG.md`.
- The repository may also contain a local `SWARMLORD_CHATLOG.md` for quick typing; treat the private root file as the source of truth for the bridge.

## Ops helpers (paths and env)

- Bridge launcher: `ops/dual_repo/run_bridge.sh` — exports `HFO_ROOT`, aligns chat/JSON/DB paths, exports `.env` with `set -a`, supports PTB via `SWARM_TELEGRAM_PTB=1`.
- Telegram bot launcher: `ops/dual_repo/run_telegram_bot.sh` — sources `.env` (root or ops) and writes startup paths to `temp/otel/telegram.log`.
- Pre‑clean: `scripts/swarmlord/start_all.sh` stops stray bot/watcher/mirror processes before starting the bridge (enabled by default with `SWARM_PRECLEAN=1`).

## Intents → actions (canonical set)

- plan day
  - Perceive: read mission intent for the day; collect context notes.
  - React: propose time blocks and MITs; set chunk limits and tripwires.
  - Engage: write a mini plan to chat; optionally update a StateStore topic.
  - Yield: append blackboard receipt; ask Swarmlord to Verify.
- work on <topic>
  - Perceive: set current_topic; load recent evidence.
  - React: outline checklist; emit stigmergy signal recruit(topic,+1) with TTL.
  - Engage: perform one bounded step; log evidence_refs.
  - Yield: summarize and set next micro-step.
- clean fifteen
  - Timer-oriented nudge with start/finish markers and a short review.
- arc fifty
  - Route to ARC sanity runner (limit=50), then summarize metrics to chat and receipts.

## PREY + receipts contract (tiny)

- Inputs: mission intent, daily chat file path, allowlisted model hint, safety limits.
- Outputs: artifacts (code/docs/config), blackboard receipts, per-lane artifacts, optional digest.
- Safety: ≤200 lines per write; no placeholders; tripwires active; explicit revert on FAIL.
- Verify: independent check must PASS before claiming persistent outcomes.

## Stigmergy (pilot scope)

- Signals: `{topic, signal_type: recruit|inhibit|sustain, strength, ttl_s, source, evidence_refs, timestamp}`.
- Storage: append to JSONL mirror and DuckDB table; decay by TTL; propose next actions when thresholds cross.

## Model and cost controls

- Allowlist: enforced in client (e.g., gpt-5-mini, grok-4-fast, deepseek-v3.2-exp, GPT-OSS 20B/120B, qwen3-235b…).
- Defaults: reasoning enabled for supported models; budgets bounded (token/timeout).
- Resiliency: retry on empty content; drop response_format on retry where needed.

## Edge cases to handle

- Conflicts in daily file from cross-device edits → resolve by keeping single source of truth per day and short commits.
- Bridge downtime → backlog processing on resume; idempotent handlers by evidence_hash and offsets.
- Missing API key → Engage emits spans with ok=false and content_preview=null; receipts still append.
- Large replies → enforce ≤200 lines; chunk if needed and append receipts per chunk.
- Telegram no-reply → ensure `last_chat_id` is present in `temp/swarmlord/telegram_state.json`. If missing, send any message to the bot to initialize, then restart the bridge.

## Minimal “how to operate” (human)

- Author from phone: open the day’s chat in GitHub Mobile, start a line with “Obsidian ”.
- Let the bridge do PREY and append receipts. Inspect runs in `hfo_crew_ai_swarm_results/YYYY-MM-DD/run-<ts>/`.
- For ARC sanity, use “Obsidian arc fifty” and check digest and metrics; receipts go to blackboard and DuckDB.

## Roadmap (grounded)

- Now (fast): keep file-watcher bridge; standardize the four intents above; ensure receipts include evidence_refs.
- Near-term: expose the bridge to phone via Tailscale/Cloudflare Tunnel; optionally add Open WebUI as a front-end that still writes to the same chat file and JSONL mirrors.
- Later: Dify/LangGraph Server “control room” with richer multi-agent orchestration while preserving receipts and gate policies.

## Decision helpers

- Do you want fully local-only or are cloud APIs via OpenRouter acceptable?
- Is voice required for v1, or can we layer STT/TTS after the base chat loop is steady?
- Can you keep a small always-on process running (home server or VPS), or should we lean on GitHub workflows and a self-hosted runner?

---

BLUF for grounding: Keep the repo as the chat surface today; the bridge maps wake-word lines to PREY intents, writes receipts to blackboard and DuckDB, and uses allowlisted models with strict budgets. Layer richer UI/voice later without changing the contract.

## Privacy deployment patterns (dual-repo split)

- Private operator repo (new, private):
  - swarmlord_chat/ (daily chat, JSONL, DuckDB)
  - hfo_blackboard/ (receipts JSONL)
  - hfo_crew_ai_swarm_results/ (lane artifacts)
  - temp/otel/ (traces)
- Public code repo (this repo):
  - Code, SSOT docs, and optional sanitized digests under `hfo_crew_ai_public_digests/YYYY-MM-DD/`.

Operating notes
- Edit chat from phone in the private repo via GitHub Mobile.
- The Chromebook bridge clones both repos, processes private chat, and appends private receipts.
- If publishing, push sanitized digests to the public repo only; never raw chat or secrets.

Helper assets
- Guide: `ops/dual_repo/README.md`
- Bootstrap script: `ops/dual_repo/private_repo_bootstrap.sh`
- Public digests folder: `hfo_crew_ai_public_digests/`
