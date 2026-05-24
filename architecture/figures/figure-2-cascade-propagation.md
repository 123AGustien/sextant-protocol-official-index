# Figure 2 — Cascade Propagation Over Time

## Concept

This figure describes how a single shock propagates through the system over time.

---

## Time Evolution

### t0 — Shock Initiation
- Single node failure
- Localised disruption

---

### t1 — Direct Impact
- Immediate neighbours affected
- Load redistribution begins

---

### t2 — Cross-Layer Spread
- Multi-layer propagation begins
- Hidden dependencies activate

---

### t3 — Secondary Failures
- Non-adjacent nodes fail
- Capacity collapse begins

---

### t4 — System Saturation
- Cascade reaches peak spread
- Recovery or collapse begins

---

## State Representation

Each node state:

S_i(t) ∈ {0,1,2}

- 2 = operational
- 1 = degraded
- 0 = failed

---

## Key Insight

Failure is not linear — it is multiplicative across dependency layers.
