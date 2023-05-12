# ATU Galway Data Analytics Hdip 2023  
## Programming & Scripting Module Project Analysing the Iris Flower Data Set  
Created by Rebecca Feeley   
Student ID G00425652  

# Introduction
This repository contains my pands project for the Programming and Scripting module which forms part of the ATU Galway HDIP in Data Analytics 2023.   
This repository contains the research conducted on the Iris Data Set, the introduction and manipulation of the data, and the analysis conducted on the data, producing various visualisations such as historgrams and scatter plots, and the summary of my findings.  

# Technical Requirements
## To download this Project
1. Go to my repository on Github at https://github.com/rebeccaf1918/pands-project
2. From there, you can choose how to use the repository whether that is downloading it as a zipfile or cloning the repository.  

## Requirements to run the code
This code is written in Python programming language and there are a few requirments necessary for the operate of the project code.
1. Install Python - latest version 3.11.0 (I recommend to install Anaconda with it for expanded programming   capabilities)
2. Install the Visual Studio Code (or alternativly, your source code editor of preference)  
3. Install Cmder (or alternatively, your command line interpreter of preference)  
4. Install all the Python libraries required  


## Overview of Fisher's Iris Data Set
Fisher's Iris Data Set was created by Ronald Fisher in 1936 to demonstrate ....

