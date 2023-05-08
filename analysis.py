# analysis.py
# Author: Rebecca Feeley

import numpy as np 
import pandas as pd #import pandas library
import seaborn as sea 
import matplotlib.pyplot as plt 
import sys

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
#print (iris_data.tail())
#print ("The number of rows and columns respectively, are" , iris_data.shape) #shows shape ????

#print (iris_data.info())
#print (iris_data.describe()) #count of each column along with their mean value, standard deviation, minimum and maximum values.
#print (iris_data)
#check all data correct

#iris_data.Species.replace({'Iris-setosa':0,'Iris-versicolor':1, 'Iris-virginica':2}, inplace=True)
### Label encoding since the algorithms we are going to use do not take non numerical or boolean data as inputs (rewrite)
#print (type(iris_data))

#print (iris_data.isnull().any()) # find any null values
#print (iris_data.isnull().sum()) # missing any array like object
#print (iris_data.value_counts("Species")) # check if dataset is balanced

#with open ("Iris_summary_data.txt", 'w') as f: # prints it to txt file (add reference etc)
 #   f.write(iris_data.describe().to_string()) #f(close) maybe??

#iris_data.Species.replace({'Iris-setosa':0,'Iris-versicolor':1, 'Iris-virginica':2}, inplace=True)
### Label encoding since the algorithms we are going to use do not take non numerical or boolean data as inputs (rewrite)

#print (iris_data)
# (change code) print('\n************************ ANALYSIS OF THE IRIS DATASET *************************\n\n') 