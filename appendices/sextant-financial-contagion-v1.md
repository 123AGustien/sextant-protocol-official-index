# Appendix E — Cross-Border Financial Contagion Layer (v1.0)

## 1. Purpose

This appendix models how financial instability propagates across borders through interconnected banking, trade, and liquidity networks.

---

## 2. Network Representation

Define global financial network:

G_f = (N, L)

Where:
- N = financial institutions / economies
- L = exposure links (credit, trade, FX, derivatives)

---

## 3. Exposure Matrix

Define exposure:

X(i, j) ∈ [0,1]

Where:
- i = source economy
- j = exposed economy

---

## 4. Contagion Function

Financial stress propagation:

F_j(t+1) = F_j(t) + Σ X(i,j) × F_i(t)

---

## 5. Default Cascade Condition

Default occurs when:

F_j(t) ≥ θ_j

Leading to:
- credit tightening
- liquidity withdrawal
- cross-border shock transmission

---

## 6. Systemic Contagion Trigger

Global contagion occurs when:

Σ F_j(t) / |N| ≥ λ_f

---

## 7. Interpretation

This model captures:

- cross-border shock transmission
- financial network fragility
- systemic global cascade risk
