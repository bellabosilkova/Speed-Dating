#Printing Python's version
import sys
print(sys.version)

#Importing the necessary packages
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

#Importing the dataset
df = pd.read_csv('C:\\Speed_Dating_Data.csv', encoding="ISO-8859-1")

#Choosing relevant data relating to gender, desired attributes, rated attributes and decisions of participants
df = df[["gender", "attr1_1", "sinc1_1", "intel1_1", "fun1_1", "amb1_1", "shar1_1", "attr", "sinc", "intel", "fun", "amb", "shar", "dec"]]

#Removing rows containing empty cells and non-numberical values
df.replace(["NaN", 'NaT'], np.nan, inplace = True)
df = df.dropna()

#Removing male participants
df = df[df.gender != 1]

#Saving summary statistics
df.describe().to_csv("C:\\Users\\bella\\Documents\\Python Scripts\\female_summary_statistics.csv")

#Heading for visual clarity
print ("Desired Attributes")

#Calculating desired attributes as percentages 
Total_attr1_1 = df['attr1_1'].sum() / df['attr1_1'].count()
print ("%.2f" % Total_attr1_1)

Total_sinc1_1 = df['sinc1_1'].sum() / df['sinc1_1'].count()
print ("%.2f" % Total_sinc1_1)

Total_intel1_1 = df['intel1_1'].sum() / df['intel1_1'].count()
print ("%.2f" % Total_intel1_1)

Total_fun1_1 = df['fun1_1'].sum() / df['fun1_1'].count()
print ("%.2f" % Total_fun1_1)

Total_amb1_1 = df['amb1_1'].sum() / df['amb1_1'].count()
print ("%.2f" % Total_amb1_1)

Total_shar1_1 = df['shar1_1'].sum() / df['shar1_1'].count()
print ("%.2f" % Total_shar1_1)

#Removing rows containing 0 in the dec column so that "Yes" responses can be viewed independantly 
df = df[df.dec != 0]

#Summing the ratings corresponding to "Yes" decisions
Total_attr_yes = df['attr'].sum()

Total_sinc_yes = df['sinc'].sum()

Total_intel_yes = df['intel'].sum()

Total_fun_yes = df['fun'].sum()

Total_amb_yes = df['amb'].sum()

Total_shar_yes = df['shar'].sum()

Total_all_yes = float(Total_attr_yes) + float(Total_sinc_yes) + float(Total_intel_yes) + float(Total_fun_yes) + float(Total_amb_yes) + float(Total_shar_yes)

#Heading for visual clarity
print ("Average Attributes for Yes reponses")

#Adjusting each individual attribute rating so that they can be displayed as percentages of the total attribute rating
attr_yes = float(Total_attr_yes) / float(Total_all_yes) * 100
print ("%.2f" % attr_yes)

sinc_yes = float(Total_sinc_yes) / float(Total_all_yes) * 100
print ("%.2f" % sinc_yes)

intel_yes = float(Total_intel_yes) / float(Total_all_yes) * 100
print ("%.2f" % intel_yes)

fun_yes = float(Total_fun_yes) / float(Total_all_yes) * 100
print ("%.2f" % fun_yes)

amb_yes = float(Total_amb_yes) / float(Total_all_yes) * 100
print ("%.2f" % amb_yes)

shar_yes = float(Total_shar_yes) / float(Total_all_yes) * 100
print ("%.2f" % shar_yes)

#Importing the complete dataset again so that the values corresponding to the "No" reponses can be utilised
df = pd.read_csv('C:\\Speed_Dating_Data.csv', encoding="ISO-8859-1")
fields = df.columns

#Choosing relevant data relating to gender, desired attributes, rated attributes and decisions of participants
df = df[["gender", "attr1_1", "sinc1_1", "intel1_1", "fun1_1", "amb1_1", "shar1_1", "attr", "sinc", "intel", "fun", "amb", "shar", "dec"]]

#Removing rows containing empty cells and non-numberical values
df.replace(["NaN", 'NaT'], np.nan, inplace = True)
df = df.dropna()

#Removing male participants
df = df[df.gender != 1]

#Removing rows containing 1 in the dec column so that "No" responses can be viewed independantly 
df = df[df.dec != 1]

#Summing the ratings corresponding to "No" decisions
Total_attr_no = df['attr'].sum()

Total_sinc_no = df['sinc'].sum()

Total_intel_no = df['intel'].sum()

Total_fun_no = df['fun'].sum()

Total_amb_no = df['amb'].sum()

Total_shar_no = df['shar'].sum()

