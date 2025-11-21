/**
 * V²C-SPIRAL-QUORUM Protocol Block Definition
 *
 * Hierarchical verification-validation-consensus protocol
 * with nested holonic PREY loops, Thompson Sampling annealing,
 * and confidence-weighted quorum consensus.
 */

package HFO::Gen30::SPIRAL {

    import HFO::Gen30::*;
    import ScalarValues::*;

    /**
     * SPIRAL Orchestrator (Outer Loop - Strategic)
     *
     * Multi-round iterative refinement with:
     * - Thompson Sampling temperature annealing
     * - Bidirectional feedback between rounds
     * - Automatic convergence detection
     */
    part def SpiralOrchestrator {

        // Configuration
        attribute max_rounds : Integer = 3;
        attribute convergence_threshold : Real = 0.8;  // 80% for HIGH consensus
        attribute stability_threshold : Real = 0.8;    // 80% overlap = stable

        // State
        attribute current_round : Integer = 1;
        attribute mission_spec : MissionSpec;
        attribute round_history : PREYState[*];

        // Ports
        port mission_in : MissionInput;
        port digest_out : ResearchOutput;
        port stigmergy : StigmergyChannel;

        /**
         * Main execution flow
         */
        action execute_mission {
            in mission : MissionSpec;
            out digest : DigestResult;

            // Initialize state
            bind current_round = 1;
            bind previous_digest = null;

            // SPIRAL loop
            loop while should_continue() {

                // Calculate temperature for this round (Thompson Sampling)
                perform calculate_temperature {
                    in round_num = current_round;
                    in max_rounds = mission.max_rounds;
                    out temperature = get_annealing_temp();
                }

                // Run PREY loop with feedback from previous round
                perform run_prey_loop {
                    in intent = mission.intent;
                    in constraints = mission.constraints;
                    in previous_digest = previous_digest;
                    in temperature = temperature;
                    in round_number = current_round;
                    out current_digest = prey_result;
                }

                // Check convergence
                perform check_convergence {
                    in current = current_digest;
                    in previous = previous_digest;
                    out converged = is_converged();
                    out stable = is_stable();
                }

                // Update state
                send round_history := round_history + current_digest;
                send previous_digest := current_digest;
                send current_round := current_round + 1;

                // Break conditions
                if converged or stable or current_round > max_rounds {
                    break;
                }
            }

            // Return final digest
            return current_digest;
        }

        /**
         * Thompson Sampling temperature schedule
         *
         * Annealing: High temp (explore) → Low temp (exploit)
         */
        action calculate_temperature {
            in round_num : Integer;
            in max_rounds : Integer;
            out temperature : Real;

            // Linear annealing: 0.8 → 0.3
            calc temp_linear = 0.8 - (0.5 * (round_num / max_rounds));

            // Exponential annealing (alternative)
            calc temp_exp = 0.8 * (0.375 ^ (round_num / max_rounds));

            // Use linear by default
            return temp_linear;
        }

        /**
         * Convergence detection
         */
        action check_convergence {
            in current : DigestResult;
            in previous : DigestResult [0..1];
            out converged : Boolean;
            out stable : Boolean;

            // HIGH consensus = converged
            if current.convergence_status == ConvergenceLevel::HIGH {
                send converged := true;
                return;
            }

            // No previous round = not stable
            if previous == null {
                send converged := false;
                send stable := false;
                return;
            }

            // Check findings stability (80%+ overlap)
            perform calculate_overlap {
                in findings_1 = current.validation.agreed_findings;
                in findings_2 = previous.validation.agreed_findings;
                out overlap_ratio = jaccard_similarity();
            }

            send stable := (overlap_ratio >= stability_threshold);
            send converged := false;
        }

        /**
         * PREY Loop execution (delegates to PREYOrchestrator)
         */
        action run_prey_loop {
            in intent : String;
            in constraints : String [0..1];
            in previous_digest : DigestResult [0..1];
            in temperature : Real;
            in round_number : Integer;
            out prey_result : DigestResult;

            // Delegate to PREY orchestrator
            perform delegate PREYOrchestrator.execute {
                in intent = intent;
                in constraints = constraints;
                in previous_digest = previous_digest;
                in temperature = temperature;
                in round_number = round_number;
                out result = prey_result;
            }
        }
    }

    /**
     * PREY Orchestrator (Inner Loop - Tactical)
     *
     * Single-round scatter-gather execution:
     * - Sense: Interpret mission + retrieve precedents
     * - Make Sense: Generate research strategy
     * - Act: Scatter N researchers + validate + synthesize
     * - Yield: Return digest
     */
    part def PREYOrchestrator {

        // Configuration
        attribute num_researchers : Integer = 10;
        attribute timeout_seconds : Integer = 300;

        // State
        attribute state : PREYState;

        // Ports
        port mission_in : MissionInput;
        port digest_out : ResearchOutput;
        port stigmergy : StigmergyChannel;

        /**
         * PREY execution (single round)
         */
        action execute {
            in intent : String;
            in constraints : String [0..1];
            in previous_digest : DigestResult [0..1];
            in temperature : Real;
            in round_number : Integer;
            out result : DigestResult;

            // SENSE / PERCEIVE
            perform sense_phase {
                in intent = intent;
                in constraints = constraints;
                in previous_digest = previous_digest;
                out mission_understanding = bridger_output;
            }

            // MAKE SENSE / REACT
            perform make_sense_phase {
                in understanding = mission_understanding;
                in previous_results = previous_digest;
                out research_strategy = strategy;
            }

            // ACT / EXECUTE
            perform act_phase {
                in strategy = research_strategy;
                in temperature = temperature;
                in num_researchers = num_researchers;
                out researcher_outputs = research_results;
            }

            // YIELD / FEEDBACK
            perform yield_phase {
                in outputs = researcher_outputs;
                in round_number = round_number;
                out digest = final_digest;
            }

            return final_digest;
        }

        /**
         * SENSE phase: Bridger agent interprets mission
         */
        action sense_phase {
            in intent : String;
            in constraints : String [0..1];
            in previous_digest : DigestResult [0..1];
            out mission_understanding : BridgerOutput;

            // Delegate to Bridger agent
            perform delegate Bridger.interpret {
                in user_intent = intent;
                in user_constraints = constraints;
                in previous_round_feedback = previous_digest;
                out understanding = mission_understanding;
            }
        }

        /**
         * MAKE SENSE phase: Generate research strategy
         */
        action make_sense_phase {
            in understanding : BridgerOutput;
            in previous_results : DigestResult [0..1];
            out research_strategy : ResearchStrategy;

            // Analyze gaps from previous round
            if previous_results != null {
                perform identify_gaps {
                    in previous = previous_results;
                    out gaps = knowledge_gaps;
                }
                send strategy := generate_strategy_with_gaps(understanding, gaps);
            } else {
                send strategy := generate_initial_strategy(understanding);
            }
        }

        /**
         * ACT phase: Scatter-gather N researchers
         */
        action act_phase {
            in strategy : ResearchStrategy;
            in temperature : Real;
            in num_researchers : Integer;
            out researcher_outputs : ResearcherOutput[*];

            // Parallel scatter-gather
            parallel for i in 1..num_researchers {
                perform Shaper.research {
                    in worker_id = i;
                    in prompt = strategy.prompts[i];
                    in temperature = temperature;
                    in stigmergy_channel = stigmergy;
                    out output = researcher_outputs[i];
                }
            }
        }

        /**
         * YIELD phase: Validate + Synthesize → Digest
         */
        action yield_phase {
            in outputs : ResearcherOutput[*];
            in round_number : Integer;
            out digest : DigestResult;

            // Validation (Immunizer + Disruptor)
            perform validate {
                in researcher_outputs = outputs;
                out validation_result = validation;
            }

            // Synthesis (Assimilator)
            perform synthesize {
                in outputs = outputs;
                in validation = validation;
                out synthesis_result = synthesis;
            }

            // Build digest
            send digest := DigestResult {
                round_number = round_number,
                convergence_status = validation.consensus_level,
                validation = validation,
                synthesis = synthesis,
                artifacts_path = get_artifacts_path(),
                timestamp = now()
            };
        }
    }

    // Supporting data structures

    attribute def BridgerOutput {
        attribute mission_intent : String;
        attribute constraints : String [0..1];
        attribute optimized_prompt : String;
        attribute precedent_context : String [0..1];
    }

    attribute def ResearchStrategy {
        attribute prompts : String[*];  // One per researcher
        attribute focus_areas : String[*];
        attribute gaps_to_fill : String[*];
    }
}
