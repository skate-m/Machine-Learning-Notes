D = {}
P='03-model-evaluation-and-ml-practice/'
D[P+'01-train-cv-test.md'] = r"""
**Why not use all the data for training?** A model can look perfect on the data it was trained on simply because it memorised it. To know how it will behave on *new* data, you must keep some data aside that the model never trained on.

**The three sets and their jobs.**

| Set | Used for |
|---|---|
| Training set | Fit the parameters $w,b$ |
| Cross-validation (CV) set | Choose between models (degree, $\lambda$, network size) |
| Test set | One final, honest estimate of performance |

A common way to split is about 60% / 20% / 20%, though the exact split depends on how much data you have.

**A tiny worked example.** Three test examples with predictions $f=[2,3,5]$ and true values $y=[2,4,3]$. The errors are $0,-1,2$, the squares $0,1,4$ (sum $5$), so $J_{test} = 5/(2\cdot3)\approx 0.83$.

**Why the regularization term is left out when reporting errors.** The term $\frac{\lambda}{2m}\sum w_j^2$ is a tool to keep the weights small *while fitting*. It is not part of how wrong the predictions are. The reported errors $J_{train}$, $J_{cv}$, $J_{test}$ only measure the prediction mistakes, so they can be compared fairly between models with different $\lambda$.

**How to read the results.** If $J_{train}$ is low but $J_{cv}$ is much higher, the model is overfitting. If both are high, it is underfitting (see [Bias and variance](03-bias-and-variance.md)).

**Common mistake.** Tuning the model while looking at the test set. Then the test set is no longer unseen, and its score looks better than reality.
"""
D[P+'02-model-selection.md'] = r"""
**The question.** Should the model be a straight line, a quadratic, a cubic ... or a degree-10 polynomial? Training error cannot answer this: it will almost always prefer the most complex model.

**The procedure, step by step.**

1. Fit each candidate model on the **training** set.
2. Compute the cross-validation cost $J_{cv}$ of each one.
3. Pick the model with the **lowest** $J_{cv}$.
4. Only now measure $J_{test}$ of that one model, to report how well it should do on new data.

**Example with made-up numbers** (to show the idea only):

| Degree | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| $J_{cv}$ | 0.90 | 0.35 | 0.30 | 0.42 |

The lowest value is at degree 3, so degree 3 is chosen. Degree 4 is more flexible but does worse on the CV set, which suggests it has started to overfit.

**Why the test set must not be used for choosing.** If you pick the model that looks best on the test set, the test set has helped decide, so its score is slightly too optimistic. This is what the source's postscript warns about. Keeping the CV set for choosing and the test set for a final check avoids it.

**Other things you can choose this way.** The same method works for the regularization parameter $\lambda$, the number of features, and the size of a neural network. For a classifier, the fraction of wrongly classified examples can be used as the cost.

**Common mistake.** Choosing the model by training cost. A very flexible model has almost zero training cost even when it is overfit.
"""
D[P+'03-bias-and-variance.md'] = r"""
**A simple way to diagnose.** Compare three numbers: the baseline (what a human or a good benchmark achieves), the training error and the cross-validation error.

| What you see | Diagnosis |
|---|---|
| Training error far above baseline | High bias (underfitting) |
| CV error far above training error | High variance (overfitting) |
| Both gaps large | Both problems |
| Both gaps small | Good |

**Applying it to the speech example.** Baseline $10.6\%$, training $10.8\%$, CV $14.8\%$.

- Bias gap: $10.8-10.6 = 0.2\%$, which is tiny, so the model fits the training data about as well as a human could.
- Variance gap: $14.8-10.8 = 4.0\%$, which is large. The model does much worse on data it has not seen, so the main problem is **variance**.

**Why the baseline matters.** A training error of $10.8\%$ sounds high by itself. It only looks bad or good when compared with what is achievable, here $10.6\%$.

**How $\lambda$ fits in.** A very large $\lambda$ forces simple models (high bias). A very small $\lambda$ allows complex ones (high variance). The $\lambda$ with the lowest $J_{cv}$ is a good choice.

**The neural-network recipe.** The source's flowchart gives a loop: if the network does not do well on the training set, make it bigger; if it does well on training but not on the CV set, get more data. Repeat until both are good. This works because a large network (with regularization if needed) can usually fit the training data well, and more data then cures the variance.

**Common mistake.** Collecting more data when the real problem is high bias. More data does not help a model that is too simple.
"""
D[P+'04-learning-curves-and-debugging.md'] = r"""
**What a learning curve shows.** Train on 10 examples, then 20, then 30, and so on, and record $J_{train}$ and $J_{cv}$ each time. Plotting them against the training-set size shows how the model behaves as it gets more data.

**Why the two curves move as they do.**

- $J_{train}$ **goes up** with more data. With only a few examples a model can fit them all perfectly; with many it can't.
- $J_{cv}$ **goes down** with more data, because the model learns more of the real pattern.

**What the curve tells you.**

- *High bias:* both curves flatten out at a high error, close to each other. More data will not help, because the model is too simple.
- *High variance:* there is a big gap between a low $J_{train}$ and a higher $J_{cv}$. More data usually helps close the gap.

**Why each fix in the table works.**

| Fix | Why |
|---|---|
| More training examples | Harder to memorise, so less variance |
| Smaller set of features | Simpler model, less variance |
| Increase $\lambda$ | Smaller weights, simpler model, less variance |
| Additional features | More flexible model, less bias |
| Polynomial features | Can fit curves, less bias |
| Decrease $\lambda$ | Less penalty, more flexible, less bias |

**Common mistake.** Trying a fix without first diagnosing. Adding features to a model that is overfitting makes it worse.
"""
D[P+'05-data-centric-improvements.md'] = r"""
**Why data can matter more than code.** The model is only as good as the data it learns from. Often the quickest improvement is better or more relevant data, not a cleverer algorithm.

**Adding data, but the right data.** Suppose error analysis shows that a spam classifier fails mostly on pharmacy spam. Collecting *more pharmacy-spam examples* helps more than collecting more of everything, and it is cheaper.

**Data augmentation.** You take a real example and change it in a way that keeps its label. A picture of the letter "A" stays an "A" when rotated a little, zoomed or made lighter. Each change gives a new training example for free. Important: the change must be realistic. Rotating the digit 6 by 180° makes a 9, which would give the wrong label.

**Data synthesis.** You create new examples from scratch. In the source's example, you type letters in many fonts and colours and take screenshots. This gives lots of labelled examples because you already know which letter you typed.

**Why this is useful.** These methods give more varied data, so they mainly reduce variance (overfitting).

**Common mistake.** Adding noise or changes that never happen in real use. The model then learns to handle situations that do not occur, and the real-world performance does not improve.
"""
D[P+'06-ml-development-and-error-analysis.md'] = r"""
**Development is a loop.** You rarely get a good model on the first try. You choose a design, train it, look at what goes wrong, and use that to choose the next design. Diagnostics such as [bias and variance](03-bias-and-variance.md) and error analysis tell you what to change.

**What error analysis does.** It helps you decide where to spend your effort. Look at the examples the model got wrong, group them by type, and count.

**Reading the spam example.** Shares of the 54 tagged mistakes:

| Category | Count | Share |
|---|---|---|
| Pharma | 21 | about 39% |
| Phishing (steal passwords) | 18 | about 33% |
| Unusual email routing | 7 | about 13% |
| Text in image | 5 | about 9% |
| Deliberate misspellings | 3 | about 6% |

Fixing a rare category (3 cases) can improve things by at most a little. Fixing a large one can remove a big part of the errors. The two biggest categories here, pharma and phishing, deserve the attention.

**Note on the counts.** The categories do not need to add up to the number of examples checked: an example might fit no listed category, or more than one.

**A practical limit.** Manually checking about 100 examples is feasible. For very large error sets, sample 100 or so of them.

**Common mistake.** Spending weeks on a problem that causes only 3% of the errors.
"""
D[P+'07-precision-recall-f1.md'] = r"""
**Why accuracy is not enough.** Imagine a disease that only 1 in 100 people has. A "model" that always says *healthy* is right 99% of the time, yet it finds nobody who is ill. Precision and recall look at the positive class directly.

**Plain-language meaning.**

- **Precision:** of all the cases the model *called* positive, how many really were? (How trustworthy is a positive prediction?)
- **Recall:** of all the cases that really *are* positive, how many did the model find? (How few did it miss?)

**Worked example (made-up).** Out of 100 cases: TP = 8, FP = 2, FN = 4, TN = 86.

- Precision $= 8/(8+2) = 0.80$
- Recall $= 8/(8+4) \approx 0.67$
- $F_1 = 2\cdot 0.80\cdot 0.67 / (0.80+0.67) \approx 0.73$

**The trade-off.** If you only flag a case when you are very sure, precision goes up (few false alarms) but recall goes down (you miss cases). If you flag anything suspicious, recall goes up but precision goes down. Which to prefer depends on the cost of each kind of mistake.

**Why $F_1$ uses the harmonic mean.** The ordinary average of $P=0.5$ and $R=0.02$ would be $0.26$, which looks acceptable. The $F_1$ value is $2(0.5)(0.02)/0.52 \approx 0.04$, which correctly shows that the model is poor. $F_1$ is low unless *both* precision and recall are reasonably high.

**Common mistake.** Swapping the rows and columns of the confusion matrix. In the source, rows are *predicted* and columns are *actual*.
"""
D[P+'08-transfer-learning.md'] = r"""
**The idea.** Training a large network from scratch needs a lot of data and time. Someone may already have trained a network on a huge dataset. Its early layers have learned general things (in images: edges, corners, simple shapes) that are useful for many tasks. You reuse them and only adapt the rest.

**The two options in the source.**

1. **Change only the output layer** (fine tuning in the source's words): keep the downloaded parameters for all earlier layers and train just the output layer. This suits a **small** dataset, because only a few parameters must be learned.
2. **Train all parameters**: start from the downloaded values and let every layer adjust. This suits a **larger** dataset, and usually gives better results if you have the data.

**A rule you must respect.** The input type must be the same: a network pretrained on images can help another image task, but not an audio task.

**Why it works even for a different task.** If the original network learned to recognise cats and dogs, its early layers can also help recognise, say, handwritten digits, because both need to detect strokes and shapes.

**Common mistake.** Changing the input size or type so that it no longer matches the pretrained network.
"""
D[P+'09-ml-project-cycle-and-deployment.md'] = r"""
**The four stages in plain words.**

1. **Scope:** decide what the project is for and what a good result means.
2. **Collect data:** gather and label the examples.
3. **Train model:** train, run error analysis and improve step by step. You may go back to collect more data.
4. **Deploy:** put the model into real use, watch how it behaves and keep it working.

**Why the arrows go back.** Things you learn late (for example, that the model is weak on a type of audio) send you back to earlier stages (collect more of that audio). Real projects loop.

**What deployment looks like.** In the source's example, the phone app records an audio clip $x$ and sends it over the internet (an *API call*) to a server. The server runs the model and sends back the text $\hat y$. The model stays on the server, so it can be updated without changing the app.

**Why monitoring matters.** After release, the real data can change (new accents, new words). Watching the model's performance lets you notice and retrain.

**What MLOps is.** The source's note says *MLOps* is for deploying large-scale models. It is the set of practices for deploying, monitoring and updating models reliably.

**Common mistake.** Treating deployment as the end. The model needs care afterwards.
"""

