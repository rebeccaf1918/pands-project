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
iris_data.columns = ["Sepal Length (cm)", "Sepal Width (cm)", "Petal Length (cm)", "Petal Width (cm)", "Species"]
#print(iris_data.head()) # prints top 5 rows by default to check headings for columns adding correctly

print (iris_data.shape) 
print (iris_data.info)
print (iris_data.describe)






