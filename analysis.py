# analysis.py
# Author: Rebecca Feeley

# Importing the various libraries required to complete the analysis of the data
import numpy as np 
import pandas as pd 
import seaborn as sea 
import matplotlib.pyplot as plt 
import sys
# I have downloaded the csv data file to the directory. It can also be gotten online at https://archive.ics.uci.edu/ml/machine-learning-databases/iris/
iris_data = pd.read_csv("iris_dataset.csv", header=None) #iris_data = iris data set 
#header=None is used here so that it is recognised that there is no header in the downloaded CSV file; the data itself begins from the first line 
column_names = ["Sepal_Length(cm)", "Sepal_Width(cm)", "Petal_Length(cm)", "Petal_Width(cm)", "Species"] # I assigned names to each of the columns
iris_data = pd.read_csv("iris_dataset.csv", names = column_names, header=None)

# Firstly, I need to explore the data and check for null values, mean, median etc and get a general sense of the data

original_stdout = sys.stdout 
with open ("Iris_summary_data.txt", "w") as f: #w to write to file and opened it as it didn't already exist  
    sys.stdout = f # i had an issue w/writing to file and error re text IOwrapper taking only one arg (3 given) - to avoid this I used sys=st.dout
    #I used this to redirect the output of the python code to the specified iris txt file rather than printing in the terminal console
    print("\n!!!!!!!!!!!!!!!ANALYSIS OF THE IRIS DATASET!!!!!!!!!!!!!!!\n")
    print(iris_data,'\n') # printing the iris data set by itself without modification to check the data
    print("A brief summary of the Iris Flower data contained in the data frame:")
    print(iris_data.info(),'\n')
    print("\nA description of each column of the dataset including basic statistical analysis:\n", iris_data.describe(),'\n')
    print("The number of rows and columns respectively, are:\n", iris_data.shape, '\n')
    print("The top 5 rows of the dataset:\n", iris_data.head(), '\n')
    print("The last 5 rows of the dataset:\n", iris_data.tail(), '\n')
    print("To check if the dataset has any null values\n",(iris_data.isnull().any()),'\n') #if any are missing, result will display as TRUE
    print("To check if the dataset has equal rows in each species column i.e is balanced\n",iris_data.value_counts("Species"), '\n')
    print("The median value for each column grouped by species is:\n", iris_data.groupby("Species").median(),'\n')  
    print("The mean value for each column grouped by species is:\n", iris_data.groupby("Species").mean(), '\n')
    sys.stdout = original_stdout # this changes the output of any subsequent code back to the terminal console itself


# Below is the code to produce histograms of the data as per the project requirements:
iris_data = pd.read_csv("iris_dataset.csv", names=column_names)
#iris_data.hist(bins=8, color='purple', edgecolor='black', grid=False, figsize=(8,8)) # this is a builtin function to create multiple separate histograms of each column (i.e sepal length, then petal width etc) 
# However, the function doesnt categorise based on the species type, it just displays the frequency of each variable type (e.g sepal length) without specifying the species 
plt.suptitle('Histogram of the Length and Width of each Variable') #this function formats the title properly at the top of the image, otherwise it was showing overtop of the image
plt.subplots_adjust(top=0.9, hspace=0.4) #adjust space between graphs as titles were overlapping and unclear
#plt.show() #commented out for clarity and so imaged saved will not be blank
plt.savefig('Histograms of the Length & Width of each Variable')
plt.close()

# Heatmap of the correlation between each variable
#print(iris_data.corr(method='pearson')) # kendall method of data analysis https://www.geeksforgeeks.org/python-pandas-dataframe-corr/
sea.heatmap(iris_data.corr(method='pearson'), annot=True, linewidths=1) # line width is set to create outline for each rectangle for visual ease
# Pearson method of analysis is quite useful here. 1 means total positive correlation, 0 is no correlation and 
# -1 is total negative correlation. The results for the iris data set are across the range from 1 to -1.
plt.suptitle('Heatmap of the correlation between each variable')
plt.subplots_adjust(left=0.25, bottom = 0.3)
#plt.show()
plt.savefig("Heatmap of the Variables' Correlation")

# I wanted to compare Sepal Length across the three species, Sepal Width across the three species, and so on.
# To do this, I needed to split the species column to separate out each of the 3 species category. As I already established that each species had 50 entries,
# I was able to split the data using numpy tuples as indexes i.e the first 50 lines are the Setosa category, 51 onwards is versicolor and so on 
Setosa = iris_data[0:50] # includes 1st to 49th row  
Versicolor = iris_data[50:100]
Virginica = iris_data[100:150]

