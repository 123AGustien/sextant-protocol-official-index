# Appendix D — Sextant Protocol Economic Coupling Model (v1.0)

## 1. Purpose

This appendix extends the Sextant Protocol into macroeconomic systems by modeling how infrastructure-level failures propagate into economic variables through coupling mechanisms.

---

## 2. Economic State Variables

Define economic system vector:

E(t) = {GDP, L, C, I, X, M}

Where:
- GDP = output level
- L = liquidity
- C = consumption
- I = investment
- X = exports
- M = imports

---

## 3. Coupling Function

Economic coupling to system failure:

EC_i(t) = α × S_i(t) × β_i

Where:
- S_i(t) = infrastructure stress state
- α = transmission coefficient
- β_i = sector sensitivity factor

---

## 4. Shock Transmission Model

Economic shock propagation:

ΔE(t) = Σ EC_i(t)

Meaning:
Infrastructure stress aggregates into macroeconomic deviation.

---

## 5. Nonlinear Amplification

When coupling exceeds threshold:

EC_i(t) > θ_e

Then:

ΔE(t) → exponential response

---

## 6. Interpretation

This model links:

- infrastructure stress → economic output distortion
- system failures → macroeconomic volatility
- cascade propagation → GDP instability risk
