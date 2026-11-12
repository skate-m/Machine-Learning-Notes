# Mean Normalization

> **Source page:** 31 (bottom) · Estimating the rating of a user who hasn't rated anything.

The rating matrix (rows = movies, columns = users 1–5; "?" = not rated) and the row means $\mu$:

| | User 1 | User 2 | User 3 | User 4 | User 5 | $\mu$ (as written) |
|---|:-:|:-:|:-:|:-:|:-:|:-:|
| Movie 1 | 5 | 5 | 0 | 0 | ? | 2.5 |
| Movie 2 | 5 | ? | ? | 0 | ? | 2.5 |
| Movie 3 | ? | 4 | 0 | ? | ? | 2 |
| Movie 4 | 0 | 0 | 5 | 4 | ? | 2.5 |
| Movie 5 | 0 | 0 | 5 | 0 | ? | 1.25 |

For **user 5** (assuming 2 features): $w^{(5)}=\begin{bmatrix}0\\0\end{bmatrix}$ and $b^{(5)}=0$, so

$$
w^{(5)}\cdot x^{(1)} + b^{(5)} + \mu_1 = 0 + 2.5 = 2.5
$$

A user with no ratings is therefore predicted the average rating of each movie.

> **Note on the source (possible inconsistency):** the mean of movie 4's known ratings $(0,0,5,4)$ is $9/4=2.25$, but the page writes $2.5$. The other four means match their rows. The value is preserved as written; the handwriting may be $2.25$ ([UNCLEAR IN SOURCE], p. 31).

## Detailed Explanation

> **Additional Explanation:**  
> This explanation has been added to improve understanding and is not a direct transcription of the original handwritten notes.
>
> **The problem.** A brand-new user has rated nothing. With the cost function above, the regularization term pushes this user's weights $w^{(5)}$ towards 0 and there is no data to pull them away, so the model predicts a rating of 0 for every movie. That is not a useful prediction.
>
> **The fix.** Work with ratings *relative to each movie's average*.
>
> 1. Compute each movie's average rating $\mu_i$ (using only the existing ratings).
> 2. Subtract it from the ratings before learning.
> 3. When predicting, **add it back**: $\;w^{(j)}\cdot x^{(i)}+b^{(j)}+\mu_i$.
>
> **Subtracting the average, worked for movie 1.** The ratings $5,5,0,0$ have mean $2.5$. After subtracting: $2.5,\ 2.5,\ -2.5,\ -2.5$.
>
> **What happens for the new user.** Their $w$ and $b$ stay at 0, so the prediction is $0+0+\mu_1 = 2.5$. A new user is therefore guessed to rate each movie about as the average user does.
>
> **Why rows (movies) and not columns (users).** We want a sensible guess for a user with no history, and the only thing we know about them is how other users rated each movie.
>
> **Check of the source's numbers.** Movie 4's known ratings are $0,0,5,4$, whose mean is $2.25$, but the page shows $2.5$ (flagged in the note above).
>
> **Common mistake.** Forgetting to add $\mu_i$ back when making the final prediction.

## Related topics

- Previous: [Binary labels](04-binary-labels.md)
- Next: [Finding related items](06-finding-related-items.md)