# Collaborative Filtering versus Content-Based Filtering

> **Source page:** 30 (bottom)

- **Collaborative filtering:** recommend items to you based on the ratings of users who gave similar ratings.
- **Content-based filtering:** recommend items to you based on features of the user and the item to find a good match.

**Example features (from the source):**

| User features $x_u^{(j)}$ (for user $j$) | Movie features $x_m^{(i)}$ (for movie $i$) |
|---|---|
| Age, gender, country | Year, genre, reviews |

## Detailed Explanation

> **Additional Explanation:**  
> This explanation has been added to improve understanding and is not a direct transcription of the original handwritten notes.
>
> **Two different sources of information.**
>
> | Method | Information used | One-line idea |
> |---|---|---|
> | Collaborative filtering | Ratings from many users | "People who rated like you liked this." |
> | Content-based filtering | Features of the user *and* the item | "This item matches your profile." |
>
> **An example of each.**
>
> - *Collaborative:* you and another user both loved the same five films. That user also loved a sixth film that you have not seen, so it is recommended to you.
> - *Content-based:* you are 25 years old and the film is a recent action movie. Using what is known about people like you and about such films, the system predicts a good match.
>
> **What the features can be (from the source).** User features: age, gender, country. Movie features: year, genre, reviews. The two sets of features can be different lengths.
>
> **What each needs.** Collaborative filtering needs enough ratings from enough users. Content-based filtering needs good features for both sides. In practice, systems often combine ideas from both.
>
> **Common mistake.** Thinking content-based filtering ignores ratings. It still learns from the ratings; the difference is that it also uses the features.

## Related topics

- Previous: [Notation](01-recommender-systems-notation.md)
- Next: [Collaborative filtering cost function](03-collaborative-filtering-cost.md)
- Content-based with neural networks: [Content-based filtering with deep learning](07-content-based-deep-learning.md)