<div align="center">

# Machine Learning Notes

**Structured machine learning notes with mathematical explanations, worked examples and visual breakdowns of core algorithms.**

[![GitHub stars](https://img.shields.io/github/stars/skate-m/Machine-Learning-Notes?style=flat)](https://github.com/skate-m/Machine-Learning-Notes/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/skate-m/Machine-Learning-Notes?style=flat)](https://github.com/skate-m/Machine-Learning-Notes/network)
[![Last commit](https://img.shields.io/github/last-commit/skate-m/Machine-Learning-Notes)](https://github.com/skate-m/Machine-Learning-Notes/commits/main)

</div>

---

## Overview

Machine Learning Notes is a topic-organised study resource covering the mathematical foundations and practical ideas behind common machine learning algorithms.

The notes are organised as short, linked Markdown chapters rather than one long document. Equations use LaTeX, and explanatory additions are labelled so readers can distinguish them from source-note transcriptions.

The repository is being built module by module. **The supervised-learning module is currently available; the remaining modules will be added as they are prepared.**

## Learning map

| Module | Topics | Status |
|---|---|---|
| [01 · Supervised learning](01-supervised-learning/README.md) | Linear and logistic regression, gradient descent, feature scaling, feature engineering, overfitting and regularization | Available |
| [02 · Advanced learning algorithms](02-advanced-learning-algorithms/) | Neural networks, forward propagation, activation functions, backpropagation and model training | In progress |
| [03 · Model evaluation and ML practice](03-model-evaluation-and-ml-practice/) | Train / validation / test sets, bias and variance, error analysis and learning curves | Planned |
| [04 · Decision trees and ensembles](04-decision-trees-and-ensembles/) | Decision trees, entropy, information gain, random forests and boosting | Planned |
| [05 · Unsupervised learning](05-unsupervised-learning/) | Clustering, K-means, anomaly detection and Gaussian distributions | Planned |
| [06 · Recommenders and reinforcement learning](06-recommenders-and-reinforcement-learning/) | Collaborative filtering, content-based recommendations and reinforcement learning | Planned |

## Start here: supervised learning

The first module contains nine chapters:

1. [Linear regression](01-supervised-learning/01-linear-regression.md)
2. [Linear regression with multiple features](01-supervised-learning/02-multiple-features-and-vectorization.md)
3. [Feature scaling](01-supervised-learning/03-feature-scaling.md)
4. [Gradient descent in practice](01-supervised-learning/04-gradient-descent-in-practice.md)
5. [Feature engineering and polynomial regression](01-supervised-learning/05-feature-engineering-and-polynomial-regression.md)
6. [Decision boundary](01-supervised-learning/06-decision-boundary.md)
7. [Logistic loss, cost and gradient descent](01-supervised-learning/07-logistic-loss-and-cost.md)
8. [Overfitting](01-supervised-learning/08-overfitting.md)
9. [Regularization](01-supervised-learning/09-regularization.md)

See the [supervised-learning index](01-supervised-learning/README.md) for source-page references and chapter navigation.

## Repository structure

```text
Machine-Learning-Notes/
├── 01-supervised-learning/
│   ├── README.md
│   └── 01-09 topic chapters
├── 02-advanced-learning-algorithms/
├── 03-model-evaluation-and-ml-practice/
├── 04-decision-trees-and-ensembles/
├── 05-unsupervised-learning/
├── 06-recommenders-and-reinforcement-learning/
├── assets/
│   ├── diagrams/
│   └── figures/
├── CONTRIBUTING.md
└── README.md
```

## How these notes are organised

- **Source notes:** formulas, examples and topic ordering are transcribed from the underlying study material.
- **Additional explanations:** clarifications added for readability are explicitly labelled.
- **Uncertain readings:** ambiguous handwriting or notation is called out rather than silently guessed.
- **Navigation:** chapters link to prerequisites and related topics wherever possible.
- **Figures:** diagrams and plots are kept in the shared `assets/` directory and referenced from the relevant chapter.

GitHub renders LaTeX math in Markdown, so equations can be read directly in the repository.

## Contributing

Corrections, clearer explanations, typo fixes and original diagrams are welcome through pull requests. Read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting changes.

Please make sure proposed material is your own work or that you have permission to contribute it. A pull request does not, by itself, transfer copyright ownership; a separate written contributor agreement may be required for substantial contributions.

## Copyright and reuse

No open-source or Creative Commons licence is currently granted for this repository. Unless a file states otherwise, the original material is reserved by its respective copyright holder. Public visibility on GitHub is not permission to republish, sell or redistribute the notes.

This is an independent educational study resource, not an official course publication. Third-party course content and trademarks remain the property of their respective owners.
