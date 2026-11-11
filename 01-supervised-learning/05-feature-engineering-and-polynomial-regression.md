# Feature Engineering and Polynomial Regression

> **Source page:** 8 (bottom) · Designing better features, and fitting curves instead of straight lines.

## 1. Feature engineering

**Feature engineering** means using intuition to design new features, by transforming or combining the original features.

**Example (from the source):** instead of taking *length* and *breadth* as two different features, take a single feature **area**.

## 2. Polynomial regression

Use $x^n$ or $\sqrt[n]{x}$ to fit the curve better. Example from the source:

$$
y = w_1x + w_2x^2 + w_3x^3 + b
$$

The source adds: *"Details in course 2 – Adv. learning algorithms."*

## 3. Related topics

- Previous: [Gradient descent in practice](04-gradient-descent-in-practice.md)
- Choosing the degree of the polynomial: [Model selection](../03-model-evaluation-and-ml-practice/02-model-selection.md) and [Bias and variance](../03-model-evaluation-and-ml-practice/03-bias-and-variance.md)