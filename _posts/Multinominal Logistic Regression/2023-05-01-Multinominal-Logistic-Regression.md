---
tag: Logistic Regression
title: Multinominal Logistic Regression
---

Multinomial logistic regression is a statistical method used for predicting categorical outcomes with more than two categories. It is particularly useful when the dependent variable is categorical rather than continuous.


## **Categorical Predictions**
In **multinomial logistic regression**, the model predicts the probabilities of an observation belonging to each category of the dependent variable. These probabilities can be interpreted as the likelihood of the observation falling into each category. The predicted category is typically the one with the highest probability, making it a *categorical* prediction rather than a *continuous* one.

In contrast, standard logistic regression, also known as **binary logistic regression**---a special case of [Binomial Logistic Regression](https://s-lasch.github.io/2023/03/16/Binomial-Logistic-Regression.html)---is used when the dependent variable has two categories only. It predicts the probability of an observation belonging to one category versus another. The predictions in binary logistic regression are continuous probabilities between `0` and `1`.

## **Under the Hood**
Below is the mathematics behind multinomial logistic regression. These equations represent a set of log-linear models, where the logarithm of the ratio of the probabilities of each class is linearly related to a predictor variable $X_i$ through a coefficient (or slope) parameter, denoted by $\beta_1$, $\beta_2$, ..., $\beta_{K-1}$. The notation $\text{P}(Y_i = K)$ represents the probability of observation $i$ belonging to class $K$, where $K$ is an integer representation of each class, starting at 1.

<p align="center">
      <img src='https://raw.githubusercontent.com/s-lasch/s-lasch.github.io/main/_posts/Multinominal%20Logistic%20Regression/image_2023-05-17_214302887.png' 
           alt='Natural log probabilities.'
           width='40%' />
<p align="center"><em>Image by Author</em></p>
</p>

From these equations, we can simplify to the ones below, which are alternate forms of the equations we saw earlier. They are derived from the fact that the probabilities of all $K$ classes must sum to 1. In these equations, $\text{P}(Y_i = K)$ is used as a reference category, and the probabilities of the other $K-1$ categories are expressed relative to this reference category using exponential functions of the predictor variable $X_i$ and the corresponding coefficient $\beta_K$.

The exponential function $e$ in these equations is used to transform the linear predictor (i.e., $\beta_K \cdot X_i$) into a probability, which is always positive and bounded between 0 and 1. By applying the exponential function $e$ to both sides of the previous equations, we get the following for the first class:

<p align="center">
      <img src='https://raw.githubusercontent.com/s-lasch/s-lasch.github.io/main/_posts/Multinominal%20Logistic%20Regression/image_2023-05-16_230159351.png' 
           alt='Probability equations after exponentiation.' />
<p align="center"><em>Image by Author</em></p>
</p>

These equations are often used in the context of multinomial logistic regression, where the goal is to predict the probability of an observation belonging to each of $K$ classes based on one or more predictor variables.

## **About the Data**
In this example, we will be using University of California, Irvine's [abalone dataset](https://archive.ics.uci.edu/ml/datasets/abalone) to predict the gender of an abalone. A multivariate linear regression model can be used to predict the age, though for this example, we are predicting the gender of a given abalone based on several distinct features.

Using the Python `pandas` package, we can see the shape of the data, as well as the first few rows.

``` python
df = pd.read_csv("https://raw.githubusercontent.com/s-lasch/CIS-280/main/abalone.csv")
df.shape
```

``` python
df.head()

| sex | length | diameter | height | whole_weight | shucked_weight | viscera_weight | shell_weight | rings |
------------------------------------------------------------------------------------------------------------
| M	| 0.455  | 0.365    | 0.095  | 0.5140       | 0.2245         | 0.1010         | 0.150        | 15   |
| M	| 0.350  | 0.265    | 0.090  | 0.2255       | 0.0995         | 0.0485         | 0.070        | 7    |
| F	| 0.530  | 0.420    | 0.135  | 0.6770       | 0.2565         | 0.1415         | 0.210        | 9    |
| M	| 0.440  | 0.365    | 0.125  | 0.5160       | 0.2155         | 0.1140         | 0.155        | 10   |
| I	| 0.330  | 0.255    | 0.080  | 0.2050       | 0.0895         | 0.0395         | 0.055        | 7    |
```

## **Processing the Data**


## **The Model**

## **Training the Model**

## **Validation**
