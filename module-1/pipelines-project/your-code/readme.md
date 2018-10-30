# Web Data Pipeline Project

## Obtention of the database

The database used for the completion of this xercise has been inherited from the Pandas Project completed on week 2 of the bootcamp. Such database contains information about the crimes committed in USA between 2013 and 2018 where a fire gun was involved. The database's original csv was too heavy to upload to GitHub hence it was purged prior to the start of the current exercise conservin all register but just the first 10 columns and renaming the file as **"CrimeData_Cleaned_PP2"**


## Purpose of the exercise

The current project consists in the creation of a pipeline which contains the following phases:
* Acquire
* Wrangle
* Analyze
* Report
As a result of the pipeline, a .png should be generated with the visualization of our analysis.


## Development of the pipeline

The first step in the script has been allocated to import the necessary packages and to define the global variables:
```
import pandas as pd
import numpy as np
import pymysql
import sqlalchemy
import matplotlib.pyplot as plt
import seaborn as sns

inYear = int(input('Enter the year: '))
inState = str(input('Enter the state: '))
title="Monthly distribution of the number of killed people in %s in %s" % (inState,inYear)
```

After that, we have define the function corresponding the acquiring phase of the pipeline. This function reads the database from the same location as the pipelines script lives in:
```
def acquire():
    originalData=pd.read_csv('./CrimeData_Cleaned_PP2.csv')
    
    return originalData
```

The next phase of the pipeline contains the wrangle function which takes the return from the acquire function as an argument. This function  cleans and prepare the data within the database in order to make it ready for the next phase:
```
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
 ```

The analyze function takes workingData (the return from the Wrangle function) as an argument and transforms and operates with the dataset in order to get the results the script aims for.
```
def analyze(workingData):
    #define the month rank in inYear where more crimes were committed in inState

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
    
    return finalData
```

Both the visualize and the save_viz functions could be considered part of the reporting phase of the pipeline. Taking the return of the analyze function as argument (finalData), the visualize function will convert such data into a bar chart where the months will be in the X axis and the number of killed people will be in the Y axis. The save_viz function will save such chart into a .png file in the same directory as the script is located in.
```
def visualize(finalData):
    fig, ax = plt.subplots(figsize=(12,10))
    barchart=sns.barplot(data=finalData, x='Month', y='n_killed')
    plt.title(title + "\n", fontsize=16)
    
    return barchart


def save_viz(barchart):
    fig = barchart.get_figure()
    fig.savefig(title + '.png')
```

The last part of code contained in the script is aimed to prevent the code to be executed automatically when imported into other scripts and to force the execution of all functions in chain when the script is run.
```
if __name__ == '__main__':
    originalData = acquire()
    workingData = wrangle(originalData)
    finalData = analyze(workingData)
    barchart = visualize(finalData)
    save_viz(barchart)
```

As a result of the consecutive execution of the functions included in our pipeline, the script will return a barchart containing information about the number of killed people in a specific state and in a specific year as defined by the user.
