---
hexagon:
  ontos:
    id: e9e1f3c5-ceab-49fb-8d61-f4200c06ee10
    type: md
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T11:07:36.039243Z'
    generation: 51
  topos:
    address: eyes/archive/hfo_gem/gen_33/OBSIDIAN_ROLES_DETAILED.md
    links: []
  telos:
    viral_factor: 0.0
    meme: OBSIDIAN_ROLES_DETAILED.md
---

# OBSIDIAN 8 Roles - Detailed Mapping

**Created**: 2025-11-17
**Purpose**: Comprehensive role definitions, MAS mappings, and usage across loops

---

## Philosophy: Functional Seats, Not Rigid Assignments

**OBSIDIAN roles are functional positions**, not fixed identities:
- Same role can appear at multiple loop levels (Observer in PREY, SWARM, GROWTH, HIVE)
- Roles are composable (Bridger translates in both PREY and SWARM)
- Fractal structure (same role definition scales across agent → tactical → strategic → apex)

**Standing on Giants' Shoulders**: All roles map to established MAS (Multi-Agent Systems) archetypes:
- No invention, only composition
- Backed by academic literature (Weiss 2013, DARPA 2021)
- Production-proven patterns

---

## 8 OBSIDIAN Roles

### 1. Observer (Perceiver)

**Function**: Sense environment, gather signals, collect context

**MAS Analogue**: Perceiver (BDI architecture - Belief-Desire-Intention)

**Academic Sources**:
- Rao & Georgeff (1991) - BDI architecture
- Wooldridge (2002) - Agent sensing

**Where Used**:
- **PREY**: Perceive step (gather files, precedents, stigmergy signals)
- **SWARM**: Watch step (monitor NATS telemetry, query pgvector)
- **GROWTH**: Monitor multi-round progress
- **HIVE**: Observe production metrics (LangSmith, OpenTelemetry)

**Code Example** (PREY):
```python
class ObserverAgent:
    """Perceive environment - gather all available context"""

    def perceive(self, state: PREYState) -> Observations:
        observations = {
            # Workspace context
            "files": list_files(state["workspace_dir"]),
            "file_tree": build_file_tree(state["workspace_dir"]),

            # Historical context
            "precedents": query_pgvector(
                query=state["intent"],
                k=5,
                min_quality=0.7
            ),

            # Real-time context
            "nats_signals": fetch_stigmergy_signals(state["run_id"]),
            "heartbeats": get_active_agents(state["run_id"]),

            # System context
            "telemetry": get_health_metrics(),
            "resource_usage": check_resource_limits()
        }

        return observations
```

**Code Example** (SWARM):
```python
class SWARMObserver:
    """Watch real-time + historical signals"""

    async def watch(self, run_id: str, intent: str):
        # Real-time monitoring
        nats_sub = await self.nats.subscribe(f"hfo.stigmergy.{run_id}.*")

        # Historical context
        precedents = self.pgvector.find_similar_missions(
            query=intent,
            k=10,
            min_quality=0.8
        )

        return {
            "real_time": nats_sub,
            "historical": precedents
        }
```

---

### 2. Bridger (Mediator)

**Function**: Translate between levels, interpret signals, synthesize

**MAS Analogue**: Mediator (coordination pattern)

**Academic Sources**:
- Gamma et al. (1994) - Mediator pattern (Design Patterns)
- Jennings (2000) - Agent-mediated coordination

**Where Used**:
- **PREY**: React step (interpret observations → plan actions)
- **SWARM**: Review step (translate quorum → executive summary)
- **GROWTH**: Translate intent → SWARM parameters
- **HIVE**: Integrate step (translate vision → SysML v2 SSOT)

