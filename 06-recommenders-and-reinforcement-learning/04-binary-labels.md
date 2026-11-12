# Collaborative Filtering with Binary Labels

> **Source page:** 31 (top) · For labels such as favourites, likes and clicks.

Predict the probability of $y^{(i,j)}=1$ as

$$
g\left(w^{(j)}\cdot x^{(i)} + b^{(j)}\right),\qquad g(z)=\frac{1}{1+e^{-z}}
$$

## Cost function for the binary application

The cross-entropy loss for a **single example**:

$$
L\left(f_{(w,b,x)}(x),\,y\right) = -y\log\left(f_{(w,b,x)}(x)\right) - (1-y)\log\left(1-f_{(w,b,x)}(x)\right)
$$

Summed over the rated pairs:

$$
J(w,b,x) = \sum_{(i,j):\,r(i,j)=1}L\left(f_{(w,b,x)}(x),\,y^{(i,j)}\right)
\qquad\text{with}\qquad
f_{(w,b,x)}(x) = g\left(w^{(j)}\cdot x^{(i)}+b^{(j)}\right)
$$

## Detailed Explanation

> **Additional Explanation:**  
> This explanation has been added to improve understanding and is not a direct transcription of the original handwritten notes.
>
> **When labels are yes/no.** Often there are no star ratings, only signals such as *liked*, *favourited*, *clicked* or *watched to the end*. Define $y^{(i,j)}=1$ for the positive signal and $0$ for the negative. The task is now like logistic regression.
>
> **The prediction.** Apply the sigmoid $g$ to the same expression as before. The result is the predicted probability that user $j$ will respond positively to item $i$.
>
> **Worked numbers.** If $z = w^{(j)}\cdot x^{(i)}+b^{(j)}=1.5$, the predicted probability is $g(1.5)=\frac{1}{1+e^{-1.5}}\approx 0.82$. If the user really did click ($y=1$) the loss is $-\ln(0.82)\approx 0.20$; if they did not click ($y=0$) it is $-\ln(0.18)\approx 1.7$, a much larger penalty.
>
> **Why the log loss is used.** Same reason as in [logistic regression](../01-supervised-learning/07-logistic-loss-and-cost.md): it punishes confident wrong predictions heavily.
>
> **Only rated pairs count.** As before, the cost is summed over pairs with $r(i,j)=1$, i.e. where we actually know the label.
>
> **Common mistake.** Treating a missing click as a "0". If the user never saw the item, that is *unknown*, not a negative label.

## Related topics

- Previous: [Collaborative filtering cost](03-collaborative-filtering-cost.md)
- Next: [Mean normalization](05-mean-normalization.md)
- The same loss: [Logistic loss](../01-supervised-learning/07-logistic-loss-and-cost.md)