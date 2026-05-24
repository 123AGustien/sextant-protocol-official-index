import numpy as np

class SextantEngine:
    def __init__(self, adjacency_matrix, threshold_vector):
        self.W = np.array(adjacency_matrix)
        self.theta = np.array(threshold_vector)
        self.n = len(threshold_vector)
        self.S = np.ones(self.n) * 2  # all operational

    def compute_load(self):
        return self.W.T @ self.S

    def step(self):
        L = self.compute_load()

        new_S = self.S.copy()

        for i in range(self.n):
            if L[i] < self.theta[i]:
                new_S[i] = max(0, self.S[i] - 1)

        self.S = new_S
        return self.S

    def run(self, steps=10):
        history = [self.S.copy()]
        for _ in range(steps):
            history.append(self.step().copy())
        return np.array(history)
