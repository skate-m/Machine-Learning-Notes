# Adding Data, Data Augmentation and Data Synthesis

> **Source page:** 49 · Getting more useful training data.

## 1. Adding data

A quicker fix with high impact is to **add error-related data only**.

## 2. Data augmentation

Modify an existing training example to create new training data.

**Example (from the source):** rotate, zoom, change contrast — for letters recognition.

## 3. Data synthesis

Create entirely new examples. For example, in a text analysis model you can type in letters in different fonts and colours and screenshot them to feed the model.

> **Note (from the source):** engineering the data used by the model, instead of just improving the code, will go a long way.

## Detailed Explanation

> **Additional Explanation:**  
> This explanation has been added to improve understanding and is not a direct transcription of the original handwritten notes.
>
> **Why data can matter more than code.** The model is only as good as the data it learns from. Often the quickest improvement is better or more relevant data, not a cleverer algorithm.
>
> **Adding data, but the right data.** Suppose error analysis shows that a spam classifier fails mostly on pharmacy spam. Collecting *more pharmacy-spam examples* helps more than collecting more of everything, and it is cheaper.
>
> **Data augmentation.** You take a real example and change it in a way that keeps its label. A picture of the letter "A" stays an "A" when rotated a little, zoomed or made lighter. Each change gives a new training example for free. Important: the change must be realistic. Rotating the digit 6 by 180° makes a 9, which would give the wrong label.
>
> **Data synthesis.** You create new examples from scratch. In the source's example, you type letters in many fonts and colours and take screenshots. This gives lots of labelled examples because you already know which letter you typed.
>
> **Why this is useful.** These methods give more varied data, so they mainly reduce variance (overfitting).
>
> **Common mistake.** Adding noise or changes that never happen in real use. The model then learns to handle situations that do not occur, and the real-world performance does not improve.

## 4. Related topics

- Previous: [Learning curves and debugging](04-learning-curves-and-debugging.md)
- Next: [ML development and error analysis](06-ml-development-and-error-analysis.md)