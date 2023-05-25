---
tag: K-Nearest Neighbors
title: Confusion Matrices
---

Obviously, our goal is to model our data as accurately as possible. For classification problems such as logistic regression and kNN, this is where **confusion matrices** are useful. They will make calcuating the precision, recall, accuracy, and other metrics possible, and it is not difficult to fully understand how they work.


### **Confusion Matrices**
A **confusion matrix** is the primary way to evaluate the results of a classification model. If the previous explanations did not suffice, refer to my previous articles on [Binomial](https://s-lasch.github.io/2023/03/16/Binomial-Logistic-Regression.html) and [Multinomial](https://s-lasch.github.io/2023/05/01/Multinominal-Logistic-Regression.html) logistic regression models for more information about classification models. 

In both binary and multi-class confusion matrices, the diagonal values represent true positives and true negatives, while the non-diagonal values represent false positives or false negatives depending on their positions. The rows represent the predicted values, and the columns represent the truth values, which are the original values.


### **Truth Value Reference**

To make things more clear in the sections to come, below are the different truth values along with their meanings:
* **True Positive (TP):** The model correctly predicts a true value.
* **True Negative (TN):** The model correctly predicts a false value.
* **False Positive (FP):** The model incorrectly predicts a true value when it should have been false.
* **False Negative (FN):** The model incorrectly predicts a false value when it should have been true.


### **Binary Confusion**

In a binary confusion matrix, we are only dealing with two classes. By comparing the values across different confusion matrices, you can assess if there is a reduction in misclassifications. This works for all classification models, including logistic regression, or kNN models. Fig. 1 below demonstrates what a binary confusion matrix looks like, as well as how to interpret the values inside.

<p align="center">
      <img src="https://raw.githubusercontent.com/s-lasch/s-lasch.github.io/main/images/binary__confusion_matrix.png" 
           alt="Binary Confusion Matrix"/>
<p align="center"><em>Fig 1. Binary confusion matrix (image by author)</em></p>
</p>

Fig. 2 uses the results of a pregnancy test to further drive home a binary confusion table, as well as understanding the truth values TP, TN, FP, and FN. 

<p align="center">
      <img src="https://raw.githubusercontent.com/s-lasch/s-lasch.github.io/main/images/truth_table_example.png" 
           alt="Pregnancy confusion matrix example."/>
<p align="center"><em>Fig 2. Example of binary confusion matrix with pregnancy results (image by author)</em></p>
</p>


### **Multi-class Confusion**

Multi-class confusion matrices get increasingly complex with the more classes we add. In our example, we will be using four classes, and a kNN algorithm for classification. Fig. 3 represents this type of confusion matrix. 

Typically, the first step in interpreting a confusion matrix should start with identifying positive and negative classes. For our case, we are attempting to classify unseen data as belonging to one of four classes: `BERGF`, `BERGM`, `NORSEM`, and `NORSEF`. Since it would make no sense to favor one population over another, we will need to calculate accuracy, precision, recall, etc. for each class.

<p align="center">
      <img src="https://raw.githubusercontent.com/s-lasch/s-lasch.github.io/main/images/multi_class_confusion_matrix.png" alt="Multi-class Confusion Matrix" 
           width="40%"/>
<p align="center"><em>Fig 3. Multi-class confusion matrix (image by author)</em></p>
</p>

This classification table, (we'll call it $M$), provides a decent amount of information: 
* Judging by the diagonal values, the model correctly predicted 130 correct samples out of the 219 total. This means that the **overall accuracy is 59.3%**, a terrible score.
* The model confused NORSE females with BERG females and NORSE males. This is evident with the values $M_{3,1} = 10$ (row 3 column 1) and $M_{3,4} = 12$. 
* To determine the extent to which the model should be optimized, we need to use these values to calculate some metrics.

---

## **Evaluation Metrics**
Below are some of the most common evaluation metrics used for classification models.

### **Precision**

Precision measures how precise or accurate the positive predictions of a classifier are. It is the ratio of true positives to the sum of true positives and false positives. Precision indicates how many of the instances *predicted* as positive are *actually positive.*
$$\text{precision} = \frac{TP}{TP+FP}$$  

Let's calculate precision for the `BERGF` class. We need the true positives, $M_{1,1}$, and the false positives, $M_{1,2} + M_{1,3} + M_{1,4}$.
<p align="center">
      <img src="https://raw.githubusercontent.com/s-lasch/s-lasch.github.io/cdf2efb58bdee99a99f052494423c04a056ae228/images/bergf_precision.svg" />
</p>

As a rule of thumb, you should optimize your model for precision when you want to decrease the number of false positives.


### **Recall**

Recall, also known as sensitivity or true positive rate, measures the ability of the classifier to correctly identify positive instances. It is the ratio of true positives to the sum of true positives and false negatives. Recall indicates the proportion of actual positive instances that are correctly predicted. $$\text{recall} = \frac{TP}{TP + FN}$$

Let's calculate recall for the `BERGM` class. 
<p align="center">
      <img src="https://raw.githubusercontent.com/s-lasch/s-lasch.github.io/cdf2efb58bdee99a99f052494423c04a056ae228/images/bergm_recall.svg" />
</p>

You should optimize your model for recall if you want to decrease the number of false negatives.


### **Accuracy**

Accuracy measures of how often the classifier correctly predicts the class of an instance. It is the ratio of the correctly classified instances to the total number of instances in the dataset. Higher accuracy indicates a better overall performance of the classifier. In the Multi-class Confusion section, we calculated the model's overall accuracy by adding all the correct predictions and dividing it by the number of total samples. 


### **F1-score**

Another common metric is the F1-score, which rates the successfulness of a classification model. It is the [harmonic mean](https://www.investopedia.com/terms/h/harmonicaverage.asp) of both the precision and recall for a given class. The benefit of a harmonic mean rather than a simple average is that it punishes extreme values. If a classification model has a precision of 1.0 and a recall of 0.0, has a simple average of 0.5, and an F1-score of 0. Below is the formula to calculate the F1-score.

<p align="center">
      <img src="https://raw.githubusercontent.com/s-lasch/s-lasch.github.io/2cb57db2189794a4b1ff610a7ffedbb45701de89/images/general_f1_score.svg" />
</p>

For a multi-class classifier, instead of calculating an overall F1-score, we must calculate the F1-score for each class individually, in a one-versus-rest fashion. So, we just need to apply the formulas for precision, recall, and F1-score for each class.

<p align="center">
      <img src="https://raw.githubusercontent.com/s-lasch/s-lasch.github.io/2cb57db2189794a4b1ff610a7ffedbb45701de89/images/multiclass_f1_score.svg" />
</p>

The following equations demonstrates how we can calculate the F1-scores for each class in the multi-class confusion matrix from above. 

<p align="center">
      <img src="https://raw.githubusercontent.com/s-lasch/s-lasch.github.io/main/images/multi_class_confusion_matrix.png" width="40%"
           alt="Multi-class Confusion Matrix"/>
</p>

First we need to find the precision and recall for the `BERGF` class, then apply the above equation to find the F1-score:

<p align="center">
      <img src="https://raw.githubusercontent.com/s-lasch/s-lasch.github.io/d9fdd5dbf0328e874a38afa11b35ecdb3f2709aa/images/f1_bergf.svg" />
</p>

Then, we calculate precision and recall for the remaining classes:

<p align="center">
      <img src="https://raw.githubusercontent.com/s-lasch/s-lasch.github.io/d9fdd5dbf0328e874a38afa11b35ecdb3f2709aa/images/prec_and_recall_rest.svg" />
</p>

Finally, we apply the F1-score equation to each class:

<p align="center">
      <img src="https://raw.githubusercontent.com/s-lasch/s-lasch.github.io/d9fdd5dbf0328e874a38afa11b35ecdb3f2709aa/images/f1_score_rest.svg" />
</p>
