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
3. The most frequent Sepal Length is between 6 and 6.5 (I should note the histogram is slightly skewed to the right)
4. The most frequent Sepal Width is between 3 and 3.5
5. The most frequent Petal Length is between 1 and 2.
6. The most frequent Petal Width is between 0 and 0.5


However, I decided it would be more useful to visualise the data if the histograms of the Length & Width of the features specified the species type. I wanted to compare Sepal Length across the three species, Sepal Width across the three species, and so on.
Thus, in order to do this, I needed to separate the 'Species' column into 3 parts for each of the species type. Through the information I gathered at the beginning of the project, I know that the 3 species type are split equally into 50 entries on each. I used numpy to use the formatting of numpy tuples as indexes i.e the first 50 lines are the Setosa category, 51 onwards is versicolor and so on.
Then, I used the built-in .distplot() function which displays multiple statistical representations of numerical data, including histrograms, rug plot and kernel density estimation. I chose the distplot function as I felt it was easier to comprehend the visualisation of data with these features on the same axis.

<img width="392" alt="image" src="https://github.com/rebeccaf1918/pands-project/assets/123907810/830d3ac9-300d-439f-96c0-77efb244941a">  

<img width="394" alt="image" src="https://github.com/rebeccaf1918/pands-project/assets/123907810/d86c4891-7915-4564-91e1-f2961c1bcb6b">

<img width="392" alt="image" src="https://github.com/rebeccaf1918/pands-project/assets/123907810/2f469e31-a6af-46bd-9fee-8b9a4a8dc379">  

<img width="392" alt="image" src="https://github.com/rebeccaf1918/pands-project/assets/123907810/08424ba9-3940-4297-8897-2be49cac8ed6">  

The distplots allowed me to see that:
1. The Petal Length & Petal Width of the Iris Setosa frequently are much shorter than the same features of the other two species.  
2. There is a lot of overlap amongst the three species with regard to the Sepal Length & Sepal Width and as a result, these features will not be very helpful for distinguishing species type.
3. There is very little overlap amongst the three species with regard to the Petal Length & Petal Width. 
4. There is no overlap beween the Setosa and the other two species type, and slight overlap between the Versicolor and Virginica species with regard to Petal Length and Petal Width. Thus, this will be more useful to distinguish the species type.

I then looked at scatterplots to build upon the data insights above.  

### Scatterplots
Per the requirements of the project, I then created scatter plots of the data set.
Scatter plots are very helpful for showing the relationship between two numerical data values. Thus, I first began by creating a scatter plot showing the correlation relationship between the Sepal Length and Sepal Width (without specifying which of the dots correspond to which species type.)
I also completed such a scatter plot of the Petal Length and Petal Width.
Pandas includes a bulit-in function which I used to create the scatter plots. However, I did not save these as I found the scatter plots which specified species type was more helpful and I did not want to clutter the repository.  

I then used the Seaborn function sea.scatterplot to create a scatter plot displaying the relationship between Sepal Length & Sepal Width, with a separate color dot corresponding to each species type.
I also completed a scatter plot displaying the relationship between Petal Length & Petal Width, with a separate color dot corresponding to each species type.

<img width="513" alt="image" src="https://github.com/rebeccaf1918/pands-project/assets/123907810/610a95e3-170e-4c81-a6f8-0c671cfe7cc5">
<img width="390" alt="image" src="https://github.com/rebeccaf1918/pands-project/assets/123907810/b8875429-7182-4ec8-9cbe-ef36d0213de9">    


The scatter plot of Sepal Length x Sepal Width visualised that:  
1. While Setosa species has the largest sepal widths of all the species, it also has smaller sepal lengths in comparison to the Versicolour and Virginica. Also, the sepal lengths of the Setosa are small in relation to its relatively larger sepal widths.
2. The Versicolour flower mostly occurs within the spectrum of the Setosa and Virginica highest and lowest values. Thus, the Versicolour sepal lengths and sepal widths lie in the middle of the Setosa and Virginica.
3. The Virginica flower has the larger sepal lengths of the species, but its sepal widths are relatively smaller.

