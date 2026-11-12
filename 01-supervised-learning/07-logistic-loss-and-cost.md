# Logistic Loss, Cost and Gradient Descent

> **Source pages:** 2 (logistic loss, simplified loss), 3 (bottom, why MSE cannot be used), 5 (cost and gradient descent) · The loss and cost used for logistic regression.

## 1. Logistic loss (log loss)

For one training example the loss is

$$
L\left(f_{\vec w,b}(\vec x^{(i)}),\,y^{(i)}\right) =
\begin{cases}
-\log\left(f_{\vec w,b}(\vec x^{(i)})\right) & \text{if } y^{(i)}=1\\[4pt]
-\log\left(1-f_{\vec w,b}(\vec x^{(i)})\right) & \text{if } y^{(i)}=0
\end{cases}
$$

### Why $-\log$?

The source's sketch of $-\log(f)$ and the notes beside it say (for the case $y^{(i)}=1$):

- As $f_{\vec w,b}(\vec x^{(i)}) \to 1$, the loss $\to 0$.
- As $f_{\vec w,b}(\vec x^{(i)}) \to 0$, the loss $\to \infty$.

**Therefore the loss is lowest when $f_{\vec w,b}(\vec x)$ predicts close to the true label $y^{(i)}$.**

![Log loss curves for y=1 and y=0](../assets/figures/log-loss.png)

*Figure: $-\log(f)$ (for $y=1$) and $-\log(1-f)$ (for $y=0$). Each is near 0 when the prediction matches the label and grows very large when it does not.*

## 2. Simplified loss function

The two cases combine into one expression:

$$
L\left(f_{\vec w,b}(\vec x^{(i)}),\,y^{(i)}\right) = -y^{(i)}\log\left(f_{\vec w,b}(\vec x)\right) - \left(1-y^{(i)}\right)\log\left(1-f_{\vec w,b}(\vec x)\right)
$$

> **Additional Explanation:**  
> This explanation has been added to improve understanding and is not a direct transcription of the original handwritten notes.  
> When $y^{(i)}=1$ the second term vanishes, and when $y^{(i)}=0$ the first term vanishes, so this single line reproduces both cases above.

## 3. Why we cannot take MSE as the cost function

The source compares the shape of the cost curve:

| Model | Cost | Shape |
|---|---|---|
| Linear regression | squared error | **Convex** |
| Logistic regression | squared error | **Non-convex** (many bumps) |

A non-convex cost has several dips, so gradient descent can get stuck. This is why the log loss above is used instead.

![Convex versus non-convex cost](../assets/figures/mse-convex-vs-nonconvex.png)

*Figure: schematic redrawing of the source's two sketches.*

## 4. Cost function

$$
J(\vec w,b) = -\frac{1}{m}\sum_{i=1}^{m}\left[y^{(i)}\log\left(f(\vec x^{(i)})\right) + \left(1-y^{(i)}\right)\log\left(1-f(\vec x^{(i)})\right)\right]
$$

> **Note on the source:** on the page the superscripts $(i)$ are not written on every term (for example $f(x)$ instead of $f(x^{(i)})$). They are added here for consistency.

## 5. Gradient descent

$$
\text{repeat}\ \{
$$

$$
w_j = w_j - \alpha\,\frac{\partial J}{\partial w_j}\quad(j=1,2,3,\dots,n)
\qquad
b = b - \alpha\,\frac{\partial J}{\partial b}
$$

$$
\}
$$

with the derivatives written in the source as

$$
\frac{\partial J}{\partial w_j} = \frac{1}{m}\sum_{i=1}^{m}\left(f(\vec x^{(i)})-y^{(i)}\right)x_j^{(i)}
\qquad
\frac{\partial J}{\partial b} = \frac{1}{m}\sum_{i=1}^{m}\left(f(\vec x^{(i)})-y^{(i)}\right)
$$

where

$$
f(\vec x) = \frac{1}{1+e^{-(\vec w\cdot\vec x+b)}}
$$

> **Additional Explanation:**  
> This explanation has been added to improve understanding and is not a direct transcription of the original handwritten notes.  
> These updates look the same as those of linear regression; the difference is the definition of $f$, which here is the sigmoid of $\vec w\cdot\vec x+b$.

## Detailed Explanation

> **Additional Explanation:**  
> This explanation has been added to improve understanding and is not a direct transcription of the original handwritten notes.
>
> **What the output means.** For logistic regression, $f_{\vec w,b}(\vec x)$ is the model's belief, as a number between 0 and 1, that the label is 1. The loss should be small when that belief agrees with the real label and large when it does not.
>
> **Worked examples (natural logarithm).**
>
> | True $y$ | Prediction $f$ | Loss |
> |---|---|---|
> | 1 | 0.99 | $-\ln(0.99) \approx 0.01$ (very small) |
> | 1 | 0.90 | $-\ln(0.90) \approx 0.105$ |
> | 1 | 0.10 | $-\ln(0.10) \approx 2.30$ (large) |
> | 0 | 0.10 | $-\ln(0.90) \approx 0.105$ |
> | 0 | 0.99 | $-\ln(0.01) \approx 4.6$ (very large) |
>
> Being confidently wrong is punished very heavily. Being unsure costs a little. That is exactly the behaviour we want.
>
> **A tiny cost calculation.** Two examples: $(f=0.9,\ y=1)$ and $(f=0.2,\ y=0)$. The losses are $0.105$ and $-\ln(0.8)=0.223$. So $J = (0.105 + 0.223)/2 \approx 0.164$.
>
> **Why not squared error.** With the sigmoid inside, squared error produces a bumpy surface with many flat regions and dips, so gradient descent can stall. The log loss gives a single bowl-shaped (convex) surface, so one global minimum is reachable.
>
> **Common mistakes.**
>
> - Using $\log(0)$. A prediction of exactly 0 or 1 that is wrong gives infinite loss, so numerical code keeps $f$ slightly away from 0 and 1.
> - Using the linear-regression formula for $f$. Here $f$ is the sigmoid of $\vec w\cdot\vec x+b$.

## 6. Related topics

- Previous: [Decision boundary](06-decision-boundary.md)
- Next: [Overfitting](08-overfitting.md)
- The same loss written in code: [TensorFlow and model training steps](../02-advanced-learning-algorithms/06-tensorflow-and-training-steps.md)