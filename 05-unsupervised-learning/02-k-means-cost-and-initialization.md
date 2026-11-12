# K-Means Cost Function and Random Initialization

> **Source page:** 20 · Notation, the distortion cost and how to avoid a poor starting point.

## 1. Notation

- $c^{(i)}$ = index of the cluster $(1,2,\dots,K)$ to which example $x^{(i)}$ is currently assigned.
- $\mu_k$ = cluster centroid $k$ (location).
- $\mu_{c^{(i)}}$ = cluster centroid of the cluster to which example $x^{(i)}$ has been assigned (location).

## 2. Distortion (cost function)

$$
J\left(c^{(1)},\dots,c^{(m)},\mu_1,\dots,\mu_K\right) = \frac{1}{m}\sum_{i=1}^{m}\left\lVert x^{(i)}-\mu_{c^{(i)}}\right\rVert^2
$$

## 3. Random initialization

```text
For i = 1 to 100 {
    Randomly initialize K-means.
    Run K-means. Get c(1), ..., c(m), mu_1, ..., mu_K
    Compute cost function (distortion)  J(c(1), ..., c(m), mu_1, ..., mu_K)
}
Pick the set of clusters that gives the lowest cost.
```

## Detailed Explanation

> **Additional Explanation:**  
> This explanation has been added to improve understanding and is not a direct transcription of the original handwritten notes.
>
> **What the cost measures.** The distortion $J$ is the average squared distance between each point and the centroid of its own cluster. Tight clusters give a small $J$. It is a score for how good a clustering is.
>
> **Worked example** (continuing the one-dimensional case with clusters $\{1,2,3\}$ at $\mu=2$ and $\{10,11,12\}$ at $\mu=11$):
>
> $$ J = \frac{1}{6}\left[(1-2)^2 + 0 + (3-2)^2 + (10-11)^2 + 0 + (12-11)^2\right] = \frac{4}{6}\approx 0.67 $$
>
> **A useful property.** Each assign step and each move step can only keep $J$ the same or make it smaller. It never goes up. So K-means always settles, although not always at the best possible clustering.
>
> **Why random initialization matters.** Depending on where the centroids start, K-means can settle in a *local minimum*, a clustering that is stable but not the best one. For example, two centroids might both start inside one real group and split it, while another real group has to share a single centroid.
>
> **The fix in the source.** Run the whole algorithm many times (the source uses 100), each time from a new random start, compute $J$ for each result, and keep the clustering with the **lowest** $J$.
>
> **Common mistake.** Comparing the cost of runs that used different values of $K$ and picking the lowest. A bigger $K$ always lowers $J$ (see [Choosing K](03-choosing-k.md)).

## 4. Related topics

- Previous: [Clustering and K-means](01-clustering-and-k-means.md)
- Next: [Choosing the value of K](03-choosing-k.md)