**Code Example** (PREY):
```python
class BridgerAgent:
    """Interpret observations and plan actions"""

    def react(self, observations: Observations, intent: str) -> Actions:
        # Interpret observations with LLM
        interpretation = self.llm.invoke(
            f"""
            Observations: {json.dumps(observations)}

            Intent: {intent}

            Based on these observations, what actions should be taken?
            Consider:
            - Which files are relevant?
            - What precedents apply?
            - What tools are needed?

            Provide action plan with specific tool calls.
            """
        )

        # Parse actions from interpretation
        actions = self.parse_actions(interpretation)

        return actions
```

**Code Example** (SWARM):
```python
class SWARMBridger:
    """Synthesize quorum into executive summary"""

    def synthesize(self, quorum_result: QuorumResult, validation: ReviewResult):
        # Translate Byzantine consensus to human-readable
        summary = self.llm.invoke(
            f"""
            Quorum Level: {quorum_result.consensus_level}
            Weighted Score: {quorum_result.weighted_score}

            Findings from {len(quorum_result.cluster.responses)} researchers:
            {self.format_findings(quorum_result.cluster.responses)}

            Validation:
            - Hallucinations: {validation.hallucination_count}
            - Citation Coverage: {validation.citation_coverage}
            - Precedent Alignment: {validation.precedent_alignment}

            Synthesize into:
            1. BLUF (Bottom Line Up Front) - 2-3 sentences
            2. Key Findings (3-5 bullet points)
            3. Evidence Trail (citations)
            4. Confidence Assessment
            """
        )

        return summary
```

---

### 3. Shaper (Planner/Executor)

**Function**: Execute actions, invoke tools, transform state

**MAS Analogue**: Planner (HTN - Hierarchical Task Network)

**Academic Sources**:
- Nau et al. (2003) - SHOP2 planner
- Ghallab et al. (2004) - Automated Planning

**Where Used**:
- **PREY**: Execute step (invoke tools, read files, grep search)
- **SWARM**: Act step (execute map-reduce-filter)
- **HIVE**: Integrate step (auto-generate code from SSOT)

**Code Example** (PREY):
```python
class ShaperAgent:
    """Execute planned actions via tool invocation"""

    def execute(self, actions: Actions) -> Results:
        results = []

        for action in actions:
            if action["type"] == "read_file":
                result = read_file(
                    path=action["path"],
                    start_line=action.get("start_line", 1),
                    end_line=action.get("end_line", None)
                )

            elif action["type"] == "grep_search":
                result = grep_search(
                    pattern=action["pattern"],
                    directory=action["directory"],
                    file_pattern=action.get("file_pattern", "*")
                )

            elif action["type"] == "list_files":
                result = list_files(
                    directory=action["directory"],
                    pattern=action.get("pattern", "*"),
                    recursive=action.get("recursive", True)
                )

            results.append({
                "action": action,
                "result": result,
                "timestamp": datetime.utcnow()
            })

        return results
```

---

### 4. Injector (Resource Provider)

**Function**: Provision resources, spawn agents, allocate compute

**MAS Analogue**: Executor (resource management)

**Academic Sources**:
- Russell & Norvig (2020) - Resource allocation
- Chevaleyre et al. (2006) - Multi-agent resource allocation

**Where Used**:
- **SWARM**: Act step (spawn 10-100-1000 agents)
- **GROWTH**: Provision multiple SWARM loops
- **HIVE**: Deploy via GitOps (provision K8s resources)

**Code Example** (SWARM):
```python
class SWARMInjector:
    """Provision agents for swarm execution"""

    async def provision_agents(self, params: MissionParameters):
        agents = []

        for i in range(params.num_agents):
            # Provision Firecracker VM
            vm = await self.firecracker.create_vm(
                vcpu_count=1,
                mem_size_mib=512,
                timeout=params.timeout_per_agent
            )

            # Spawn Ray actor
            agent = await self.ray.remote(
                ResearcherActor,
                args=[
                    params.model_roster[i],
                    params.temperature,
                    vm
                ]
            )

            agents.append({
                "agent_id": i,
                "model": params.model_roster[i],
                "vm": vm,
                "actor": agent
            })

        return agents
```

