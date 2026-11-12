D = {}
D['01-supervised-learning/01-linear-regression.md'] = r"""
**The big idea.** Suppose you want to predict the price of a house from its size. Linear regression draws the straight line that best follows the data. Once the line is drawn, you can read off a price for any new size. The line is controlled by two numbers: $w$ (how steep it is) and $b$ (where it crosses the vertical axis).

**Why we need a cost function.** Many lines are possible, so we need one number that says how bad a line is. For every training example we take *prediction minus true value*. We square it so that errors above and below the line do not cancel, and so that big mistakes count more. We then average over the $m$ examples. The extra $\frac{1}{2}$ is only for convenience: when we take the derivative, the 2 from the square cancels it.

**Worked example (made-up data).** Take three examples: $(x,y) = (1,1), (2,2), (3,3)$.

- With $w=1,\ b=0$ the line passes through every point, so $J=0$. This is the best possible line.
- With $w=0.5,\ b=0$ the predictions are $0.5, 1, 1.5$. The errors are $-0.5, -1, -1.5$, the squares are $0.25, 1, 2.25$ (sum $3.5$), so $J = 3.5/(2\cdot 3) \approx 0.583$.

**One step of gradient descent on that bad line** ($w=0.5,\ b=0,\ \alpha=0.1$).

- $\frac{\partial J}{\partial w} = \frac{1}{3}\left[(-0.5)(1)+(-1)(2)+(-1.5)(3)\right] = -2.33$
- $\frac{\partial J}{\partial b} = \frac{1}{3}(-0.5-1-1.5) = -1$
- New values: $w = 0.5 - 0.1(-2.33) \approx 0.733$ and $b = 0 - 0.1(-1) = 0.1$.

Both numbers moved towards the better line ($w=1,\ b=0$). The derivative is negative, so subtracting it *increases* the parameter.

**How to read the derivative.** The derivative tells you which way the cost goes up. Gradient descent walks the opposite way, downhill, a little at a time.

**Common mistakes.**

- Updating $w$ first and then using the *new* $w$ to update $b$. Both updates must use the old values.
- Using a learning rate that is too large, so the cost goes up instead of down.
- Forgetting that the cost is measured on the *training* data only.
"""
D['01-supervised-learning/02-multiple-features-and-vectorization.md'] = r"""
**Why more than one feature.** A house price depends on size, but also on the number of bedrooms, the number of floors and the age. Each feature $x_j$ gets its own weight $w_j$. A large positive weight means "this feature pushes the price up"; a negative weight means it pushes it down.

**Worked example (made-up numbers).** Let $\vec w = [0.1,\ 4,\ 10,\ -2]$, $b = 80$ and a house $\vec x = [2104,\ 5,\ 1,\ 45]$ (size, bedrooms, floors, age).

$$ f = 0.1(2104) + 4(5) + 10(1) + (-2)(45) + 80 = 210.4 + 20 + 10 - 90 + 80 = 230.4 $$

**Why the dot product notation helps.** Writing $\vec w\cdot\vec x + b$ replaces a long sum with a short expression. It also means the same formula works for 2 features or 2 million.

**Why vectorization is faster.** The loop in the notes multiplies one pair at a time. `np.dot` hands the whole job to optimised code that can multiply many pairs at once on modern hardware. The result is the same, but it can be many times faster, which matters a lot with large data.

**Gradient descent with many features.** The rule is the same as before, applied once per weight. The only thing that changes is the last factor, $x_j^{(i)}$, which is the value of the $j$-th feature in the $i$-th example. A feature that is large in an example makes the matching weight change more.

**Common mistakes.**

- Mixing up $x_j^{(i)}$: the *bottom* index is the feature, the *top* index in brackets is the example.
- Forgetting the bias $b$ after calling `np.dot(w, x)`.
- Updating the weights one after another instead of all together.
"""
D['01-supervised-learning/03-feature-scaling.md'] = r"""
**The problem.** Imagine $x_1$ is the size of a house (300 to 2000) and $x_2$ the number of bedrooms (0 to 5). A small change in the weight of $x_1$ changes the prediction a lot, because $x_1$ is large. The same change for $x_2$ barely matters. The cost surface becomes a long thin valley, and gradient descent bounces from side to side instead of going straight to the bottom. Scaling the features to similar sizes makes the valley more round, so fewer steps are needed.

**Worked example with the source's numbers.** Take a house with $x_1 = 1000$.

| Method | Calculation | Result |
|---|---|---|
| Divide by max | $1000/2000$ | $0.5$ |
| Mean normalization | $(1000-600)/(2000-300)$ | $\approx 0.235$ |
| Z-score | $(1000-600)/450$ | $\approx 0.889$ |

**Which one to use?** All three do the same job. Z-score is useful when you want to know "how many standard deviations from the average is this value?". Dividing by the maximum is the simplest. In practice the exact choice matters less than doing *some* scaling when the ranges are very different.

**A good target.** Aim for features that lie roughly between $-1$ and $1$. Ranges such as $-3$ to $3$ are fine. Ranges like $-100$ to $100$, or $-0.001$ to $0.001$, are worth rescaling.

**Common mistakes.**

- Computing $\mu$ and $\sigma$ again on the test data. Use the $\mu$ and $\sigma$ from the *training* data for every new example.
- Scaling the features during training but forgetting to scale the input at prediction time.
"""
D['01-supervised-learning/04-gradient-descent-in-practice.md'] = r"""
**Why plot the cost.** Gradient descent is only useful if the cost really goes down. Plotting $J$ against the iteration number is the quickest health check. If every iteration makes $J$ smaller, things are working.

**The stopping rule, step by step.** The source uses $\varepsilon = 10^{-3} = 0.001$. Suppose $J$ is $0.5000$ after one iteration and $0.4995$ after the next. The drop is $0.0005$, which is $\le 0.001$, so we declare convergence. A small $\varepsilon$ makes you wait longer for a slightly better answer; a large one stops early.

**Reading the two bad curves.**

- *Zig-zag:* each step jumps over the bottom of the valley to the other side, then back. The step is too big.
- *Always rising:* each step jumps so far that it lands higher than where it started. Again the step is too big, or the code has a sign error (for example $+\alpha$ instead of $-\alpha$).

**A quick debugging trick.** Run with a very small $\alpha$. If $J$ still does not decrease on every iteration, the problem is a bug, not the learning rate.

**How to search for $\alpha$.** Try $0.001$, then about three times larger each time: $0.003,\ 0.01,\ 0.03,\ 0.1,\dots$ Run a few iterations for each and look at the curve. Choose the largest value that still gives a smooth, steadily falling curve, because it reaches the bottom fastest.

**Common mistakes.**

- Judging convergence by the number of iterations alone. The number needed changes a lot between problems (30 for one, 100 000 for another).
- Changing the data scaling and the learning rate at the same time, so you cannot tell which helped.
"""
D['01-supervised-learning/05-feature-engineering-and-polynomial-regression.md'] = r"""
**Feature engineering in plain words.** The columns you are given are not always the best way to describe the problem. If a house has a *length* and a *breadth*, the price probably depends on the *area*, which is length $\times$ breadth. Giving the model the area directly makes its job easier, because it does not have to discover the product by itself. This is how your own knowledge of the problem improves the model.

**Why polynomial regression is still "linear".** The model $y = w_1x + w_2x^2 + w_3x^3 + b$ is a curve in $x$, but it is still a straight combination of the *features* $x$, $x^2$ and $x^3$. So the same linear-regression machinery (cost function and gradient descent) works. You just treat $x^2$ and $x^3$ as extra features.

**Choosing the shape.** If the data bends up and then flattens, $x$ and $\sqrt{x}$ together may fit better than $x$ and $x^2$. Different powers give different curves, and you can compare them with the cross-validation cost (see [Model selection](../03-model-evaluation-and-ml-practice/02-model-selection.md)).

**An important link to scaling.** If $x$ goes from 1 to 1000, then $x^2$ goes up to $10^6$ and $x^3$ up to $10^9$. These ranges are hugely different, so [feature scaling](03-feature-scaling.md) becomes very important for polynomial features.

**Common mistakes.**

- Adding very high powers "just in case". The curve then wiggles to hit every point, which is [overfitting](08-overfitting.md).
- Forgetting to scale the new features.
"""
D['01-supervised-learning/06-decision-boundary.md'] = r"""
**What the boundary means.** The model outputs a number $f(\vec x)=g(z)$ between 0 and 1, which we read as the chance that $y=1$. We predict class 1 when $f\ge 0.5$ and class 0 otherwise. Because the sigmoid gives exactly $0.5$ at $z=0$, the dividing line between the two predictions is the set of points where $z=0$.

**Worked example 1: the line** $z = x_1 + x_2 - 3$ (so $w_1=w_2=1,\ b=-3$). Treat the **x** points as class 1.

- Point $(1,1)$: $z = 1+1-3 = -1 < 0$, so it is on the **o** side (class 0).
- Point $(3,2)$: $z = 3+2-3 = 2 > 0$, so it is on the **x** side (class 1).
- Point $(2,1)$: $z=0$, exactly on the boundary.

**Worked example 2: the circle** $z = x_1^2 + x_2^2 - 1$.

- Point $(0.5, 0.5)$: $z = 0.25+0.25-1 = -0.5 <0$, so it is inside the circle (**o**).
- Point $(2, 0)$: $z = 4 - 1 = 3 > 0$, so it is outside the circle (**x**).

**Why squared features give a curve.** The boundary is still "$z=0$", but now $z$ is made from $x_1^2$ and $x_2^2$. A straight line in the *new* features becomes a curve in the original picture. This is the same trick as [polynomial regression](05-feature-engineering-and-polynomial-regression.md).

**Common mistake.** Thinking the boundary is where $f=1$. It is where $f=0.5$, the point of maximum uncertainty.
"""
D['01-supervised-learning/07-logistic-loss-and-cost.md'] = r"""
**What the output means.** For logistic regression, $f_{\vec w,b}(\vec x)$ is the model's belief, as a number between 0 and 1, that the label is 1. The loss should be small when that belief agrees with the real label and large when it does not.

**Worked examples (natural logarithm).**

| True $y$ | Prediction $f$ | Loss |
|---|---|---|
| 1 | 0.99 | $-\ln(0.99) \approx 0.01$ (very small) |
| 1 | 0.90 | $-\ln(0.90) \approx 0.105$ |
| 1 | 0.10 | $-\ln(0.10) \approx 2.30$ (large) |
| 0 | 0.10 | $-\ln(0.90) \approx 0.105$ |
| 0 | 0.99 | $-\ln(0.01) \approx 4.6$ (very large) |

Being confidently wrong is punished very heavily. Being unsure costs a little. That is exactly the behaviour we want.

**A tiny cost calculation.** Two examples: $(f=0.9,\ y=1)$ and $(f=0.2,\ y=0)$. The losses are $0.105$ and $-\ln(0.8)=0.223$. So $J = (0.105 + 0.223)/2 \approx 0.164$.

**Why not squared error.** With the sigmoid inside, squared error produces a bumpy surface with many flat regions and dips, so gradient descent can stall. The log loss gives a single bowl-shaped (convex) surface, so one global minimum is reachable.

**Common mistakes.**

- Using $\log(0)$. A prediction of exactly 0 or 1 that is wrong gives infinite loss, so numerical code keeps $f$ slightly away from 0 and 1.
- Using the linear-regression formula for $f$. Here $f$ is the sigmoid of $\vec w\cdot\vec x+b$.
"""
D['01-supervised-learning/08-overfitting.md'] = r"""
**An everyday comparison.** A student who memorises last year's exam answers does perfectly on those exact questions but fails new questions. That is overfitting: great on the training data, poor on new data. A student who does not study at all (underfitting) does badly everywhere.

**How to recognise each case.**

| Case | Training error | Error on new data | Common name |
|---|---|---|---|
| Underfit | high | high | high bias |
| Good fit | low | low | generalizes well |
| Overfit | very low | much higher | high variance |

**Why "bias" and "variance".** A high-bias model has a strong built-in assumption (for example "it is a straight line") that may be wrong. A high-variance model changes a lot if you change a few training points, because it follows the noise.

**The three remedies, explained.**

1. *More training data.* With more points, a wiggly curve cannot pass through all of them, so it is forced to be smoother.
2. *Fewer features.* Fewer features mean a simpler model with less freedom to chase noise. The cost is that you might throw away something useful.
3. *Regularization.* Keep all the features but stop the weights from becoming large. This is usually the gentlest option (see [Regularization](09-regularization.md)).

**Common mistake.** Judging a model only by its training error. Always check performance on data the model has not seen (see [Train / CV / Test](../03-model-evaluation-and-ml-practice/01-train-cv-test.md)).
"""
D['01-supervised-learning/09-regularization.md'] = r"""
**Why small weights give smooth curves.** To make a curve twist sharply you need big coefficients, especially on high powers like $x^3$ and $x^4$. If we punish large weights, the model can no longer afford sharp twists, so the curve relaxes.

**What $\lambda$ does.** The new cost is a balance between two goals: fit the data (first term) and keep the weights small (second term). $\lambda$ sets how much each goal matters.

| $\lambda$ | What happens |
|---|---|
| $0$ | No penalty, so it can overfit. |
| Moderate | Good balance. |
| Very large | All weights are pushed close to 0, so $f\approx b$, a flat line. This underfits. |

**Why only $w_j$ and not $b$.** The sums in the notes run over $j=1..n$ and do not include $b$. The bias only shifts the whole curve up or down and does not make it wiggle.

**What the extra term does inside gradient descent.** Write the update out:

$$ w_j = w_j - \alpha\left[\frac{1}{m}\sum\left(f-y\right)x_j + \frac{\lambda}{m}w_j\right] = w_j\left(1-\alpha\frac{\lambda}{m}\right) - \alpha\frac{1}{m}\sum\left(f-y\right)x_j $$

So each step first **shrinks** $w_j$ slightly by the factor $\left(1-\alpha\lambda/m\right)$, then applies the usual correction. With $\alpha=0.01,\ \lambda=1,\ m=50$ the factor is $1-0.0002 = 0.9998$, a tiny shrink at every step, which adds up over many iterations.

**The source's "1000" example.** Putting a large coefficient (1000) on $w_3^2$ and $w_4^2$ forces those two weights to be almost 0. $\lambda$ does the same for *all* weights when we do not know which ones to punish.

**Common mistakes.**

- Choosing $\lambda$ by looking at the training error. Choose it using the cross-validation set (see [Bias and variance](../03-model-evaluation-and-ml-practice/03-bias-and-variance.md)).
- Forgetting that scaled features are needed, or the penalty hits the large-range features unfairly.
"""

