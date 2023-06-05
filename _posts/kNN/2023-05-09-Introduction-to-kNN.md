---
tag: $k$-Nearest Neighbors
title: Introduction to $k$-NN
---

> **NOTE:** *all data and figures in this post are made using* `numpy` *and* `matplotlib`*.* 

### **TODO:**

#### Overview
- [ ] Add an overview

#### Uses
- [ ] Add some use cases for $k$-NN

#### The Classification Algorithm
- [x] Create an example of a $k$-NN problem
- [x] Type up rough notes describing the code 
- [ ] Clean up notes for optimal/alternative approaches for finding $k$
- [ ] Include `plotly` scatter matrix in this section (maybe)

<br>
<br>

## **Overview**

## **Uses**

## **The Classification Algorithm**


### **Finding Optimal $k$**

*This method involves using **cross-validation** to determine the optimal value of $k$. It involves choosing a fixed value for $k$ and constructing a [confusion matrix](https://s-lasch.github.io/2023/05/22/Confusion-Matrices.html) of each feature. Then, we calculate the [various evaluation metrics](https://s-lasch.github.io/2023/05/22/Classification-Evaluation.html). Doing this for numerous values of $k$, the optimal value will have the minimal amount of false positives and false negatives.*
- [ ] Clean up this section

### **Alternative Method**

*This is the method of finding a circle with radius, $r$, which the number of neighbors is determined by counting all data points that exist within that circle. Also, the data point should be put in the center of the cirlcle.*

## **Voronoi Diagrams**

A Voronoi Diagram is

> *…used to define and delineate proximal regions around individual data points by using polygonal boundaries.*
>
> – [*sciencedirect.com*](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjYns2h0av_AhU-lYkEHTf0AMAQFnoECCoQAw&url=https%3A%2F%2Fwww.sciencedirect.com%2Ftopics%2Fearth-and-planetary-sciences%2Fvoronoi-diagram%23%3A~%3Atext%3DThiessen%2520polygon%2520maps%252C%2520which%2520are%2Cpoints%2520by%2520using%2520polygonal%2520boundaries.&usg=AOvVaw333h_4NjhxXbSupF4Jt32j)

These diagrams have a [wide variety of uses](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjYns2h0av_AhU-lYkEHTf0AMAQFnoECCYQAw&url=https%3A%2F%2Fwww.irishtimes.com%2Fnews%2Fscience%2Fhow-voronoi-diagrams-help-us-understand-our-world-1.2947681%23%3A~%3Atext%3DVoronoi%2520diagrams%2520have%2520applications%2520in%2Cbased%2520on%2520exploratory%2520drill%2520holes.&usg=AOvVaw2y07KO-_HNPpHJu22OOvuW) in science, as well as in biological structures and engineering. They can be used to identify nearest airports in case of diversions, or aid mining engineers in aiding mineral resources from drill holes. 

These diagrams represent a form of classification similar to $k$-NN. Each line represents the half-way point between any two given points. These lines intersect at vertices, which are equidistant from three points instead of two. 

<p align="center">
      <img src='https://raw.githubusercontent.com/s-lasch/s-lasch.github.io/00febf318615169eb7b22c485974137b104548c8/images/voronoi_tessellation_example.svg' 
           alt='Voronoi diagram.'
           width='60%' />
<p align="center"><em>Voronoi diagram (image by author)</em></p>
</p>

Let’s add some more color to this plot. We can really see how this resembles a $k$-NN model if we color each polygon to match the point inside. 

<p align="center">
      <img src='https://raw.githubusercontent.com/s-lasch/s-lasch.github.io/00febf318615169eb7b22c485974137b104548c8/images/voronoi_tessellation_colored.svg' 
           alt='Voronoi diagram colored.'
           width='60%' />
<p align="center"><em>Voronoi diagram with colored polygons (image by author)</em></p>
</p>

This isn’t exactly like a $k$-NN problem, though it is remarkably similar. You can see one area where this approach is very prone to overfitting—the landlocked green polygon surrounded by blue. Even though this point is actually green, it is fine-tuned to the special quirks of this randomly generated dataset. 

Models that become fine-tuned to the dataset are dangerous because they can have a very high performance at training time, yet fail abysmally during inference. It is likely that the green point in the blue area is just an outlier, and so by classifying a *whole region* of outliers, we may severely limit the accuracy of our model during inference by choosing this model.  
