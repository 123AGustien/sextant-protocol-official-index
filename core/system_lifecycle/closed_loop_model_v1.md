# 🔁 Closed-Loop Resilience Model v1
## Sextant Protocol Index Layer

---

# 🧭 Purpose

This model defines the transition from linear simulation to adaptive system behavior.

---

# ⚙️ System Flow (Before)

Dependency → Failure → Cascade → Output

---

# 🔁 System Flow (After Upgrade)

Dependency → Failure → Cascade → Observation → Governance Decision → Recovery → New State

---

# 📡 Closed-Loop Components

## 1. Observation Layer
- Collects cascade output
- Records system state after failure propagation

## 2. Severity Scoring Layer
- Converts cascade impact into numerical risk index
- Uses:
  - Dependency Strength (DS)
  - Propagation Sensitivity (PS)
  - Coupling Density (CD)
  - Observability Delay (OD)

Formula:
RI = (DS × PS × CD) / OD

---

## 3. Governance Decision Layer
- Evaluates risk score
- Produces decision:
  - APPROVE
  - ISOLATE
  - RESTRICT
  - BLOCK

---

## 4. Recovery Layer
- Adjusts node states after decision
- Restores or isolates system components

---

## 5. State Update Layer
- Writes new system baseline
- Feeds into next simulation cycle

---

# 🧠 Key Principle

The system is no longer linear.

It is:
> iterative, adaptive, and feedback-driven

---

# ⚠️ Constraint Rule

Governance does not execute.
Engine does not decide.
Index defines structure of both.
