# Sextant Protocol – Risk Scoring Engine (v1.0)

## 1. Purpose

This document defines a **quantitative scoring model** for evaluating systemic risk signals within the Sextant Protocol framework.

It converts qualitative risk signals into structured comparative metrics.

This is a modelling tool, not a predictive or operational system.

---

## 2. Core Scoring Dimensions

Each risk signal is evaluated across three axes:

### 2.1 Severity (S)
Measures potential system impact if the risk materialises.

Scale:
- 1 = minimal impact  
- 5 = moderate system disruption  
- 10 = critical system-wide failure potential  

---

### 2.2 Propagation (P)
Measures how quickly and widely a risk can spread across system layers.

Scale:
- 1 = isolated/local  
- 5 = multi-component spread  
- 10 = cross-domain cascading propagation  

---

### 2.3 Detectability (D)
Measures how easily the risk can be observed before or during propagation.

Scale:
- 1 = highly visible / easily detected  
- 5 = partially observable  
- 10 = low visibility / delayed detection  

---

## 3. Risk Index Formula

Each risk is assigned a composite score:


---

## 4. Interpretation Model

| Risk Index Range | Classification |
|-----------------|----------------|
| 1 – 5           | Low Structural Risk |
| 6 – 20          | Moderate Structural Risk |
| 21 – 50         | High Structural Risk |
| 51+             | Critical Structural Risk |

---

## 5. Application to Existing Risk Signals

### 5.1 Cascading Dependency Amplification
- Severity: 8  
- Propagation: 9  
- Detectability: 6  
- RI = 12.0  

---

### 5.2 Observability Lag Under AI Complexity
- Severity: 7  
- Propagation: 8  
- Detectability: 9  
- RI = 6.22  

---

### 5.3 Infrastructure–Decision Layer Convergence
- Severity: 9  
- Propagation: 8  
- Detectability: 7  
- RI = 10.28  

---

## 6. System Insight

The model highlights a key structural property:

> Risks with moderate severity but high propagation and low detectability dominate systemic instability.

---

## 7. Relationship to Architecture

This scoring engine integrates with:

- Risk Signal Register → qualitative definitions  
- Cascade Layer → propagation modelling  
- Observability Layer → detection constraints  
- Executive Layer → summarisation of risk posture  

---

## 8. Intended Use

This engine is intended for:

- comparative risk analysis  
- infrastructure resilience research  
- system dependency evaluation  
- scenario modelling and stress testing  

---

## 9. Closing Statement

The Risk Scoring Engine provides a structured method for quantifying systemic risk within the Sextant Protocol framework, enabling consistent comparison across heterogeneous risk conditions. 
