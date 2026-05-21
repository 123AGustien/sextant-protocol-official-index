# 🧭 Sextant Protocol — System Map (Unified View)

## Overview

This document provides a single consolidated view of all system layers in the Sextant Protocol ecosystem.

---

## 🧱 Core Architecture Layers

### 1. INDEX LAYER (System Truth)
Defines canonical structure of the system:

- Dependency graphs
- Node definitions
- System topology
- Risk model structure

📌 Purpose:
> Defines what the system is

---

### 2. ENGINE LAYER (Execution)

Responsible for simulation logic:

- Graph Engine
- Baseline Simulator
- Cascade Engine
- Routing Engine

📌 Purpose:
> Executes system behavior under uncertainty

---

### 3. GOVERNANCE LAYER (Interpretation)

Defines system constraints and semantics:

- Execution boundaries
- Policy interpretation rules
- Structural constraints
- Control logic definitions

📌 Purpose:
> Defines how the system is interpreted

---

### 4. OBSERVABILITY LAYER

Measures system behavior:

- Metrics engine
- Benchmark runner
- Scenario comparison outputs

📌 Purpose:
> Evaluates system performance

---

## 🔄 System Flow

```text
INDEX → ENGINE → OBSERVABILITY
        ↓
   GOVERNANCE (interpretation overlay)
