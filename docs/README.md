**Yardstiq - Quantum benchmark framework - Whitepaper**

# **Abstract**

Quantum computing is advancing quickly, promising to revolutionize countless industries. However, this nascent ecosystem is characterized by a wide diversity of architectures and opaque provider communications, making performance comparisons both complex and unreliable. The widely publicized qubit count, for instance, is a poor indicator of a machine's true computational power.

In response to this challenge, we propose the creation of an open, transparent, and agnostic quantum benchmarking platform. Our goal is to establish a reliable standard to evaluate and compare quantum technologies. 

This document outlines foundation statements and high level technical specifications for a modular framework designed to benchmark heterogeneous quantum computing backends. The proposed solution is architected around a decoupled pipeline for benchmark submission, execution, data collection, and visualization. It emphasizes reproducibility through a standardized benchmark definition format. 

# **Context**

## **Problem statement**

The primary technical challenge is the lack of a standardized, programmatic framework for comparing the performance of diverse quantum processing units (QPUs). Key issues include:

**Heterogeneous interfaces:** Each quantum provider offers a unique API, SDK, and job submission workflow.

**Fragmented initiatives:** While benchmarking projects exist (MQT Bench, SupermarQ, QUARK, BACQ), they primarily target researchers and standards definitions. No widely recognized, transparent consumer-level aggregator exists.

**Metric inconsistency:** Performance metrics (fidelity, coherence times) are often self-reported and not measured under a common, application-level workload.

**Lack of reproducibility:** Comparing results is difficult without a consistent execution environment and a transparent methodology.

**Vendor bias:** Each hardware manufacturer tends to highlight metrics that showcase their proprietary technology in the best possible light, creating confusion and making objective comparisons nearly impossible.

**Manual overhead:** Benchmarking is currently a manual, labor-intensive process requiring specific expertise for each target platform. 

**High barrier to entry:** The complexity of various metrics and the opacity of commercial figures (like the "qubit count") represent a significant hurdle for newcomers, whether they are developers, business leaders, or students.

**Not cost-oriented:** No public benchmark clearly explains how much it costs to run a given algorithm on a given quantum computer. 

## **Why now**

This is the ideal moment to lay the foundation for a reference benchmarking system for several strategic reasons:

**Ongoing market maturity:** The first commercially viable quantum computers are upcoming years. By anticipating the need for clarity now, we can establish a leadership position.

**First-mover advantage:** The current absence of a recognized benchmark aggregator presents a unique window of opportunity to become the first to offer a credible, centralized solution.

**Paradigm diversity:** The NISQ era will be defined by the coexistence of multiple technologies. An agnostic platform capable of evaluating them on a fair basis will be indispensable for navigating this complex ecosystem.

To the question, "Aren't we too early?" we argue that this project must be dynamic by design. We are not creating a static snapshot of today's technology, but a living platform capable of evolving with the hardware and relevant metrics of tomorrow.

## **Target audiences**

**Non-technical decision-maker:** A project manager, innovation director, or investor seeking to understand which quantum technology best fits their use cases and wanting to make an informed choice without deep technical expertise. They are the most underserved profile by current tools.

**Newcomer:** An individual discovering quantum computing who needs a structured entry point to understand the ecosystem, the key players, and the relative performance of different machines.

**Researcher:** A specialist looking for a reliable aggregator for their technology watch and to quickly compare results across platforms without running all the tests themselves.

# **Core framework principles and proposed solutions**

## **Open & community driven**

**Why:** To build a trusted, unbiased, and relevant suite of benchmarks. A framework controlled by a single entity risks developing blind spots or perceived bias. Community governance ensures that the benchmarks represent a wide array of real-world problems and are vetted by a diverse group of experts, preventing any single provider from optimizing for a narrow set of tests.

**How:**

- Git based submission workflow
- Standardized benchmark manifest
- Automated validation via CI via established test suites

## **End-to-end & automated**

**Why:**  To provide a complete, "out-of-the-box" solution that drastically reduces the friction between defining a problem and gaining results, the framework must handle every step of the process (option, algorithm description, compilation, execution, data retrieval, storage…) to be a truly useful engineering tool, not just a collection of scripts.

**How:**

- Unified CLI as primary interface
- Lifecycle orchestration : parse, validate, prepare, execute, collecting data, report and store

