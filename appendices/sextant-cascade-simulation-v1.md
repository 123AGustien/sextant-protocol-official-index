# Appendix B — Sextant Protocol Cascade Simulation Extension (v1.0)

## 1. Purpose

This appendix extends the Sextant Protocol mathematical formalization by defining how failure propagates dynamically across multi-node systems under iterative simulation steps.

It formalizes cascade evolution beyond static dependency graphs into time-evolving system behavior.

---

## 2. Cascade State Evolution

Let system state be:

S(t) = [S₁(t), S₂(t), ..., Sₙ(t)]

Cascade evolution is defined as:

S(t+1) = F(S(t), W, θ, P)

Where:
- W = dependency matrix
- θ = node thresholds
- P = probabilistic failure vector
- F = transition function

---

## 3. Propagation Kernel

Failure propagation from node i → j:

K(i, j, t) = w(i, j) × P_i(t)

Where:
- K = propagation intensity
- w(i, j) = dependency weight
- P_i(t) = failure probability at time t

---

## 4. Cascade Amplification Rule

A cascade amplifies when:

Σ K(i, j, t) > θ_j

Meaning node j transitions state due to aggregated upstream stress.

---

## 5. Multi-Step Cascade Depth

Cascade depth d is defined recursively:

P_d = P_0 × Π K_k

Where:
- P_0 = initial failure event
- K_k = propagation kernel at step k

---

## 6. Systemic Cascade Condition

A system-wide cascade occurs when:

|S_failed(t)| / |V| ≥ λ

Where:
- λ = cascade activation threshold
- V = total node set

---

## 7. Interpretation

This model captures:

- recursive failure propagation
- multi-hop dependency amplification
- nonlinear system collapse behavior
- delayed cascade activation effects
 Appendix B–C: Cascade Simulation Extension and Control Recovery Dynamics