Total_all_no = float(Total_attr_no) + float(Total_sinc_no) + float(Total_intel_no) + float(Total_fun_no) + float(Total_amb_no) + float(Total_shar_no)

#Heading for visual clarity
print ("No")

#Adjusting each individual attribute rating so that they can be displayed as percentages of the total attribute rating
attr_no = float(Total_attr_no) / float(Total_all_no) * 100
print ("%.2f" % attr_no)

sinc_no = float(Total_sinc_no) / float(Total_all_no) * 100
print ("%.2f" % sinc_no)

intel_no = float(Total_intel_no) / float(Total_all_no) * 100
print ("%.2f" % intel_no)

fun_no = float(Total_fun_no) / float(Total_all_no) * 100
print ("%.2f" % fun_no)

amb_no = float(Total_amb_no) / float(Total_all_no) * 100
print ("%.2f" % amb_no)

shar_no = float(Total_shar_no) / float(Total_all_no) * 100
print ("%.2f" % shar_no)

#Creating a 1D numpy array containing all 18 of the variables
lst = [[Total_attr1_1, Total_sinc1_1, Total_intel1_1, Total_fun1_1, Total_amb1_1, Total_shar1_1], [attr_yes, sinc_yes, intel_yes, fun_yes, amb_yes, shar_yes], [attr_no, sinc_no, intel_no, fun_no, amb_no, shar_no]]
array = np.array(lst, float)

#Creating a dataframe from the array
dataset = pd.DataFrame({'Attractiveness':array[:,0],'Sincerity':array[:,1],'Intelligence':array[:,2],'Fun':array[:,3],'Ambition':array[:,4],'Shared Interests':array[:,5]})

#Radar chart 1

#Importing the necessary package
from math import pi

#Number of variables included in the radar chart
categories=list(dataset)[0:]
N = len(categories)

#Angle of each axis in the radar chart (divide the plot to the number of variables)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]
 
#Initialising the spider plot
ax = plt.subplot(111, polar=True)
 
#First axis to be on top:
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)

#Draw one axe per variable and add the labels
plt.xticks(angles[:-1], categories)
 
#Draw y labels
ax.set_rlabel_position(0)
plt.yticks([10,20,30], ["10","20","30"], color="grey", size=7)
plt.ylim(0,21)
 
#Plotting each category of attributes 
#Desired Attribute
values=dataset.loc[0].values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="Desired")
ax.fill(angles, values, 'b', alpha=0.1)
 
#Yes Attributes
values=dataset.loc[1].values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="Yes")
ax.fill(angles, values, 'r', alpha=0.1)
 
#Legend
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

#Save Radar Chart 1
plt.savefig("C:\\Users\\bella\\Documents\\Python Scripts\\radar_chart1.png")

#Radar chart 2

#Number of variables included in the radar chart
categories=list(dataset)[0:]
N = len(categories)

#Angle of each axis in the radar chart (divide the plot by the number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]
 
#Initialising the spider plot
ax = plt.subplot(111, polar=True)
 
#First axis to be on top
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)

#Draw one axe per variable and add the labels
plt.xticks(angles[:-1], categories)
 
#Draw y labels
ax.set_rlabel_position(0)
plt.yticks([10,20,30], ["10","20","30"], color="grey", size=7)
plt.ylim(0,21)
 
#Plotting each category of attributes 
#Desired Attributes
values=dataset.loc[0].values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="Desired")
ax.fill(angles, values, 'b', alpha=0.1)

#No Attributes
values=dataset.loc[2].values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="No")
ax.fill(angles, values, 'r', alpha=0.1)
 
#legend
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

#Save Radar Chart 2
plt.savefig("C:\\Users\\bella\\Documents\\Python Scripts\\radar_chart2.png")

#Radar chart 3

#Number of variables included in the radar chart
categories=list(dataset)[0:]
N = len(categories)

#Angle of each axis in the radar chart(divide the plot to the number of variables)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]
 
#Initialising the spider plot
ax = plt.subplot(111, polar=True)
 
#First axis to be on top 
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)

#Draw one axe per variable and add the labels 
plt.xticks(angles[:-1], categories)
 
#Draw y labels
ax.set_rlabel_position(0)
plt.yticks([10,20,30], ["10","20","30"], color="grey", size=7)
plt.ylim(0,20)
 
#Plotting each category of attributed
#Yes attributes
values=dataset.loc[1].values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="Yes")
ax.fill(angles, values, 'r', alpha=0.1)

#No attributes
values=dataset.loc[2].values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="No")
ax.fill(angles, values, 'r', alpha=0.1)
 
#legend
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

#Save Radar Chart 3
plt.savefig("C:\\Users\\bella\\Documents\\Python Scripts\\radar_chart3.png")

