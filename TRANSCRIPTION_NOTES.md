# Transcription Notes and Source Audit

This file lets readers tell **what the handwritten source says** apart from **what was added while digitising it**.

## 1. Pages inspected

**53 of 53 pages** of the handwritten PDF were inspected. Three pairs of pages are exact duplicates:

| Duplicate pages | Content |
|---|---|
| 7 and 12 | Decision trees vs neural networks |
| 15 and 28 | Backpropagation vs gradient descent |
| 52 and 53 | Train/test and train/cross-validation/test procedure |

Several pages are photographed rotated by 90° (2, 3, 4, 5, 15, 22, 23, 26, 27, 28, 29, 35, 37, 40); they were read in their rotated orientation. The source is not in learning order, so the notes are reordered by prerequisite.

## 2. Page-to-topic mapping

| PDF page | Topic | Main contents | Status | Note file |
|---|---|---|---|---|
| 1 | Entropy as a measure of impurity | $H(p_1)$, curve, information gain remark | Transcribed | [Entropy](04-decision-trees-and-ensembles/02-entropy.md) |
| 2 | Logistic (log) loss, simplified loss | loss cases, $-\log$ sketch | Transcribed | [Logistic loss](01-supervised-learning/07-logistic-loss-and-cost.md) |
| 3 | Decision boundary; why not MSE | linear and circular boundaries, convex vs non-convex | Transcribed | [Decision boundary](01-supervised-learning/06-decision-boundary.md), [Logistic loss](01-supervised-learning/07-logistic-loss-and-cost.md) |
| 4 | Overfitting | underfit/ideal/overfit sketches, 3 remedies | Transcribed | [Overfitting](01-supervised-learning/08-overfitting.md) |
| 5 | Gradient descent for logistic regression | cost, updates, sigmoid | Transcribed | [Logistic loss and cost](01-supervised-learning/07-logistic-loss-and-cost.md) |
| 6 | Z-score normalization; checking convergence | $\sigma,\mu$, ranges, $\varepsilon=10^{-3}$ | Transcribed (one digit flagged) | [Feature scaling](01-supervised-learning/03-feature-scaling.md), [GD in practice](01-supervised-learning/04-gradient-descent-in-practice.md) |
| 7 | Decision trees vs neural networks | comparison lists | Transcribed | [Trees vs NNs](04-decision-trees-and-ensembles/08-trees-vs-neural-networks.md) |
| 8 | Learning-rate note; feature engineering; polynomial regression | $\alpha$ values, area example | Transcribed | [GD in practice](01-supervised-learning/04-gradient-descent-in-practice.md), [Feature engineering](01-supervised-learning/05-feature-engineering-and-polynomial-regression.md) |
| 9 | XGBoost | features, code | Transcribed | [XGBoost](04-decision-trees-and-ensembles/07-xgboost.md) |
| 10 | Sampling with replacement; random forest | algorithm, $K=\sqrt n$ | Transcribed | [Random forest](04-decision-trees-and-ensembles/06-random-forest.md) |
| 11 | Course 3; clustering; K-means | intuition, algorithm | Transcribed | [K-means](05-unsupervised-learning/01-clustering-and-k-means.md) |
| 12 | Duplicate of page 7 | — | Duplicate | (as page 7) |
| 13 | Information gain | cat/dog example, formula | Transcribed | [Information gain](04-decision-trees-and-ensembles/03-information-gain.md) |
| 14 | Course I; linear regression | model, cost, gradient descent | Transcribed (cost index flagged) | [Linear regression](01-supervised-learning/01-linear-regression.md) |
| 15 | Backprop vs gradient descent | table | Transcribed | [Backprop vs GD](02-advanced-learning-algorithms/07-backpropagation-vs-gradient-descent.md) |
| 16 | Feature scaling | normalization, mean normalization | Transcribed | [Feature scaling](01-supervised-learning/03-feature-scaling.md) |
| 17 | One-hot encoding; regression trees | table, variance example | Transcribed (one digit flagged) | [One-hot](04-decision-trees-and-ensembles/04-one-hot-encoding.md), [Regression trees](04-decision-trees-and-ensembles/05-regression-trees.md) |
| 18 | Linear regression with multiple features | model, vectorization, GD | Transcribed | [Multiple features](01-supervised-learning/02-multiple-features-and-vectorization.md) |
| 19 | Choosing K (elbow) | sketch, remarks | Transcribed | [Choosing K](05-unsupervised-learning/03-choosing-k.md) |
| 20 | K-means notation, distortion, random init | formulas, loop | Transcribed | [K-means cost](05-unsupervised-learning/02-k-means-cost-and-initialization.md) |
| 21 | Anomaly detection intuition | density estimation, $\varepsilon$ | Transcribed | [Anomaly detection](05-unsupervised-learning/05-anomaly-detection.md) |
| 22 | Multiclass; softmax | formulas, 4-class example | Transcribed | [Softmax](02-advanced-learning-algorithms/04-multiclass-and-softmax.md) |
| 23 | Activation functions | linear, sigmoid, ReLU, others | Transcribed | [Activation functions](02-advanced-learning-algorithms/03-activation-functions.md) |
| 24 | Adam; types of layers | convolutional ECG example | Transcribed (labels partly unclear) | [Adam and layers](02-advanced-learning-algorithms/08-adam-and-layer-types.md) |
| 25 | Sparse categorical cross-entropy | loss cases, curve | Transcribed | [Softmax](02-advanced-learning-algorithms/04-multiclass-and-softmax.md) |
| 26 | For loop vs vectorization | Dense code | Transcribed (brackets unclear) | [Vectorization](02-advanced-learning-algorithms/05-vectorization-dense-layer.md) |
| 27 | Intuition; TensorFlow | 25/15/1 network, Keras note | Transcribed (indices partly unclear) | [Layer computation](02-advanced-learning-algorithms/02-layer-computation.md), [TensorFlow](02-advanced-learning-algorithms/06-tensorflow-and-training-steps.md) |
| 28 | Duplicate of page 15 | — | Duplicate | (as page 15) |
| 29 | Model training steps (TensorFlow) | 3-step table | Transcribed | [TensorFlow](02-advanced-learning-algorithms/06-tensorflow-and-training-steps.md) |
| 30 | Finding related items; collaborative vs content-based | distance, definitions | Transcribed | [Related items](06-recommenders-and-reinforcement-learning/06-finding-related-items.md), [Collab vs content](06-recommenders-and-reinforcement-learning/02-collaborative-vs-content-based.md) |
| 31 | Binary-label collaborative filtering; mean normalization | cross-entropy, matrix | Transcribed (one value flagged) | [Binary labels](06-recommenders-and-reinforcement-learning/04-binary-labels.md), [Mean normalization](06-recommenders-and-reinforcement-learning/05-mean-normalization.md) |
| 32 | Ranking; retrieval; reinforcement learning (return) | pipeline, Mars rover | Transcribed | [Retrieval and ranking](06-recommenders-and-reinforcement-learning/08-retrieval-and-ranking.md), [Return](06-recommenders-and-reinforcement-learning/09-reinforcement-learning-return.md) |
| 33 | Content-based deep learning; retrieval and ranking | $v_u\cdot v_m$, two networks | Transcribed (labels unclear) | [Content-based DL](06-recommenders-and-reinforcement-learning/07-content-based-deep-learning.md) |
| 34 | Evaluating anomaly detection | data splits, metrics | Transcribed | [Evaluating anomaly detection](05-unsupervised-learning/06-evaluating-anomaly-detection.md) |
| 35 | Regularized linear and logistic regression | cost, gradient descent | Transcribed | [Regularization](01-supervised-learning/09-regularization.md) |
| 36 | Gaussian distribution | formula, $\mu,\sigma^2$ | Transcribed | [Gaussian](05-unsupervised-learning/04-gaussian-distribution.md) |
| 37 | Regularized cost function (intuition) | penalty example, $\lambda$ | Transcribed (digits flagged) | [Regularization](01-supervised-learning/09-regularization.md) |
| 38 | Collaborative filtering cost | 3 cost formulas, GD | Transcribed | [CF cost](06-recommenders-and-reinforcement-learning/03-collaborative-filtering-cost.md) |
| 39 | Choosing features; recommender notation | notation list | Transcribed | [Anomaly detection](05-unsupervised-learning/05-anomaly-detection.md), [Notation](06-recommenders-and-reinforcement-learning/01-recommender-systems-notation.md) |
| 40 | Course 2; neural networks | t-shirt example, notation, image recognition | Transcribed (labels flagged) | [Neural networks](02-advanced-learning-algorithms/01-neural-networks.md) |
| 41 | Policy; Q function | definition, $Q(2,\leftarrow)=50$ | Transcribed (cell values unclear) | [Policy and Q](06-recommenders-and-reinforcement-learning/10-policy-and-q-function.md) |
| 42 | Bias/variance diagnostics | curve, speech example | Transcribed | [Bias and variance](03-model-evaluation-and-ml-practice/03-bias-and-variance.md) |
| 43 | Deployment; precision/recall matrix | server/app, confusion matrix | Transcribed (scribble not read) | [Deployment](03-model-evaluation-and-ml-practice/09-ml-project-cycle-and-deployment.md), [Precision/recall](03-model-evaluation-and-ml-practice/07-precision-recall-f1.md) |
| 44 | Transfer learning; cycle of ML project | summary, cycle | Transcribed | [Transfer learning](03-model-evaluation-and-ml-practice/08-transfer-learning.md), [Project cycle](03-model-evaluation-and-ml-practice/09-ml-project-cycle-and-deployment.md) |
| 45 | Decision trees | cat tree, stopping rules | Transcribed | [Decision trees](04-decision-trees-and-ensembles/01-decision-trees.md) |
| 46 | Precision, recall, F1 | formulas, trade-off | Transcribed | [Precision/recall/F1](03-model-evaluation-and-ml-practice/07-precision-recall-f1.md) |
| 47 | Bias/variance trade-off for NNs | flowchart, priorities | Transcribed | [Bias and variance](03-model-evaluation-and-ml-practice/03-bias-and-variance.md) |
| 48 | Learning curve; debugging | curve, fix table | Transcribed | [Learning curves](03-model-evaluation-and-ml-practice/04-learning-curves-and-debugging.md) |
| 49 | Adding data; augmentation; synthesis | text | Transcribed | [Data-centric](03-model-evaluation-and-ml-practice/05-data-centric-improvements.md) |
| 50 | ML development; error analysis | loop, spam counts | Transcribed (conclusion flagged) | [Error analysis](03-model-evaluation-and-ml-practice/06-ml-development-and-error-analysis.md) |
| 51 | Model selection | degrees 1–10, remarks | Transcribed (Hinglish translated) | [Model selection](03-model-evaluation-and-ml-practice/02-model-selection.md) |
| 52 | Train/test; train/CV/test | formulas | Transcribed | [Train/CV/test](03-model-evaluation-and-ml-practice/01-train-cv-test.md) |
| 53 | Duplicate of page 52 | — | Duplicate | (as page 52) |

