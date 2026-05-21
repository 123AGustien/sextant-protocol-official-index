# 🧭 Sextant Protocol — System Map (Unified View)

## Overview

This document provides a consolidated view of all system layers in the Sextant Protocol ecosystem.

It defines how components interact across structure, execution, interpretation, and evaluation layers.

---

## 🧱 Core Architecture Layers

### 1. INDEX LAYER (System Truth)

Defines the canonical structure of the system.

Includes:

- Dependency graphs  
- Node definitions  
- System topology  
- Risk model structure  

📌 Purpose:
> Defines what the system is

---

### 2. ENGINE LAYER (Execution)

Responsible for simulation logic and runtime behavior.

Includes:

- Graph Engine  
- Baseline Simulator  
- Cascade Engine  
- Routing Engine  

📌 Purpose:
> Executes system behavior under uncertainty

---

### 3. GOVERNANCE LAYER (Interpretation)

Defines constraints and interpretation rules.

Includes:

- Execution boundaries  
- Policy interpretation rules  
- Structural constraints  
- Control logic definitions  

📌 Purpose:
> Defines how system behavior is interpreted and constrained

---

### 4. OBSERVABILITY LAYER

Measures and evaluates system behavior.

Includes:

- Metrics engine  
- Benchmark runner  
- Scenario comparison outputs  

📌 Purpose:
> Evaluates system performance across conditions

---
## 🔄 System Flow

```text
INDEX → ENGINE → OBSERVABILITY
        ↓
   GOVERNANCE (interpretation overlay)
