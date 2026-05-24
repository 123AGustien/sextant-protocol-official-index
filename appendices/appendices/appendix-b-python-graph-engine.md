# 🧮 Appendix B — Python Graph Engine (Cascade Simulation)

## Overview

This appendix implements the Sextant Protocol mathematical formalization (Appendix B) as a computational simulation engine.

It translates:

- Graph structure (G = V, E)
- Dependency weights (W)
- Node state vectors (S)
- Probabilistic failure dynamics
- Cascade propagation rules

into a deterministic + probabilistic Python simulation.

---

# 🧠 1. System Representation

We define the system as a directed weighted graph:

G = (V, E)

Where:
- V = nodes (infrastructure entities)
- E = directed dependencies between nodes

Represented in Python using an adjacency matrix:

```python
import numpy as np

# Node states:
# 0 = failed
# 1 = degraded
# 2 = operational

S = np.array([2, 2, 2, 2])
