# Feature Scaling

> **Source pages:** 16 (item "5) Feature Scaling"), 6 (top, Z-score normalization) · Rescaling features that have very different ranges. The source's running example uses two features: $300 \le x_1 \le 2000$ and $0 \le x_2 \le 5$.

> **Additional Explanation:**  
> This explanation has been added to improve understanding and is not a direct transcription of the original handwritten notes.  
> Features with very different ranges (here roughly 300–2000 versus 0–5) are brought to comparable ranges so that gradient descent can treat them evenly.

## 1. Normalization: divide by the maximum

Divide each feature by its maximum (extreme) value.

$$
\frac{300}{2000}\le\frac{x_1}{2000}\le\frac{2000}{2000}\ \Rightarrow\ 0.15\le x_{1,\text{scaled}}\le 1
$$

$$
\frac{0}{5}\le\frac{x_2}{5}\le\frac{5}{5}\ \Rightarrow\ 0\le x_{2,\text{scaled}}\le 1
$$

## 2. Mean normalization

The source uses the means $\mu_1=600$ and $\mu_2=2.3$ (the average of each feature) and divides by the range (max − min).

$$
x_1 = \frac{x_1-\mu_1}{2000-300}\ \Rightarrow\ -0.18\le x_1\le 0.82
$$

$$
x_2 = \frac{x_2-\mu_2}{5-0}\ \Rightarrow\ -0.46\le x_2\le 0.54
$$

## 3. Z-score normalization

Uses the standard deviation $\sigma$ and the mean $\mu$ of each feature: $\sigma_1=450$, $\sigma_2=1.4$, $\mu_1=600$, $\mu_2=2.3$.

$$
x_1 = \frac{x_1-\mu_1}{\sigma_1}\ \Rightarrow\ -0.67\le x_1\le 3.1
\qquad
x_2 = \frac{x_2-\mu_2}{\sigma_2}\ \Rightarrow\ -1.6\le x_2\le 1.9
$$

> **Note on the source:** the upper limit of $x_1$ is handwritten in a way that could be read as "3.1" or "8.1". It is read as 3.1 because $(2000-600)/450 \approx 3.11$.

## 4. Summary of the three methods

| Method | Formula | Range of $x_1$ | Range of $x_2$ |
|---|---|---|---|
| Divide by max | $x/x_{max}$ | 0.15 to 1 | 0 to 1 |
| Mean normalization | $(x-\mu)/(x_{max}-x_{min})$ | −0.18 to 0.82 | −0.46 to 0.54 |
| Z-score | $(x-\mu)/\sigma$ | −0.67 to 3.1 | −1.6 to 1.9 |

## 5. Related topics

- Previous: [Multiple features](02-multiple-features-and-vectorization.md)
- Next: [Gradient descent in practice](04-gradient-descent-in-practice.md)