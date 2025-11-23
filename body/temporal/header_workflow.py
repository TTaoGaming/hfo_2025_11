from datetime import timedelta
from temporalio import activity, workflow
from temporalio.common import RetryPolicy
from body.config import Config


@activity.defn
async def run_header_swarm_activity(file_path_str: str) -> str:
    """
    Executes the Header Swarm to crystallize a file.
    """
    from pathlib import Path
    from body.hands.header_swarm import HeaderSwarm
    import yaml

    path = Path(file_path_str)
    if not path.exists():
        return f"❌ File not found: {path}"

    try:
        swarm = HeaderSwarm(path)
        header = await swarm.generate_header()

        # Write back to file (Logic moved from main_async to here)
        # Reconstruct YAML
        face_dict = header.face.model_dump()
        hexagon_dict = header.hexagon.model_dump()
        face_dict["hexagon"] = hexagon_dict

        new_yaml = yaml.dump(face_dict, sort_keys=False, allow_unicode=True)

        # Add comments
        new_yaml = new_yaml.replace(
            "hexagon:",
            "\n# ==================================================================\n# 🤖 THE HEXAGON (Swarm Generated)\n# ==================================================================\nhexagon:",
        )

        # Read original body
        content = path.read_text(encoding="utf-8")
        parts = content.split("---", 2)
        if len(parts) >= 3:
            body = parts[2]
        else:
            body = content  # Fallback if no frontmatter

        new_content = f"---\n{new_yaml}---\n{body}"
        path.write_text(new_content, encoding="utf-8")

        return f"✅ Swarm Crystallization Complete: {path}"

    except Exception as e:
        return f"❌ Error during swarm execution: {str(e)}"


@workflow.defn
class HeaderSwarmWorkflow:
    @workflow.run
    async def run(self, file_path_str: str) -> str:
        return await workflow.execute_activity(
            run_header_swarm_activity,
            file_path_str,
            start_to_close_timeout=timedelta(seconds=Config.SWARM_TIMEOUT),
            retry_policy=RetryPolicy(
                initial_interval=timedelta(seconds=5),
                maximum_interval=timedelta(seconds=60),
                maximum_attempts=3,
            ),
        )
