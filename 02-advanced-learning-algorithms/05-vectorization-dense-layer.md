# For Loop versus Vectorization (Dense Layer)

> **Source page:** 26 · The same Dense layer written with a loop and with matrix operations.

## 1. Example data

```python
x = np.array([200, 17])
W = np.array([[1, -3, 5],
              [-2, 4, -6]])
b = np.array([-1, 1, 2])
```

> **Note on the source:** the bracket nesting of `x` and `b` is not fully clear on the page ([UNCLEAR IN SOURCE], p. 26). The values $200, 17$, the matrix $W$ and the bias $-1, 1, 2$ are as written.

## 2. Loop method

```python
def Dense(a_in, W, b):
    units = W.shape[1]
    a_out = np.zeros(units)
    for j in range(units):
        w = W[:, j]
        z = np.dot(w, a_in) + b[j]
        a_out[j] = g(z)
    return a_out
```

## 3. Vectorized method

```python
def dense(A_in, W, B):
    Z = np.matmul(A_in, W) + B
    A_out = g(Z)
    return A_out
```

> **Note (from the source):** knowledge of what is going on under the hood is useful, but use TensorFlow to create models. The activation function `g` is not defined on the page.

## Detailed Explanation

> **Additional Explanation:**  
> This explanation has been added to improve understanding and is not a direct transcription of the original handwritten notes.
>
> **What a Dense layer does.** Every unit in the layer takes all the inputs, multiplies by its own weights, adds its own bias and applies $g$. Putting the weights of all units side by side as the columns of a matrix $W$ lets us do all units at once.
>
> **Following the example numbers.** Take $x = [200, 17]$, $W$ with columns $[1,-2]$, $[-3,4]$, $[5,-6]$ and $b=[-1,1,2]$. (`W.shape[1]` is 3, so there are 3 units.)
>
> - Unit 1: $200(1) + 17(-2) - 1 = 165$
> - Unit 2: $200(-3) + 17(4) + 1 = -531$
> - Unit 3: $200(5) + 17(-6) + 2 = 900$
>
> So $z = [165, -531, 900]$. If $g$ is the sigmoid, the outputs are about $[1,\ 0,\ 1]$.
>
> **Why the matrix version is better.** The loop version handles one unit at a time. The `np.matmul` version computes all units in one operation, which is much faster and is what real libraries do.
>
> **Shapes to keep in mind.** `A_in` has shape (examples, inputs), `W` has shape (inputs, units), so `Z` has shape (examples, units).
>
> **Common mistakes.**
>
> - Mixing up the order in `np.matmul(A_in, W)`. The inner dimensions must match.
> - Forgetting that `g` must be defined; the page does not define it.

## 4. Related topics

- Previous: [Multiclass and softmax](04-multiclass-and-softmax.md)
- Next: [TensorFlow and model training steps](06-tensorflow-and-training-steps.md)
- Vectorization for linear regression: [Multiple features and vectorization](../01-supervised-learning/02-multiple-features-and-vectorization.md)