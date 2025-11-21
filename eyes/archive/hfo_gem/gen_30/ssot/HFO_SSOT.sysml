/**
 * HFO Gen 30 SSOT - Main Package
 *
 * Single Source of Truth for Hive Fleet Obsidian V²C-SPIRAL-QUORUM architecture
 *
 * Auto-generates:
 * - Python orchestrator implementation
 * - OBSIDIAN agent classes
 * - Stigmergy coordination layer
 * - Test suites
 * - Docker Compose configs
 * - Documentation
 */

package HFO::Gen30 {

    import ScalarValues::*;
    import Collections::*;
    import Time::*;

    // ========================================================================
    // CORE DATA STRUCTURES
    // ========================================================================

    /**
     * Mission specification from user
     */
    attribute def MissionSpec {
        attribute intent : String;
        attribute constraints : String [0..1];
        attribute max_rounds : Integer = 3;
        attribute num_researchers : Integer = 10;
        attribute temperature_schedule : TemperatureSchedule;
    }

    /**
     * Thompson Sampling annealing schedule
     */
    attribute def TemperatureSchedule {
        attribute initial_temp : Real = 0.8;  // Round 1: exploration
        attribute final_temp : Real = 0.3;    // Round N: exploitation
        attribute schedule_type : String = "linear";  // linear | exponential
    }

    /**
     * PREY State (shared across nested loops)
     */
    attribute def PREYState {
        attribute round_number : Integer;
        attribute mission_intent : String;
        attribute mission_constraints : String [0..1];
        attribute previous_digest : DigestResult [0..1];  // Bidirectional feedback
        attribute researcher_outputs : ResearcherOutput[*];
        attribute validation_result : ValidationResult;
        attribute synthesis_result : SynthesisResult;
        attribute convergence_status : ConvergenceLevel;
    }

    /**
     * Convergence levels for quorum
     */
    enum def ConvergenceLevel {
        enum HIGH;    // >80% weighted agreement
        enum MEDIUM;  // 60-80% agreement
        enum LOW;     // <60% agreement
    }

    /**
     * Individual researcher output
     */
    attribute def ResearcherOutput {
        attribute researcher_id : String;
        attribute findings : String;
        attribute confidence_scores : ConfidenceMap;  // Dict[claim, confidence]
        attribute verified_claims : String[*];        // Claims with [VERIFIED] tag
        attribute sources : String[*];                // Citations
        attribute timestamp : Time::Instant;
    }

    /**
     * Confidence map: claim → confidence score
     */
    attribute def ConfidenceMap {
        attribute entries : ConfidenceEntry[*];
    }

    attribute def ConfidenceEntry {
        attribute claim : String;
        attribute confidence : Real;  // 0.0 to 1.0
    }

    /**
     * Validation results from Immunizer + Disruptor
     */
    attribute def ValidationResult {
        attribute consensus_level : ConvergenceLevel;
        attribute agreed_findings : String[*];      // 50%+ researchers
        attribute contested_claims : String[*];     // <50% agreement
        attribute hallucinations : HallucinationFlag[*];
        attribute outliers : OutlierReport[*];
    }

    /**
     * Hallucination detection flag
     */
    attribute def HallucinationFlag {
        attribute claim : String;
        attribute researchers : String[*];  // Who made this claim
        attribute evidence : String;        // Why flagged (no source, contradiction)
        attribute severity : Real;          // 0.0 (minor) to 1.0 (fabrication)
    }

    /**
     * Outlier researcher report
     */
    attribute def OutlierReport {
        attribute researcher_id : String;
        attribute unique_findings : String[*];
        attribute divergence_score : Real;  // How different from consensus
    }

    /**
     * Synthesis results from Assimilator
     */
    attribute def SynthesisResult {
        attribute bluf : String;                    // Bottom Line Up Front
        attribute executive_summary : String;
        attribute quorum_analysis : String;
        attribute confidence_weighted_summary : String;
        attribute suggested_visualizations : String[*];
    }

    /**
     * Final digest output
     */
    attribute def DigestResult {
        attribute round_number : Integer;
        attribute convergence_status : ConvergenceLevel;
        attribute validation : ValidationResult;
        attribute synthesis : SynthesisResult;
        attribute artifacts_path : String;
        attribute timestamp : Time::Instant;
    }

    // ========================================================================
    // STIGMERGY LAYER (NATS-based coordination)
    // ========================================================================

    /**
     * Stigmergy signal types
     */
    enum def StigmergySignalType {
        enum HEARTBEAT;   // Agent alive check
        enum CONFIDENCE;  // Self-assessment
        enum CITATION;    // Source verification
        enum ALERT;       // Critical issue
        enum QUORUM;      // Consensus status
    }

    /**
     * Heartbeat signal (Ant pheromone pattern)
     */
    attribute def HeartbeatSignal {
        attribute researcher_id : String;
        attribute timestamp : Time::Instant;
        attribute status : String;         // active | blocked | complete
        attribute current_task : String;
        attribute ttl_seconds : Integer = 30;
    }

    /**
     * Confidence signal
     */
    attribute def ConfidenceSignal {
        attribute researcher_id : String;
        attribute timestamp : Time::Instant;
        attribute confidence_level : Real;  // 0.0 to 1.0
        attribute reason : String;          // cannot_read_files | low_data_quality | high_confidence
        attribute context : String;
    }

    /**
     * Citation signal (for cross-validation)
     */
    attribute def CitationSignal {
        attribute researcher_id : String;
        attribute timestamp : Time::Instant;
        attribute citations : CitationEntry[*];
    }

    attribute def CitationEntry {
        attribute source : String;
        attribute claim : String;
        attribute verified : Boolean;
        attribute verification_method : String;  // file_read | grep_search | semantic_search
    }

    /**
     * Alert signal (critical issues)
     */
    attribute def AlertSignal {
        attribute alert_type : String;  // hallucination_detected | quorum_failure | low_confidence_quorum
        attribute severity : String;    // critical | warning | info
        attribute timestamp : Time::Instant;
        attribute details : AlertDetails;
    }

    attribute def AlertDetails {
        attribute researchers_affected : String[*];
        attribute evidence : String;
        attribute recommended_action : String;  // abort_mission | flag_output | request_human_review
    }

    // ========================================================================
    // INTERFACES (Ports)
    // ========================================================================

    port def MissionInput {
        in attribute intent : String;
        in attribute constraints : String [0..1];
    }

    port def ResearchOutput {
        out attribute findings : ResearcherOutput;
    }

    port def StigmergyChannel {
        in out attribute signals : StigmergySignal[*];
    }

    attribute def StigmergySignal {
        attribute signal_type : StigmergySignalType;
        attribute payload : String;  // JSON-encoded specific signal
        attribute ttl_seconds : Integer [0..1];
    }

}
