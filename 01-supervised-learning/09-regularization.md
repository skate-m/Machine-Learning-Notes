# Regularization

> **Source pages:** 37 (regularized cost function), 35 (regularized linear and logistic regression) · Keeping the parameters $w_j$ small to reduce overfitting.

## 1. Intuition

The source sketches a quadratic fit $w_1x + w_2x^2 + b$ and a wiggly fit $w_1x+w_2x^2+w_3x^3+w_4x^4+b$, and draws an arrow from the wiggly curve to a smoother one.

To make $w_3$ and $w_4$ small, **penalize** them:

$$
\frac{1}{2m}\sum\left(f(x)-y\right)^2 + 1000\,w_3^2 + 1000\,w_4^2
$$

> In order for the cost to be lower, $w_3$ and $w_4$ have to be small, as their coefficient is big.

![Overfit curve versus regularised curve](../assets/figures/regularization-effect.webp)

*Figure: the same overfitting polynomial without and with a penalty on large weights (synthetic data).*

The source also shows how the coefficients change when a curve is smoothed, for example from $f(x)=28x_1-385x_2^2+39x_3^3$ to $f(x)=13x_1-0.23x_2^2+0.000014x_3^3$.

> **Note on the source:** these coefficients are read from the handwriting and could contain misread digits; they only illustrate that large coefficients become small.

## 2. Regularized cost function

If we don't know which $w_j$ to penalize, penalize all of them:

$$
J = \frac{1}{2m}\sum_{i=1}^{m}\left(f(x^{(i)})-y^{(i)}\right)^2 + \underbrace{\frac{\lambda}{2m}\sum_{j=1}^{n}w_j^2}_{\text{regularization term}}
$$

- $\lambda$ is the **regularization parameter**.
- The $2m$ is just for scaling.

## 3. Regularized linear regression

$$
\min_{\vec w,b} J(\vec w,b) = \min_{\vec w,b}\left[\frac{1}{2m}\sum_{i=1}^{m}\left(f(x^{(i)})-y^{(i)}\right)^2 + \frac{\lambda}{2m}\sum_{j=1}^{n}w_j^2\right]
$$

Gradient descent:

$$
w_j = w_j - \alpha\,\frac{\partial J}{\partial w_j},\qquad
\frac{\partial J}{\partial w_j} = \frac{1}{m}\sum_{i=1}^{m}\left(f(x^{(i)})-y^{(i)}\right)x_j^{(i)} + \underbrace{\frac{\lambda}{m}w_j}_{\text{regularized}}
$$

$$
b = b - \alpha\,\frac{\partial J}{\partial b},\qquad
\frac{\partial J}{\partial b} = \frac{1}{m}\sum_{i=1}^{m}\left(f(x^{(i)})-y^{(i)}\right)
$$

## 4. Regularized logistic regression

$$
J = -\frac{1}{m}\sum_{i=1}^{m}\left[y^{(i)}\log\left(f(x^{(i)})\right) + \left(1-y^{(i)}\right)\log\left(1-f(x^{(i)})\right)\right] + \frac{\lambda}{2m}\sum_{j=1}^{n}w_j^2
$$

Gradient descent:

$$
w_j = w_j - \alpha\,\frac{\partial J}{\partial w_j},\qquad
\frac{\partial J}{\partial w_j} = \frac{1}{m}\left(f(x)-y\right)x + \frac{\lambda}{m}w_j
$$

**$b$ is the same** as in the unregularized case.

> **Note on the source:** in the logistic cost the page has no brackets around the two log terms (the minus sign is written only in front of the first), and the derivative is written without a summation sign. Both are completed above in the usual way; see [TRANSCRIPTION_NOTES](../TRANSCRIPTION_NOTES.md).

## 5. Related topics

- Previous: [Overfitting](08-overfitting.md)
- Choosing $\lambda$: [Bias and variance](../03-model-evaluation-and-ml-practice/03-bias-and-variance.md) and [Debugging a learning algorithm](../03-model-evaluation-and-ml-practice/04-learning-curves-and-debugging.md)
- Cost evaluation excludes the regularization term: [Train / cross-validation / test](../03-model-evaluation-and-ml-practice/01-train-cv-test.md)