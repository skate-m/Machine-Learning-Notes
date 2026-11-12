# Regression Trees

> **Source page:** 17 (bottom) · Trees that predict a number instead of a class.

## 1. Example: predicting weight

The tree splits on **Ear shape** and the output is the animal's **weight**.

| Node | Examples (weights) | Variance | $w$ |
|---|---|---|---|
| Root | all | 20.51 | — |
| Pointy (left) | 7.2, 9.2, … | 1.47 | $w^{left}=5/10$ |
| Floppy (right) | 8.8, 20, … etc. | 21.87 | $w^{right}=5/10$ |

> **Note on the source:** the floppy variance is written "21-87" and is read as 21.87 ([UNCLEAR IN SOURCE], p. 17).

## 2. Splitting rule

> **From the source:** same information-gain formula, just use **variance instead of entropy**.

$$
\text{gain} = \text{Var}\left(\text{root}\right) - \left(w^{left}\,\text{Var}\left(\text{left}\right) + w^{right}\,\text{Var}\left(\text{right}\right)\right)
$$

> **Additional Explanation:**  
> This explanation has been added to improve understanding and is not a direct transcription of the original handwritten notes.  
> With the numbers above: $20.51 - (0.5\times 1.47 + 0.5\times 21.87) = 20.51 - 11.67 = 8.84$.

## Detailed Explanation

> **Additional Explanation:**  
> This explanation has been added to improve understanding and is not a direct transcription of the original handwritten notes.
>
> **What changes compared with a classification tree.** The tree now predicts a *number* (an animal's weight). The structure is the same: splits on features, with leaves at the bottom. Only two things change: how a split is judged and what a leaf predicts.
>
> **How a split is judged.** A good split makes the weights inside each branch similar to each other, i.e. gives a **small variance**. Variance measures how spread out the numbers are. So we replace entropy with variance in the same formula.
>
> **Check of the source's numbers.**
>
> - Root variance: $20.51$.
> - Weighted variance after the split: $0.5(1.47)+0.5(21.87) = 11.67$.
> - Gain: $20.51 - 11.67 = 8.84$.
>
> The *pointy* branch became very uniform (variance 1.47), so the split helps a lot, even though the floppy branch is still spread out.
>
> **A small variance example.** Weights $7.2$ and $9.2$: the mean is $8.2$, and the variance is $\frac{(7.2-8.2)^2+(9.2-8.2)^2}{2}=1.0$.
>
> **What a leaf predicts.** For a new animal, the usual choice is the **average weight** of the training examples in the leaf it reaches.
>
> **Common mistake.** Using entropy for a numerical target. Entropy is for classes; use variance for numbers.

## 3. Related topics

- Previous: [One-hot encoding](04-one-hot-encoding.md)
- The classification version: [Information gain](03-information-gain.md)
- Next: [Random forest](06-random-forest.md)