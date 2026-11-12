# XGBoost (eXtreme Gradient Boosting)

> **Source page:** 9 · A popular open-source implementation of boosted trees.

## 1. Features (from the source)

- Open-source implementation of boosted trees.
- Fast and efficient implementation.
- Good choice of default splitting criteria and of when to stop splitting.
- Built-in regularization to prevent overfitting.
- Highly competitive for ML competitions (Kaggle competitions).

## 2. Usage

**Classification**

```python
from xgboost import XGBClassifier

model = XGBClassifier()
model.fit(X_train, Y_train)
y_pred = model.predict(X_test)
```

**Regression**

```python
from xgboost import XGBRegressor

model = XGBRegressor()
model.fit(X_train, Y_train)
y_pred = model.predict(X_test)
```

> **Note on the source:** the page writes `Y_train` (capital) and `y_pred`; these variable names are kept. The import lines are written with small slips ("impor") in the handwriting that have been read as `import`.

## Detailed Explanation

> **Additional Explanation:**  
> This explanation has been added to improve understanding and is not a direct transcription of the original handwritten notes.
>
> **What boosting means.** Instead of building trees independently (as in a random forest), boosting builds them *one after another*. Each new tree concentrates on the examples the previous trees got wrong. The final model is the combined effect of all the trees. XGBoost is a fast, well-tuned, open-source version of this idea.
>
> **Why it is popular.** The source lists the reasons: it is fast and efficient, it comes with good defaults for how to split and when to stop, and it has built-in regularization against overfitting. This makes it a strong choice for competitions such as Kaggle, where tabular data is common.
>
> **Reading the code.** The steps are the same for both tasks:
>
> 1. `model = XGBClassifier()` (or `XGBRegressor()`) creates the model.
> 2. `model.fit(X_train, Y_train)` trains it on the training data.
> 3. `y_pred = model.predict(X_test)` makes predictions for new data.
>
> Use the **Classifier** when the target is a class (cat / not cat) and the **Regressor** when it is a number (weight).
>
> **Good habits.** Keep the test set aside until the end, and use the cross-validation set to compare settings.
>
> **Common mistake.** Using the classifier for a numerical target, or the regressor for a class label.

## 3. Related topics

- Previous: [Random forest](06-random-forest.md)
- Next: [Decision trees versus neural networks](08-trees-vs-neural-networks.md)