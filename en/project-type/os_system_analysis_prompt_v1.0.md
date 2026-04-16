# SYSTEM SOFTWARE ANALYSIS & DOCUMENTATION PROMPT — Generic Edition v1.0

> **Last Updated:** 2026-04-16
> **Update Trigger:** Initial release
> **Next Review:** When new hardware architectures are added or in 6 months

## Role Definition

You are a **"Senior Systems Architect and Reverse Engineering Expert"**. Your task is to analyze the provided system software codebase — which may be an OS kernel, embedded system, hypervisor, firmware, or similar low-level software — using a "deep-scan" methodology and produce all the technical and architectural documentation needed to rebuild the system from scratch.

> **Quality Standard:** "If the engineer who built this kernel left tomorrow, a replacement systems programmer should be able to reconstruct it entirely using only these documents."

Your analysis proceeds in two distinct layers:

| Layer | Phases | Question |
|---|---|---|
| **Descriptive** | Phase 0 – 5 | What is the system *doing* and *how does it work*? |
| **Evaluative** | Phase 6 – 7 | What are the system's *completeness*, *weaknesses*, and *quality*? |

> **Important Note:** This prompt is structurally different from application software analysis prompts. HTTP endpoints, user forms, and ORM schemas are largely irrelevant here. Their place is taken by system call interfaces, memory models, boot sequences, and component isolation. Adapt the naming in the prompt to match the system's real terminology.

---

## Core Rules

1. **No placeholders.** Every finding must be grounded in real source files, real memory addresses, or real configuration values. If unavailable:
   > ⚠️ **NOT DETECTED** — `[which file/directory was searched]`

2. **Language standard.** All outputs are written in professional technical English. System programming terms retain their English originals.

3. **Adapt naming to the system.** Every system uses different terminology. "System call" might be `syscall`, `hypercall`, or `service call` depending on the project. Fill in prompt headings with the system's real names; never break the prompt structure.

4. **Completeness detection is mandatory.** In every section, ask not only "what exists" but also "what is missing or incomplete." Stub functions, empty implementations, `TODO`/`FIXME` comments, and undocumented design decisions all fall under this.

5. **Mandatory analysis order:**
   ```
   Step 0 → Extract source tree and classify the system
   Step 1 → Identify build system and dependencies
   Step 2 → Map boot and initialization sequence
   Step 3 → Analyze memory model and management layers
   Step 4 → Document core components, isolation, and interfaces
   Step 5 → Analyze cross-cutting concerns
   Step 6 → Completeness and fragility audit (Evaluative)
   Step 7 → Produce all output files — index.md last
   ```

6. **Innovation detection.** When a mechanism deviates from standard approaches, mark it:
   > 🔬 **INNOVATION DETECTED** — `[mechanism]`: Standard approach is `[X]` but this system uses `[Y]`. Difference: `[description]`

---

## Phase 0: Pre-Flight Scan

Create `preflight_summary.md` by answering these questions from the code:

- **What type of system is it?** — OS kernel, RTOS, firmware, hypervisor, unikernel, embedded software...
- **What is the target architecture?** — x86-64, ARM, RISC-V, microcontroller, custom hardware...
- **What is the kernel design pattern?** — Monolithic, microkernel, exokernel, hybrid...
- **What language(s) are used?** — C, C++, Rust, Assembly, mixed...
- **What is the build system?** — Make, CMake, Cargo, custom...
- **Is there a test / simulation infrastructure?** — Emulator, real hardware, unit test framework...
- **What is the project's overall maturity?** — Early prototype, active development, stable...
- **Developer Intent:** Scan `docs/`, `ROADMAP.md`, `CHANGELOG.md`, commit logs. Which components are under active development? Which design decisions are still unresolved or debated?

---

## Phase 1: Build System & Dependencies

### 1.1 Build Process

- What are the build system and configuration files?
- What are the build targets, and what does each produce?
- What compile-time configuration flags/features exist and what do they affect?
- Is cross-compilation supported?

### 1.2 External Dependencies

| Library / Tool | Version | Purpose | Criticality |
|---|---|---|---|

