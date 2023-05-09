# analysis.py
# Author: Rebecca Feeley

# importing the various libraries I require to complete the analysis of the data
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
#iris_data.columns = ["Sepal Length (cm)", "Sepal Width (cm)", "Petal Length (cm)", "Petal Width (cm)", "Species"]
column_names = ["Sepal Length (cm)", "Sepal Width (cm)", "Petal Length (cm)", "Petal Width (cm)", "Species"]
iris_data = pd.read_csv("iris_dataset.csv", names = column_names)

#necessary to explore the data
#print(iris_data.head()) # prints top 5 rows by default to check headings for columns adding correctly
#print (iris_data.describe()) #count of each column along with their mean value, standard deviation, minimum and maximum values.
#check all data correct
#iris_data.Species.replace({'Iris-setosa':0,'Iris-versicolor':1, 'Iris-virginica':2}, inplace=True)
### Label encoding since the algorithms we are going to use do not take non numerical or boolean data as inputs (rewrite)
#print (type(iris_data))
#print (iris_data.isnull().sum()) # missing any array like object
#print (iris_data.value_counts("Species")) # check if dataset is balanced
#print(iris_data.groupby("Species").min())
#Dropping the ID Column since there is no impact of this column on the final Prediction.
#drop Id column
#dataset = dataset.drop('Id',axis=1)
#dataset.head()

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

