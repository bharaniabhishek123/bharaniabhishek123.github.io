---
layout: post
title: Hinge Loss Gradient Computation
---

Let's implement the hinge loss and and it's gradient as a part of assignment for CS221.  

## Loss Function
Let's define our Loss function by:

$$Loss_{hinge}(x,y,w) = \ max(0, 1- w . \phi(x) y $$

Where: 
+ $w$ is our weight vector. So for example $w_j^{\intercal} = [w_{j1},\  w_{j2},\  \ldots, w_{jD}]$
+ $X \in \mathbb{R}^{N \times D} $ where each $x_{i}$ are a single example we want to classify. $x_{i} = [x_{i1},\  x_{i2},\  \ldots,\  x_{iD}]$
+ $y$ is the correct class of $x_i$

+ also, notice that $\ w. \phi(x)$ is a scalar

## Analytic gradient
We want to compute $\nabla_{w}Loss_{hinge}(x,y,w)$

$$\nabla_{w}Loss_{hinge}(x,y,w) = (-\phi(x) \ y \if \ w.\phi(x) \y \lt 1 \\
                 \0 \   otherwise)
$$

## Vectorized implementation
Now that we understand how the gradient of the hinge loss function is computed. We will implement it using Python. As the unvectorized implementation is quite straightforward, I will only derive the vectorized implementation. The full Python code can be found below 
```python
wordidx = {"pretty":0, "good":1, "bad":2, "plot":3, "not":4, "scenery":5}
X = ["pretty bad","good plot" ,"not good","pretty scenery"]
y = [-1,1,-1,1]


import numpy as np 
def onehotEncoding(review,wordidx):
    """
    Input the review to get the one hot coded vector
    """
    res = np.zeros((1,6))

    for word in review.split():
        
        idx = wordidx[word]
        res[:,idx] +=1
    return np.array(res)
    
    
def hingeloss(x,y,W):
    
    return max(0,1- y* np.dot(W.T,x))

def dhingeloss(x,y,W):
# One important thing to note here is 
# y*np.dot(x, W.T) == y * np.dot(W.T,x)
# I first tried y * np.dot(W.T,x) and it gave error as
# The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

# first wrong dot product    
#    if (y * np.dot(W.T,x)) < 1:
#        return x*y
#    else:
#        return np.array(0)

    
     if (y*np.dot(x, W.T)) < 1:
#     if (y * x.dot(W.T)) < 1:
         return  (x * y )
     else:
         return 0

W = np.zeros((1,6))
print("w before stocastic", W)
eta = 0.5
for i,x in enumerate(X):
    X_train = onehotEncoding(x,wordidx)
    y_train = y[i]
    W = W+ eta* dhingeloss(X_train,y_train,W)



print("w after stocastic", W)

#[ 0. ,  0. , -0.5,  0.5, -0.5,  0.5]

```  
Alternatively,
```
python
import numpy as np


X = np.array([
    [1,0,1,0,0,0],
    [0,1,0,1,0,0],
    [0,1,0,0,1,0],
    [1,0,0,0,0,1],
])

y = np.array([-1,1,-1,1])

def svm_sgd(X, Y):

    w = np.zeros(len(X[0]))
    eta = 0.5

    for i, x in enumerate(X):
        if (Y[i]*np.dot(X[i], w)) < 1:
            w = w + eta * ( (X[i] * Y[i]) )
    return w

w = svm_sgd(X,y)
print(w)

```