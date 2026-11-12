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

## Detailed Explanation

> **Additional Explanation:**  
> This explanation has been added to improve understanding and is not a direct transcription of the original handwritten notes.
>
> **Why more than one feature.** A house price depends on size, but also on the number of bedrooms, the number of floors and the age. Each feature $x_j$ gets its own weight $w_j$. A large positive weight means "this feature pushes the price up"; a negative weight means it pushes it down.
>
> **Worked example (made-up numbers).** Let $\vec w = [0.1,\ 4,\ 10,\ -2]$, $b = 80$ and a house $\vec x = [2104,\ 5,\ 1,\ 45]$ (size, bedrooms, floors, age).
>
> $$ f = 0.1(2104) + 4(5) + 10(1) + (-2)(45) + 80 = 210.4 + 20 + 10 - 90 + 80 = 230.4 $$
>
> **Why the dot product notation helps.** Writing $\vec w\cdot\vec x + b$ replaces a long sum with a short expression. It also means the same formula works for 2 features or 2 million.
>
> **Why vectorization is faster.** The loop in the notes multiplies one pair at a time. `np.dot` hands the whole job to optimised code that can multiply many pairs at once on modern hardware. The result is the same, but it can be many times faster, which matters a lot with large data.
>
> **Gradient descent with many features.** The rule is the same as before, applied once per weight. The only thing that changes is the last factor, $x_j^{(i)}$, which is the value of the $j$-th feature in the $i$-th example. A feature that is large in an example makes the matching weight change more.
>
> **Common mistakes.**
>
> - Mixing up $x_j^{(i)}$: the *bottom* index is the feature, the *top* index in brackets is the example.
> - Forgetting the bias $b$ after calling `np.dot(w, x)`.
> - Updating the weights one after another instead of all together.

## 4. Related topics

- Next: [Feature scaling](03-feature-scaling.md)
- Vectorization of a neural-network layer: [Vectorization of a Dense layer](../02-advanced-learning-algorithms/05-vectorization-dense-layer.md)