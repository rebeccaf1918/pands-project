# analysis.py
# Author: Rebecca Feeley

# Importing the various libraries required to complete the analysis of the data
import numpy as np 
import pandas as pd 
import seaborn as sea 
import matplotlib.pyplot as plt 
import sys
# I have downloaded the data... can also be gotten online at (give url)
iris_data = pd.read_csv("iris_dataset.csv", header=None) #iris_data = iris data set 
#header=None is used here so that it is recognised that there is no header in the downloaded CSV file; 
# the data itself begins from the first line 
# https://stackoverflow.com/questions/34091877/how-to-add-header-row-to-a-pandas-dataframe
# https://stackoverflow.com/questions/28162358/append-a-header-for-csv-file/28162530#28162530
column_names = ["Sepal_Length(cm)", "Sepal_Width(cm)", "Petal_Length(cm)", "Petal_Width(cm)", "Species"]
iris_data = pd.read_csv("iris_dataset.csv", names = column_names, header=None)

#necessary to explore the data
#iris_data.Species.replace({'Iris-setosa':0,'Iris-versicolor':1, 'Iris-virginica':2}, inplace=True)
### Label encoding since the algorithms we are going to use do not take non numerical or boolean data as inputs (rewrite)
#print(iris_data.groupby("Species").min())
#Dropping the ID Column since there is no impact of this column on the final Prediction.
#dataset = dataset.drop('Id',axis=1)

original_stdout = sys.stdout 
with open ("Iris_summary_data.txt", "w") as f: #w to write to file opened (add notes)
    sys.stdout = f # i had issue w/writing to file and error re text IOwrapper takes one arg (3 given) - to avoid this
    print("\n!!!!!!!!!!!!!!!ANALYSIS OF THE IRIS DATASET!!!!!!!!!!!!!!!\n")
    print(iris_data,'\n') 
    print("A brief summary of the Iris Flower data contained in the data frame:")
    print(iris_data.info(),'\n')
    print("\nA description of each column of the dataset including basic statistical analysis:\n", iris_data.describe(),'\n')
    print("The number of rows and columns respectively, are:\n", iris_data.shape, '\n')
    print("The top 5 rows of the dataset:\n", iris_data.head(), '\n')
    print("The last 5 rows of the dataset:\n", iris_data.tail(), '\n')
    print("To check if the dataset has any null values\n",(iris_data.isnull().any()),'\n')#if missing, will display true
    print("To check if the dataset has equal rows in each species column i.e is balanced\n",iris_data.value_counts("Species"), '\n')
    print("The median value for each column grouped by species is:\n", iris_data.groupby("Species").median(),'\n') # https://stackoverflow.com/questions/72050177/futurewarning-dropping-of-nuisance-columns-in-dataframe-reductions-warning-wh
    print("The mean value for each column grouped by species is:\n", iris_data.groupby("Species").mean(), '\n')#https://www.statology.org/pandas-mean-by-group/
    sys.stdout = original_stdout
#add more to txt file here, or maybe keep in original terminal output


####   HISTROGRAM    #####
iris_data = pd.read_csv("iris_dataset.csv", names=column_names)
iris_data.hist(bins=5, color='pink', edgecolor='black', grid=False) # doesnt have even x and y intervals
#plt.show() # built in function to create histograms of each columns - doesnt split by species

#rewrite & explain code re histograms -Dra  (not split by species)
fig, axs = plt.subplots(2, 2, figsize=(10,10))
fig.tight_layout()
sea.histplot(data=iris_data, x='Sepal_Length(cm)', ax=axs[0,0], bins=7, color='blue')
sea.histplot(data=iris_data, x='Sepal_Width(cm)', ax=axs[0,1], bins=7, color='purple')
sea.histplot(data=iris_data, x='Petal_Length(cm)', ax=axs[1,0], bins=7, color='yellow')
sea.histplot(data=iris_data, x='Petal_Width(cm)', ax=axs[1,1], bins=7, color='green')
plt.suptitle('Histogram of the Length and Width of each Variable in cm') #https://matplotlib.org/3.https://www.geeksforgeeks.org/how-to-set-the-spacing-between-subplots-in-matplotlib-in-python/5.1/api/_as_gen/matplotlib.pyplot.suptitle.html
plt.subplots_adjust(hspace=0.7) #adjust space between plots as titles werent showing properly #
plt.show()   #plt.savefig('attributes_general')










##### Scatter Plots #######   MULTIVARITAE ANALYSIS OF CORRELATION FIRST BETWEEN SIMILAR CHARACTERISTICS THEN SPECIES
iris_data = pd.read_csv("iris_dataset.csv", names=column_names)
iris_data_scatter = iris_data.plot(kind='scatter', x='Sepal_Length(cm)', y='Sepal_Width(cm)', color='purple', title='Sepal Length vs Sepal Widthin cm')
plt.show()
iris_data = pd.read_csv("iris_dataset.csv", names=column_names)
iris_data_scatter = iris_data.plot(kind='scatter', x='Petal_Length(cm)', y='Petal_Width(cm)')
plt.show()

sea.scatterplot(data=iris_data, x='Sepal_Length(cm)', y='Sepal_Width(cm)', hue='Species')
plt.plot() #split by species diff colours
plt.show()  ##### From the above graph we can see that (REWRITE)
# Iris-virginica has a longer sepal length while Iris-setosa has larger sepal width
# For setosa sepal width is more than sepal length

sea.scatterplot(data=iris_data, x='Petal_Length(cm)', y='Petal_Width(cm)', hue='Species')
plt.plot()#split by species diff colours
plt.show()

sea.pairplot(iris_data, hue='Species')
plt.plot()
plt.show() ### fix up formatting