---

### 5. Disruptor (Red Team)

**Function**: Challenge consensus, adversarial testing, find gaps

**MAS Analogue**: Adversary (adversarial reasoning)

**Academic Sources**:
- Littman (2001) - Adversarial planning
- Kott et al. (2023) - Autonomous Intelligent Cyber-defense Agent

**Where Used**:
- **SWARM**: Review step (challenge consensus, identify weaknesses)
- **GROWTH**: Validate step (find gaps between rounds)
- **HIVE**: Verify step (chaos engineering, integration tests)

**Code Example** (SWARM):
```python
class SWARMDisruptor:
    """Red team: Challenge consensus, find weaknesses"""

    def challenge_consensus(self, quorum_result: QuorumResult):
        critiques = []

        # Challenge 1: Fabricated citations?
        for response in quorum_result.cluster.responses:
            for citation in response.citations:
                if not self.file_exists(citation.file_path):
                    critiques.append({
                        "type": "fabricated_citation",
                        "severity": "high",
                        "agent_id": response.agent_id,
                        "citation": citation
                    })

        # Challenge 2: Contradictions within consensus?
        contradictions = self.find_contradictions(
            quorum_result.cluster.responses
        )
        critiques.extend(contradictions)

        # Challenge 3: Missing critical information?
        gaps = self.identify_gaps(
            quorum_result.cluster.responses,
            expected_topics=["architecture", "implementation", "risks"]
        )
        critiques.extend(gaps)

        # Challenge 4: Precedent misalignment?
        precedent_issues = self.check_precedent_alignment(
            quorum_result.cluster.responses
        )
        critiques.extend(precedent_issues)

        return critiques
```

---

### 6. Immunizer (Blue Team)

**Function**: Validate quality, enforce constraints, circuit breakers

**MAS Analogue**: Safety-Guard (runtime verification)

**Academic Sources**:
- Leucker & Schallhart (2009) - Runtime verification
- Alur et al. (2013) - Safety monitoring

**Where Used**:
- **SWARM**: Watch step (detect anomalies), Review step (validate quality)
- **GROWTH**: Validate step (cross-round consistency)
- **HIVE**: Verify step (Hive Guards, static validation)

**Code Example** (SWARM Watch):
```python
class SWARMImmunizer:
    """Blue team: Detect anomalies, enforce quality gates"""

    async def watch_for_anomalies(self, run_id: str):
        # Subscribe to confidence signals
        sub = await self.nats.subscribe(f"hfo.stigmergy.{run_id}.confidence.*")

        low_confidence_agents = set()

        async for msg in sub.messages:
            signal = json.loads(msg.data)

            # Detect low confidence
            if signal["confidence"] < 0.5:
                low_confidence_agents.add(signal["agent_id"])

            # Circuit breaker: 5+ agents stuck
            if len(low_confidence_agents) >= 5:
                await self.nats.publish_alert(
                    alert_type="low_confidence_quorum",
                    severity="critical",
                    agents=list(low_confidence_agents),
                    action="abort_mission"
                )
                raise LowConfidenceQuorumError(
                    f"{len(low_confidence_agents)} agents report low confidence"
                )
```

**Code Example** (SWARM Review):
```python
class SWARMImmunizer:
    """Validate quality against gates"""

    def validate_quality(self, quorum_result: QuorumResult, critiques: List[Critique]):
        # Gate 1: Quorum threshold
        if quorum_result.weighted_score < 0.7:
            raise QuorumFailureError(
                f"Weighted score {quorum_result.weighted_score} below 0.7"
            )

        # Gate 2: Hallucination limit
        hallucination_count = len([
            c for c in critiques
            if c["type"] == "fabricated_citation"
        ])
        if hallucination_count > 2:
            raise HallucinationError(
                f"{hallucination_count} fabricated citations detected"
            )

        # Gate 3: Citation coverage
        total_responses = len(quorum_result.cluster.responses)
        responses_with_citations = len([
            r for r in quorum_result.cluster.responses
            if len(r.citations) > 0
        ])
        citation_coverage = responses_with_citations / total_responses

        if citation_coverage < 0.5:
            raise LowCitationCoverageError(
                f"Only {citation_coverage:.0%} of responses have citations"
            )

        return ValidationResult(
            passed=True,
            quorum_score=quorum_result.weighted_score,
            hallucination_count=hallucination_count,
            citation_coverage=citation_coverage
        )
```

