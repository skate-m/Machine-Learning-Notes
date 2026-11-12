<p align="center">
  <img src="assets/diagrams/banner.svg" alt="Machine Learning Notes" width="100%">
</p>

# Machine Learning Notes

A set of digital notes made from **53 pages of handwritten Machine Learning notes**. The handwriting has been typeset, the equations rewritten in LaTeX, and the sketches redrawn as diagrams placed right next to the explanation they support.

**Who is it for?** University students learning Machine Learning who want short, structured notes for learning and revision.

> The notes follow the topics of the source and nothing else. Wherever the handwriting was unclear, or looked like a slip, it is flagged instead of silently fixed — see [TRANSCRIPTION_NOTES.md](TRANSCRIPTION_NOTES.md). Text added to help understanding is always marked **Additional Explanation**.

## Learning roadmap

![Recommended order of the six modules](assets/diagrams/learning-roadmap.svg)

1. Start with **supervised learning** — everything else builds on its cost functions and gradient descent.
2. Move to **neural networks**, which reuse those ideas.
3. Learn how to **evaluate and improve** models (bias, variance, error analysis).
4. Study **decision trees and ensembles** as the other major family of supervised models.
5. Continue with **unsupervised learning** (clustering, anomaly detection).
6. Finish with **recommender systems and reinforcement learning**.

## Table of contents

{{TOC}}
## Repository features

- **Digitised notes** — every page of the handwritten PDF is accounted for.
- **Mathematical equations** — KaTeX/LaTeX equations that render on GitHub.
- **Embedded visualisations** — SVG diagrams and Matplotlib figures inside each topic page.
- **Structured learning sequence** — pages reordered by prerequisite, not by notebook order.
- **Student-friendly explanations** — every topic ends with a *Detailed Explanation* (intuition, worked examples, common mistakes), clearly labelled as an addition to the handwritten source.
- **Source audit** — [TRANSCRIPTION_NOTES.md](TRANSCRIPTION_NOTES.md) lists unclear handwriting, apparent errors and every added explanation.

## Navigation

- Each module folder has a `README.md` with its topic list.
- Each topic page ends with **Related topics** links to the previous, next and connected notes.
- Quick links: [Linear regression](01-supervised-learning/01-linear-regression.md) · [Neural networks](02-advanced-learning-algorithms/01-neural-networks.md) · [Bias and variance](03-model-evaluation-and-ml-practice/03-bias-and-variance.md) · [Decision trees](04-decision-trees-and-ensembles/01-decision-trees.md) · [K-means](05-unsupervised-learning/01-clustering-and-k-means.md) · [Recommenders](06-recommenders-and-reinforcement-learning/01-recommender-systems-notation.md)

## Optional: browse as a website

The same Markdown files can be viewed as a dark-themed documentation site (Midnight Lavender palette, search, KaTeX):

```bash
pip install -r requirements.txt
bash scripts/serve_site.sh          # opens http://127.0.0.1:8000
```

## Regenerating figures

```bash
pip install numpy matplotlib
python scripts/make_figures.py      # assets/figures/*.png
python scripts/make_diagrams.py     # assets/diagrams/*.svg
python scripts/build_indexes.py     # module READMEs, this README, mkdocs.yml
```

*Colour palette: background `#171821`, cards `#2C2B40`, accent `#A78BFA` / `#E89BB5`, maths `#EAC477`, success `#91C7A5`.*