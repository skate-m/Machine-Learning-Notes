# Train / Cross-validation / Test Procedure

> **Source pages:** 52 and 53 (identical pages) · How the cost is computed on the training, cross-validation and test sets.

## 1. Train/test procedure for linear regression (MSE) — "not ideal"

The source labels this first procedure *not ideal* (it has only two sets). Fit the parameters by minimising the cost $J$:

$$
J = \frac{1}{2m_{train}}\sum_{i=1}^{m_{train}}\left(f(\vec x^{(i)})-y^{(i)}\right)^2 + \frac{\lambda}{2m_{train}}\sum w_j^2
$$

**Test error:**

$$
J_{test} = \frac{1}{2m_{test}}\left[\sum_{i=1}^{m_{test}}\left(f_{\vec w,b}\left(\vec x_{test}^{(i)}\right)-y_{test}^{(i)}\right)^2\right]
$$

The training error $J_{train}$ is computed in the same way.

> **Note (from the source):** apply the same logic for classification.

## 2. Train / cross-validation / test procedure

Calculate the cost for all three sets similarly, **without the regularization term in any of them**. The new term is the cross-validation cost:

$$
J_{cv} = \frac{1}{2m_{cv}}\left[\sum_{i=1}^{m_{cv}}\left(f\left(\vec x_{cv}^{(i)}\right)-y_{cv}^{(i)}\right)^2\right]
$$

> **Note on the source:** the cost $J$ in section 1 contains the regularization term, while the instruction in section 2 says to evaluate the errors without it. Both statements are on the page. The regularization term belongs to the function that is *minimised* during fitting; the *reported* errors $J_{train}$, $J_{cv}$, $J_{test}$ leave it out.

## Detailed Explanation

> **Additional Explanation:**  
> This explanation has been added to improve understanding and is not a direct transcription of the original handwritten notes.
>
> **Why not use all the data for training?** A model can look perfect on the data it was trained on simply because it memorised it. To know how it will behave on *new* data, you must keep some data aside that the model never trained on.
>
> **The three sets and their jobs.**
>
> | Set | Used for |
> |---|---|
> | Training set | Fit the parameters $w,b$ |
> | Cross-validation (CV) set | Choose between models (degree, $\lambda$, network size) |
> | Test set | One final, honest estimate of performance |
>
> A common way to split is about 60% / 20% / 20%, though the exact split depends on how much data you have.
>
> **A tiny worked example.** Three test examples with predictions $f=[2,3,5]$ and true values $y=[2,4,3]$. The errors are $0,-1,2$, the squares $0,1,4$ (sum $5$), so $J_{test} = 5/(2\cdot3)\approx 0.83$.
>
> **Why the regularization term is left out when reporting errors.** The term $\frac{\lambda}{2m}\sum w_j^2$ is a tool to keep the weights small *while fitting*. It is not part of how wrong the predictions are. The reported errors $J_{train}$, $J_{cv}$, $J_{test}$ only measure the prediction mistakes, so they can be compared fairly between models with different $\lambda$.
>
> **How to read the results.** If $J_{train}$ is low but $J_{cv}$ is much higher, the model is overfitting. If both are high, it is underfitting (see [Bias and variance](03-bias-and-variance.md)).
>
> **Common mistake.** Tuning the model while looking at the test set. Then the test set is no longer unseen, and its score looks better than reality.

## 3. Related topics

- Next: [Model selection](02-model-selection.md)
- The regularization term: [Regularization](../01-supervised-learning/09-regularization.md)