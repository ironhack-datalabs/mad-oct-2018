import pandas as pd
import numpy as np
import pymysql
import sqlalchemy
import matplotlib.pyplot as plt
import seaborn as sns

#inYear = int(input('Enter the year: '))
#inState = str(input('Enter the state: '))

#introduce while True if possible

def acquire():
    originalData=pd.read_csv('./CrimeData_Cleaned_PP2.csv')
    
    return originalData



def wrangle(originalData):
    workingData=originalData.iloc[:, 0:7]

    #I remove all null to work just with clean data
    null_cols = workingData.isnull().sum()*100/len(workingData.incident_id)
    toRemove=[i for i in null_cols.index.where(null_cols.values>0) if str(i)!='nan']
    workingData=workingData.dropna(subset=toRemove)   

    #I create the columns Year and Month coming from the date column for easiness

    workingData['Year']=[int(i[0:4]) for i in workingData['date']]
    workingData['Month']=[int(i[5:7]) for i in workingData['date']]

    #I remove the column date to avoid redundancy
    workingData=workingData.drop(columns=['date'])

    return workingData

def analyze(workingData):
    #define the month rank in inYear where more crimes were committed in inState
    while True:
        try:
            inYear = int(input('Enter the year: '))
            if (inYear == workingData['Year']).any():
                print("Correct")    
            else:
                raise ValueError ("Wrong year")

            inState = str(input('Enter the state: '))   
            if (inState == workingData['state']).any():
                print("Correct")
            else:
                raise ValueError ("Wrong state") 
        
        except:
            print ("wrong input")
        else:
            title="Monthly distribution of the number of killed people in %s in %s" % (inState,inYear)
            break

    #Remove all register that are not coincident with inYear:
    workingData=workingData.drop(workingData[workingData['Year']!=inYear].index)
    #Remove all register that are not coincident with inState:
    workingData=workingData.drop(workingData[workingData['state']!=inState].index)

    #Obtain total number of killed per month
    workingData=workingData.groupby(["Month"]).sum()
    workingData['Month']=workingData.index
    
    #Replace the numeric convention with the month names
    finalData=workingData.iloc[:, [1,4]]
    finalData.loc[finalData['Month']==1, "Month"] = "January"
    finalData.loc[finalData['Month']==2, "Month"] = "February"
    finalData.loc[finalData['Month']==3, "Month"] = "March"
    finalData.loc[finalData['Month']==4, "Month"] = "April"
    finalData.loc[finalData['Month']==5, "Month"] = "May"
    finalData.loc[finalData['Month']==6, "Month"] = "June"
    finalData.loc[finalData['Month']==7, "Month"] = "July"
    finalData.loc[finalData['Month']==8, "Month"] = "August"
    finalData.loc[finalData['Month']==9, "Month"] = "September"
    finalData.loc[finalData['Month']==10, "Month"] = "October"
    finalData.loc[finalData['Month']==11, "Month"] = "November"
    finalData.loc[finalData['Month']==12, "Month"] = "December"
    
    return finalData, title

def visualize(finalData,title):
    #title = 'test'
    fig, ax = plt.subplots(figsize=(12,10))
    barchart=sns.barplot(data=finalData, x='Month', y='n_killed')
    plt.title(title + "\n", fontsize=16)
    
    return barchart


def save_viz(barchart,title):
    #title='test'
    fig = barchart.get_figure()
    fig.savefig(title + '.png')

if __name__ == '__main__':
    originalData = acquire()
    workingData = wrangle(originalData)
    finalData, tit = analyze(workingData)
    barchart = visualize(finalData, tit)
    save_viz(barchart, tit)