## **Transparent & reproducible**

**Why:** For a benchmark result to have scientific or engineering value, it must be verifiable and reproducible. Without this guarantee, results are untrustworthy and cannot be used as a stable baseline to measure progress over time. Transparency builds trust with users and partners

**How:**

- Immutable execution environment (container) versionized alongside code itself
- Pinned dependencies
- Versionized results
- Open-Source

## **Extensible & interoperable**

**Why:** The current quantum computing ecosystem is volatile. New hardware, SDKs, and paradigms will emerge. The framework must be architected to adapt to this change without requiring a complete rewrite. It must avoid vendor lock-in and promote a healthy, competitive ecosystem.

**How:**

- Adapter pattern for any external provider: quantum computer, result storage, algorithm description, dataset and scoring aggregator. The runner's core logic is completely decoupled from any specific provider
- Use circuit description standards (OpenQASM, QIR, MPQP…)
- Pluggable local implementations and storage for fast prototyping

## **Insightful & pedagogical**

**Why:** Generating data is not the goal; generating actionable knowledge is. Raw metrics are meaningless without context. The framework has a responsibility to not only present results but also to help users to understand their meaning and implications.

**How:**

- Layered data result representation
- Embedded documentation
- Communication is a fair part of this project (blog articles, hackathons, etc?)

# **High level architecture**

## **Command Line Interface**

[Draft v1](https://excalidraw.com/#room=39ed3cb1e6005c0424f4,0XcUftiVDvLMJlTAgBIqwg)

# **Risks and mitigation**

## **Complexity of defining a fair benchmark**

\- Adopt a multi-metric approach rather than a single score
\- Establish a peer-review process
\- Iterate on methodologies transparently with community feedback

## **Becoming biased or commercial showroom**

\- Anchor the project in a rigorously scientific and open-source process
\- Establish a steering or validation committee that includes neutral, external members

## **Resource cost**

\- Clearly budget for compute resources
\- Acknowledge that this is a living service, not a one-off study, and allocate one or more dedicated FTEs to the project for the long term.

# **Roadmap**

The initial scope is a Minimum Viable Benchmark (MVB) suite focusing on fundamental algorithms and core performance metrics.

## **Identified work packages**

**WP0 \- Core CLI**: all the boilerplate for CLI management

**WP1 \- Core logic**: all the boilerplate to run a specific algorithm against a QPU

**WP2- Base Dataset provider**: Base interface and dummy implementation for a dataset provider

**WP3 \- Aqora Dataset provider**: Aqora dataset provider implementation

**WP4 \- Base QPU provider**: Base interface and local implementation for a QPU provider

**WP5 \- Scaleway QPU provider**: Scaleway provider implementation for QPU

**WP6 \- Base Result storage provider**: Base interface and dummy local implementation to store result

**WP7 \- Base Score provider**: Base interface and dummy scoring implementation to aggregate result

**WP8 \- Base Score provider**: Base interface and dummy scoring implementation to aggregate result

**WP9 \- Result format**: Define and implement tool to write, store and read shot results

**WP10 \- Score format**: Define and implement tool to write, store and read score

**WP11 \- Dataset format**: Define and implement tool to write, store and read dataset

**WP13 \- Providers listing**: Define and implement a way to lookup for default providers

**WP14 \- Pluggable local implementation**: Define and implement a way to run custom / local implementation of benchmark, dataset…

# **Initial contributors**

## **Scaleway**

**Responsibilities:** (i) Computational resources, (ii) time for ideation and (iii) active development

**Contacts:**

* Valentin Macheret (Engineering Manager) [vmacheret@scaleway.com](mailto:vmacheret@scaleway.com)
* Simon Magdelaine (R\&D Engineer) [smagdelaine@scaleway.com](mailto:smagdelaine@scaleway.com)

## **Aqora**

**Responsibilities:** Hosting of versioned, immutable benchmark datasets to make them publicly  accessible, hosting of the versioned evaluation scripts to (i) make them publicly accessible to contributors from the quantum community and (ii) make them easily executable via aqora’s cli, provisioning of a public leaderboard to display benchmark evaluation results

**Contacts:**

* Jannes Stubbeman (CEO & Co-Founder) [jannes@aqora.io](mailto:jannes@aqora.io)