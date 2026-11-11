# Linear Regression with Multiple Features

> **Source page:** 18 · Extends the model to $n$ features and introduces vectorization (the source's item "4) LR with multiple features").

## 1. The model

$$
f_{\vec w,b}(\vec x) = w_1x_1 + w_2x_2 + \dots + w_nx_n + b
$$

This can be written compactly as a dot product:

$$
f_{\vec w,b}(\vec x) = \vec w\cdot\vec x + b
$$

In NumPy the dot product is `np.dot()`.

> **Note:** the cost function remains the same (see [Linear Regression](01-linear-regression.md)).

## 2. Vectorization

Vectorization replaces the explicit loop with a single dot-product call.

```python
# Before (loop)
f = 0
for i in range(0, n):
    f += w[i] * x[i]
f += b

# After (vectorized)
np.dot(w, x)
```

> **Note on the source:** the "After" column of the page shows only `np.dot(w, x)`. The bias $b$ is part of the model above, so it still has to be added to the result.

## 3. Gradient descent for multiple features

Every feature has a different weight, so every weight gets its own update:

$$
w_1 = w_1 - \alpha\,\frac{1}{m}\sum_{i=1}^{m}\left(f_{\vec w,b}(\vec x^{(i)})-y^{(i)}\right)x_1^{(i)}
$$

$$
\vdots
$$

$$
w_n = w_n - \alpha\,\frac{1}{m}\sum_{i=1}^{m}\left(f_{\vec w,b}(\vec x^{(i)})-y^{(i)}\right)x_n^{(i)}
$$

## 4. Related topics

- Next: [Feature scaling](03-feature-scaling.md)
- Vectorization of a neural-network layer: [Vectorization of a Dense layer](../02-advanced-learning-algorithms/05-vectorization-dense-layer.md)