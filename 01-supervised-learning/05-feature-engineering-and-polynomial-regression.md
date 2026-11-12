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

## Detailed Explanation

> **Additional Explanation:**  
> This explanation has been added to improve understanding and is not a direct transcription of the original handwritten notes.
>
> **Feature engineering in plain words.** The columns you are given are not always the best way to describe the problem. If a house has a *length* and a *breadth*, the price probably depends on the *area*, which is length $\times$ breadth. Giving the model the area directly makes its job easier, because it does not have to discover the product by itself. This is how your own knowledge of the problem improves the model.
>
> **Why polynomial regression is still "linear".** The model $y = w_1x + w_2x^2 + w_3x^3 + b$ is a curve in $x$, but it is still a straight combination of the *features* $x$, $x^2$ and $x^3$. So the same linear-regression machinery (cost function and gradient descent) works. You just treat $x^2$ and $x^3$ as extra features.
>
> **Choosing the shape.** If the data bends up and then flattens, $x$ and $\sqrt{x}$ together may fit better than $x$ and $x^2$. Different powers give different curves, and you can compare them with the cross-validation cost (see [Model selection](../03-model-evaluation-and-ml-practice/02-model-selection.md)).
>
> **An important link to scaling.** If $x$ goes from 1 to 1000, then $x^2$ goes up to $10^6$ and $x^3$ up to $10^9$. These ranges are hugely different, so [feature scaling](03-feature-scaling.md) becomes very important for polynomial features.
>
> **Common mistakes.**
>
> - Adding very high powers "just in case". The curve then wiggles to hit every point, which is [overfitting](08-overfitting.md).
> - Forgetting to scale the new features.

## 3. Related topics

- Previous: [Gradient descent in practice](04-gradient-descent-in-practice.md)
- Choosing the degree of the polynomial: [Model selection](../03-model-evaluation-and-ml-practice/02-model-selection.md) and [Bias and variance](../03-model-evaluation-and-ml-practice/03-bias-and-variance.md)