## 3. Ambiguous or uncertain handwriting

Marked `[UNCLEAR IN SOURCE]` in the notes.

| Page | What is unclear | How it was handled |
|---|---|---|
| 6 | Upper limit of $x_1$ after z-scoring: "3.1" or "8.1" | Read as 3.1 ($(2000-600)/450\approx3.11$) |
| 17 | Floppy-ear variance "21-87" | Read as 21.87 |
| 24 | Labels "a₁–a₅" and layer sizes in the ECG sketch | Described in words only |
| 26 | Bracket nesting in `np.array(...)` for `x` and `b` | Written as 1-D arrays; flagged |
| 27 | Index labels in the expressions for $a^{[2]}, a^{[3]}$ | Described by pattern, not copied |
| 31 | Mean of movie 4 written 2.5 (known ratings give 2.25) | Kept as written; flagged |
| 33 | Labels beside the user-preference vector | Not transcribed |
| 37 | Coefficients in $f(x)=28x_1-385x_2^2+39x_3^3$ and its smoothed version | Transcribed; flagged as possibly misread |
| 40 | Labels on the middle layer of the image-recognition sketch | "eyes, nose, …" |
| 41 | Values in cells 2–3 of the Q-function sketch | Only the value 50 (confirmed by the calculation) is used |
| 43 | Scribbled-out first attempts at precision/recall | Not transcribed (final definitions are on p. 46) |

