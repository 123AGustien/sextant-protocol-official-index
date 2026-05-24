# Appendix C — Sextant Protocol Control & Recovery Dynamics (v1.0)

## 1. Purpose

This appendix defines system stabilization, recovery, and control-layer response mechanisms following cascade propagation events.

It extends the model from failure behavior into post-failure system dynamics.

---

## 2. Control State Function

Define control state:

C(t) ∈ {0,1,2}

Where:
- 0 = no intervention
- 1 = partial stabilization
- 2 = full recovery mode

---

## 3. Recovery Function

System recovery is defined as:

S_i(t+1) = S_i(t) + R_i(t)

Where:

R_i(t) = α × (θ_i - L_i(t))

- α = recovery coefficient
- θ_i = resilience threshold
- L_i(t) = system load

---

## 4. Stabilization Condition

A node stabilizes when:

L_i(t) ≤ θ_i

AND upstream propagation:

K(i, j, t) → 0

---

## 5. Control Trigger Function

Control activates when:

Σ P_i(t) ≥ γ

Where:
- γ = system risk activation threshold

---

## 6. Isolation Response Model

When cascade exceeds threshold:

I(t) = isolate({nodes | P_i(t) > δ})

Where:
- δ = isolation threshold
- I(t) = isolation set

---

## 7. System Recovery Phases

Recovery is modeled in 3 phases:

### Phase 1 — Containment
- stop propagation
- isolate failing nodes

### Phase 2 — Stabilization
- reduce load pressure
- restore partial node states

### Phase 3 — Reintegration
- reconnect isolated nodes
- restore full system graph

---

## 8. Interpretation

This model formalizes:

- system recovery after cascade failure
- control-layer intervention logic
- isolation and reintegration behavior
- resilience feedback loops
