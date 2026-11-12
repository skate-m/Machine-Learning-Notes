# Finding Related Items

> **Source pages:** 30 (top), 33 (note)

The features $x^{(i)}$ of item $i$ are quite hard to interpret. To find other items related to it, find item $k$ with $x^{(k)}$ similar to $x^{(i)}$, i.e. with the **smallest distance**:

$$
\sum_{l=1}^{n}\left(x_l^{(k)}-x_l^{(i)}\right)^2 \equiv \left\lVert x^{(k)}-x^{(i)}\right\rVert^2
$$

With learned movie vectors (see [content-based filtering with deep learning](07-content-based-deep-learning.md)), the source's note reads: to find a movie similar to $i$, minimise $\left\lVert v_m^{(k)}-v_m^{(i)}\right\rVert^2$.

## Detailed Explanation

> **Additional Explanation:**  
> This explanation has been added to improve understanding and is not a direct transcription of the original handwritten notes.
>
> **The idea.** To show "similar movies", find movies whose feature vectors are close to the vector of the movie you are looking at. Close means a small squared distance.
>
> **Worked example.** Let $x^{(i)}=(1,2)$.
>
> - Movie $k$ with $x^{(k)}=(2,4)$: distance$^2$ $=(2-1)^2+(4-2)^2 = 1+4=5$.
> - Movie $j$ with $x^{(j)}=(1,3)$: distance$^2$ $=0+1=1$.
>
> Movie $j$ is closer, so it is the more related one. To get a list, compute the distance to every movie and take the smallest few (not counting the movie itself).
>
> **Why a note about interpretability.** The learned features are just numbers, and no one may know what each one means. You do not need to: the distance between them still captures similarity.
>
> **With the vectors from the two-network model.** The same idea applies using $v_m$, the learned movie vectors (see [Content-based filtering with deep learning](07-content-based-deep-learning.md)). The smaller $\lVert v_m^{(k)}-v_m^{(i)}\rVert^2$ is, the more related the movies are.
>
> **A practical tip.** This calculation can be done ahead of time (offline), so that "similar items" are ready when a user visits.
>
> **Common mistake.** Including the item itself, which always has distance 0.

## Related topics

- Previous: [Mean normalization](05-mean-normalization.md)
- Next: [Content-based filtering with deep learning](07-content-based-deep-learning.md)