"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: cf2ed3e8-aa55-4006-9d9a-355fd252e14b
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T11:07:35.063580Z'
    generation: 51
  topos:
    address: body/hands/infrastructure_gitops.py
    links: []
  telos:
    viral_factor: 0.0
    meme: infrastructure_gitops.py
"""
import os
import sys
import subprocess
import logging
import asyncio
import yaml
import fnmatch
from typing import List, Dict, Any
from pydantic import BaseModel, Field
import instructor
from openai import AsyncOpenAI
from dotenv import load_dotenv

# Ensure we can import from body
sys.path.append(os.getcwd())
from body.constants import DEFAULT_MODEL  # noqa: E402

# Load Env
load_dotenv()

# Setup Logging
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger("gitops")


class CommitMessage(BaseModel):
    """Structured commit message."""

    title: str = Field(
        ..., description="Conventional Commit title (e.g., 'feat: add gitops agent')"
    )
    description: str = Field(..., description="Detailed description of changes")
    emoji: str = Field(..., description="Relevant emoji for the change")


class GitOpsAgent:
    def __init__(self):
        self.api_key = os.getenv("OPENROUTER_API_KEY") or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            logger.warning("⚠️  No API Key found. LLM features will be disabled.")
            self.client = None
        else:
            self.client = instructor.from_openai(
                AsyncOpenAI(
                    base_url="https://openrouter.ai/api/v1",
                    api_key=self.api_key,
                ),
                mode=instructor.Mode.JSON,
            )
        self.model = DEFAULT_MODEL
        self.registry_path = "brain/registry.yaml"

    def run_command(self, command: str, check: bool = True) -> str:
        """Run a shell command and return output."""
        try:
            result = subprocess.run(
                command, shell=True, check=check, capture_output=True, text=True
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            logger.error(f"❌ Command failed: {command}")
            logger.error(f"Error: {e.stderr}")
            if check:
                raise
            return ""

    def get_status(self) -> List[str]:
        """Get list of changed files."""
        output = self.run_command("git status --porcelain")
        if not output:
            return []
        # Parse porcelain output (XY PATH)
        files = []
        for line in output.split("\n"):
            if len(line) > 3:
                files.append(line[3:])
        return files

    def load_registry(self) -> Dict[str, Any]:
        """Load the Holocron."""
        if not os.path.exists(self.registry_path):
            logger.warning("⚠️  Registry not found. Skipping Slop Check.")
            return {}
        with open(self.registry_path, "r") as f:
            return yaml.safe_load(f)

    def is_slop(self, file_path: str, registry: Dict[str, Any]) -> bool:
        """Check if a file is allowed by the registry."""
        if not registry:
            return False  # Fail open if registry missing

        # 1. Check Root
        if file_path in registry.get("root", []):
            return False

        # 2. Check Organs
        for organ, data in registry.get("organs", {}).items():
            organ_path = data.get("path", "")
            if file_path.startswith(organ_path):
                # Check contents patterns
                for pattern in data.get("contents", []):
                    # Simple glob match
                    if fnmatch.fnmatch(os.path.basename(file_path), pattern):
                        return False
                    # Also check if pattern is a directory
                    if pattern.endswith("/") and pattern.strip("/") in file_path:
                        return False
                # Check allowlist
                if os.path.basename(file_path) in data.get("allowlist", []):
                    return False

        return True

    def check_guards(self):
        """Run Hive Guards."""
        logger.info("🛡️  Running Hive Guards...")
        try:
            self.run_command("make guards")
            logger.info("✅ Guards Passed.")
        except subprocess.CalledProcessError:
            logger.error("❌ Guards Failed. Aborting GitOps.")
            raise Exception("Guards Failed")

    async def generate_commit_message(self, files: List[str]) -> CommitMessage:
        """Generate a semantic commit message using LLM."""
        if not self.client:
            return CommitMessage(
                title="chore: auto-commit",
                description="Automated commit by GitOps Agent (No LLM)",
                emoji="🤖",
            )

        # Get a summary of changes (limit to avoid context overflow)
        # If too many files, just send file list
        if len(files) > 10:
            diff_context = f"Files Changed ({len(files)}):\n" + "\n".join(files[:50])
        else:
            diff_context = self.run_command("git diff --stat")

        prompt = (
            "You are the GitOps Agent for Hive Fleet Obsidian.\n"
            "Generate a Conventional Commit message for the following changes.\n\n"
            f"{diff_context}\n\n"
            "Rules:\n"
            "1. Use Conventional Commits (feat, fix, docs, style, refactor, test, chore).\n"
            "2. Be concise but descriptive.\n"
            "3. Choose a relevant emoji."
        )

        return await self.client.chat.completions.create(
            model=self.model,
            response_model=CommitMessage,
            messages=[{"role": "user", "content": prompt}],
        )

    async def execute_cycle(self):
        """Run the full GitOps cycle."""
        logger.info("🦅 GitOps Agent Initialized (Gen 51).")

        # 1. Check Status
        files = self.get_status()
        if not files:
            logger.info("✨ Workspace is clean. Nothing to commit.")
            return

        file_count = len(files)
        logger.info(f"🔍 Found {file_count} changed files.")

        # 2. Slop Check
        registry = self.load_registry()
        slop_files = [f for f in files if self.is_slop(f, registry)]
        if slop_files:
            logger.warning(f"⚠️  Potential Slop Detected ({len(slop_files)} files):")
            for f in slop_files[:5]:
                logger.warning(f"   - {f}")
            if len(slop_files) > 5:
                logger.warning(f"   ... and {len(slop_files)-5} more.")
            # For now, we warn but proceed (Soft Governance)
            # raise Exception("Slop Detected")

        # 3. Run Guards
        self.check_guards()

        # 4. Stage Changes
        logger.info("📦 Staging changes...")
        self.run_command("git add .")

        # 5. Generate Commit Message
        logger.info("🧠 Generating semantic commit message...")
        try:
            commit = await self.generate_commit_message(files)
            full_message = f"{commit.emoji} {commit.title}\n\n{commit.description}\n\n[Generated by GitOps Agent]"
            logger.info(f"📝 Commit Message: {commit.title}")
        except Exception as e:
            logger.warning(f"⚠️  LLM Generation failed: {e}. Using fallback.")
            full_message = f"🛡️ Hive Guard: Auto-Commit via GitOps Agent\n\n{file_count} files changed."

        # 6. Commit
        # Escape quotes
        safe_message = full_message.replace('"', '"')
        try:
            self.run_command(f'git commit -m "{safe_message}"')
        except subprocess.CalledProcessError:
            logger.warning("⚠️  Commit failed (likely due to pre-commit hooks).")
            logger.info("🔄 Attempting to stage fixes and retry commit...")
            self.run_command("git add .")
            self.run_command(f'git commit -m "{safe_message}"')

        # 7. Push with Resilience

        # 7. Push with Resilience
        logger.info("☁️  Pushing to cloud...")
        try:
            self.run_command("git push origin main")
            logger.info("✅ Push Successful.")
        except subprocess.CalledProcessError:
            logger.warning("⚠️  Push failed. Attempting Pull --rebase...")
            try:
                self.run_command("git pull --rebase origin main")
                self.run_command("git push origin main")
                logger.info("✅ Push Successful after Rebase.")
            except subprocess.CalledProcessError:
                logger.error("❌ GitOps Failed. Manual intervention required.")
                raise


if __name__ == "__main__":
    agent = GitOpsAgent()
    asyncio.run(agent.execute_cycle())