#Pie Charts

#Changing the indexes (0, 1, 2) to labels (Desired, Yes, No)
dataset.rename(index={0:'Desired', 1:'Yes', 2:'No'}, inplace=True)

#Pie Chart 1 (Desired attributes)
labels = 'Attractiveness', 'Sincerity', 'Intelligence', 'Fun', 'Ambition', 'Shared Interests'
attributes = [Total_attr1_1, Total_sinc1_1, Total_intel1_1, Total_fun1_1, Total_amb1_1, Total_shar1_1]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'orange', 'hotpink']

#Explode 3rd slice
explode = (0, 0.0, 0.1, 0, 0, 0)  
fig = plt.gcf()
fig.set_size_inches(4.5,4.5)
 
#Plotting the pie chart
plt.pie(attributes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=80)
plt.axis()
plt.show()
plt.savefig("C:\\Users\\bella\\Documents\\Python Scripts\\pie_chart_female_desired.png")

#Pie chart 2 (Yes attributes)
labels = 'Attractiveness', 'Sincerity', 'Intelligence', 'Fun', 'Ambition', 'Shared Interests'
attributes = [attr_yes, sinc_yes, intel_yes, fun_yes, amb_yes, shar_yes]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'orange', 'hotpink']

#Explode 3rd slice
explode = (0, 0, 0.1, 0, 0, 0)
fig = plt.gcf()
fig.set_size_inches(4.5,4.5)
 
#Plot
plt.pie(attributes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=80)
plt.axis()
plt.show()
plt.savefig("C:\\Users\\bella\\Documents\\Python Scripts\\pie_chart_female_yes.png")

#Pie Chart 3 (No attributes)
labels = 'Attractiveness', 'Sincerity', 'Intelligence', 'Fun', 'Ambition', 'Shared Interests'
attributes = [attr_no, sinc_no, intel_no, fun_no, amb_no, shar_no]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'orange', 'hotpink']

#Explode 3rd slice
explode = (0, 0, 0.1, 0, 0, 0)
fig = plt.gcf()
fig.set_size_inches(4.5,4.5)
 
#Plot
plt.pie(attributes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=80)
plt.axis()
plt.show()
plt.savefig("C:\\Users\\bella\\Documents\\Python Scripts\\pie_chart_female_no.png")

#Executing the same process except this time for male participants

#Importing the complete dataset
df = pd.read_csv('C:\\Speed_Dating_Data.csv', encoding="ISO-8859-1")

#Choosing relevant data relating to gender, desired attributes, rated attributes and decisions of participants
df = df[["gender", "attr1_1", "sinc1_1", "intel1_1", "fun1_1", "amb1_1", "shar1_1", "attr", "sinc", "intel", "fun", "amb", "shar", "dec"]]

#Removing rows containing empty cells and non-numberical values
df.replace(["NaN", 'NaT'], np.nan, inplace = True)
df = df.dropna()

#Removing female participants
df = df[df.gender != 0]

#Saving summary statistics
df.describe().to_csv("C:\\Users\\bella\\Documents\\Python Scripts\\male_summary_statistics.csv")

#Heading for visual clarity
print ("Desired Attributes")

#Calculating desired attributes as percentages 
Total_attr1_1 = df['attr1_1'].sum() / df['attr1_1'].count()
print ("%.2f" % Total_attr1_1)

Total_sinc1_1 = df['sinc1_1'].sum() / df['sinc1_1'].count()
print ("%.2f" % Total_sinc1_1)

Total_intel1_1 = df['intel1_1'].sum() / df['intel1_1'].count()
print ("%.2f" % Total_intel1_1)

Total_fun1_1 = df['fun1_1'].sum() / df['fun1_1'].count()
print ("%.2f" % Total_fun1_1)

Total_amb1_1 = df['amb1_1'].sum() / df['amb1_1'].count()
print ("%.2f" % Total_amb1_1)

Total_shar1_1 = df['shar1_1'].sum() / df['shar1_1'].count()
print ("%.2f" % Total_shar1_1)

#Removing rows containing 0 in the dec column so that "Yes" responses can be viewed independantly 
df = df[df.dec != 0]

#Summing the ratings corresponding to "Yes" decisions
Total_attr_yes = df['attr'].sum()

Total_sinc_yes = df['sinc'].sum()

Total_intel_yes = df['intel'].sum()

Total_fun_yes = df['fun'].sum()

Total_amb_yes = df['amb'].sum()

Total_shar_yes = df['shar'].sum()