The scatter plot of Petal Length x Petal Width visualised that:
1. The iris Setosa has the smallest petal lengths and petal widths, and these features are smaller by a relatively large margin in comparison to the Versicolour and Virginica (i.e Setosa = smallest feature measurements)
2. Similarly to the previous scatter plot, the Versicolour flower petal lengths and petal widths occur within the spectrum of the Setosa and Virginica highest and lowest values (i.e Versicolour = average feature measurements)
3. The Virginica flower has the high petal lengths, as well as petal widths (i.e Virginica = highest feature measurements)

I should note that at this point I also utilised the seaborn .pairplot() function to visualise the pair-wise relationships of the flower features amongst all the species in the dataset and confirm the conclusions I already derived from the previous visualisations

<img width="340" alt="image" src="https://github.com/rebeccaf1918/pands-project/assets/123907810/90acc37f-9ae0-495a-9140-6f5318a0f87b">  

In order to confirm the data insights I gleaned from the data set, I decided to use two more visualisations of the data.

### Heatmap & Boxplot
[Heatmaps](https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/) are very useful for visualisation of data by presenting the analysis of the data as colours in two dimensions, i.e it shows the correlation between the features of the Iris flower species.  
I used the built-in seaborn function .heatmap() to create the heatmap, and I specifed the correlation method to be used as Pearson. I found that this data visualisation was the easiest to understand, even for someone not very familiar with the Iris data set.  
[Pearson Correlation](https://www.geeksforgeeks.org/python-pandas-dataframe-corr/) is commonly used for numerical variables, as are in the Iris data set. It assigns over the range from -1 to 0 to 1 for correlation visualisation, with -1 meaning total negative correlation, 0 meaning there is no correlation and 1 meaning total positive correlation.   

<img width="392" alt="image" src="https://github.com/rebeccaf1918/pands-project/assets/123907810/4676c8f7-1265-476e-8ef9-f338010f49a8">  

As a result, in the heatmap for the Iris data set, we can see that:  
1. There is high correlation between Petal Length and Petal Width.  
2. There is good-high correlation between Petal Length and Sepal Width
3. There is also good-high correlation between Petal Width and Sepal Length.
4. Also, there is almost total negative correlation between Petal Length and Sepal Width  
5. There is almost total negtive correlation between Petal Width and Sepal Width.

Finally, I created [Boxplots](https://practicaldatascience.co.uk/data-science/how-to-visualise-data-using-boxplots-in-seaborn) for the Iris flower features of each species type. While these visualisations are not as intuitive to read as the heatmap, they provide the reader with a lot of information on the data set, including any outliers, the minimum and maximum value and more.
I used the seaborn .boxplot function to create a boxplot of the Sepal Length, Sepal Width, Petal Length and Petal Width respectively.  

<img width="591" alt="image" src="https://github.com/rebeccaf1918/pands-project/assets/123907810/09dfc1a6-5c42-40a7-bc93-78fe3ba0cbf5">  

<img width="591" alt="image" src="https://github.com/rebeccaf1918/pands-project/assets/123907810/c63156b9-f38f-4c42-a4a7-ddcffc914f65">  

<img width="591" alt="image" src="https://github.com/rebeccaf1918/pands-project/assets/123907810/d3516f9a-028b-4279-a525-f4ec030b732f">  

<img width="587" alt="image" src="https://github.com/rebeccaf1918/pands-project/assets/123907810/f2ad6fac-92a7-49e2-b18b-817c96ccdabf">  

From the boxplots, I gleaned the following:
1. The range of measurements for both petal length and petal width of the Setosa are quite narrow, especially in comparison with the Versicolour and Virginica ranges.
2. The median of the Sepal Width of each species are relatively similar, and so it would be difficult to use these measurments to try and distinguish species type.
3. The boxplots correspond to the previous insights that Iris Setosa has the smallest features (except for sepal width) and Setosa has outliers; Iris Versicolour has average features and Iris Virginica has the highest features.

At this point, I had completed analysis and visualisations of the data which enabled me to form an opinion on what the data contained in relation to the Iris flower species. However, there are many more ways of completing statistical analysis on the data, including boxplots, violinplots and other formats of data visualisation. Such data analysis has been conducted on the Iris data set many times, but I believe that any further analysis would not add any new insights into the data and would just be for superficial and stylistic visualisation, rather than contributing to my understanding.

## Summary & Conclusion  
Taking all of the researach, analysis and data visualisations into account, I think that the Iris Data Set raw data can be used for distinguishing one Iris flower species class from another. (I would like to note from the outset that there are many more Iris flower species and these methods of classification will only apply to the three species included in the data.)
A common theme throughout the data visualisations is that the Iris Setosa is not like the other species. For example, the scatterplots and distplots demonstrate that the Iris Setosa Petal Length, Petal Width and Sepal Length are obviously smaller in comparison to the other species, and have a much narrower range. Interestingly, the Sepal Width of the Iris Setosa is larger than both the Iris Versicolour and Iris Virginica. 
Consequently, I can make the assumption that any iris flower with a petal length of less than approx   
2.1cm must be an Iris Setosa. Also, any Iris flower with a petal width of less than 0.6cm must be an Iris Setosa. This is evidenced by the fact that the Petal Length and Petal Width distplots have little overlap, with the Iris Setosa being quite seperate from Iris Versicolour and Iris Virginica and thus Petal Length and Petal Width are good classification features. 
Thus, I would be able to make an educated guess distinguishing the Iris Setosa from the Iris Versicolour; and distinguishing the Iris Setosa from the Iris Virginica.  
However, it would be more difficult to distinguish between the Iris Versicolour and Iris Virginica as they have many more instances of overlap, as evidenced in the histograms of Sepal Length and Sepal Width. Those histograms have significant overlap amongst the three species, and so would make poor classification features on their own.



 Specifically the petal length to petal width ratio can be helpful in distinguishing the two species
 The correlation map for the overall dataset shows a negative correlation between sepal width and petal width/length. This is likely caused by the setosa plant which has the widest sepals and narrowest/shortest petals.
These negative correlations are non-existent in the individual species maps, suggesting that at a species level sepal width does not negatively influence petal width or length.
The overall correlation map shows a near-perfect correlation between petal length/width. This is also evident in the scatter plot; this variable pair output is the closer to a straight line than any of the others. This is likely because while the versicolor plant has both the longest and widest petals, setosa has both the narrowest and shortest. Therefore, within the data set as a whole, long petals is likely to also mean wide petals and vice versa.
However, within the three species, versicolor is the only group that maintains a strong correlation between these variables. This is also visible on the scatterplot; although the datapoints as a unit form a straight line, the plot doesn't appear to be linear within the setosa/versicolor species.
Within the overall data set there is a strong positive correlation between sepal length and petal length/width. This is likely due to the versicolor plant having the longest sepals and longest/widest petals: as sepal length increases so do the petal measurements.
This relationship is also evident in the scatter plots for these variable pairs; these plots are closest to a straight line of all variable combinations.
The strong positive association between petal length and sepal length is also present in the versicolor and virginica plants, but not for setosa. This suggests that within the first two species groups, longer petals also indicate longer sepals, but this is not necessarily the case for setosa plants. This is clearly visible in the scatter plots, a linear relationship seems to exist between the former but not the latter.
Within the setosa species group, a strong correlation exists between sepal length and width, to a much greater extent than the other two groups. It can therefore be assumed that longer sepals are associated with with increased sepal width within this species group.



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

