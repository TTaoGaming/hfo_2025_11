"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: mission-evolution-gap
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T12:00:00+00:00'
    generation: 51
  topos:
    address: body/mission_evolution_gap.py
    links: []
  telos:
    viral_factor: 0.0
    meme: mission_evolution_gap.py
"""

import logging

import psycopg2
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

# Configure Logging
logging.basicConfig(level=logging.ERROR)
console = Console()

# Configuration
DB_CONFIG = {
    "dbname": "hfo_unified_memory",
    "user": "hfo_admin",
    "password": "phoenix_password",
    "host": "localhost",
    "port": "5435",
}


def get_db_connection():
    """Connect to the HFO Memory (Postgres)."""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        console.print(f"[bold red]❌ Database Connection Failed:[/bold red] {e}")
        return None


def analyze_evolution_gap():
    """Analyze the drift between Gen 51 and Gen 52 in the Knowledge Graph."""
    conn = get_db_connection()
    if not conn:
        return

    console.print(
        Panel(
            "🧬 [bold cyan]Evolutionary Gap Analysis (Gen 51 vs Gen 52)[/bold cyan]",
            expand=False,
        )
    )

    with conn.cursor() as cur:
        # 1. Get Total Count
        cur.execute("SELECT COUNT(*) FROM knowledge_graph;")
        total_nodes = cur.fetchone()[0]

        # 2. Deep Content Scan for "generation: 51" vs "generation: 52"
        cur.execute(
            """
            SELECT
                CASE
                    WHEN content ILIKE '%generation: 51%' THEN '51'
                    WHEN content ILIKE '%generation: 52%' THEN '52'
                    ELSE 'Unknown'
                END as detected_gen,
                COUNT(*) as count
            FROM knowledge_graph
            GROUP BY detected_gen
            ORDER BY detected_gen;
        """
        )
        rows = cur.fetchall()

    conn.close()

    # Display Results
    table = Table(title="Deep Content Analysis (Header Scan)")
    table.add_column("Detected Generation", style="cyan")
    table.add_column("Count", style="magenta")
    table.add_column("Percentage", style="green")

    gen_counts = {str(r[0]): r[1] for r in rows}

    gen_51_count = gen_counts.get("51", 0)
    gen_52_count = gen_counts.get("52", 0)
    # unknown_count = gen_counts.get("Unknown", 0)

    # Calculate Drift
    drift_percentage = (gen_51_count / total_nodes) * 100 if total_nodes > 0 else 0
    evolution_percentage = (gen_52_count / total_nodes) * 100 if total_nodes > 0 else 0

    for gen, count in gen_counts.items():
        pct = (count / total_nodes) * 100
        table.add_row(str(gen), str(count), f"{pct:.1f}%")

    console.print(table)

    console.print(f"\n[bold]Total Nodes:[/bold] {total_nodes}")
    console.print(
        f"[bold yellow]⚠️  Legacy Drift (Gen 51 Content):[/bold yellow] {drift_percentage:.1f}%"
    )
    console.print(
        f"[bold green]🚀 Evolution Progress (Gen 52 Content):[/bold green] {evolution_percentage:.1f}%"
    )

    if drift_percentage > 50:
        console.print("\n[bold red]🚨 CRITICAL DRIFT DETECTED[/bold red]")
        console.print(
            "The majority of the Brain content still contains Gen 51 headers."
        )
        console.print(
            "Recommendation: Initiate [bold]Aggressive Exemplar Assimilation[/bold] to upgrade legacy nodes."
        )


if __name__ == "__main__":
    analyze_evolution_gap()
