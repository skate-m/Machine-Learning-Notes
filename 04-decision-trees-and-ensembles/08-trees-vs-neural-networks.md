# Decision Trees versus Neural Networks

> **Source pages:** 7 and 12 (identical pages) · When to prefer each.

## Decision trees and tree ensembles

- Work well on structured (tabular) data.
- Not recommended for unstructured data (images, audio, etc.).
- Fast.
- Small decision trees may be human interpretable.

## Neural networks

- Work well on all types of data.
- May be slower than trees.
- Work with transfer learning.
- When building a system of multiple models, it might be easier to string together multiple neural networks.

## Detailed Explanation

> **Additional Explanation:**  
> This explanation has been added to improve understanding and is not a direct transcription of the original handwritten notes.
>
> **A quick way to choose.**
>
> | Your data looks like... | Good first choice |
> |---|---|
> | A table with columns (prices, ages, counts) | Decision tree, random forest or XGBoost |
> | Images, audio, text | Neural network |
> | A pipeline of several models trained together | Neural networks |
>
> **Why trees suit tables.** Table columns usually mean something on their own, and splitting on them is natural. Trees train quickly, so you can try many ideas, and a small tree can be explained to others.
>
> **Why neural networks suit raw signals.** The useful features in a picture or a sound are not given; the network learns them layer by layer (see [Neural networks](../02-advanced-learning-algorithms/01-neural-networks.md)). They can also use [transfer learning](../03-model-evaluation-and-ml-practice/08-transfer-learning.md) from a pretrained network.
>
> **Why networks are easier to combine.** All the parts are trained with gradient descent, so several networks can be linked and trained together as one system. Trees cannot be trained together in that way.
>
> **Speed.** The source notes that neural networks may be slower. Trees often give a good answer in a short time.
>
> **Common mistake.** Using a neural network on a small table of data because it sounds more advanced. A tree-based model is often better and faster there.

## Related topics

- Previous: [XGBoost](07-xgboost.md)
- [Neural networks](../02-advanced-learning-algorithms/01-neural-networks.md) and [Transfer learning](../03-model-evaluation-and-ml-practice/08-transfer-learning.md)