Q='04-decision-trees-and-ensembles/'
D[Q+'01-decision-trees.md'] = r"""
**How a tree makes a prediction.** Start at the top (the root). At each decision node, check one feature and follow the matching branch. Keep going until you reach a leaf, which holds the answer. In the cat example: *pointy ears* → check *face shape* → *round* → **Cat**.

**The two decisions and why they matter.**

- *Decision 1 (which feature to split on):* a good split gives branches that are as pure as possible (mostly one class). We measure this with [entropy](02-entropy.md) and [information gain](03-information-gain.md).
- *Decision 2 (when to stop):* if you keep splitting until every leaf is perfectly pure, the tree can memorise the training data and overfit. The stopping rules in the source all prevent a tree from becoming too large or too specific.

**The four stopping rules, in plain words.**

| Rule | Why |
|---|---|
| Node is 100% one class | Nothing left to separate |
| Tree reaches the maximum depth | Keeps the tree small and easier to read |
| Purity gain is below a threshold | The split adds almost nothing |
| Too few examples in the node | A split on a handful of examples is unreliable |

**Why people like trees.** A small tree can be read and explained, as the source notes (see [Trees vs neural networks](08-trees-vs-neural-networks.md)).

**Common mistake.** Letting the tree grow until every leaf is pure. It then fits noise.
"""
D[Q+'02-entropy.md'] = r"""
**What impurity means.** A node with 5 cats and 5 dogs is as mixed as it can be (very impure). A node with 10 cats and 0 dogs is pure. Entropy gives each case a number: 0 for pure, up to 1 for the most mixed.

**Worked values** (using $\log_2$):

| $p_1$ | Meaning | $H(p_1)$ |
|---|---|---|
| 0 or 1 | Pure | 0 |
| $1/3$ | 1 cat in 3 | 0.918 |
| 0.2 or 0.8 | Mostly one class | 0.722 |
| 0.5 | Perfectly mixed | 1 |

For example, $H(0.5) = -0.5\log_2 0.5 - 0.5\log_2 0.5 = 0.5 + 0.5 = 1$.

**Why use $\log_2$.** Using base 2 makes the maximum value exactly 1, which is neat.

**Why take $0\log 0 = 0$.** $\log 0$ is not defined. But when $p$ is very small, $p\log p$ gets closer and closer to 0, so defining it as 0 is the sensible choice. It lets the formula work for pure nodes.

**The shape of the curve.** It is a hill: zero at both ends and highest in the middle. Entropy does not care which class is the majority; $p_1=0.2$ and $p_1=0.8$ are equally mixed.

**Common mistake.** Reading entropy as "probability of a cat". It measures how mixed the node is, not which class dominates.
"""
D[Q+'03-information-gain.md'] = r"""
**The goal.** Pick the feature whose split makes the two branches as pure as possible. Information gain measures that: how much did entropy drop?

**Why the branches are weighted.** A branch with 9 of the 10 examples matters much more than one with 1 example. So each branch's entropy is multiplied by $w$, the fraction of examples that went to it. In the source's example both branches have $w=5/10$.

**Checking the ear-shape example.**

- Root: $H(0.5) = 1$.
- Left: $H(0.8)\approx 0.722$. Right: $H(0.2)\approx 0.722$.
- Weighted average after the split: $0.5(0.722)+0.5(0.722) = 0.722$.
- Gain: $1 - 0.722 \approx 0.28$.

**Comparing with another feature (hypothetical).** Suppose splitting on *face shape* gave a left branch of 7 examples with 4 cats and a right branch of 3 with 1 cat. Then $H(4/7)\approx 0.985$, $H(1/3)\approx 0.918$, the weighted entropy is $0.7(0.985)+0.3(0.918)\approx 0.965$, and the gain is $\approx 0.03$. Ear shape (0.28) wins clearly, so it is chosen for the root.

**Recursive splitting.** After the root is split, you repeat the same steps inside each branch on the examples that landed there, until a stopping rule from [Decision trees](01-decision-trees.md) applies.

**Common mistake.** Forgetting the weights $w$ and averaging the two branch entropies equally.
"""
D[Q+'04-one-hot-encoding.md'] = r"""
**The problem.** A tree split asks a yes/no question. With ear shape coded as 0 and 1 (pointy / floppy) that is easy. If a third value, *oval*, appears, a single 0/1 feature can no longer represent it.

**The solution.** Make one yes/no feature for each possible value. Exactly one of them is 1 ("hot") for each animal.

| Animal | Pointy ears | Floppy ears | Oval ears |
|---|:-:|:-:|:-:|
| A (pointy) | 1 | 0 | 0 |
| B (floppy) | 0 | 1 | 0 |
| C (oval) | 0 | 0 | 1 |

(The first row and the last row are the two shown in the source; the middle row follows the same rule.)

**Why this works well.** Every new feature is a simple yes/no question, so the tree can keep using two-way splits, and the information-gain formula is unchanged.

**It is useful beyond trees.** Neural networks and linear or logistic regression need numbers. A code like 1, 2, 3 would wrongly suggest that oval is "bigger" than floppy. One-hot features avoid this.

**Common mistake.** Coding categories as 1, 2, 3 and feeding them to a model that treats them as quantities.
"""
D[Q+'05-regression-trees.md'] = r"""
**What changes compared with a classification tree.** The tree now predicts a *number* (an animal's weight). The structure is the same: splits on features, with leaves at the bottom. Only two things change: how a split is judged and what a leaf predicts.

**How a split is judged.** A good split makes the weights inside each branch similar to each other, i.e. gives a **small variance**. Variance measures how spread out the numbers are. So we replace entropy with variance in the same formula.

**Check of the source's numbers.**

- Root variance: $20.51$.
- Weighted variance after the split: $0.5(1.47)+0.5(21.87) = 11.67$.
- Gain: $20.51 - 11.67 = 8.84$.

The *pointy* branch became very uniform (variance 1.47), so the split helps a lot, even though the floppy branch is still spread out.

**A small variance example.** Weights $7.2$ and $9.2$: the mean is $8.2$, and the variance is $\frac{(7.2-8.2)^2+(9.2-8.2)^2}{2}=1.0$.

**What a leaf predicts.** For a new animal, the usual choice is the **average weight** of the training examples in the leaf it reaches.

**Common mistake.** Using entropy for a numerical target. Entropy is for classes; use variance for numbers.
"""
D[Q+'06-random-forest.md'] = r"""
**The idea.** A single decision tree can change a lot if the training data changes a little (high variance). A random forest builds many different trees and lets them vote. Mistakes of individual trees tend to cancel out.

**How each tree gets different data.** With sampling with replacement, each new training set has size $m$, but some examples appear twice or more and others not at all. Each draw misses a particular example with probability $1-\frac{1}{m}$, so for large $m$ about $1/e\approx 37\%$ of the original examples are left out of any one new set, and about $63\%$ appear at least once. So every tree sees a slightly different version of the data.

**Why randomise the features too.** Without it, strong features would win at the top of almost every tree, so the trees would look alike and voting would add little. Letting each node choose from only a random $K<n$ features makes the trees more different.

**Choosing $K$.** The source's rule is $K=\sqrt{n}$. For $n=100$ features that gives $K=10$ candidates at each node.

**Making the final prediction.** For classification, each tree votes and the majority class wins.

**Trade-offs.** More trees usually do not hurt accuracy but take longer to train and use. A forest is also harder to read than one small tree.

**Common mistake.** Forgetting to put the example back after picking it. Without replacement, each new set would just be a copy of the original.
"""
D[Q+'07-xgboost.md'] = r"""
**What boosting means.** Instead of building trees independently (as in a random forest), boosting builds them *one after another*. Each new tree concentrates on the examples the previous trees got wrong. The final model is the combined effect of all the trees. XGBoost is a fast, well-tuned, open-source version of this idea.

**Why it is popular.** The source lists the reasons: it is fast and efficient, it comes with good defaults for how to split and when to stop, and it has built-in regularization against overfitting. This makes it a strong choice for competitions such as Kaggle, where tabular data is common.

**Reading the code.** The steps are the same for both tasks:

1. `model = XGBClassifier()` (or `XGBRegressor()`) creates the model.
2. `model.fit(X_train, Y_train)` trains it on the training data.
3. `y_pred = model.predict(X_test)` makes predictions for new data.

Use the **Classifier** when the target is a class (cat / not cat) and the **Regressor** when it is a number (weight).

**Good habits.** Keep the test set aside until the end, and use the cross-validation set to compare settings.

**Common mistake.** Using the classifier for a numerical target, or the regressor for a class label.
"""
D[Q+'08-trees-vs-neural-networks.md'] = r"""
**A quick way to choose.**

| Your data looks like... | Good first choice |
|---|---|
| A table with columns (prices, ages, counts) | Decision tree, random forest or XGBoost |
| Images, audio, text | Neural network |
| A pipeline of several models trained together | Neural networks |

**Why trees suit tables.** Table columns usually mean something on their own, and splitting on them is natural. Trees train quickly, so you can try many ideas, and a small tree can be explained to others.

**Why neural networks suit raw signals.** The useful features in a picture or a sound are not given; the network learns them layer by layer (see [Neural networks](../02-advanced-learning-algorithms/01-neural-networks.md)). They can also use [transfer learning](../03-model-evaluation-and-ml-practice/08-transfer-learning.md) from a pretrained network.

**Why networks are easier to combine.** All the parts are trained with gradient descent, so several networks can be linked and trained together as one system. Trees cannot be trained together in that way.

**Speed.** The source notes that neural networks may be slower. Trees often give a good answer in a short time.

**Common mistake.** Using a neural network on a small table of data because it sounds more advanced. A tree-based model is often better and faster there.
"""