## The Data
The [Iris Flower Data Set](https://en.wikipedia.org/wiki/Iris_flower_data_set) is a multivariate data set which was used in a 1936 paper by Ronald Fisher titled  
"The Use of Multiple Measurements in Taxonomic Problems as an example of Linear Discriminant Analysis."  
The data itself about the sepal and petal measuresments of the Iris Setosa, Iris Virginica and Iris Versicolour flowers were collected by Dr Edgar Anderson in Canada.   
The Iris data set has long been utilised in Data Analysis, Statistics and Machine Learning, with everyone from beginners to experts being familiar with it.   
The data set is used for multivariate data analysis and in Machine Learning as a test study for various statistical classification techniques, due to the simplicity, small and uniformly measured sample size of the data set and lack of null values or missing values.   

The Iris Data Set contains 50 samples from each of the three species of Iris Flower:
1. Iris Setosa
2. Iris Versicolour
3. Iris Virginica  

Contained in each species sample, there are 4 measurements available, measured in centimeters:
1. Septal Length 
2. Septal Width 
3. Petal Length 
4. Petal Width   

![image](https://github.com/rebeccaf1918/pands-project/assets/123907810/4da42b93-c8be-4770-a872-732e612d1b11)

By collecting the data on the 4 attributes from each of the 3 species, Fisher wanted to see if it would be possible to determine or even predict the Iris species type based on the 4 above features alone.  
Using various combinations of these 4 features, Fisher created a linear discriminant model to distinguish each species type from each other.  
The data set consists of 4 columns with the measurements of Sepal Length, Sepal Width, Petal Length, Petal Width; and a 5th column which displays the species class.  


# My Research & Analysis Conducted on the Iris Data Set  
## Requirements & Instructions  
In order to begin my analysis of the data set, I began by importing the libraries I would need to view and manipulate the data:
[Pandas](https://www.w3schools.com/python/pandas/pandas_intro.asp) is quite useful for analysing and manipulating data and making a dataset readable.
[Numpy](https://www.w3schools.com/python/numpy/default.asp) is short for 'Numerical Python' and is helpful for working with number arrays 
[Matplotlib](https://matplotlib.org/) is used for creating visualisations in Python from boxplots to scatterplots. 
[Seaborn](https://seaborn.pydata.org/tutorial/introduction) is built on top of Matplotlib and is used for creating statisical visualisations, with added features.
[Sys](https://www.geeksforgeeks.org/python-sys-module/) is has various useful features which assist in creating Python code such as allowing command line arguments to be passed to a script.

Following this, I downloaded the Iris Data Set from [UC Irvine Machine Learning](https://archive.ics.uci.edu/ml/machine-learning-databases/iris/). I then stored this data in a CSV file in my repository. 
I then read used the Pandas library to read the data from the CSV file to allow me to manipulate the data with Python code.  
As the CSV file did not include headings on the columns, I had to add the headings to the dataset.  

## Summary Overview of Data Set  
Now that the data set is downloaded, it is necessary to look at the overall data imported itself and get a general sense of the data. There are multiple built in functions available in pandas which I utilised to do this.
I opened a txt file using write 'w' mode to write all of the information gathered on the dataset to this txt file.  

I used the .info() function to get a concise, simple overview of the data. From this I learned that:
- There are 150 data entries in the data set.
- There are no Null values in the data set.
- There are 4 columns containing numerical values and 1 class column.  

I used the .describe() function to give a more complete statistical overview of the data. From this I learned:
- There are 150 flower measurements for each feature
- The mean 
- The standard deviation
- The minimum values
- The maximum values 
- The 25%, 50% and 75% percentiles 

I used the .shape() function to check how many rows and columns are in the data set. From this I learned:
- There are 150 rows 
- The are 5 columns

I also used the .value_counts() function to check if the dataset is balanced, i.e whether there are an equal number of rows (entries) for each of the species. From this I learned that:
- Yes, the dataset is balanced.

I then used the .groupby() function to get the minimum and maximum measurements of each feature of the species. This was very useful and I found myself making some preliminary theories based on these results:
- The setosa minimum measurements are much less than the other features in all but Sepal Length.
- The above is also true for the maximum measurements of the setosa.
- Due to this insight, I positied that the Iris Setosa would be more easily distinguishable.

Now that I had a better understanding of the content of the data set, I was able to begin creating visualisations of the data to draw conclusions.

## Data Visualisation
### Histograms
Per the requirements of the project, I began by creating histograms (more accurately, distplots) of the data set.
Histograms are very useful for plotting the frequency distributions in numerical data. I was able to use histograms to create a visual display of the distrubtion of the features of the Iris data set, with the x-axis corresponding to the feature (e.g Sepal Length) and the y-axis corresponding to the count frequency of each feature.  
Pandas includes a built-in function .hist() which I used to plot histograms for the flower features in the dataset.
I then adjusted the style and format of the histograms, including the colour, removing the background grid and setting the amount of intervals to be displayed in the histogram.
I then saved the 4 histograms created for each of the features to a .png in the repository.

<img width="400" alt="image" src="https://github.com/rebeccaf1918/pands-project/assets/123907810/c2f8b59a-3df1-4265-b1c0-604f866bfdcb">


From the above histograms, I came to the following conclusions:
1. Due to the fact the histograms do not specify the species corresponding to each feature, I could see that 
there was standalone bins(or bars) to the left, indicating shorter petal length and width.  At this point, I cannot determine which flower that would be, but I know that petal length and petal width are distinctive, which will be important for determining the species.
2. There is a lot of overlap between the 3 species regarding sepal length and sepal width, so those features will not be as distinctive for determining species.

However, I decided it would be more useful to visual the data if the histograms of the Length & Width of the features specified the species type. I wanted to compare Sepal Length across the three species, Sepal Width across the three species, and so on.
Thus, in order to do this, I needed to separate the 'Species' column into 3 parts for each of the species type. Through the information I gathered at the beginning of the project, I know that the 3 species type are split equally into 50 entries on each. I used numpy to use the formatting of numpy tuples as indexes i.e the first 50 lines are the Setosa category, 51 onwards is versicolor and so on.
Then, I used the built-in .distplot() function which displays multiple statistical representations of numerical data, including histrograms, rug plot and kernel density estimation. I chose the distplot function as I felt it was easier to comprehend the visualisation of data with these features on the same axis.

<img width="392" alt="image" src="https://github.com/rebeccaf1918/pands-project/assets/123907810/830d3ac9-300d-439f-96c0-77efb244941a">  

<img width="394" alt="image" src="https://github.com/rebeccaf1918/pands-project/assets/123907810/d86c4891-7915-4564-91e1-f2961c1bcb6b">

<img width="392" alt="image" src="https://github.com/rebeccaf1918/pands-project/assets/123907810/2f469e31-a6af-46bd-9fee-8b9a4a8dc379">  

<img width="392" alt="image" src="https://github.com/rebeccaf1918/pands-project/assets/123907810/08424ba9-3940-4297-8897-2be49cac8ed6">  





### Scatterplots


### Heatmap & Pairplot









## References
1. https://github.com/Prasanna-Mohanty/IRIS-Dataset-Analysis-Using-Python/blob/master/IRIS.ipynb
2. https://stackoverflow.com/questions/3263672/the-difference-between-sys-stdout-write-and-print
3. https://www.statology.org/pandas-mean-by-group/
4. https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/
5. https://towardsdatascience.com/classification-basics-walk-through-with-the-iris-data-set-d46b0331bf82
6. https://www.tutorialspoint.com/exploratory-data-analysis-on-iris-dataset
7. https://www.geeksforgeeks.org/python-seaborn-tutorial/
8. https://datagy.io/histogram-python/
9. https://stackoverflow.com/questions/31726643/how-to-plot-in-multiple-subplots
10. https://stackoverflow.com/questions/28162358/append-a-header-for-csv-file/28162530#28162530
11. https://stackoverflow.com/questions/34091877/how-to-add-header-row-to-a-pandas-dataframe
12. https://matplotlib.org/3.https://www.geeksforgeeks.org/
13. https://www.geeksforgeeks.org/how-to-set-the-spacing-between-subplots-in-matplotlib-in-python/
14. https://stackoverflow.com/questions/72050177/
15. https://stackoverflow.com/questions/72223610/dropping-invalid-columns-futurewarning
16. https://www.statology.org/pandas-mean-by-group/
17. https://stackoverflow.com/questions/34926517/stop-sys-stdout-from-writing-to-a-text-file
18. https://en.wikipedia.org/wiki/Iris_flower_data_set

