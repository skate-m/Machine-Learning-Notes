# Linear Regression

> **Source page:** 14 · The first topic of *Course I: Supervised ML, Regression and Classification*. Linear regression predicts a number from an input by fitting a straight line.

## 1. The model (univariate)

With a single input feature $x$ the model is a straight line:

$$
f_{w,b}(x) = wx + b
$$

- $w$ is the **weight**.
- $b$ is the **bias**.

*(The source writes the left-hand side as $f(w,b)$.)*

## 2. Cost function

The cost function measures how badly the line fits the data. The goal is to **minimise** it.

$$
J(w,b) = \frac{1}{2m}\sum_{n=0}^{m}\left(f_{w,b}-y\right)^2
$$

> **Note on the source:** the page writes the sum from $n=0$ to $m$ and leaves out the example index on $f$ and $y$. This is preserved above exactly as written.

> **Additional Explanation:**  
> This explanation has been added to improve understanding and is not a direct transcription of the original handwritten notes.  
> The same cost is normally written with the sum running over the $m$ training examples, $i=1,\dots,m$, and with the prediction and target of each example:
> $$J(w,b) = \frac{1}{2m}\sum_{i=1}^{m}\left(f_{w,b}(x^{(i)})-y^{(i)}\right)^2$$
> Each term is the squared gap between the prediction and the true value. This is the form used from here onwards.

## 3. Gradient descent

Gradient descent is the algorithm used to **minimise the cost**. It repeatedly updates both parameters:

$$
w = w - \alpha\,\frac{\partial J(w,b)}{\partial w}
$$

$$
b = b - \alpha\,\frac{\partial J(w,b)}{\partial b}
$$

$\alpha$ is the **learning rate**:

| Learning rate | Effect on step size |
|---|---|
| Large | Step size increases (↑) |
| Small | Step size decreases (↓) |

![Gradient descent with a small and a large learning rate](../assets/figures/gradient-descent-step-size.png)

*Figure: with a small $\alpha$ each step is small; with a large $\alpha$ the steps are big and can overshoot the minimum (illustrative cost, not from the source).*

> **Additional Explanation:**  
> This explanation has been added to improve understanding and is not a direct transcription of the original handwritten notes.  
> Both parameters are normally updated *simultaneously*: compute both partial derivatives with the current $w,b$ first, then assign the new values.

## 4. Related topics

- Next: [Multiple features and vectorization](02-multiple-features-and-vectorization.md)
- How to pick $\alpha$ and check that gradient descent works: [Gradient descent in practice](04-gradient-descent-in-practice.md)