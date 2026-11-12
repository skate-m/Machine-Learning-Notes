# One-Hot Encoding

> **Source page:** 17 (top) · Handling a feature that can take more than two values.

Currently, ear shape is coded as 0 for **pointy** ears and 1 for **floppy** ears. If we want more values for a feature, such as **oval** ears, the source uses one binary column per value:

| Ear shape: Pointy | Floppy | Oval |
|:-:|:-:|:-:|
| 1 | 0 | 0 |
| 0 | 0 | 1 |

*(The two rows are the source's examples: a pointy-eared and an oval-eared animal.)*

> **Rule (from the source):** if a categorical feature can take on $K$ values, create $K$ binary features (0 or 1 valued).

## Detailed Explanation

> **Additional Explanation:**  
> This explanation has been added to improve understanding and is not a direct transcription of the original handwritten notes.
>
> **The problem.** A tree split asks a yes/no question. With ear shape coded as 0 and 1 (pointy / floppy) that is easy. If a third value, *oval*, appears, a single 0/1 feature can no longer represent it.
>
> **The solution.** Make one yes/no feature for each possible value. Exactly one of them is 1 ("hot") for each animal.
>
> | Animal | Pointy ears | Floppy ears | Oval ears |
> |---|:-:|:-:|:-:|
> | A (pointy) | 1 | 0 | 0 |
> | B (floppy) | 0 | 1 | 0 |
> | C (oval) | 0 | 0 | 1 |
>
> (The first row and the last row are the two shown in the source; the middle row follows the same rule.)
>
> **Why this works well.** Every new feature is a simple yes/no question, so the tree can keep using two-way splits, and the information-gain formula is unchanged.
>
> **It is useful beyond trees.** Neural networks and linear or logistic regression need numbers. A code like 1, 2, 3 would wrongly suggest that oval is "bigger" than floppy. One-hot features avoid this.
>
> **Common mistake.** Coding categories as 1, 2, 3 and feeding them to a model that treats them as quantities.

## Related topics

- Previous: [Information gain](03-information-gain.md)
- Next: [Regression trees](05-regression-trees.md)