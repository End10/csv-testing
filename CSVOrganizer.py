import os
import pandas as pd

def csvOrganizer(file, column):
    """
    organizes a csv file based on given absolute file location
    Args: 
    file (file[.csv]): csv file

    Output (Dictionary[String,Integer]): organized list combining repeated elements
    """
    snackList = []
    df = pd.read_csv(file)
    print(df[column])

    for i in df[column]:
        snackList.append(i.split(','))
        
    print(snackList)
    
print("paste copied path of file")

filePath = input()
#"C:\Users\Jamesb\OneDrive - The University of Chicago\Documents\Keller Snack voting.csv"
csvOrganizer(filePath.replace('"', ""), "What snack are you craving for?\n(disregard the photo, big back and proud 👅👅👅)")