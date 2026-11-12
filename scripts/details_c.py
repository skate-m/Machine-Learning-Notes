D = {}
U='05-unsupervised-learning/'
D[U+'01-clustering-and-k-means.md'] = r"""
**Supervised versus unsupervised.** In supervised learning every example comes with a correct answer $y$. In clustering there are no answers. The algorithm looks at the points and groups those that are close to each other, for example customers with similar behaviour.

**K-means in two repeating steps.** Think of $K$ "centres" (centroids) that move until they settle in the middle of groups.

1. *Assign:* every point joins the nearest centroid.
2. *Move:* every centroid moves to the average position of the points that joined it.

**Worked example in one dimension.** Points: $1, 2, 3, 10, 11, 12$ with $K=2$ and starting centroids $\mu_1=1$, $\mu_2=12$.

- *Assign:* $1,2,3$ are closest to $\mu_1$; $10,11,12$ are closest to $\mu_2$.
- *Move:* $\mu_1 = (1+2+3)/3 = 2$ and $\mu_2=(10+11+12)/3=11$.
- *Assign again:* nothing changes, so the algorithm has finished.

**Why "closest" uses the squared distance.** Minimising $\lVert x^{(i)}-\mu_k\rVert^2$ gives the same winner as minimising the plain distance, and it is simpler to compute and to write.

**When to stop.** When the assignments no longer change (or change very little), the centroids stop moving.

**An edge case.** A centroid can end up with no points. Then its mean is undefined. A common choice is to drop that cluster (so $K$ becomes smaller) or to start that centroid again at a random place.

**Common mistake.** Thinking the result is always the same. The starting positions matter (see [K-means cost and initialization](02-k-means-cost-and-initialization.md)).
"""
D[U+'02-k-means-cost-and-initialization.md'] = r"""
**What the cost measures.** The distortion $J$ is the average squared distance between each point and the centroid of its own cluster. Tight clusters give a small $J$. It is a score for how good a clustering is.

**Worked example** (continuing the one-dimensional case with clusters $\{1,2,3\}$ at $\mu=2$ and $\{10,11,12\}$ at $\mu=11$):

$$ J = \frac{1}{6}\left[(1-2)^2 + 0 + (3-2)^2 + (10-11)^2 + 0 + (12-11)^2\right] = \frac{4}{6}\approx 0.67 $$

**A useful property.** Each assign step and each move step can only keep $J$ the same or make it smaller. It never goes up. So K-means always settles, although not always at the best possible clustering.

**Why random initialization matters.** Depending on where the centroids start, K-means can settle in a *local minimum*, a clustering that is stable but not the best one. For example, two centroids might both start inside one real group and split it, while another real group has to share a single centroid.

**The fix in the source.** Run the whole algorithm many times (the source uses 100), each time from a new random start, compute $J$ for each result, and keep the clustering with the **lowest** $J$.

**Common mistake.** Comparing the cost of runs that used different values of $K$ and picking the lowest. A bigger $K$ always lowers $J$ (see [Choosing K](03-choosing-k.md)).
"""
D[U+'03-choosing-k.md'] = r"""
**Why the cost cannot choose $K$ by itself.** If you allow more clusters, every point gets closer to a centroid, so $J$ always falls. In the extreme case with $K=m$, every point is its own cluster and $J=0$. That is useless as a grouping. So we cannot just pick the $K$ with the smallest $J$.

**How the elbow method works.**

1. Run K-means for $K=1,2,3,\dots$
2. Plot $J$ against $K$.
3. Look for the "elbow", the place where the curve stops dropping steeply and starts to flatten.

In the source's sketch, $J$ falls quickly until $K=3$ and slowly afterwards. After the elbow, extra clusters buy very little, so $K=3$ is a good choice.

**When there is no clear elbow.** Sometimes the curve falls smoothly. Then the plot cannot decide for you, and the source says the number of clusters depends on the **use case**. For example, if a company wants to sell T-shirts in sizes, the question is how many sizes it is practical to make. The business reason decides, not only the data.

**A good habit.** Look at the resulting clusters and ask whether they are useful for the real goal.

**Common mistake.** Searching for an elbow that is not there and picking one by feel.
"""
D[U+'04-gaussian-distribution.md'] = r"""
**What the curve says.** The Gaussian (bell curve) is a model of how values are spread around an average. Most values are close to the mean $\mu$, and far-away values become rarer and rarer. The height of the curve at $x$, $p(x)$, tells you how common values near $x$ are.

**What the two parameters do.**

- $\mu$ moves the centre of the curve left or right.
- $\sigma$ sets the width. A small $\sigma$ makes a tall narrow bell; a large $\sigma$ a low wide one.

**A useful fact.** About 68% of the values lie within one $\sigma$ of $\mu$, and about 95% within two $\sigma$.

**Worked example.** Data: $1, 2, 3$.

- $\mu = (1+2+3)/3 = 2$
- $\sigma^2 = \frac{(1-2)^2+(2-2)^2+(3-2)^2}{3}=0.667$, so $\sigma\approx 0.816$
- $p(2) = \frac{1}{\sqrt{2\pi}(0.816)}\approx 0.489$
- $p(4) = 0.489\cdot e^{-\frac{(4-2)^2}{2(0.667)}} = 0.489\cdot e^{-3}\approx 0.024$

The value 4 is much less likely than 2 under this model. This idea is the basis of [anomaly detection](05-anomaly-detection.md).

**Note on the formula.** The source divides by $m$ when computing $\sigma^2$. Some textbooks divide by $m-1$; for large data the difference is tiny.

**Common mistake.** Treating $p(x)$ as a probability that $x$ happens exactly. For a continuous value it is a *density*; compare values of $p(x)$ to each other rather than reading them as chances.
"""
D[U+'05-anomaly-detection.md'] = r"""
**The goal.** Find the data points that do not look like the rest, such as an engine that behaves in an unusual way. We do this without examples of every kind of failure: we learn what *normal* looks like and flag what does not fit.

**How the rule works.** Fit a model $p(x)$ to normal data (for example Gaussians as in the [previous note](04-gaussian-distribution.md)). A new point with a very small $p(x)$ is unlikely under the normal pattern, so it is flagged.

**Applying it to the Gaussian example.** With $\varepsilon = 0.05$: $p(2)=0.489\ge\varepsilon$ is **normal**, while $p(4)=0.024<\varepsilon$ is an **anomaly**.

**Choosing $\varepsilon$.**

- If $\varepsilon$ is too large, many normal points are flagged (false alarms).
- If $\varepsilon$ is too small, real anomalies are missed.

It is tuned using a cross-validation set (see [Evaluating anomaly detection](06-evaluating-anomaly-detection.md)).

**One common way to use several features.** With features such as heat and vibration, a typical approach is to model each feature with its own Gaussian and multiply the results: a point is unusual if at least one feature is very unusual.

**Why features matter so much.** If a failure shows up only in a *combination* of features, no single feature looks odd. Creating a ratio feature (for example, one measurement divided by another) can make the failure stand out. That is why the source says feature engineering is crucial.

**Making features Gaussian.** Taking the log of a skewed feature often makes its histogram look like a bell, which suits the model better.

**Common mistake.** Keeping a feature whose $p(x)$ looks the same for normal and anomalous examples. It carries no signal.
"""
D[U+'06-evaluating-anomaly-detection.md'] = r"""
**Why a special data split.** Anomalies are very rare. In the source's example only 20 of 10 000 engines are flawed ($0.2\%$). A "detector" that always says *normal* would be right $9980/10\,000 = 99.8\%$ of the time, so accuracy is useless here. We need metrics that focus on the rare class.

**What goes where.**

- The **training set** contains only good engines. The model learns what normal looks like. No labels are needed here.
- The **CV set** contains good engines and a few anomalies. It has labels, and is used to tune $\varepsilon$ and to decide which features to use.
- The **test set** (if there is one) has the same kind of mix and gives a final check.

The anomalies are shared between CV and test (10 each) because there are so few of them.

**The alternative split.** With very few anomalies, you can skip the test set and put all 20 into the CV set. The price is a higher risk that the choices you made fit the CV set too closely (overfitting to it).

**Tuning step by step.**

1. Fit $p(x)$ on the training set.
2. Compute $p(x)$ for each CV example and apply the rule $p(x)<\varepsilon \Rightarrow y=1$.
3. Score the result with precision, recall or $F_1$ (see [Precision, recall and F1](../03-model-evaluation-and-ml-practice/07-precision-recall-f1.md)).
4. Try other $\varepsilon$ values and features and keep what scores best.

**Common mistake.** Putting anomalies in the training set. The point is to learn only the normal pattern.
"""

