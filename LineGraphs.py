#Importing the necessary packages
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

#Variable for loop
counter = 0

#Loop to run the code two times. Once for each gender.
while counter < 2:
    
    #Importing the dataset
    df = pd.read_csv('C:\\Speed_Dating_Data.csv', encoding="ISO-8859-1")

    #Choosing relevant data relating to gender, desired attributes, rated attributes and decisions of participants
    df = df[["gender", "attr1_1", "sinc1_1", "intel1_1", "fun1_1", "amb1_1", "shar1_1", "attr", "sinc", "intel", "fun", "amb", "shar", "dec"]]

    #Removing rows containing empty cells and non-numberical values
    df.replace(["NaN", 'NaT'], np.nan, inplace = True)
    df = df.dropna()
    
    #Removing male participants on the first iteration through the loop and female participants on the second iteration
    df = df[df.gender == counter]
    
    #Removing rows containing 0 in the dec column so that "Yes" responses can be viewed independantly 
    df = df[df.dec != 0]
    
    #Calculating the average attribute ratings of "Yes" responses
    Total_attr_yes = df['attr'].sum() / df['attr'].count()
    
    Total_sinc_yes = df['sinc'].sum() / df['sinc'].count()
    
    Total_intel_yes = df['intel'].sum() / df['intel'].count()
    
    Total_fun_yes = df['fun'].sum() / df['fun'].count()
    
    Total_amb_yes = df['amb'].sum() / df['amb'].count()
    
    Total_shar_yes = df['shar'].sum() / df['shar'].count()
    
    #Importing the complete dataset again so that the values corresponding to the "No" reponses can be utilised
    df = pd.read_csv('C:\\Speed_Dating_Data.csv', encoding="ISO-8859-1")
    
    #Choosing relevant data relating to gender, desired attributes, rated attributes and decisions of participants
    df = df[["gender", "attr1_1", "sinc1_1", "intel1_1", "fun1_1", "amb1_1", "shar1_1", "attr", "sinc", "intel", "fun", "amb", "shar", "dec"]]
    
    #Removing rows containing empty cells and non-numberical values
    df.replace(["NaN", 'NaT'], np.nan, inplace = True)
    df = df.dropna()
    
    #Removing male participants on the first iteration through the loop and female participants on the second iteration
    df = df[df.gender == counter]
    
    #Removing rows containing 0 in the dec column so that "No" responses can be viewed independantly 
    df = df[df.dec != 1]
    
    #Calculating the average attribute ratings of "No" responses
    Total_attr_no = df['attr'].sum() / df['attr'].count()
    
    Total_sinc_no = df['sinc'].sum() / df['sinc'].count()
    
    Total_intel_no = df['intel'].sum() / df['intel'].count()
    
    Total_fun_no = df['fun'].sum() / df['fun'].count()
    
    Total_amb_no = df['amb'].sum() / df['amb'].count()
    
    Total_shar_no = df['shar'].sum() / df['shar'].count()
    
    #Creating a 1D numpy array containing all 12 of the variables
    lst = [[Total_attr_no, Total_sinc_no, Total_intel_no, Total_fun_no, Total_amb_no, Total_shar_no], [Total_attr_yes, Total_sinc_yes, Total_intel_yes, Total_fun_yes, Total_amb_yes, Total_shar_yes]]
    array = np.array(lst, float)
    
    #Creting a dataframe from the array
    dataset_line = pd.DataFrame({'Attractiveness':array[:,0],'Sincerity':array[:,1],'Intelligence':array[:,2],'Fun':array[:,3],'Ambition':array[:,4],'Shared Interests':array[:,5]})
    
    #Transposing the dataframe
    dataset_line = dataset_line.transpose()
    
    #Line Graph
    
    #Multiple line plot
    line_graph = dataset_line
    lines = line_graph.plot.line(fontsize=8, marker='o')
    fig = plt.gcf()
    
    #Setting graph size
    fig.set_size_inches(6,4)
    fig.autofmt_xdate()
    
    #Legend
    plt.legend(fancybox=True, framealpha=1, shadow=True, borderpad=0.1)
    
    #Save Line Graph
    plt.savefig("C:\\Users\\bella\\Documents\\Python Scripts\\line_graph_female.png")

    counter +=1
