---
tag: K-Nearest Neighbors
title: Confusion Matrices
---

## **Background**

Obviously, our goal is to model our data as accurately as possible. This is where **confusion matrices** come into play. They will make calcuating the precision, recall, accuracy, and other metrics possible, and it is not difficult to fully understand.


### **Confusion Matrices**
A **confusion matrix** is the primary way to evaluate the results of a classification model. If the previous explanations did not suffice, refer to my previous articles on [Binomial](https://s-lasch.github.io/2023/03/16/Binomial-Logistic-Regression.html) and [Multinomial](https://s-lasch.github.io/2023/05/01/Multinominal-Logistic-Regression.html) logistic regression models for more information about classification models. 

In both binary and multi-class confusion matrices, the diagonal values represent true positives and true negatives, while the non-diagonal values represent false positives or false negatives depending on their positions. The rows represent the predicted values, and the columns represent the truth values, which are the original values.


### **Truth Value Reference**

To make things more clear in the sections to come, below are the different truth values along with their meanings:
* **True Positive (TP):** The model correctly predicts a true value.
* **True Negative (TN):** The model correctly predicts a false value.
* **False Positive (FP):** The model incorrectly predicts a true value when it should have been false.
* **False Negative (FN):** The model incorrectly predicts a false value when it should have been positive true.


### **Binary Confusion**

In a binary confusion matrix, we are only dealing with two classes. By comparing the values across different confusion matrices, you can assess if there is a reduction in misclassifications. This works for all classification models, including logistic regression, or kNN models. 

<p align="center">
      <img src="https://raw.githubusercontent.com/s-lasch/s-lasch.github.io/main/images/binary_confusion_matrix.png" 
           alt="Binary Confusion Matrix"/>
<p align="center"><em>Image by Author</em></p>
</p>


### **Multi-class Confusion**

Multi-class confusion matrices get increasingly complex with the more classes we add. In our example, we will be using four classes, and a kNN algorithm for classification. Fig. 4 represents this type of confusion matrix. 

Typically, the first step in interpreting a confusion matrix should start with identifying positive and negative classes. For our case, we are attempting to classify unseen data as belonging to one of four classes: `BERGF`, `BERGM`, `NORSEM`, and `NORSEF`. Since it would make no sense to favor one population over another, we will need to calculate accuracy, precision, recall, etc. for each class.

<p align="center">
      <img src="https://raw.githubusercontent.com/s-lasch/s-lasch.github.io/main/images/multiclass_confusion_matrix.png" 
           alt="Multi-class Confusion Matrix"/>
<p align="center"><em>Image by Author</em></p>
</p>

This classification table, (we'll call it $M$), provides a decent amount of information: 
* Judging by the diagonal values, the model correctly predicted 130 correct samples out of the 219 total. This means that the **overall accuracy is 59.3%**, a terrible score.
* The model confused NORSE females with BERG females and NORSE males. This is evident with the values $\text{M}_{3,1} = 10$ (row 3 column 1) and $\text{M}_{3,4} = 12$. 
* To determine the extent to which the model should be optimized, we need to use these values to calculate some metrics.

---

## **Evaluation Metrics**

### **Precision**

Precision measures how precise or accurate the positive predictions of a classifier are. It is the ratio of true positives to the sum of true positives and false positives. Precision indicates how many of the instances *predicted* as positive are *actually positive.*
$$\text{precision} = \frac{TP}{TP+FP}$$  

Let's calculate precision for the `BERGF` class. We need the true positives, $\text{M}_{1,1}$, and the false positives, $\text{M}_{1,2} + \text{M}_{1,3} + \text{M}_{1,4}$
$$\text{BERGF precision} = \frac{30}{30 + (10 + 7 + 1)} = 0.625$$

As a rule of thumb, you should optimize your model for precision when you want to decrease the number of false positives.


### **Recall**

Recall, also known as sensitivity or true positive rate, measures the ability of the classifier to correctly identify positive instances. It is the ratio of true positives to the sum of true positives and false negatives. Recall indicates the proportion of actual positive instances that are correctly predicted. $$\text{recall} = \frac{TP}{TP + FN}$$

Let's calculate recall for the `BERGM` class. $$\text{BERGM recall} = \frac{33}{33 + (10 + 5 + 8)} = 0.5893$$

You should optimize your model for recall if you want to decrease the number of false negatives.


### **Accuracy**

Accuracy measures of how often the classifier correctly predicts the class of an instance. It is the ratio of the correctly classified instances to the total number of instances in the dataset. Higher accuracy indicates a better overall performance of the classifier. In the Multi-class Confusion section, we calculated the model's overall accuracy by adding all the correct predictions and dividing it by the number of total samples. 