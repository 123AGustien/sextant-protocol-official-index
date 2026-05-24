import numpy as np

class SextantEngine:
    def __init__(self, adjacency_matrix, threshold_vector, beta=1.5):
        self.W = np.array(adjacency_matrix, dtype=float)
        self.theta = np.array(threshold_vector, dtype=float)
        self.beta = beta

        self.n = len(threshold_vector)

        # 2 = operational, 1 = degraded, 0 = failed
        self.S = np.ones(self.n) * 2

    # -----------------------------
    # Load function: L_i(t)
    # -----------------------------
    def compute_load(self):
        return self.W.T @ self.S

    # -----------------------------
    # Sigmoid function σ(x)
    # -----------------------------
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-self.beta * x))

    # -----------------------------
    # Probabilistic failure model
    # P_i(t)
    # -----------------------------
    def compute_failure_prob(self, L):
        return self.sigmoid(L - self.theta)

    # -----------------------------
    # State update rule (deterministic + probabilistic)
    # -----------------------------
    def step(self):
        L = self.compute_load()
        P = self.compute_failure_prob(L)

        new_S = self.S.copy()

        for i in range(self.n):

            # deterministic degradation
            if L[i] < self.theta[i]:
                new_S[i] = max(0, self.S[i] - 1)

            # probabilistic collapse layer
            if P[i] > 0.85:
                new_S[i] = 0
            elif P[i] > 0.5:
                new_S[i] = max(0, self.S[i] - 1)

        self.S = new_S
        return self.S, P

    # -----------------------------
    # Run full cascade simulation
    # -----------------------------
    def run(self, steps=10):
        history = []

        for t in range(steps):
            S, P = self.step()

            history.append({
                "step": t,
                "state": S.copy(),
                "probability": P.copy()
            })

        return history
