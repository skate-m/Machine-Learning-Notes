# Decision Boundary

> **Source page:** 3 (top) · Where a classification model switches from predicting one class to the other.

## 1. Linear boundary

The model first computes

$$
z = \vec w\cdot\vec x + b
$$

The boundary is where $z=0$. The source's example:

$$
z = x_1 + x_2 - 3 = 0 \quad\Longrightarrow\quad x_1 + x_2 = 3
$$

This is a straight line. In the source's sketch the points marked **o** lie on one side of it and the points marked **x** on the other.

## 2. Non-linear boundaries

Using squared features gives a curved boundary:

$$
f(\vec x) = g\left(w_1x_1^2 + w_2x_2^2 + b\right)
$$

$$
z = x_1^2 + x_2^2 - 1 \quad\Longrightarrow\quad x_1^2 + x_2^2 = 1
$$

This is a circle. In the source's sketch the **o** points are inside the circle and the **x** points are outside.

![Linear and circular decision boundaries](../assets/figures/decision-boundaries.png)

*Figure: left, the line $x_1+x_2=3$; right, the circle $x_1^2+x_2^2=1$. The points are synthetic and only illustrate the two examples drawn in the source.*

> **Additional Explanation:**  
> This explanation has been added to improve understanding and is not a direct transcription of the original handwritten notes.  
> Here $g$ is the sigmoid function (defined in [Logistic loss and cost](07-logistic-loss-and-cost.md)). Since $g(0)=0.5$, the boundary is the set of points where $z=0$.

## 3. Related topics

- Next: [Logistic loss and cost](07-logistic-loss-and-cost.md)