R='06-recommenders-and-reinforcement-learning/'
D[R+'01-recommender-systems-notation.md'] = r"""
**The situation.** A movie service has many users and many movies, but each user has rated only a few. The goal is to predict the ratings that are *missing* and recommend the movies with high predicted ratings.

**How to read the notation.** $r(i,j)$ tells you whether a rating exists; $y^{(i,j)}$ is the rating itself, defined only when $r(i,j)=1$.

**A tiny made-up example** (3 movies, 2 users):

| | User 1 | User 2 |
|---|---|---|
| Movie 1 | 5 | ? |
| Movie 2 | ? | 4 |
| Movie 3 | 2 | 1 |

Here $r(1,1)=1$ and $y^{(1,1)}=5$, but $r(1,2)=0$, so $y^{(1,2)}$ is not defined. For user 1, $m^{(1)}=2$ (they rated 2 movies).

**The prediction.** For user $j$ and movie $i$ the prediction is $\vec w^{(j)}\cdot\vec x^{(i)}+b^{(j)}$: the movie's features $x^{(i)}$ are combined using the user's own weights. Each user has their own $w^{(j)}$ and $b^{(j)}$, which describe their taste.

**Why this is like linear regression.** For one user this is simply a linear regression, where the "training examples" are the movies that user has rated.

**Common mistake.** Mixing up the two indices. In $y^{(i,j)}$ the **movie** comes first and the **user** second.
"""
D[R+'02-collaborative-vs-content-based.md'] = r"""
**Two different sources of information.**

| Method | Information used | One-line idea |
|---|---|---|
| Collaborative filtering | Ratings from many users | "People who rated like you liked this." |
| Content-based filtering | Features of the user *and* the item | "This item matches your profile." |

**An example of each.**

- *Collaborative:* you and another user both loved the same five films. That user also loved a sixth film that you have not seen, so it is recommended to you.
- *Content-based:* you are 25 years old and the film is a recent action movie. Using what is known about people like you and about such films, the system predicts a good match.

**What the features can be (from the source).** User features: age, gender, country. Movie features: year, genre, reviews. The two sets of features can be different lengths.

**What each needs.** Collaborative filtering needs enough ratings from enough users. Content-based filtering needs good features for both sides. In practice, systems often combine ideas from both.

**Common mistake.** Thinking content-based filtering ignores ratings. It still learns from the ratings; the difference is that it also uses the features.
"""
D[R+'03-collaborative-filtering-cost.md'] = r"""
**The cost, part by part.**

- *The squared error term:* $\left(w^{(j)}\cdot x^{(i)}+b^{(j)}-y^{(i,j)}\right)^2$ compares the prediction with the real rating. It is added up **only over pairs with $r(i,j)=1$**, i.e. ratings that exist.
- *The $w$ regularization term:* keeps each user's weights small.
- *The $x$ regularization term:* keeps the movie features small too, when they are learned.

**Why learn the features $x$ as well.** In collaborative filtering we may not know good features for the movies. If many users have rated them, we can learn both: the users' weights *and* the movies' features. That is why $x$ appears as a parameter in the gradient descent updates.

**Counting parameters.** With $n_u$ users, $n_m$ movies and $n$ features per movie: each user has $n$ weights and one bias, giving $n_u(n+1)$, and each movie has $n$ features, giving $n_m n$. The total is $n_u(n+1)+n_mn$.

**How the training works.** Repeat: compute the three derivatives, update all $w$, $b$ and $x$ together by a small step $\alpha$, and watch the cost fall.

**Why it works.** A movie's features get adjusted so that users who like it rate it high and users who dislike it rate it low. Features end up describing what users care about, even if nobody named those features.

**Common mistake.** Summing over all user–movie pairs. Missing ratings must be skipped.
"""
D[R+'04-binary-labels.md'] = r"""
**When labels are yes/no.** Often there are no star ratings, only signals such as *liked*, *favourited*, *clicked* or *watched to the end*. Define $y^{(i,j)}=1$ for the positive signal and $0$ for the negative. The task is now like logistic regression.

**The prediction.** Apply the sigmoid $g$ to the same expression as before. The result is the predicted probability that user $j$ will respond positively to item $i$.

**Worked numbers.** If $z = w^{(j)}\cdot x^{(i)}+b^{(j)}=1.5$, the predicted probability is $g(1.5)=\frac{1}{1+e^{-1.5}}\approx 0.82$. If the user really did click ($y=1$) the loss is $-\ln(0.82)\approx 0.20$; if they did not click ($y=0$) it is $-\ln(0.18)\approx 1.7$, a much larger penalty.

**Why the log loss is used.** Same reason as in [logistic regression](../01-supervised-learning/07-logistic-loss-and-cost.md): it punishes confident wrong predictions heavily.

**Only rated pairs count.** As before, the cost is summed over pairs with $r(i,j)=1$, i.e. where we actually know the label.

**Common mistake.** Treating a missing click as a "0". If the user never saw the item, that is *unknown*, not a negative label.
"""
D[R+'05-mean-normalization.md'] = r"""
**The problem.** A brand-new user has rated nothing. With the cost function above, the regularization term pushes this user's weights $w^{(5)}$ towards 0 and there is no data to pull them away, so the model predicts a rating of 0 for every movie. That is not a useful prediction.

**The fix.** Work with ratings *relative to each movie's average*.

1. Compute each movie's average rating $\mu_i$ (using only the existing ratings).
2. Subtract it from the ratings before learning.
3. When predicting, **add it back**: $\;w^{(j)}\cdot x^{(i)}+b^{(j)}+\mu_i$.

**Subtracting the average, worked for movie 1.** The ratings $5,5,0,0$ have mean $2.5$. After subtracting: $2.5,\ 2.5,\ -2.5,\ -2.5$.

**What happens for the new user.** Their $w$ and $b$ stay at 0, so the prediction is $0+0+\mu_1 = 2.5$. A new user is therefore guessed to rate each movie about as the average user does.

**Why rows (movies) and not columns (users).** We want a sensible guess for a user with no history, and the only thing we know about them is how other users rated each movie.

**Check of the source's numbers.** Movie 4's known ratings are $0,0,5,4$, whose mean is $2.25$, but the page shows $2.5$ (flagged in the note above).

**Common mistake.** Forgetting to add $\mu_i$ back when making the final prediction.
"""
D[R+'06-finding-related-items.md'] = r"""
**The idea.** To show "similar movies", find movies whose feature vectors are close to the vector of the movie you are looking at. Close means a small squared distance.

**Worked example.** Let $x^{(i)}=(1,2)$.

- Movie $k$ with $x^{(k)}=(2,4)$: distance$^2$ $=(2-1)^2+(4-2)^2 = 1+4=5$.
- Movie $j$ with $x^{(j)}=(1,3)$: distance$^2$ $=0+1=1$.

Movie $j$ is closer, so it is the more related one. To get a list, compute the distance to every movie and take the smallest few (not counting the movie itself).

**Why a note about interpretability.** The learned features are just numbers, and no one may know what each one means. You do not need to: the distance between them still captures similarity.

**With the vectors from the two-network model.** The same idea applies using $v_m$, the learned movie vectors (see [Content-based filtering with deep learning](07-content-based-deep-learning.md)). The smaller $\lVert v_m^{(k)}-v_m^{(i)}\rVert^2$ is, the more related the movies are.

**A practical tip.** This calculation can be done ahead of time (offline), so that "similar items" are ready when a user visits.

**Common mistake.** Including the item itself, which always has distance 0.
"""
D[R+'07-content-based-deep-learning.md'] = r"""
**Why use two networks.** The user's features $x_u$ (age, country, past behaviour) and the movie's features $x_m$ (year, genre, reviews) are different kinds of information and can have different lengths. One network turns each user into a vector $v_u$, and a second network turns each movie into a vector $v_m$. Both vectors must have the **same length**, so that their dot product can be computed.

**Reading the dot product.** If one component of $v_u$ means "likes romance" and the matching component of $v_m$ means "is romantic", then multiplying them is large when both are large. Adding such products up gives a score for how well movie and user match.

**Tiny made-up example.** $v_u=[1,\ 0.5]$ and $v_m=[4,\ 2]$ give $1\cdot4+0.5\cdot2=5$.

**Training.** The cost compares the dot product with the real rating for every pair that has one, and adds regularization for the networks. Training changes the weights of **both** networks together to reduce this cost.

**The benefit.** Once trained, $v_m$ for each movie can be computed ahead of time. To recommend, you only need to compute $v_u$ for the current user and find movies with a high dot product, or to find similar movies using the distance between the $v_m$ vectors.

**Common mistake.** Choosing different output sizes for the two networks. The dot product needs equal lengths.
"""
D[R+'08-retrieval-and-ranking.md'] = r"""
**Why two steps.** A large service can have millions of items. Running the full neural network on every item for every visitor would take too long. So the job is split:

1. **Retrieval:** quickly build a shortlist of items that *might* be good.
2. **Ranking:** use the more careful (slower) model only on the shortlist, and sort it.

**Building the shortlist.** The source's examples: from each of the user's last 10 watched films, take 10 similar ones; add the top 20 films in the user's country; and so on. Combine the lists, remove duplicates, and remove films already watched.

**The trade-off.** A longer shortlist is more likely to include something the user would love, so recommendations are better. But ranking takes longer, so the page loads more slowly. How long the shortlist should be is found by **offline experiments**: try different lengths on stored data and measure both quality and speed.

**Filtering unwanted items.** The note on "amelioration" says that problematic content (hate speech, fraud, scams, violent content) should be filtered out. This can be done as part of building or ranking the list.

**Common mistake.** Making the shortlist very large "just in case". The speed cost may outweigh the gain.
"""
D[R+'09-reinforcement-learning-return.md'] = r"""
**The setting.** An agent (here, a rover) is in a *state* and receives a *reward* when it gets to certain states. It wants to collect as much total reward as possible.

**What the discount factor does.** A reward that arrives later is worth a bit less. With $\gamma=0.9$, a reward after 3 steps is multiplied by $0.9^3=0.729$. Closer to 1 means the agent is more patient; closer to 0 means it cares mostly about rewards right now.

**Extending the source's calculation** (an illustration using the same formula, moving left each time with $\gamma = 0.9$):

| Start state | Return |
|---|---|
| 1 (terminal, reward 100) | 100 |
| 2 | $0.9\times100 = 90$ |
| 3 | $0.9^2\times100 = 81$ |
| 4 | $0.9^3\times100 = 72.9$ |
| 5 | $0.9^4\times100 = 65.61$ |

The 72.9 in the source is exactly the value for state 4, which agrees with the idea that the number comes from heading left from state 4.

**Why a return and not just a single reward.** Sometimes the best first move gives zero reward but leads to a big reward later. The return captures that.

**Comparing the two goals.** From state 5, going left gives 65.61, but going right to state 6 gives 40 immediately. So the left route is better there. From state 6 itself the answer is already 40.

**Common mistake.** Forgetting that the powers of $\gamma$ grow with the number of steps. The first reward is not discounted at all ($\gamma^0=1$).
"""
D[R+'10-policy-and-q-function.md'] = r"""
**What a policy is.** A rule that says what to do in each state. For the rover, a policy might say "from states 2, 3 and 4 move left; from state 5 move right". Writing it as a function, $\pi(s)=a$. The best policy is the one with the highest return.

**What $Q(s,a)$ means.** It is the return you would get if you start in state $s$, take action $a$ **once**, and then behave in the best possible way afterwards. It lets you compare actions directly.

**Reading the source's example** ($\gamma=0.5$, four states, rewards 100 and 40 at the ends).

- $Q(2,\leftarrow)=0+0.5\times100 = 50$: step left to state 1 and collect 100, discounted once.

**Checking the other action** (an extra calculation with the same rule). Moving right from state 2 puts you in state 3, and from there the best plan is to go left: $0+0.5\times0+0.25\times100=25$. So $Q(2,\rightarrow)=0+0.5\times25=12.5$.

Since $50>12.5$, the best action in state 2 is **left**.

**Linking Q and the policy.** In each state the best action is the one with the largest $Q$:

$$ \pi(s)=\arg\max_{a}Q(s,a) $$

So if you know all the $Q$ values, you also know the best policy.

**Markov decision process.** The source's note says these methods are Markov decision processes. In short, what happens next depends only on the current state and the chosen action, not on the earlier history.

**Common mistake.** Reading $Q(s,a)$ as the reward of one step. It is the whole discounted return.
"""