---
layout: post
title: Genearlization, Unsupervised learning and K-mean (Lecture 3)
---

What is the true objective of Machine Learning ?  
1. minimize error on training set   
2. minimize training error with regularization  
3. minimize error on unseen future examples  
4. lean about machines  

In machine learning our goal is to minimize error on unseen future examples.  

Test set contains examples not used for training and represent these unseen future examples.  

## Approximation and estimation error
$$f^*$$ perfect predictor  
$$g$$ best predictor in the class  
$$f^{\^}$$ f hat  is predictor from our training data  

Approximation error is : "How good is the hypothesis class ?"  
Estimation error is : "How good is the learned predictor relative to the hypothesis class ?"  
$$Err(f^{\^}) -Err(f^*)$$

$$Err(f^{\^}) - Err(g) + Err(g) -Err(f^*)$$  
$$estimation error + approximation error$$  

## Effect of hypthesis class size  
As hypothesis class increases and we are getting closer to correct classifier.  
Approximation error decreases but estimation error increases as complexity increases.  

Analogy : Wallet on the road and return to original owner. 
When only a few people around you can around and ask.  
or  
We need to ask all the people at stanford via email. Each question asked to each person is an example and increase the size of hypothesis.  The harder it becomes to figure out the correct hypthesis.  

##Hyphothesis size  
If it goes down, then estimation error goes down but approx. error goes up.  
One thing we can do is to reduce the dimensionality. If we have 3 features then weight vector are in 3-D. Try removing features  .
Second we can control the norm of the ||w|| and keep it small.  It controls how many hypothesis we are considering. Use regularization by adding $\frac{\lambda w^2}{2} $ to the loss, if lambda is large then value of regularization will be more.Use early stopping to contron the norm.  

Idea is to minimize the training error by keeping hypothesis class small.  


##Hyperparameters   
Properties of learning algorithm, such as regularization parameter $\lambda$, number of iterations T, step size $\eta$.  
How do we choose hyperparameters ?  
Choose hyperparameters to minimize Training error ?  
No, then the effect of regularization will be zero. we may end up choosing $\lamda$=0$ and overfit.  
Choose hyperparameters to minimize Test error ?  
No, Choosing parameters based on test set make the estimates unreliable. Test set purpose is to make prediction better on unseen examples so we should not tune hyperparameters for it.  

We need to randomly take 10-15% of the training set and use it to estimate test error.This is called as hold out validation set and act as surrogate for test set.  


#Unsupervised Learning  
Expensive to get labeled data. Unlabeled data is easy to obtain.  

##Clustering  
given set of input points, output assignment of each point to a cluster.  
$$D_{train} = {x_1,x_2,....x_n}$$
$$[z_1,....z_n]$$

we want to output similar points in same cluster and dissimilar points in different clusters.  
Objective function that defines clustering.  
for each cluster k = 1,2....K , represented by a centroid $\mu_k E R^d $  
want each point $\phi(x)$ close to its assigned centroid $\mu_{z_{i}}$
objective function:  
$$Loss_{kmeans}(z,\mu) = \sum_{i=1}^k ||\phi(x_i) - \mu_{z_{i}}||^2$$  
Guranteed to converge to a local minimum but not to a global minimum.  