---

### 7. Assimilator (Learner)

**Function**: Learn from results, integrate knowledge, update memory

**MAS Analogue**: Learner (reinforcement learning, case-based reasoning)

**Academic Sources**:
- Sutton & Barto (2018) - Reinforcement Learning
- Aamodt & Plaza (1994) - Case-Based Reasoning

**Where Used**:
- **PREY**: Yield step (capture feedback, update pgvector)
- **SWARM**: Mutate step (learn from results, update MAP-Elites archive)
- **GROWTH**: Synthesize step (integrate multi-round findings)
- **HIVE**: Evolve step (analyze Gen N → propose Gen N+1)

**Code Example** (PREY):
```python
class AssimilatorAgent:
    """Capture feedback and learn"""

    def yield_feedback(self, state: PREYState) -> Feedback:
        # Synthesize feedback from action results
        feedback = self.llm.invoke(
            f"""
            Actions taken: {state['actions']}
            Results: {state['action_results']}

            Assess:
            1. Did we achieve the goal?
            2. What worked well?
            3. What could be improved?
            4. What should we do next?
            """
        )

        # Store to pgvector for future retrieval
        self.pgvector.store_mission(
            run_id=state["run_id"],
            intent=state["intent"],
            feedback=feedback,
            metadata={
                "agent_id": state["agent_id"],
                "timestamp": datetime.utcnow(),
                "num_actions": len(state["actions"]),
                "goal_achieved": self.check_goal_completion(feedback)
            }
        )

        return feedback
```

**Code Example** (SWARM Mutate):
```python
class SWARMAssimilator:
    """Learn from SWARM results, update archive"""

    def learn(self, params: MissionParameters, review: ReviewResult):
        # Calculate quality score
        quality_score = (
            review.quorum_score * 0.4 +
            (1 - review.hallucination_rate) * 0.3 +
            review.citation_coverage * 0.2 +
            review.precedent_alignment * 0.1
        )

        # Behavior descriptor (where in config space)
        behavior = [
            params.num_agents,
            params.temperature,
            self.measure_prompt_complexity(params.prompt_template)
        ]

        # Add to MAP-Elites archive
        self.archive.add(
            config=params.to_dict(),
            quality=quality_score,
            behavior=behavior,
            metadata={
                "run_id": params.run_id,
                "timestamp": datetime.utcnow(),
                "review": review.to_dict()
            }
        )

        # Store best config to pgvector
        if quality_score > 0.8:
            self.pgvector.store_high_quality_config(
                config=params,
                quality=quality_score
            )
```

---

### 8. Navigator (Strategist/Swarmlord)

**Function**: Strategic coordination, planning, meta-orchestration

**MAS Analogue**: Strategist/Coordinator (centralized planning)

**Academic Sources**:
- Boutilier et al. (1999) - Planning under uncertainty
- Tambe (1997) - Teamwork coordination

**Where Used**:
- **SWARM**: Set step (define mission parameters, swarm config)
- **GROWTH**: Plan step (orchestrate multi-round SPIRAL)
- **HIVE**: Evolve step (design generation architecture)

