import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

fuzzStrength = 75


def csvOrganizer(file, column):
    """
    organizes a csv file based on given absolute file location
    Args: 
    file (file[.csv]): csv file

    Output (Dictionary[String,Integer]): organized list combining repeated elements
    """
    csvList = []
    gList = []
    df = pd.read_csv(file)
    print(df[column])

    for i in df[column]:
        csvList.append(i.split(','))

    for i in csvList:
        gList += i
        
    for i in gList:
        i = i.lower()

    return gList
        
    
def fuzzCheck(gList):
    """
    descr
    Args:
    Returns (List[str]): list of fuzzed strings replaced with 
    """
    fuzzedList = gList.copy()
    #print(fuzzedList) debugging

    for i in gList:
        for j in gList:
            if i==j:
                continue
            if j not in fuzzedList or i not in fuzzedList:
                continue
            if fuzz.partial_token_sort_ratio(i,j) > fuzzStrength:
                if len(str(j)) >= len(str(i)):
                    fuzzedList.remove(j)
                    fuzzedList.append(i)
                    #print("changed "+j+" into: "+i)
                else:
                    fuzzedList.remove(i)
                    fuzzedList.append(j)
                    #print("changed "+i+" into: "+j) more debbuging and helped test variables

    fuzzedList.sort()
    return fuzzedList


print("paste copied path of file")

filePath = input()
#"C:\Users\Jamesb\OneDrive - The University of Chicago\Documents\Keller Snack voting.csv"
snackFuzzList = (fuzzCheck(csvOrganizer(filePath.replace('"', ""), "What snack are you craving for? (please limit to 3 snacks)")))
print(snackFuzzList)


