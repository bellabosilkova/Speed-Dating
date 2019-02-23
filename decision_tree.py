#Importing the necessary packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
from sklearn import tree
from sklearn import metrics
from sklearn import cross_validation
from sklearn.tree import DecisionTreeClassifier
import graphviz

#Importing the dataset
df = pd.read_csv('C:\\Speed_Dating_Data.csv', encoding="ISO-8859-1")

#Choosing relevant data relating to gender, rated attributes and decisions of participants
df = df[["gender", "attr", "amb", "dec"]]

#Removing rows containing empty cells and non-numberical values
df.replace(["NaN", 'NaT'], np.nan, inplace = True)
df = df.dropna()

#Making a copy of the dataset
df_female = df

#Removing male participants from the original dataset
df = df[df.gender != 0]

#Removing female participants from the copied dataset
df_female = df_female[df_female.gender != 1]

#Creating a decision tree from the original dataset
X = df.values[:, 1:3]
Y = df.values[:, 3]

#Splitting the data into training data and test data with a 70:30 ratio
X_train, X_test, Y_train, Y_test = sklearn.cross_validation.train_test_split(X, Y,test_size=0.30)
df_tree = DecisionTreeClassifier(max_depth=3, min_samples_leaf=2)

#Fitting the training data to the model
df_tree.fit(X_train,Y_train)

#Predicting the model using the test data
y_pred = df_tree.predict(X_test)

#Printing the decision tree
print(metrics.classification_report(Y_test, y_pred))
print(metrics.confusion_matrix(Y_test, y_pred))
with open('C:\\Users\\bella\\Documents\\Python Scripts\\male_classifier.txt','w') as f:
    f = tree.export_graphviz(df_tree, class_names=["No Match", "Match"], feature_names = ["Attractiveness", "Ambition"], out_file=f)
    
#Creating a decision tree from the copied dataset
X = df_female.values[:, 1:3]
Y = df_female.values[:, 3]

#Splitting the data into training data and test data with a 70:30 ratio
X_train, X_test, Y_train, Y_test = sklearn.cross_validation.train_test_split(X, Y,test_size=0.30)
df_female_tree = DecisionTreeClassifier(max_depth=3, min_samples_leaf=2)

#Fitting the training data to the model
df_female_tree.fit(X_train,Y_train)

#Predicting the model using the test data
y_pred = df_female_tree.predict(X_test)

#Printing the decision tree
print(metrics.classification_report(Y_test, y_pred))
print(metrics.confusion_matrix(Y_test, y_pred))
with open('C:\\Users\\bella\\Documents\\Python Scripts\\female_classifier.txt','w') as f:
    f = tree.export_graphviz(df_female_tree, class_names=["No Match", "Match"], feature_names = ["Attractiveness", "Ambition"], out_file=f)
