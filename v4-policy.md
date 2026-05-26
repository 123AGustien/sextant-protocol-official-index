# 🛡️ Sextant Protocol – Guard Layer V4 Policy (Enterprise CI Governance Ruleset)

---

## 1. Purpose

Guard Layer V4 defines a stable CI/CD governance architecture designed to eliminate infinite workflow failure loops while maintaining auditability and safe operational control.

It separates execution, detection, and compliance into independent layers to ensure system stability.

---

## 2. System Architecture Overview

V4 introduces a controlled governance structure:

- Orchestrator Layer → system execution only  
- Guard Layer → anomaly detection and optional enforcement  
- Audit Layer → logging and traceability only  
- Policy Layer → defines operational rules (this document)

---

## 3. Problem Statement (Resolved in V4)

Earlier versions (V2/V3) caused:

- Continuous CI failure loops  
- Re-triggering of guard workflows on the same state  
- Conflicting enforcement between workflows  
- Instability during merge or workflow updates  

**Root cause:**  
`.github/workflows/*` triggers caused recursive enforcement cycles.

---

## 4. Core Design Principles

### 4.1 No Infinite Failure Loops
- CI must never repeatedly fail on the same state  
- Each event must be processed once per pipeline execution  

---

### 4.2 Safe Mode First Principle

System must support:

- **SAFE mode** → logging only, no enforcement  
- **MAINTENANCE mode** → full bypass of enforcement logic  
- **NORMAL mode** → controlled execution with optional checks  

---

### 4.3 Separation of Concerns

| Layer        | Responsibility |
|--------------|----------------|
| Orchestrator | Executes workflows and simulations |
| Guard        | Detects anomalies and workflow changes |
| Audit        | Records logs and system state |
| Policy       | Defines governance rules |

---

### 4.4 Controlled Enforcement

Enforcement (blocking/failing CI) is only allowed when:

- `STRICT_MODE = true`
- Event is `push` or approved `pull_request`
- `SAFE_MODE` is not active

---

### 4.5 Maintenance Mode Rule

When SAFE_MODE or MAINTENANCE is active:

- No failures allowed  
- No blocking actions  
- Only logging permitted  
- System must continue execution  

---

## 5. CI/CD Stability Rules

To prevent recursion and CI loops:

- Avoid enforcing rules on `.github/workflows/**` without conditions  
- Use conditional logic to prevent repeated triggers  
- Ensure guard logic does not re-trigger itself infinitely  

---

## 6. Security & Governance Model

This system operates as a governance validation layer only.

It does NOT:

- control production infrastructure  
- execute external deployments  
- modify enterprise systems directly  

It DOES:

- validate workflow integrity  
- log system state changes  
- support audit and compliance review  

---

## 7. Enterprise Architecture Mapping

```text
Enterprise Systems
      ↓
CI/CD Execution Layer
      ↓
Sextant Guard V4 Governance Layer
      ↓
Audit & Logging Layer
      ↓
Human Compliance Review
