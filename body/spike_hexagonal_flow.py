"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: f127000a-a0b5-4667-b532-d124149d124e
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T11:07:34.885130Z'
    generation: 51
  topos:
    address: body/spike_hexagonal_flow.py
    links: []
  telos:
    viral_factor: 0.0
    meme: spike_hexagonal_flow.py

    hexagon:
      ontos:
        id: 5d2d98d6-4e9a-4a3c-aeae-b66cd6362075
        type: code
        owner: Genesis.Factory
        version: 1.0.0
      telos:
        meme: Spike Hexagonal Flow
        bluf: "This spike verifies the end-to-end lifecycle of a Hexagonal Holon.\n  It\
          \ tests the transition from Crystalline (Code) to Liquid (Signal) to Sedimentary\
          \ (DB)."
        viral_factor: 0.5
        intent_hash: acfc7f4508616f9b6648964a79bcc787a760d700b554d7e4edbc1b880121138e
      chronos:
        created: '2025-11-23T08:05:54.399283Z'
        last_touched: '2025-11-23T08:05:54.399290Z'
        status: active
        urgency: 0.8
        decay: 0.1
      topos:
        address: 1.X.spike_hexagonal_flow
        links: []
        location: body/spike_hexagonal_flow.py
      logos:
        schema_v: '1.0'
        signature: sig_bcdbeb05
        validators:
        - hive_guard_v1
        - genesis_integrity_check
      pathos:
        sentiment: neutral
        quality_score: 100.0
        review_status: pending_consensus
"""

# 🛡️ HIVE GUARD: ACTIVE
# ---------------------
# This file is protected by the Hive Fleet Obsidian Immunizer.
# Any manual changes to the header may be overwritten by the Genesis Protocol.
#
# INTENT SOURCE: Spike Hexagonal Flow

from rich.console import Console
from body.models.hexagon import Hexagon, Ontos, Telos, Chronos, Topos, HolonType

console = Console()


def implementation():
    """
    Executes the Shapeshifter Test: Crystalline -> Liquid -> Sedimentary.
    """
    console.print("[bold purple]🧪 Executing Spike: Hexagonal Flow[/bold purple]")

    # 1. Forge (Crystalline)
    console.print(
        "\n[bold blue]1. Forging Hexagonal Holon (Crystalline State)...[/bold blue]"
    )
    holon = Hexagon(
        ontos=Ontos(type=HolonType.MISSION, owner="Swarmlord"),
        telos=Telos(meme="Tracer Bullet", bluf="Verify the flow"),
        chronos=Chronos(urgency=0.9),
        topos=Topos(address="1.0.0"),
    )
    console.print(f"  ✅ Created Holon: [cyan]{holon.ontos.id}[/cyan]")
    console.print(f"  ✅ Urgency: [yellow]{holon.chronos.urgency}[/yellow]")

    # 2. Adapt to Liquid (Signal)
    console.print(
        "\n[bold blue]2. Adapting to Liquid State (NATS Signal)...[/bold blue]"
    )
    signal = holon.to_signal(payload={"target": "alpha"})
    console.print(f"  ✅ Signal Type: [green]{signal['type']}[/green]")
    console.print(f"  ✅ Signal Source: [green]{signal['source']}[/green]")

    # Verify Viral Factor (Telos) is present
    viral_factor = signal["data"]["hexagon"]["telos"]["viral_factor"]
    console.print(f"  ✅ Viral Factor Preserved: [yellow]{viral_factor}[/yellow]")

    # 3. Adapt to Sedimentary (Vector Metadata)
    console.print(
        "\n[bold blue]3. Adapting to Sedimentary State (Vector DB)...[/bold blue]"
    )
    meta = holon.to_vector_meta()
    console.print(f"  ✅ Metadata ID: [cyan]{meta['id']}[/cyan]")
    console.print(f"  ✅ Metadata Meme: [green]{meta['meme']}[/green]")
    console.print(f"  ✅ Metadata Urgency: [yellow]{meta['urgency']}[/yellow]")

    # 4. Verification
    if str(holon.ontos.id) == signal["id"] == meta["id"]:
        console.print(
            "\n[bold green]✨ SUCCESS: Identity (Ontos) is invariant across all states.[/bold green]"
        )
    else:
        console.print("\n[bold red]❌ FAILURE: Identity mismatch![/bold red]")


if __name__ == "__main__":
    implementation()


# End of Holon
