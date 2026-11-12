# Recommender Systems: Notation

> **Source page:** 39 (bottom) · Example: a movie recommender.

## Notation

- $r(i,j)=1$ if user $j$ has rated movie $i$ (0 otherwise).
- $y^{(i,j)}$ = rating given by user $j$ on movie $i$ (if defined).
- $w^{(j)}, b^{(j)}$ = parameters for user $j$.
- $x^{(i)}$ = feature vector for movie $i$.

For user $j$ and movie $i$, predict the rating:

$$
\vec w^{(j)}\cdot\vec x^{(i)} + b^{(j)}
$$

- $m^{(j)}$ = number of movies rated by user $j$.
- The task is to learn $w^{(j)}, b^{(j)}$.

## Detailed Explanation

> **Additional Explanation:**  
> This explanation has been added to improve understanding and is not a direct transcription of the original handwritten notes.
>
> **The situation.** A movie service has many users and many movies, but each user has rated only a few. The goal is to predict the ratings that are *missing* and recommend the movies with high predicted ratings.
>
> **How to read the notation.** $r(i,j)$ tells you whether a rating exists; $y^{(i,j)}$ is the rating itself, defined only when $r(i,j)=1$.
>
> **A tiny made-up example** (3 movies, 2 users):
>
> | | User 1 | User 2 |
> |---|---|---|
> | Movie 1 | 5 | ? |
> | Movie 2 | ? | 4 |
> | Movie 3 | 2 | 1 |
>
> Here $r(1,1)=1$ and $y^{(1,1)}=5$, but $r(1,2)=0$, so $y^{(1,2)}$ is not defined. For user 1, $m^{(1)}=2$ (they rated 2 movies).
>
> **The prediction.** For user $j$ and movie $i$ the prediction is $\vec w^{(j)}\cdot\vec x^{(i)}+b^{(j)}$: the movie's features $x^{(i)}$ are combined using the user's own weights. Each user has their own $w^{(j)}$ and $b^{(j)}$, which describe their taste.
>
> **Why this is like linear regression.** For one user this is simply a linear regression, where the "training examples" are the movies that user has rated.
>
> **Common mistake.** Mixing up the two indices. In $y^{(i,j)}$ the **movie** comes first and the **user** second.

## Related topics

- Next: [Collaborative filtering versus content-based filtering](02-collaborative-vs-content-based.md)