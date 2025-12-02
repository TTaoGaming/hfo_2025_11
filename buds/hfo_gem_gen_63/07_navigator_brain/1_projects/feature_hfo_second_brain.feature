Feature: HFO Second Brain Architecture
  As the Swarmlord
  I want to organize knowledge using the "HFO Second Brain" (PARA + Semantic Lake + Diataxis)
  So that the AI Swarm can traverse, ingest, and crystallize information efficiently without getting lost.

  Background:
    Given the root directory is "buds/hfo_gem_gen_63/brain"

  Rule: The Container must follow P.A.R.A.
    Scenario: Top-level directory structure
      Then the following directories must exist:
        | Directory      | Purpose                                      |
        | 1_projects/    | Active Missions (Hot Stigmergy)              |
        | 2_areas/       | Long-term Standards (Warm Stigmergy)         |
        | 3_resources/   | The Library (Cold Wisdom)                    |
        | 4_archives/    | Deprecated/Completed work (Frozen)           |

  Rule: The Medium must be a Semantic Lake (Stigmergy)
    Scenario: Active Projects are flat
      Given a file is in "1_projects/"
      Then it should not be in a subdirectory (Flat Hierarchy)
      And it must have a valid YAML "holon" header
      And the header must contain a "type" field

  Rule: The Crystal must follow Diataxis
    Scenario: Resources are strictly typed
      Given a file is in "3_resources/"
      Then it must be located in one of the following subdirectories:
        | Subdirectory   | Diataxis Type |
        | tutorials/     | Learning      |
        | guides/        | Doing         |
        | reference/     | Information   |
        | explanation/   | Understanding |

  Rule: Every file must be a Holon
    Scenario: Universal Header Requirement
      Given any Markdown file in the Second Brain
      Then it must start with a YAML frontmatter block
      And the block must contain "holon:"
      And the block must contain "id:"
      And the block must contain "type:"
