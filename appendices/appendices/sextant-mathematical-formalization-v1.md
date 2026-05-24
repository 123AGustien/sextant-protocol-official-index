# Sextant Protocol – Mathematical Formalization (v1.0)

## 1. System Representation

The system is defined as a directed weighted graph:

G = (V, E)

Where:
- V = set of nodes (infrastructure entities)
- E = set of directed edges (dependencies between nodes)

Each edge has a weight:

w(i, j) ∈ [0,1]

representing dependency strength from node i → node j.

---

## 2. Node State Definition

Each node i has a discrete state:

S_i(t) ∈ {0, 1, 2}

Where:
- 0 = failed
- 1 = degraded
- 2 = operational

System state vector:

S(t) = [S_1(t), S_2(t), ..., S_n(t)]

---

## 3. Dependency Load Function

Each node experiences a dependency load:

L_i(t) = Σ w(j, i) × S_j(t)

Where:
- j are upstream nodes influencing node i

---

## 4. Deterministic Failure Condition

A node transitions to a lower state when:

L_i(t) < θ_i

Where:
- θ_i = resilience threshold of node i

---

## 5. Propagation Function (Deterministic Form)

System evolution:

S(t+1) = f(S(t), W, θ)

Where:
- W = adjacency matrix
- θ = threshold vector
- f = transition rule function

---

## 6. Cascade Definition

A cascade event occurs when multiple connected nodes experience state transitions:

|S(t+1) - S(t)| > 0 across connected components

---

# PHASE 2 — PROBABILISTIC EXTENSION

## 7. Probabilistic Failure Model

Node failure is modeled probabilistically:

P_i(t) = Pr(node i fails at time t)

We define:

P_i(t+1) = σ(L_i(t) - θ_i)

---

## 8. Sigmoid Activation Function

σ(x) is defined as:

σ(x) = 1 / (1 + e^{-βx})

Where:
- β = sensitivity coefficient
- High β → abrupt failure transition
- Low β → gradual degradation

---

## 9. Edge Propagation Probability

Failure propagation across edges is defined as:

P(i → j) = w(i,j) × P_i(t)

Where:
- w(i,j) = dependency weight
- P_i(t) = upstream failure probability

---

## 10. Multi-Step Cascade Probability

Cascade probability across a path of length k:

P_cascade(k) = ∏ P(node transitions along cascade path)

This captures:
- multi-hop propagation risk
- deep system vulnerability chains

---

## 11. Expected System Failure Metric

System-wide expected failure:

E[F(t)] = Σ P_i(t)

Where:
- higher values indicate increased systemic fragility

---

## 12. Interpretation Summary

This model captures two layers of system behavior:

Deterministic layer:
- structural dependency failure
- threshold-based collapse

Probabilistic layer:
- uncertainty in failure timing
- stochastic cascade propagation
- nonlinear amplification effects

---

## END OF FORMALIZATION v1.0