## 4. Apparent mathematical or conceptual inconsistencies

The source was **not corrected**; each item is preserved and flagged in the relevant note.

1. **p. 14** — the cost sum runs from $n=0$ to $m$ and $f$, $y$ have no example index. The usual form uses $i=1,\dots,m$.
2. **p. 5 / p. 35** — the logistic cost has no brackets around the two log terms; $\partial J/\partial w_j$ for regularized logistic regression is written without a summation sign.
3. **p. 31** — $\mu_4=2.5$, but $(0+0+5+4)/4=2.25$.
4. **p. 38 / 39** — $m^{(j)}$ is defined but not used in the cost formulas; the first gradient-descent line uses subscript $i$ where the cost uses $k$.
5. **p. 36** — the Gaussian sketch marks the peak at 1; the density peak is $1/(\sqrt{2\pi}\sigma)$.
6. **p. 1** — the hand-drawn entropy curve peaks below 1; the true maximum is exactly 1.
7. **p. 50** — the conclusion says phishing (18) is the bigger problem, while pharma has the higher count (21).
8. **p. 51** — "Train data, negligible cost, underfit": a negligible training cost normally indicates overfitting.
9. **p. 52/53** — $J$ includes the regularization term, while the next section says to compute errors without it (see the note in the topic page).
10. **p. 18** — the "After" vectorized line shows `np.dot(w, x)` without `+ b`.

