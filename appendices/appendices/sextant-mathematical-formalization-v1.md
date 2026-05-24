# Sextant Protocol – Mathematical Formalization (v1.0)

## 1. System Representation

The system is defined as a directed weighted graph:

G = (V, E)

Where:
- V = set of nodes (infrastructure entities)
- E = set of directed edges (dependencies between nodes)

Each edge has a weight:

w(i, j) ∈ [0,1]

This represents dependency strength from node i → node j.

---

## 2. Node State Definition

Each node i has a state:

S_i(t) ∈ {0, 1, 2}

Where:
- 0 = failed
- 1 = degraded
- 2 = operational

System state vector:

S(t) = [S_1(t), S_2(t), ..., S_n(t)]

---

## 3. Dependency Load Function

Each node experiences dependency load:

L_i(t) = Σ (w(j, i) × S_j(t))

Where:
- j are upstream nodes affecting node i

---

## 4. Failure Condition

A node transitions state if:

L_i(t) < θ_i

Where:
- θ_i = resilience threshold of node i

If condition is met:
S_i(t+1) → 1 or 0 depending on severity

---

## 5. Propagation Function (Core Dynamics)

System evolution:

S(t+1) = f(S(t), W, θ)

Where:
- W = adjacency matrix
- θ = vector of thresholds
- f = transition rule function

---

## 6. Cascade Definition

A cascade occurs when:

|S(t+1) - S(t)| > 0 across multiple connected nodes
