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