D['02-advanced-learning-algorithms/01-neural-networks.md'] = r"""
**The idea.** A single neuron is like one small logistic regression: it takes numbers in, forms a weighted sum, and squashes the result with an activation function. A layer is several neurons that all look at the same inputs. A network stacks layers so that the output of one layer becomes the input of the next.

**Why hidden layers help.** In the t-shirt example you could try to design features by hand (affordability, awareness, perceived quality). A neural network *learns* such helpful features by itself. Each hidden neuron decides how much to use each input, and training adjusts those choices. The names in the source sketch are only a way of explaining what a hidden neuron *might* represent.

**Reading the notation.** In $a_j^{[l]} = g\left(\vec w_j^{[l]}\cdot\vec a^{[l-1]} + b_j^{[l]}\right)$:

- $l$ is the layer number, in square brackets;
- $j$ is which neuron in that layer;
- $\vec a^{[l-1]}$ is the previous layer's output, with $\vec a^{[0]}=\vec x$ (the input);
- $g$ is the activation function.

**Counting parameters (4 inputs, 3 hidden, 1 output).** Layer 1 has $4\times 3 = 12$ weights and 3 biases. Layer 2 has $3\times 1=3$ weights and 1 bias. The total is $12+3+3+1 = 19$ parameters. Every neuron has its own weight vector and its own bias.

**Why image recognition works this way.** Early layers pick up simple things such as edges, middle layers combine them into parts, and later layers combine parts into whole objects.

**Common mistakes.**

- Mixing up the bracket $[l]$ (layer) with the round bracket $(i)$ (training example).
- Thinking the hidden neurons have fixed meanings. They are learned.
"""
D['02-advanced-learning-algorithms/02-layer-computation.md'] = r"""
**Following the numbers through.** Suppose the input $\vec x$ has $n$ numbers.

1. **Layer 1 (25 units).** Each unit has its own weight vector of length $n$ and its own bias. Each produces one number. Together the 25 numbers form $\vec a^{[1]}$.
2. **Layer 2 (15 units).** Each unit now looks at the 25 numbers in $\vec a^{[1]}$, so each has 25 weights. The 15 results form $\vec a^{[2]}$.
3. **Layer 3 (1 unit).** It looks at the 15 numbers in $\vec a^{[2]}$ and gives a single number $a^{[3]}$ between 0 and 1.

**Counting parameters.** Layer 1 has $25n + 25$, layer 2 has $25\times15 + 15 = 390$, and layer 3 has $15+1 = 16$. The total is $25n + 431$. For example, with $n=100$ inputs that is 2931 parameters.

**Turning the output into a decision.** The final number is read as a probability. A common rule is to predict 1 if $a^{[3]}\ge 0.5$ and 0 otherwise.

**Why the shapes must match.** The number of weights in each unit must equal the number of values coming in. If the shapes do not match, the dot product cannot be computed. When you get a shape error in code, check this first.

**Common mistake.** Forgetting that every layer has a *separate* bias per unit, not one bias for the whole layer.
"""
D['02-advanced-learning-algorithms/03-activation-functions.md'] = r"""
**Why we need activation functions at all.** If every neuron used the linear function $g(z)=z$, then stacking layers would still give just one linear function in the end, because a linear function of a linear function is linear. A deep network would be no more powerful than plain linear regression. Non-linear activations (sigmoid, ReLU, ...) are what let a network learn curved patterns.

**Choosing the output activation by the type of answer.**

| What you predict | Output activation |
|---|---|
| Yes / no (probability) | Sigmoid |
| A number that can be positive or negative | Linear |
| A number that can only be zero or positive | ReLU |

**Choosing the hidden activation.** The source says to use ReLU by default. One reason it is popular is that it is very cheap to compute. Another is that it is flat only on one side, so gradient descent usually learns faster than with the sigmoid, which is flat on both ends.

**A few values to remember.**

- Sigmoid: $g(0)=0.5$, $g(2)\approx 0.88$, $g(-2)\approx 0.12$.
- ReLU: $g(-3)=0$, $g(2.5)=2.5$.

**Common mistake.** Using a sigmoid on the output of a regression problem. A sigmoid can never go above 1, so it cannot predict a price of 300.
"""
D['02-advanced-learning-algorithms/04-multiclass-and-softmax.md'] = r"""
**The idea.** With $N$ classes the network computes one score $z_j$ per class. Softmax turns these scores into $N$ probabilities that are all positive and add up to 1. The larger the score, the larger the probability.

**Worked example (made-up scores).** Four classes with $z = [2,\ 1,\ 0,\ -1]$.

| | $e^{z}$ | Probability $a_j$ |
|---|---|---|
| Class 1 | 7.389 | 0.644 |
| Class 2 | 2.718 | 0.237 |
| Class 3 | 1.000 | 0.087 |
| Class 4 | 0.368 | 0.032 |

The sum of the $e^{z}$ values is $11.475$, and the probabilities add up to $1$ as the source's note says.

**The loss on this example.** If the true class is 1, the loss is $-\ln(0.644)\approx 0.44$ (small, good). If the true class is 4, the loss is $-\ln(0.032)\approx 3.44$ (large, bad). Only the probability given to the *true* class matters.

**Why "sparse".** The label is stored as a single integer ($y=3$) rather than as a long list like $[0,0,1,0]$. TensorFlow's name for this form of the loss is *sparse* categorical cross-entropy.

**Link to logistic regression.** With only two classes, softmax gives the same kind of answer as the sigmoid of logistic regression.

**Common mistake.** Using sigmoid at the output for more than two classes. The outputs would not add up to 1.
"""
D['02-advanced-learning-algorithms/05-vectorization-dense-layer.md'] = r"""
**What a Dense layer does.** Every unit in the layer takes all the inputs, multiplies by its own weights, adds its own bias and applies $g$. Putting the weights of all units side by side as the columns of a matrix $W$ lets us do all units at once.

**Following the example numbers.** Take $x = [200, 17]$, $W$ with columns $[1,-2]$, $[-3,4]$, $[5,-6]$ and $b=[-1,1,2]$. (`W.shape[1]` is 3, so there are 3 units.)

- Unit 1: $200(1) + 17(-2) - 1 = 165$
- Unit 2: $200(-3) + 17(4) + 1 = -531$
- Unit 3: $200(5) + 17(-6) + 2 = 900$

So $z = [165, -531, 900]$. If $g$ is the sigmoid, the outputs are about $[1,\ 0,\ 1]$.

**Why the matrix version is better.** The loop version handles one unit at a time. The `np.matmul` version computes all units in one operation, which is much faster and is what real libraries do.

**Shapes to keep in mind.** `A_in` has shape (examples, inputs), `W` has shape (inputs, units), so `Z` has shape (examples, units).

**Common mistakes.**

- Mixing up the order in `np.matmul(A_in, W)`. The inner dimensions must match.
- Forgetting that `g` must be defined; the page does not define it.
"""
D['02-advanced-learning-algorithms/06-tensorflow-and-training-steps.md'] = r"""
**The same three steps every time.** Whether you write logistic regression by hand or build a neural network, training has the same shape:

1. **Define the model.** Say how the output is computed from the input and the parameters.
2. **Define the loss and cost.** Say how wrong the output is.
3. **Train.** Adjust the parameters to make the cost small.

**What each TensorFlow line means.**

- `Sequential([...])` stacks the layers one after another, in order.
- `Dense(...)` is one layer, where every unit is connected to all inputs.
- `model.compile(loss=...)` chooses the cost to minimise. `BinaryCrossentropy` is TensorFlow's name for the logistic loss used for yes/no answers.
- `model.fit(X, y, epochs=100)` runs the training. An **epoch** is one full pass over the training data, so 100 epochs means 100 passes.

**What happens inside `fit`.** On each step it (a) runs the network forward to get predictions, (b) measures the loss, (c) uses [backpropagation](07-backpropagation-vs-gradient-descent.md) to get the gradients, and (d) takes a gradient-descent step. This is why the source says `fit` "implements back propagation".

**Why the table matches up.** Logistic regression and the neural network use the *same* loss. The difference is only that the network has several layers of parameters instead of one.

**Common mistake.** Choosing the loss that does not match the output. A yes/no output needs the binary loss; several classes need the sparse categorical loss.
"""
D['02-advanced-learning-algorithms/07-backpropagation-vs-gradient-descent.md'] = r"""
**Two different jobs.** People often treat these as the same thing, but they do different jobs:

- *Backpropagation* answers: "**in which direction** and by how much does the cost change if I nudge each parameter?"
- *Gradient descent* answers: "**given** those directions, what should the new parameters be?"

**An analogy.** You are standing on a hillside in fog and want to reach the valley. Backpropagation is feeling the slope under your feet in every direction. Gradient descent is taking a step downhill. You repeat both many times.

**Why the chain rule appears.** In a network the cost depends on the output, which depends on the last layer's $z$, which depends on the weights. To find how the cost depends on an early weight, you multiply the small effects along that chain:

$$ \frac{\partial J}{\partial w} = \frac{\partial J}{\partial a}\cdot\frac{\partial a}{\partial z}\cdot\frac{\partial z}{\partial w} $$

**Why "backward".** The network first runs **forward** to get the output and the loss. Then it works **backwards** from the loss, reusing the pieces already computed for later layers. This reuse makes it far cheaper than working out each derivative separately.

**What you actually need to do.** Libraries such as TensorFlow do backpropagation for you inside `fit`. Knowing what it does helps you understand why training works and where it can go wrong.

**Common mistake.** Saying "backpropagation updates the weights". It only *computes* the gradients; the optimiser (gradient descent or Adam) does the update.
"""
D['02-advanced-learning-algorithms/08-adam-and-layer-types.md'] = r"""
**What Adam fixes.** With plain gradient descent you must choose one $\alpha$ for every parameter and keep it fixed. If it is too small, training is slow. If it is too large, training bounces around. Adam adjusts the step size automatically: if a parameter keeps moving in the same direction, its steps get bigger; if it keeps jumping back and forth, they get smaller. You still give it a starting $\alpha$, but it is less sensitive to the choice.

**Why convolutional layers.** A Dense layer connects every neuron to every input. For an ECG with 100 values, that means 100 weights per neuron. A convolutional neuron looks at only a small window (20 values in the source), so it has fewer weights.

**Counting the windows.** The source's windows are $x_1$–$x_{20}$, $x_{11}$–$x_{30}$, $x_{21}$–$x_{40}$: each window starts 10 values after the last one. With 100 inputs, windows of 20 and a shift of 10 there would be $(100-20)/10+1 = 9$ windows.

**Benefits.**

- Fewer parameters, so training is faster and the model overfits less.
- Each neuron focuses on a local part of the signal, such as one heartbeat shape.
- Different neurons can look at different parts of the signal.

**Common mistake.** Thinking Adam replaces gradient descent. It is a smarter version of it and still needs the gradients from backpropagation.
"""