Total_all_yes = float(Total_attr_yes) + float(Total_sinc_yes) + float(Total_intel_yes) + float(Total_fun_yes) + float(Total_amb_yes) + float(Total_shar_yes)

#Heading for visual clarity
print ("Average Attributes for Yes reponses")

#Adjusting each individual attribute rating so that they can be displayed as percentages of the total attribute rating
attr_yes = float(Total_attr_yes) / float(Total_all_yes) * 100
print ("%.2f" % attr_yes)

sinc_yes = float(Total_sinc_yes) / float(Total_all_yes) * 100
print ("%.2f" % sinc_yes)

intel_yes = float(Total_intel_yes) / float(Total_all_yes) * 100
print ("%.2f" % intel_yes)

fun_yes = float(Total_fun_yes) / float(Total_all_yes) * 100
print ("%.2f" % fun_yes)

amb_yes = float(Total_amb_yes) / float(Total_all_yes) * 100
print ("%.2f" % amb_yes)

shar_yes = float(Total_shar_yes) / float(Total_all_yes) * 100
print ("%.2f" % shar_yes)

#Importing the complete dataset again so that the values corresponding to the "No" reponses can be utilised
df = pd.read_csv('C:\\Speed_Dating_Data.csv', encoding="ISO-8859-1")
fields = df.columns

#Choosing relevant data relating to gender, desired attributes, rated attributes and decisions of participants
df = df[["gender", "attr1_1", "sinc1_1", "intel1_1", "fun1_1", "amb1_1", "shar1_1", "attr", "sinc", "intel", "fun", "amb", "shar", "dec"]]

#Removing rows containing empty cells and non-numberical values
df.replace(["NaN", 'NaT'], np.nan, inplace = True)
df = df.dropna()

#Removing female participants
df = df[df.gender != 0]

#Removing rows containing 1 in the dec column so that "No" responses can be viewed independantly 
df = df[df.dec != 1]

#Summing the ratings corresponding to "No" decisions
Total_attr_no = df['attr'].sum()

Total_sinc_no = df['sinc'].sum()

Total_intel_no = df['intel'].sum()

Total_fun_no = df['fun'].sum()

Total_amb_no = df['amb'].sum()

Total_shar_no = df['shar'].sum()

Total_all_no = float(Total_attr_no) + float(Total_sinc_no) + float(Total_intel_no) + float(Total_fun_no) + float(Total_amb_no) + float(Total_shar_no)

#Heading for visual clarity
print ("Average Attributes for No Responses")

#Adjusting each individual attribute rating so that they can be displayed as percentages of the total attribute rating
attr_no = float(Total_attr_no) / float(Total_all_no) * 100
print ("%.2f" % attr_no)

sinc_no = float(Total_sinc_no) / float(Total_all_no) * 100
print ("%.2f" % sinc_no)

intel_no = float(Total_intel_no) / float(Total_all_no) * 100
print ("%.2f" % intel_no)

fun_no = float(Total_fun_no) / float(Total_all_no) * 100
print ("%.2f" % fun_no)

amb_no = float(Total_amb_no) / float(Total_all_no) * 100
print ("%.2f" % amb_no)

shar_no = float(Total_shar_no) / float(Total_all_no) * 100
print ("%.2f" % shar_no)

#Creating a 1D numpy array containing all 18 of the variables
lst = [[Total_attr1_1, Total_sinc1_1, Total_intel1_1, Total_fun1_1, Total_amb1_1, Total_shar1_1], [attr_yes, sinc_yes, intel_yes, fun_yes, amb_yes, shar_yes], [attr_no, sinc_no, intel_no, fun_no, amb_no, shar_no]]
array = np.array(lst, float)

#Creating a dataframe from the array
dataset = pd.DataFrame({'Attractiveness':array[:,0],'Sincerity':array[:,1],'Intelligence':array[:,2],'Fun':array[:,3],'Ambition':array[:,4],'Shared Interests':array[:,5]})

#Radar chart 1

#Importing the necessary package
from math import pi

#Number of variables included in the radar chart
categories=list(dataset)[0:]
N = len(categories)

#Angle of each axis in the radar chart (divide the plot to the number of variables)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]
 
#Initialising the spider plot
ax = plt.subplot(111, polar=True)
 
#First axis to be on top:
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)

#Draw one axe per variable and add the labels
plt.xticks(angles[:-1], categories)
 
#Draw y labels
ax.set_rlabel_position(0)
plt.yticks([10,20,30], ["10","20","30"], color="grey", size=7)
plt.ylim(0,27)
 
#Plotting each category of attributes 
#Desired Attribute
values=dataset.loc[0].values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="Desired")
ax.fill(angles, values, 'b', alpha=0.1)
 
