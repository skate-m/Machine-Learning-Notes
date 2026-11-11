# Overfitting

> **Source page:** 4 · What goes wrong when a model fits the training data too closely, and three ways to overcome it.

## 1. Regression example

The source draws the same data fitted three ways:

| Fit | Label in the source | What it means |
|---|---|---|
| Straight line that misses the pattern | **Underfit** — high bias | The model is too simple. |
| Smooth curve through the data | **Generalized** — ideal | Fits the pattern and should work on new data. |
| Wiggly curve through every point | **Overfit** — high variance | The model memorises the training data. |

![Underfit, generalised and overfit regression fits](../assets/figures/underfit-generalised-overfit.png)

*Figure: the three cases from the source, redrawn with synthetic data.*

## 2. How to overcome overfitting

1. **Collecting more training samples** — with more data the fitted curve becomes smoother.
2. **Selecting features / reducing features.**
3. **Regularization** — reduce the size of the parameters $w_j$.

*(The source marks "diagrams →" next to item 3, pointing to the sketches in [Regularization](09-regularization.md).)*

## 3. Related topics

- Next: [Regularization](09-regularization.md)
- Diagnosing bias and variance: [Bias and variance](../03-model-evaluation-and-ml-practice/03-bias-and-variance.md)