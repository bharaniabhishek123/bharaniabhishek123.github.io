---
layout: post
title: Hinge Loss Gradient Computation
---

When I started attending *CS231n* class from Stanford as a self-taught person, I was a little annoyed that
they were no more explanations on how one is supposed to compute the gradient of the hinge loss. Actually,
in the [lecture](http://cs231n.github.io/optimization-1/ "Optimization") we can see the formula of the gradient of the SVM loss. Although the formula seems understandable, I still thinks we might need to get our hands dirty by doing the math.

## Loss Function
In this part, I will quickly define the problem according to the data of the first assignment of CS231n.
Let's define our Loss function by:

$$L_i = \sum\limits_{j \neq y_i}[\ max(0, x_iw_j - x_iw_{y_i} + \Delta)\ ]$$

Where: 
+ $w_j$ are the column vectors. So for example $w_j^{\intercal} = [w_{j1},\  w_{j2},\  \ldots, w_{jD}]$
+ $X \in \mathbb{R}^{N \times D} $ where each $x_{i}$ are a single example we want to classify. $x_{i} = [x_{i1},\  x_{i2},\  \ldots,\  x_{iD}]$
+ hence $i$ iterates over all N examples
+ $j$ iterates over all C classes.
+ $y_i$ is the index of the correct class of $x_i$
+ $\Delta$ is the margin paramater. In the assignment $\Delta = 1$
+ also, notice that $x_iw_j$ is a scalar

## Analytic gradient
We want to compute $\forall i,j \in [1, N]\times[1, C]$ $\nabla_{w_{j}}L_i$. We know
$w_{j} \in \mathbb{R}^{D \times 1}$, so we can write:

$$\nabla_{w_{j}}Li = 
\begin{bmatrix}
	\frac{dLi}{dw_{j1}} \\[10pt]
	\frac{dLi}{dw_{j2}} \\[10pt]
	\vdots \\
	\frac{dLi}{dw_{jD}}
\end{bmatrix}
$$

Therefore, let's compute the derivative of $\frac{dLi}{dw_{kj}}$ with $k \in [1,\ C]$. To compute this derivative I will write $L_i$ without summation ($\sum$) symbol so that will make things easier to visualize:

<div class="color-box text-80">
$$
	L_i = \max(0, x_{i1}w_{11} + x_{i2}w_{12} +\ \ldots \ + x_{ij}w_{1j} +\ \ldots \ + x_{iD}w_{1D} -  x_{i1}w_{y_{i}1} - x_{i2}w_{y_{i}2} +\ \ldots \ - x_{y_{i}D}w_{1D}) + \\[10pt]
	\max(0, x_{i1}w_{21} + x_{i2}w_{22} +\ \ldots \ + x_{ij}w_{2j} +\ \ldots \ + x_{iD}w_{2D} -  x_{i1}w_{y_{i}1} - x_{i2}w_{y_{i}2} +\ \ldots \ - x_{y_{i}D}w_{1D}) + \\[10pt]
	\vdots \\
	\max(0, x_{i1}w_{k1} + x_{i2}w_{k2} +\ \ldots \ + x_{ij}w_{kj} +\ \ldots \ + x_{iD}w_{CD} -  x_{i1}w_{y_{i}1} - x_{i2}w_{y_{i}2} +\ \ldots \ - x_{y_{i}D}w_{1D}) + \\
	\vdots \\
	\max(0, x_{i1}w_{C1} + x_{i2}w_{C2} +\ \ldots \ + x_{ij}w_{Cj} +\ \ldots \ + x_{iD}w_{CD} -  x_{i1}w_{y_{i}1} - x_{i2}w_{y_{i}2} +\ \ldots \ - x_{y_{i}D}w_{1D}) + \\[10pt]
$$
</div>
Now, we can clearly see that:

$$ \forall k \in [1,\ C]\backslash\{y_i\},\ \forall j \in [1,\ D] \ \frac{dLi}{dw_{kj}} =  1(x_iw_k - x_iw_{y_i} + \Delta > 0)x_{ij}$$

Using the definition of $\nabla_{w_{j}}Li$, we now have:

$$
\nabla_{w_{j}}Li = 
\begin{bmatrix}
	\frac{dLi}{dw_{j1}} \\[10pt]
	\frac{dLi}{dw_{j2}} \\[10pt]
	\vdots \\
	\frac{dLi}{dw_{jD}}
\end{bmatrix}
=
\begin{bmatrix}
	1(x_iw_j - x_iw_{y_i} + \Delta > 0)x_{i1} \\[10pt]
	1(x_iw_j - x_iw_{y_i} + \Delta > 0)x_{i2} \\[10pt]
	\vdots \\
	1(x_iw_j - x_iw_{y_i} + \Delta > 0)x_{iD}
\end{bmatrix}
=
1(x_iw_j - x_iw_{y_i} + \Delta > 0)\begin{bmatrix}
	x_{i1} \\[10pt]
	x_{i2} \\[10pt]
	\vdots \\
	x_{iD}
\end{bmatrix}
$$

Now, what happen when $y_i = k$? Using the form of $L_i$ in the box, we see that $w_{y_{i}j}$ intervenes in all lines. Hence we have:

$$y_i = k, \ \forall j \in [1,\ D] \ \frac{dLi}{dw_{y_{i}j}} =  -\sum\limits_{k \neq y_{i}}1(x_iw_k - x_iw_{y_i} + \Delta > 0)x_{ij}$$

and finally we can write:

$$
\nabla_{w_{y_i}}Li = 
\begin{bmatrix}
	\frac{dLi}{dw_{y_{i}1}} \\[10pt]
	\frac{dLi}{dw_{y_{i}2}} \\[10pt]
	\vdots \\
	\frac{dLi}{dw_{y_{i}D}}
\end{bmatrix}
=
\begin{bmatrix}
	-\sum\limits_{k \neq y_{i}}1(x_iw_k - x_iw_{y_i} + \Delta > 0)x_{i1} \\[10pt]
	-\sum\limits_{k \neq y_{i}}1(x_iw_k - x_iw_{y_i} + \Delta > 0)x_{i2} \\[10pt]
	\vdots \\
	-\sum\limits_{k \neq y_{i}}1(x_iw_k - x_iw_{y_i} + \Delta > 0)x_{iD}
\end{bmatrix} \\
=-\sum\limits_{k \neq y_{i}}1(x_iw_k - x_iw_{y_i} + \Delta > 0)\begin{bmatrix}
	x_{i1} \\[10pt]
	x_{i2} \\[10pt]
	\vdots \\
	x_{iD}
\end{bmatrix}
$$

## Vectorized implementation
Now that we understand how the gradient of the hinge loss function is computed. We will implement it using Python. As the unvectorized implementation is quite straightforward, I will only derive the vectorized implementation. The full Python code can be found in the [*linear_svm.py*](https://github.com/Twice22/CS231n-solutions/blob/fba2891caf54f8553f6c14ffe3d15b144ddeb93b/assignment1/cs231n/classifiers/linear_svm.py) file.

### Forward pass
Firstly we will focus on the implementation of the forward pass. In other words, we will derive a formula to compute the loss using a vectorized implementation. For a better understanding, I created a picture:

<div class="centered-img">
<img src="../images/svm/vector_svm.png" alt="Hinge loss - vectorized implementation" />
<div class="legend">Figure 1: Hinge loss - Forward pass vectorized implementation</div>
</div>

According to Figure 1, we can compute the margin as follow:

$$\text{margin} = \max\{0, XW - XW[[1...N], y] \}$$

Then we need to set the margin in the $y_i$ position to $0$ before summing out
(because the sum is over $j \setminus${$y_i$}):

$$\text{margin}[[1...N], y] = 0$$

Finally we just have to sum and add the regularization term. In python we can write:
```python
  scores = X.dot(W)
  correct_class_score = scores[np.arange(num_train), y]

  # add an axis with np.newaxis so we can perform the substraction.
  # For further information you can visit:
  # https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html
  margins = np.maximum(0, scores - correct_class_score[:, np.newaxis] + 1)
  margins[np.arange(num_train), y] = 0
  loss = np.sum(margins)
```

### Backward pass
Now that we understand how one can implement the forward pass, we will deal with a slightly more difficult challenge: How to compute the backward pass, that is to say, how to compute $\nabla_w L$ with a vectorized implementation? Firstly, we will rewrite our $\Delta_{w_{j}}L_i$ to have a better understanding of what the matrix should look like:

$$
\nabla_{w_{j}}L_i = 
\begin{bmatrix}
	\frac{dL_i}{dw_{1}} & \frac{dL_i}{dw_{2}} & \ldots & \frac{dL_i}{dw_{C}} \\
\end{bmatrix}
=
\begin{bmatrix}
	\frac{dL_i}{dw_{11}} & \frac{dL_i}{dw_{21}} & \ldots & \frac{dL_i}{dw_{y_{i}1}} & \ldots & \frac{dL_i}{dw_{C1}} \\[10pt]
	\frac{dL_i}{dw_{12}} & \frac{dL_i}{dw_{22}} & \ldots & \frac{dL_i}{dw_{y_{i}2}} & \ldots & \frac{dL_i}{dw_{C2}} \\[10pt]
	\vdots & \ddots & \ddots  & \ddots & \ddots & \vdots \\[10pt]
	\frac{dL_i}{dw_{1j}} & \frac{dL_i}{dw_{2j}} & \ldots & \frac{dL_i}{dw_{y_{i}j}} & \ldots & \frac{dL_i}{dw_{Cj}} \\[10pt]
	\vdots & \ddots & \ddots  & \ddots & \ddots & \vdots \\[10pt]
	\frac{dL_i}{dw_{1D}} & \frac{dL_i}{dw_{2D}} & \ldots & \frac{dL_i}{dw_{y_{i}D}} & \ldots & \frac{dL_i}{dw_{CD}} \\
\end{bmatrix} \\
$$

<div class="text-80">
$$
=
\begin{bmatrix}
	1(x_iw_1 - x_iw_{y_i} + \Delta > 0)x_{i1} & \ldots & -\sum\limits_{j \neq y_{i}}1(x_iw_j - x_iw_{y_i} + \Delta > 0)x_{i1} & \ldots & 1(x_iw_C - x_iw_{y_i} + \Delta > 0)x_{i1} \\[10pt]
	1(x_iw_1 - x_iw_{y_i} + \Delta > 0)x_{i2} & \ldots & -\sum\limits_{j \neq y_{i}}1(x_iw_j - x_iw_{y_i} + \Delta > 0)x_{i2} & \ldots & 1(x_iw_C - x_iw_{y_i} + \Delta > 0)x_{i2} \\[10pt]
	\vdots & \ddots & \ddots  & \ddots & \vdots \\[10pt]
	1(x_iw_1 - x_iw_{y_i} + \Delta > 0)x_{ij} & \ldots & -\sum\limits_{j \neq y_{i}}1(x_iw_j - x_iw_{y_i} + \Delta > 0)x_{ij} & \ldots & 1(x_iw_C - x_iw_{y_i} + \Delta > 0)x_{ij} \\[10pt]
	\vdots & \ddots & \ddots  & \ddots & \vdots \\[10pt]
	1(x_iw_1 - x_iw_{y_i} + \Delta > 0)x_{iD} & \ldots & -\sum\limits_{j \neq y_{i}}1(x_iw_j - x_iw_{y_i} + \Delta > 0)x_{iD} & \ldots & 1(x_iw_C - x_iw_{y_i} + \Delta > 0)x_{iD} \\
\end{bmatrix}
$$
</div>

Now that we see the shape of the matrix is is easy to write **the unvectorized naive** implementation. We just need to:

+ build a matrix of zeros having size (D,C) (same size as W)
+ assign $x_i$ to each column of this matrix if ($j \neq y_i$ and $(x_iw_j - x_iw_{y_i} + \Delta > 0)$)
+ assign $-\sum\limits_{j \neq y_{i}}1(x_iw_j - x_iw_{y_i} + \Delta > 0)x_i$ to the $y_i$ column

```python
  dW = np.zeros(W.shape) # initialize the gradient as zero

  # compute the loss and the gradient
  num_classes = W.shape[1]
  num_train = X.shape[0]
  loss = 0.0
  for i in xrange(num_train):
    scores = X[i].dot(W)
    correct_class_score = scores[y[i]]
    nb_sup_zero = 0
    for j in xrange(num_classes):
      if j == y[i]:
        continue
      margin = scores[j] - correct_class_score + 1 # note delta = 1
      if margin > 0:
        nb_sup_zero += 1
        loss += margin
        dW[:, j] += X[i]
    dW[:, y[i]] -= nb_sup_zero*X[i]
```

The vectorized implementation is slightly harder to compute but fortunately we've already done all the work. Actually during the forward pass we computed a matrix with the following elements (besides $j = y_i$ where it is 0):

$$(x_iw_j - x_iw_{y_i} + \Delta > 0)$$

So this matrix (let's call it the **margin matrix**) looks like what we want except that:

+ We want to build a matrix that has the same size as the margin matrix and that has 1 when the quantity of each cell of the margin matrix is positive and a zero otherwise
+ We want to build a matrix that has on each cell of its $j = y_i$ column the negative sum of the indicator function of all the columns (except column $y_i$) of margin matrix
+ We need to multiply this newly created matrix by X (because we see $x_{ij}$ is present in each cell of $\nabla_{w_{j}}L_i$)

So now, it is relatively straightforward:

+ We create a matrix having the dimension of the margin matrix. Let's call it **mask**. We then need to have $1$ on each cell of the **mask** matrix when the quantity on the corresponding cell of the **margin matrix** is positive. In python we can do this using:

```python
mask = np.zeros(margins.shape)
mask[margin > 0] = 1
```

+ Now, we need to change the content of each cell of the **mask matrix** when we are on the $y_i$th column. We need to put in each row of this $y_i$th column the negative value of the sum of all the values in the other rows. In python we can do that by creating a vector containing the sum of the column:

```python
np_sup_zero = np.sum(mask, axis=1)
```

then we need to replace the $y_i$th column vector of the **mask matrix** by this newly created vector by doing:

```python
mask[np.arange(num_train), y] = -np_sup_zero
```

+ finally we need to multiply by X so the final matrix has the same dimension as the W matrix: (D,C). We know mask's dimension is (N,C) and X's dimension is (N, D) so we need to return $X^{\intercal}W$:

```python
dW = X.T.dot(mask)
```

At the end, we need to divide by the number of training samples and to add the regularization term:
```python
dW /= num_train
dW += reg*W
```

## Conclusion
Finally we saw how one can compute the gradient of the hinge loss function. This wasn't difficult. The main issue we can encounter when we are asking to compute such gradient resides in the formulation of the problem. What do we need to compute? The gradient w.r.t which variables? What are the size of the variables involve? It is important to define the problem precisely, the rest will follow naturally if you already know what it means to compute a gradient. Finally we see that it can be useful to write down the matrix expression.
<br><br>