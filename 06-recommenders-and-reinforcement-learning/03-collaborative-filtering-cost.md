# Collaborative Filtering: Cost Function and Gradient Descent

> **Source page:** 38 · Learning user parameters and movie features together (ratings).

## 1. Cost for one user

To learn parameters $w^{(j)}, b^{(j)}$ for user $j$:

$$
J\left(w^{(j)},b^{(j)}\right) = \frac{1}{2}\sum_{i:\,r(i,j)=1}\left(w^{(j)}\cdot x^{(i)}+b^{(j)}-y^{(i,j)}\right)^2 + \frac{\lambda}{2}\sum_{k=1}^{n}\left(w_k^{(j)}\right)^2
$$

## 2. Cost for all users

To learn $w^{(1)},b^{(1)},\dots,w^{(n_u)},b^{(n_u)}$:

$$
J\left(w^{(1)},\dots,w^{(n_u)},\,b^{(1)},\dots,b^{(n_u)}\right) = \frac{1}{2}\sum_{j=1}^{n_u}\sum_{i:\,r(i,j)=1}\left(w^{(j)}\cdot x^{(i)}+b^{(j)}-y^{(i,j)}\right)^2 + \frac{\lambda}{2}\sum_{j=1}^{n_u}\sum_{k=1}^{n}\left(w_k^{(j)}\right)^2
$$

> **Note on the source:** $m^{(j)}$ is defined on page 39 but does not appear in these two cost formulas. They are transcribed exactly as written. $n_u$ is read as the number of users.

## 3. Final cost function (collaborative filtering)

When the movie features $x$ are also learned, they are regularized as well:

$$
J(w,b,x) = \frac{1}{2}\sum_{(i,j):\,r(i,j)=1}\left(w^{(j)}\cdot x^{(i)}+b^{(j)}-y^{(i,j)}\right)^2 + \frac{\lambda}{2}\sum_{j=1}^{n_u}\sum_{k=1}^{n}\left(w_k^{(j)}\right)^2 + \frac{\lambda}{2}\sum_{i=1}^{n_m}\sum_{k=1}^{n}\left(x_k^{(i)}\right)^2
$$

($n_m$ is read as the number of movies.)

## 4. Gradient descent

$$
w_i^{(j)} = w_i^{(j)} - \alpha\,\frac{\partial}{\partial w_i^{(j)}}J(w,b,x)
$$

$$
b^{(j)} = b^{(j)} - \alpha\,\frac{\partial}{\partial b^{(j)}}J(w,b,x)
$$

$$
x_k^{(i)} = x_k^{(i)} - \alpha\,\frac{\partial}{\partial x_k^{(i)}}J(w,b,x)
$$

> **Note (from the source):** $x$ is a **new parameter** because $x$ is also a feature that is learned. In the first update the page writes the weight subscript as $i$ while the cost uses $k$; this is preserved as written.

## Detailed Explanation

> **Additional Explanation:**  
> This explanation has been added to improve understanding and is not a direct transcription of the original handwritten notes.
>
> **The cost, part by part.**
>
> - *The squared error term:* $\left(w^{(j)}\cdot x^{(i)}+b^{(j)}-y^{(i,j)}\right)^2$ compares the prediction with the real rating. It is added up **only over pairs with $r(i,j)=1$**, i.e. ratings that exist.
> - *The $w$ regularization term:* keeps each user's weights small.
> - *The $x$ regularization term:* keeps the movie features small too, when they are learned.
>
> **Why learn the features $x$ as well.** In collaborative filtering we may not know good features for the movies. If many users have rated them, we can learn both: the users' weights *and* the movies' features. That is why $x$ appears as a parameter in the gradient descent updates.
>
> **Counting parameters.** With $n_u$ users, $n_m$ movies and $n$ features per movie: each user has $n$ weights and one bias, giving $n_u(n+1)$, and each movie has $n$ features, giving $n_m n$. The total is $n_u(n+1)+n_mn$.
>
> **How the training works.** Repeat: compute the three derivatives, update all $w$, $b$ and $x$ together by a small step $\alpha$, and watch the cost fall.
>
> **Why it works.** A movie's features get adjusted so that users who like it rate it high and users who dislike it rate it low. Features end up describing what users care about, even if nobody named those features.
>
> **Common mistake.** Summing over all user–movie pairs. Missing ratings must be skipped.

## Related topics

- Previous: [Collaborative filtering vs content-based](02-collaborative-vs-content-based.md)
- Next: [Binary labels](04-binary-labels.md)