#Yes Attributes
values=dataset.loc[1].values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="Yes")
ax.fill(angles, values, 'r', alpha=0.1)
 
#Legend
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

#Save Radar Chart 1
plt.savefig("C:\\Users\\bella\\Documents\\Python Scripts\\radar_chart1.png")

#Radar chart 2

#Number of variables included in the radar chart
categories=list(dataset)[0:]
N = len(categories)

#Angle of each axis in the radar chart (divide the plot by the number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]
 
#Initialising the spider plot
ax = plt.subplot(111, polar=True)
 
#First axis to be on top
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)

#Draw one axe per variable and add the labels
plt.xticks(angles[:-1], categories)
 
#Draw y labels
ax.set_rlabel_position(0)
plt.yticks([10,20,30], ["10","20","30"], color="grey", size=7)
plt.ylim(0,27)
 
#Plotting each category of attributes 
#Desired Attributes
values=dataset.loc[0].values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="Desired")
ax.fill(angles, values, 'b', alpha=0.1)

#No Attributes
values=dataset.loc[2].values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="No")
ax.fill(angles, values, 'r', alpha=0.1)
 
#legend
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

#Save Radar Chart 2
plt.savefig("C:\\Users\\bella\\Documents\\Python Scripts\\radar_chart2.png")

#Radar chart 3

#Number of variables included in the radar chart
categories=list(dataset)[0:]
N = len(categories)

#Angle of each axis in the radar chart(divide the plot to the number of variables)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]
 
#Initialising the spider plot
ax = plt.subplot(111, polar=True)
 
#First axis to be on top 
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)

#Draw one axe per variable and add the labels 
plt.xticks(angles[:-1], categories)
 
#Draw y labels
ax.set_rlabel_position(0)
plt.yticks([10,20,30], ["10","20","30"], color="grey", size=7)
plt.ylim(0,20)
 
#Plotting each category of attributed
#Yes attributes
values=dataset.loc[1].values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="Yes")
ax.fill(angles, values, 'r', alpha=0.1)

#No attributes
values=dataset.loc[2].values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="No")
ax.fill(angles, values, 'r', alpha=0.1)
 
#legend
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

#Save Radar Chart 3
plt.savefig("C:\\Users\\bella\\Documents\\Python Scripts\\radar_chart3.png")

#Pie Charts

#Changing the indexes (0, 1, 2) to labels (Desired, Yes, No)
dataset.rename(index={0:'Desired', 1:'Yes', 2:'No'}, inplace=True)

#Pie Chart 1 (Desired attributes)
labels = 'Attractiveness', 'Sincerity', 'Intelligence', 'Fun', 'Ambition', 'Shared Interests'
attributes = [Total_attr1_1, Total_sinc1_1, Total_intel1_1, Total_fun1_1, Total_amb1_1, Total_shar1_1]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'orange', 'hotpink']

#Explode 3rd slice
explode = (0.1, 0, 0, 0, 0, 0)  
fig = plt.gcf()
fig.set_size_inches(4.5,4.5)
 
#Plotting the pie chart
plt.pie(attributes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=80)
plt.axis()
plt.show()
plt.savefig("C:\\Users\\bella\\Documents\\Python Scripts\\pie_chart_female_desired.png")

#Pie chart 2 (Yes attributes)
labels = 'Attractiveness', 'Sincerity', 'Intelligence', 'Fun', 'Ambition', 'Shared Interests'
attributes = [attr_yes, sinc_yes, intel_yes, fun_yes, amb_yes, shar_yes]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'orange', 'hotpink']

#Explode 3rd slice
explode = (0, 0, 0.1, 0, 0, 0)
fig = plt.gcf()
fig.set_size_inches(4.5,4.5)
 
#Plot
plt.pie(attributes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=80)
plt.axis()
plt.show()
plt.savefig("C:\\Users\\bella\\Documents\\Python Scripts\\pie_chart_female_yes.png")

#Pie Chart 3 (No attributes)
labels = 'Attractiveness', 'Sincerity', 'Intelligence', 'Fun', 'Ambition', 'Shared Interests'
attributes = [attr_no, sinc_no, intel_no, fun_no, amb_no, shar_no]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'orange', 'hotpink']

#Explode 3rd slice
explode = (0, 0, 0.1, 0, 0, 0)
fig = plt.gcf()
fig.set_size_inches(4.5,4.5)
 
#Plot
plt.pie(attributes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=80)
plt.axis()
plt.show()
plt.savefig("C:\\Users\\bella\\Documents\\Python Scripts\\pie_chart_female_no.png")