## 5. Source content not confidently transcribed

- Hinglish sentences on p. 51 are translated; the originals are quoted below.
  - *"Lowest Cross Validation set (CV) cost jo bhi dega, that model to pick."*
  - *"Test data ke cost pe check karke lowest cost lete, then overfitting. Train data, negligible cost, underfit."*
- The source says the detail of backpropagation is "in notebook (jupyter)"; it is not part of the 53 pages.

## 6. Additional explanations inserted

All are labelled **Additional Explanation** in the notes.

| Note | Addition |
|---|---|
| Linear regression | Usual form of the cost with $i=1..m$; simultaneous update of $w,b$ |
| Feature scaling | Why scaling is done (short statement) |
| Decision boundary | $g$ is the sigmoid and $g(0)=0.5$ |
| Logistic loss | How the two loss cases combine; update rules resemble linear regression |
| Model selection | Reading of "use miscalculated outputs as cost" |
| Information gain | Numerical evaluation (≈0.28) |
| Regression trees | Numerical evaluation (8.84) |
| Reinforcement learning return | Which path matches the number 72.9 |
| **Every topic note (all 50)** | A **Detailed Explanation** section before *Related topics*: plain-language intuition, why the idea is needed, worked examples, common mistakes. All numbers in it are my own calculations or clearly marked made-up examples, **not** values from the source. |

The *Detailed Explanation* sections never replace or alter what the source says; they sit in their own labelled block at the end of each note. Short "Note on the source" remarks, the redrawn **figures and diagrams** (made with Python/Matplotlib and hand-built SVG, clearly captioned as schematic or illustrative where they are not computed from the source) and the table formatting are also editorial. No equation, value or topic outside the source was introduced.

## 7. Gaps in the source

The source has no page for several topics referred to in the course structure (for example the definition of the sigmoid in logistic regression, forward propagation as a named topic, or content-based filtering code). They were **not** added.