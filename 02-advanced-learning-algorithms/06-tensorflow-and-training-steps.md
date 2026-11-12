# TensorFlow and Model Training Steps

> **Source pages:** 27 (bottom, "Tensorflow"), 29 (Model Training Steps) · How a model is specified, compiled and trained, compared for logistic regression and a neural network.

## 1. TensorFlow

- TensorFlow is a machine learning package developed by **Google**.
- **Keras** is a framework in TensorFlow which gives it a layer-centric interface.
- Data is always represented in **matrices** (called *tensors*), unlike NumPy 1-D arrays. This is because it was created to handle large datasets.
- The source adds: *{Code in Lab}.*

## 2. Model training steps

| Step | Logistic regression | Neural network (TensorFlow) |
|---|---|---|
| **1. Specify how to compute the output** given input $\vec x$ and parameters $w,b$ (define the model): $f_{\vec w,b}(\vec x)=\,?$ | `z = np.dot(w, x) + b`<br>`f_x = 1 / (1 + np.exp(-z))` | `model = Sequential([`<br>`    Dense(...),`<br>`    Dense(...)`<br>`])` |
| **2. Specify loss and cost:** $L\left(f_{\vec w,b}(\vec x),y\right)$ and $J(\vec w,b)=\frac{1}{m}\sum L(f(\vec x),y)$ | **Logistic loss**<br>`loss = -y * np.log(f_x) - (1 - y) * np.log(1 - f_x)` | **Binary cross entropy**<br>`model.compile(loss = BinaryCrossentropy())` |
| **3. Train on data to minimize** $J(\vec w,b)$, e.g. gradient descent | `w = w - alpha * dj_dw`<br>`b = b - alpha * dj_db` | `model.fit(X, y, epochs=100)` |

> **Note (from the source):** `model.fit` **implements back propagation** within it (marked with stars on the page).

## Detailed Explanation

> **Additional Explanation:**  
> This explanation has been added to improve understanding and is not a direct transcription of the original handwritten notes.
>
> **The same three steps every time.** Whether you write logistic regression by hand or build a neural network, training has the same shape:
>
> 1. **Define the model.** Say how the output is computed from the input and the parameters.
> 2. **Define the loss and cost.** Say how wrong the output is.
> 3. **Train.** Adjust the parameters to make the cost small.
>
> **What each TensorFlow line means.**
>
> - `Sequential([...])` stacks the layers one after another, in order.
> - `Dense(...)` is one layer, where every unit is connected to all inputs.
> - `model.compile(loss=...)` chooses the cost to minimise. `BinaryCrossentropy` is TensorFlow's name for the logistic loss used for yes/no answers.
> - `model.fit(X, y, epochs=100)` runs the training. An **epoch** is one full pass over the training data, so 100 epochs means 100 passes.
>
> **What happens inside `fit`.** On each step it (a) runs the network forward to get predictions, (b) measures the loss, (c) uses [backpropagation](07-backpropagation-vs-gradient-descent.md) to get the gradients, and (d) takes a gradient-descent step. This is why the source says `fit` "implements back propagation".
>
> **Why the table matches up.** Logistic regression and the neural network use the *same* loss. The difference is only that the network has several layers of parameters instead of one.
>
> **Common mistake.** Choosing the loss that does not match the output. A yes/no output needs the binary loss; several classes need the sparse categorical loss.

## 3. Related topics

- Previous: [Vectorization of a Dense layer](05-vectorization-dense-layer.md)
- Next: [Backpropagation versus gradient descent](07-backpropagation-vs-gradient-descent.md)
- The logistic loss: [Logistic loss and cost](../01-supervised-learning/07-logistic-loss-and-cost.md)