**Code Example** (SWARM Set):
```python
class Navigator:
    """Strategic coordinator - Swarmlord"""

    def set_mission(self, intent: str, constraints: str) -> MissionParameters:
        # Strategic decisions
        params = MissionParameters(
            intent=intent,
            constraints=constraints,
            run_id=self.generate_run_id(),

            # Decide swarm size based on complexity
            num_agents=self.estimate_swarm_size(intent),

            # Select model roster (multi-model diversity)
            model_roster=self.select_model_roster(
                size=10,
                tiers=["ULTRA_CHEAP", "MODERATE"],
                diversity="architectural"
            ),

            # Resource planning
            timeout_per_agent=self.estimate_timeout(intent),
            max_cost=self.calculate_budget(intent),
            quality_threshold=0.7,

            # Stigmergy config
            nats_stream="HFO_STIGMERGY",
            heartbeat_ttl=30,
            confidence_ttl=60,
            citation_ttl=300
        )

        return params
```

**Code Example** (GROWTH Plan):
```python
class NavigatorGROWTH:
    """Orchestrate multi-round SPIRAL"""

    def plan_spiral(self, intent: str) -> List[RoundConfig]:
        # Round 1: Broad exploration
        round_1 = RoundConfig(
            round=1,
            focus="broad exploration",
            num_agents=10,
            temperature=0.8,  # High diversity
            quality_threshold=0.6,  # Lower bar
            prompt_template=self.exploration_template
        )

        # Round 2: Validate gaps from round 1
        round_2 = RoundConfig(
            round=2,
            focus="validate gaps",
            num_agents=10,
            temperature=0.5,  # Medium diversity
            quality_threshold=0.7,  # Standard bar
            prompt_template=self.validation_template,
            inject_previous_digest=True
        )

        # Round 3: Convergence
        round_3 = RoundConfig(
            round=3,
            focus="convergence",
            num_agents=10,
            temperature=0.3,  # Low diversity
            quality_threshold=0.8,  # High bar
            prompt_template=self.convergence_template,
            inject_previous_digest=True
        )

        return [round_1, round_2, round_3]
```

---

## Role Flexibility (Fractal Structure)

**Key Principle**: Same role definition applies at different scales

### Observer Across Loops

| Loop | Observer Function | Example |
|------|-------------------|---------|
| PREY | Perceive agent context | `list_files()`, `query_pgvector()` |
| SWARM | Watch telemetry | NATS signals, precedents |
| GROWTH | Monitor rounds | Multi-round progress tracking |
| HIVE | Observe production | LangSmith, OpenTelemetry |

### Assimilator Across Loops

| Loop | Assimilator Function | Example |
|------|----------------------|---------|
| PREY | Yield feedback | Store to pgvector |
| SWARM | Mutate configs | Update MAP-Elites archive |
| GROWTH | Integrate rounds | Synthesize multi-round findings |
| HIVE | Evolve system | Gen N → Gen N+1 proposals |

### Navigator Across Loops

| Loop | Navigator Function | Example |
|------|-------------------|---------|
| SWARM | Set mission | Define swarm parameters |
| GROWTH | Plan sequence | Multi-round SPIRAL orchestration |
| HIVE | Design architecture | Gen 33 vision (Intent/Implementation split) |

---

## MAS Literature Mapping

| OBSIDIAN Role | MAS Archetype | Primary Source |
|---------------|---------------|----------------|
| Observer | Perceiver (BDI) | Rao & Georgeff 1991 |
| Bridger | Mediator | Gamma et al. 1994 |
| Shaper | Planner (HTN) | Nau et al. 2003 |
| Injector | Executor | Russell & Norvig 2020 |
| Disruptor | Adversary | Littman 2001 |
| Immunizer | Safety-Guard | Leucker & Schallhart 2009 |
| Assimilator | Learner | Sutton & Barto 2018 |
| Navigator | Strategist/Coordinator | Tambe 1997 |

**All roles grounded in academic research** - no invention, only composition.

---

**Status**: All 8 roles formalized with MAS mappings ✅
**Next**: Implement PREY loop with Observer/Bridger/Shaper/Assimilator in LangGraph