#Histogram of each species' sepal length in centimeters (using distplot feature which also displays normal curve and a rugplot)
sea.distplot(Setosa["Sepal_Length(cm)"], color= "green") # I used seaborn to create a histogram of the Sepal Length of the three species
sea.distplot(Versicolor["Sepal_Length(cm)"], color= "blue")
sea.distplot(Virginica["Sepal_Length(cm)"], color= "purple")
plt.title("Histogram - Sepal Length of Iris Setosa, Versicolor and Virginica") # I assigned a title to the histogram
plt.xlabel('Sepal_Length' + '\nof' + '\nSetosa, Versicolor and Virginica') # I labelled the x axis
plt.ylabel('Count') # Label of the y axis
plt.subplots_adjust(bottom=0.2) # the y axis label was not visible until I adjusted the dimensions
#plt.show()
plt.savefig('Histogram of Sepal Length of the Iris Setosa, Versicolor & Virginica.png')
plt.close() # to ensure that the histograms do not overlap and become muddled

# Histogram of each species' sepal width (using distplot feature)
sea.distplot(Setosa["Sepal_Width(cm)"], color= "green")
sea.distplot(Versicolor["Sepal_Width(cm)"], color= "blue")
sea.distplot(Virginica["Sepal_Width(cm)"], color= "purple")
plt.title("Histogram - Sepal Width of Iris Setosa, Versicolor and Virginica")
plt.xlabel('Sepal_Width' + '\nof' +'\nSetosa, Versicolor and Virginica')
plt.ylabel('Count')
plt.subplots_adjust(bottom=0.2)
#plt.show()
plt.savefig('Histogram of Sepal Width of the Iris Setosa, Versicolor & Virginica.png')
plt.close()

# Histogram of each species' petal length
sea.distplot(Setosa["Petal_Length(cm)"], color= "green")
sea.distplot(Versicolor["Petal_Length(cm)"], color= "blue")
sea.distplot(Virginica["Petal_Length(cm)"], color= "purple")
plt.title("Histogram - Petal Length of 'Setosa, Versicolor and Virginica'")
plt.xlabel('Petal_Length' + '\nof' + '\nSetosa, Versicolor and Virginica')
plt.ylabel('Count')
plt.subplots_adjust(bottom=0.2)
#plt.show()
plt.savefig('Histogram of Petal Length of the Iris Setosa, Versicolor & Virginica.png')
plt.close()

# Histogram of each species' petal width
sea.distplot(Setosa["Petal_Width(cm)"], color= "green")
sea.distplot(Versicolor["Petal_Width(cm)"], color= "blue")
sea.distplot(Virginica["Petal_Width(cm)"], color= "purple")
plt.title("Histogram - Petal Width of Iris Setosa, Versicolor and Virginica")
plt.xlabel('Petal_Width' + '\nof' + '\nSetosa, Versicolor and Virginica')
plt.ylabel('Count')
plt.subplots_adjust(bottom=0.2)
#plt.show()
plt.savefig('Histogram of Petal Width of the Iris Setose, Versicolor & Virginica.png')
plt.close()






##### Scatter Plots ######
iris_data = pd.read_csv("iris_dataset.csv", names=column_names)
iris_data_scatter = iris_data.plot(kind='scatter', x='Sepal_Length(cm)', y='Sepal_Width(cm)', color='purple', title='Sepal Length x Sepal Width Correlation')
plt.show()
plt.close()

iris_data = pd.read_csv("iris_dataset.csv", names=column_names)
iris_data_scatter = iris_data.plot(kind='scatter', x='Petal_Length(cm)', y='Petal_Width(cm)', color= 'purple', title='Petal Length x Petal Width Correlation')
plt.show()
plt.close()

# Scatter plot of Sepal Length x Sepal Width
sea.scatterplot(data=iris_data, x='Sepal_Length(cm)', y='Sepal_Width(cm)', hue='Species')# this function creates a scatter plot and I have specified the data to use for the x and y axis.
plt.title('Correlation between Sepal Length & Width (with species type specified)')
plt.plot() 
plt.savefig('Scatter plot of Sepal Length x Sepal Width.png')  # save image to png file 
plt.close() # so that the data is not all put on same axis; this scatter plot is created and the data stream is closed so the next scatter plot is not imposed onto it.

# Scatter plot of Petal Length x Petal Width
sea.scatterplot(data=iris_data, x='Petal_Length(cm)', y='Petal_Width(cm)', hue='Species') # hue is used to specify that the each species type should have a different colour
plt.title('Correlation between Petal Length & Width (with species type specified)')
plt.plot()
plt.savefig('Scatter plot of Petal Length x Petal Width.png')
plt.close()


# Pairplot of variables and species combined
sea.pairplot(iris_data, hue='Species')
plt.plot()
plt.show() ### fix up formatting


