#Importing the necessary packages
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering

#Establishing an array with 7 columns
cluster_array = np.array([[0, 0, 0, 0, 0, 0, 0]])

#Variable for loop
counter = 2

#Looping through all 21 waves of participants
for counter in range(22):
    
    #Importing the dataset
    df = pd.read_csv('C:\\Speed_Dating_Data.csv', encoding="ISO-8859-1")

    #Choosing relevant data relating to wave, identification number, gender, rated attributes and decisions of participants
    df = df[["wave", "pid", "gender", "attr", "sinc", "intel", "fun", "amb", "shar", "dec"]]

    #Removing rows containing empty cells and non-numberical values
    df.replace(["NaN", 'NaT'], np.nan, inplace = True)
    df = df.dropna()
    
    #Removing female participants
    df = df[df.gender != 1]

    #Removing rows containing anything but 'counter' in the wave column
    df = df[df.wave == counter]

    #Finding the maximum participant id number
    pid_max = df['pid'].max()
    
    #Finding the minimum participant id number
    pid_min = df['pid'].min()
    
    #loop to calculate the mean attribute ratings and match rates for all participants of the specified gender in the wave
    #Participant id numbers are used calculate how many iterations of the loop there will be
    while pid_min <= pid_max:       
    
        #Selecting which participant will be looked at
        df = df[df.pid == (pid_min)]
            
        #Finding the participants mean attribute ratings
        attr_mean = df['attr'].mean()
        sinc_mean = df['sinc'].mean()
        intel_mean = df['intel'].mean()
        fun_mean = df['fun'].mean()
        amb_mean = df['amb'].mean()
        shar_mean = df['shar'].mean()
        
        #Finding the percentage of "Yes" responses the participant received
        matches_mean = df['dec'].mean()*100

        #Creating a 1D numpy array containing all 7 of the variables
        cluster_array_temp = np.array([[attr_mean, sinc_mean, intel_mean, fun_mean, amb_mean, shar_mean, matches_mean]])
        
        #Stacking the participants data
        cluster_array=np.vstack((cluster_array, cluster_array_temp))
      
        #Importing the complete dataset again so that the values for the next participant in the wave can be calculated
        df = pd.read_csv('C:\\Speed_Dating_Data.csv', encoding="ISO-8859-1")

        #Choosing relevant data relating to wave, identification number, gender, rated attributes and decisions of participants
        df = df[["wave", "pid", "gender", "attr", "sinc", "intel", "fun", "amb", "shar", "dec"]]

        #Removing rows containing empty cells and non-numberical values
        df.replace(["NaN", 'NaT'], np.nan, inplace = True)
        df = df.dropna()
        
        #Removing female participants
        df = df[df.gender != 1]

        #Removing rows containing anything but 'counter' in the wave column
        df = df[df.wave == counter]

        #Moving onto the next participant
        pid_min += 1
    
    #Moving onto the next wave
    counter += 1
    
#Creating a dataframe from the array
cluster_dataset = pd.DataFrame({'Attractiveness':cluster_array[:,0],'Sincerity':cluster_array[:,1],'Intelligence':cluster_array[:,2],'Fun':cluster_array[:,3],'Ambition':cluster_array[:,4],'Shared Interests':cluster_array[:,5], 'Decision':cluster_array[:,6]})

#Ordering the dataframe
cluster_dataset = cluster_dataset[['Attractiveness','Sincerity','Intelligence','Fun', 'Ambition', 'Shared Interests', 'Decision']]

#Starting the dataframe from the second row
cluster_dataset = cluster_dataset.iloc[1:]

#Removing rows containing empty cells and non-numberical values
cluster_dataset.replace(["NaN", 'NaT'], np.nan, inplace = True)
cluster_dataset = cluster_dataset.dropna()

#Clustering the data
X = cluster_dataset.values

#Producing a dendogram
dendrogram = sch.dendrogram(sch.linkage(X, method = 'ward'))

#Resetting counter to 0
counter = 0

#Loop to cluster all 6 attributes sepparately
while counter < 6:
    
    #Clustering the data using different colours for each cluster
    X = cluster_dataset.iloc[:, [counter,6]].values
    hc = AgglomerativeClustering(n_clusters = 3, affinity = 'euclidean', linkage = 'ward')
    y_hc = hc.fit_predict(X)
    plt.scatter(X[y_hc == 0, 0], X[y_hc == 0, 1], s=60, c = 'deepskyblue', label = 'Cluster 1')
    plt.scatter(X[y_hc == 1, 0], X[y_hc == 1, 1], s=60, c = 'gold', label = 'Cluster 2')
    plt.scatter(X[y_hc == 2, 0], X[y_hc == 2, 1], s=60, c = 'salmon', label = 'Cluster 3')
    plt.xlim(left=1, right=10)
    plt.ylim(bottom=-10, top=110)
    plt.title('Clusters of Attributes')
    
    #If loop for labelling the clusters
    if counter == 0:
        plt.xlabel('Attractiveness')
    elif counter == 1:
        plt.xlabel('Sincerity')
    elif counter == 2:
        plt.xlabel('Intelligence')
    elif counter == 3:
        plt.xlabel('Fun')
    elif counter == 4:
        plt.xlabel('Ambition')
    elif counter == 5:
        plt.xlabel('Shared Interests')
        
    #Y Label is always the same
    plt.ylabel('Percentage of Matches')
    
    #Plotting the clusters
    plt.show()
    
    #Moving onto the next attribute
    counter += 1  