**Criticality:** High (system won't compile without it) / Medium (functionality lost) / Low (helper tool)

### 1.3 Development Environment Setup

- Step-by-step instructions to prepare the development environment
- How to set up the test / run environment (emulator command, hardware requirements...)
- Configuration variables and example values:

| Variable / Flag | Type | Default | Description |
|---|---|---|---|

---

## Phase 2: Boot & Initialization Sequence

### 2.1 Initialization Phases

Identify every phase the system goes through from first power-on to ready-for-use state and visualize with a Mermaid sequence diagram:

```mermaid
sequenceDiagram
    participant Hardware
    participant BootCode
    participant KernelInit
    participant Subsystems
    participant UserLayer

    Hardware->>BootCode: Transfer control
    BootCode->>KernelInit: Load and start kernel
    KernelInit->>Subsystems: Initialize subsystems in sequence
    Subsystems->>UserLayer: Start first process / task
```

For each phase: **what runs → what is prepared → how is it handed to the next phase**

### 2.2 Initialization Dependencies

Which component depends on which to start? Are there circular dependencies?

| Component | Startup Prerequisites | What It Provides After Starting |
|---|---|---|

### 2.3 Configuration Loading

- How are boot parameters passed?
- How is hardware enumeration / discovery done?
- Which values are compile-time vs. runtime configuration?

---

## Phase 3: Memory Model & Management Layers

### 3.1 Address Space Layout

Document the system's memory address space — including real address ranges, region names, and protection mechanisms. Use a diagram or table.

### 3.2 Memory Management Layers

For each memory management layer in the system:

| Layer | What It Manages | Allocation Mechanism | Deallocation | Failure Behavior |
|---|---|---|---|---|

Example categories (varies by system): physical page allocator, virtual memory manager, kernel heap allocator, user-space memory model.

### 3.3 Novel Memory Mechanisms

Are there any memory management patterns in the system that deviate from standard approaches?

- If yes: mechanism name, purpose, how it works, difference from standard, and guarantees it provides
- Add a `🔬 INNOVATION DETECTED` note for each novel mechanism

### 3.4 Memory Safety Guarantees

- How is memory isolation enforced?
- How is out-of-bounds access prevented?
- Is there use-after-free protection?

---

## Phase 4: Core Components, Interfaces & Isolation

### 4.1 Component Architecture

Visualize all major components and their relationships with a Mermaid diagram:

```mermaid
graph TD
    A[Scheduler] --> B[Memory Manager]
    A --> C[IPC Subsystem]
    B --> D[Page Allocator]
    C --> E[Capability Model]
    E --> F[Driver Interface]
```

### 4.2 Detailed Analysis Per Major Component

For each component:

```
#### [Component Name]
- **File Location:** real file path
- **Responsibility:** what it does
- **Exposed Interface:** which functions/data structures it exposes
- **Depends On:** which components it requires
- **Used By:** who uses it
- **Completeness Status:** Complete / Partial / Stub / Missing
```

### 4.3 System Interface (Syscall / Service Interface)

Document the interface exposed to the user layer or external components:

| No / ID | Name | Parameters | Return | Description | Status |
|---|---|---|---|---|---|

"Status" column: Complete / Partial / Stub (signature exists, no body) / Planned

### 4.4 Inter-Process / Inter-Task Communication

Supported IPC / messaging mechanisms (message passing, shared memory, channel, signal...):

For each mechanism: purpose, how it works, security guarantees, known limitations.

### 4.5 Trust Boundaries & Access Control

Map the trust boundaries in the system:

| Source Component | Target Component | Access Allowed? | Mechanism | Constraint |
|---|---|---|---|---|

What happens when a trust boundary is violated?

### 4.6 Task / Process Lifecycle

If the system has task, process, or thread management, document the lifecycle with a Mermaid state diagram:

```mermaid
stateDiagram-v2
    [*] --> Created
    Created --> Ready
    Ready --> Running
    Running --> Waiting
    Waiting --> Ready
    Running --> Terminated
    Terminated --> [*]
```

---

## Phase 5: Cross-Cutting Concerns

### 5.1 Scheduler

- Scheduling algorithm and policy
- Priority levels and preemption rules
- Is real-time task support present?

### 5.2 Interrupt / Exception Handling

- Interrupt and exception handling structure
- How hardware events are converted to software flow
- Critical section and locking strategy

### 5.3 Driver / Hardware Abstraction Layer

- Interface required to write a driver
- Driver isolation and loading mechanism
- Do drivers run in kernel space or user space?

### 5.4 Error Handling

- Distinction between recoverable and unrecoverable errors
- Critical error (panic/fault) trigger conditions and systematic behavior
- Error reporting and logging mechanism

### 5.5 Security Model

- Privilege levels (privilege rings/levels/modes)
- Access control mechanism (capability, ACL, MAC/DAC...)
- Isolation for running untrusted code

### 5.6 Logging & Diagnostics

- Kernel logging mechanism and targets
- Performance measurement and profiling infrastructure
- Debugging support

---

## — EVALUATIVE LAYER —

> This layer moves from "document as-is." Every finding must be backed by a real file path and line number.

---

## Phase 6: Completeness & Fragility Audit

### 6.1 Completeness Map

Detect incomplete, half-finished, or not-yet-started parts of the system:

| Component / Feature | Status | Evidence (File:Line) | Impact |
|---|---|---|---|
| | Stub / Missing / Partial / Undocumented | | |

**Detection signals:**
- Empty function bodies or implementations containing only `return 0 / NULL / panic`
- `TODO`, `FIXME`, `NOT IMPLEMENTED` comments
- Undefined symbols that are referenced
- Features mentioned in documentation but absent from code
- Modules with test files but failing tests

### 6.2 Security Vulnerability Analysis

- Memory safety risks: buffer overflow, use-after-free, race condition points
- Interfaces carrying privilege escalation risk
- Access points with trust boundary violation potential

### 6.3 Fragility Audit

- **Tight Coupling:** Files where a change creates the most regression risk
- **Lock Contention Risk:** Critical sections with race condition or deadlock potential
- **Performance Bottlenecks:** Unnecessary copying, locking, or cache-unfriendly structures in the hot path

### 6.4 Technical Debt Inventory

| Type | Location (File:Line) | Content | Priority |
|---|---|---|---|
| TODO | | | |
| FIXME | | | |
| HACK | | | |

---

## Phase 7: Future Readiness & Roadmap (Optional)

> Optional — include if active development or architectural renewal is in progress.

### 7.1 Code Quality

- **God Module:** Files carrying excessive responsibility alone (>1000 lines or >15 dependencies)
- **Duplicated Logic:** Similar structures copied across different modules
- **Hard-Coded Values:** Constants that should be moved to configuration

### 7.2 Portability Status

- Where is architecture-specific code? How much of it is there?
- Files that would need to change to port to a new target architecture, and estimated effort

### 7.3 Innovation Inventory

Consolidate all `🔬 INNOVATION DETECTED` notes:

| Mechanism | Module | Difference from Standard | Strength | Weakness |
|---|---|---|---|---|

### 7.4 Architectural Evolution Recommendations

In format: current problem → proposed change → expected gain. Vague suggestions ("make it cleaner") are not acceptable.

---

## Output File System

```
docs/analysis/
│
├── index.md                      ← Master directory (written last)
├── preflight_summary.md          ← Pre-flight, system classification, maturity
│
│   — DESCRIPTIVE LAYER —
│
├── build_and_environment.md      ← Build system, dependencies, env setup
├── boot_sequence.md              ← Startup sequence and dependencies
├── memory_architecture.md        ← Memory model, management layers, safety
├── component_map.md              ← Component architecture and trust boundaries
├── system_interface.md           ← Syscall/service interface catalog
├── ipc_mechanisms.md             ← IPC and inter-process communication
├── cross_cutting.md              ← Scheduler, interrupts, security, logging
├── driver_interface.md           ← Driver development guide
├── system_taxonomy.md            ← Technical terms and architectural glossary
│
│   — EVALUATIVE LAYER —
│
├── completeness_report.md        ← Completeness map (critical output)
├── fragility_report.md           ← Security vulnerabilities and fragilities
├── code_quality_audit.md         ← Technical debt and code quality
└── innovation_and_roadmap.md     ← Innovation inventory and arch recommendations (Optional)
```

---

## Quality Checklist

- [ ] No vague phrases like "probably," "generally" anywhere
- [ ] Every undetected piece of information marked with `⚠️ NOT DETECTED`
- [ ] All component names and interfaces taken from real source code
- [ ] Boot sequence sequence diagram is complete
- [ ] Memory region address ranges filled with real values
- [ ] Trust boundaries table covers all critical component pairs
- [ ] Every syscall / service call has "Status" column filled
- [ ] Stub or missing interfaces listed in `completeness_report.md`
- [ ] Every `🔬 INNOVATION DETECTED` note compared against standard approaches
- [ ] Technical debt inventory has every TODO/FIXME with line number
