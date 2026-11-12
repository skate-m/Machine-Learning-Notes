# Model Selection

> **Source page:** 51 · Choosing between candidate models using the cross-validation cost.

## 1. Candidate models

Try polynomial models of increasing degree and compute the cross-validation cost $J_{cv}$ for each:

1. $f_{\vec w,b}(x) = w_1x + b \ \longrightarrow\ J_{cv}\left(w^{\langle1\rangle},b^{\langle1\rangle}\right)$
2. $f_{\vec w,b}(x) = w_1x + w_2x^2 + b \ \longrightarrow\ J_{cv}\left(w^{\langle2\rangle},b^{\langle2\rangle}\right)$
3. $f_{\vec w,b}(x) = w_1x + w_2x^2 + w_3x^3 + b$
4. $\vdots$
5. $f_{\vec w,b}(x) = w_1x + w_2x^2 + \dots + w_{10}x^{10} + b$

(The source numbers the last model "10".)

## 2. The rule

**Pick the model that gives the lowest cross-validation (CV) set cost.**

> **Note (translated from the source):** the page is written partly in Hinglish. The rule reads: *"Whichever model gives the lowest CV cost, pick that model."* The postscript reads: *"If we check the cost on the test data and take the lowest cost, then [we get] overfitting. Train data, negligible cost, underfit."* The original wording is quoted in [TRANSCRIPTION_NOTES](../TRANSCRIPTION_NOTES.md).

> **Note on the source:** the last sentence of the postscript says that picking by the training cost (which is negligible for a complex model) gives *underfit*. A negligible training cost normally signals an *overfit* model, so this statement may be a slip. It is preserved as written.

## 3. Using the method for neural networks

> **Note (from the source):** use the same method also to find out which neural network works best. "Use miscalculated outputs as cost."

> **Additional Explanation:**  
> This explanation has been added to improve understanding and is not a direct transcription of the original handwritten notes.  
> The last line is read as: for a classifier, the cost used to compare networks can be the fraction of wrongly predicted examples.

## Detailed Explanation

> **Additional Explanation:**  
> This explanation has been added to improve understanding and is not a direct transcription of the original handwritten notes.
>
> **The question.** Should the model be a straight line, a quadratic, a cubic ... or a degree-10 polynomial? Training error cannot answer this: it will almost always prefer the most complex model.
>
> **The procedure, step by step.**
>
> 1. Fit each candidate model on the **training** set.
> 2. Compute the cross-validation cost $J_{cv}$ of each one.
> 3. Pick the model with the **lowest** $J_{cv}$.
> 4. Only now measure $J_{test}$ of that one model, to report how well it should do on new data.
>
> **Example with made-up numbers** (to show the idea only):
>
> | Degree | 1 | 2 | 3 | 4 |
> |---|---|---|---|---|
> | $J_{cv}$ | 0.90 | 0.35 | 0.30 | 0.42 |
>
> The lowest value is at degree 3, so degree 3 is chosen. Degree 4 is more flexible but does worse on the CV set, which suggests it has started to overfit.
>
> **Why the test set must not be used for choosing.** If you pick the model that looks best on the test set, the test set has helped decide, so its score is slightly too optimistic. This is what the source's postscript warns about. Keeping the CV set for choosing and the test set for a final check avoids it.
>
> **Other things you can choose this way.** The same method works for the regularization parameter $\lambda$, the number of features, and the size of a neural network. For a classifier, the fraction of wrongly classified examples can be used as the cost.
>
> **Common mistake.** Choosing the model by training cost. A very flexible model has almost zero training cost even when it is overfit.

## 4. Related topics

- Previous: [Train / cross-validation / test](01-train-cv-test.md)
- Next: [Bias and variance](03-bias-and-variance.md)