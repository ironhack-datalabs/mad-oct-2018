# # WEB-PROJECT - PART 1: API

# ## 1. SPACE-X API

# Necessary modules
import requests
from pandas.io.json import json_normalize
import pandas as pd
import os,datetime
import numpy as np
date=datetime.datetime.now().date().isoformat()


# #### Generating data storage folder
destfolder='./Results-API'
if not os.path.exists(destfolder):
    os.mkdir(destfolder)

# ## Retrieve Company info

# ### Basic Info of Space X
api='https://api.spacexdata.com' # API URL
cinfo='/v3/info' # COMPANY INFO
req_SX_info=api+cinfo

# Checking if there is not the CSV file for SPACE X general Info
if not os.path.exists(destfolder+"/Space_X_info.csv"):
    
    response = requests.get(req_SX_info)
    result = response.json()

    info=json_normalize(result).T
    info.columns=['Info']
    info.to_csv(destfolder+"/Space_X_info.csv")

else:
    print("")
    print("  File "+destfolder+"/Space_X_info.csv already exists")
    print("")
    print(">>  Please, continue with Starman Information Retrieve  <<")
    pass


# ## Retrieve Upcoming Launchs Information
urlrockets='https://api.spacexdata.com/v3/launches/upcoming'

destination=destfolder+"/"+date+"_Space_X_Upcoming_Launchs.csv"

# Checking if there is not the CSV file for SPACE X Upcoming Launchs
if not os.path.exists(destination):
    
    response = requests.get(urlrockets)
    result = response.json()

    upcoming_launches=json_normalize(result)
    
    # Retrieving original columns names
    cols=(upcoming_launches.columns).unique().tolist()
    # And obtaining the unique values of columns name list
    upcoming_launches=upcoming_launches[cols]
    
    # Un-nesting the Attribute rocket.first_stage.cores
    mydicts_1=upcoming_launches['rocket.first_stage.cores']
    
    # Concatenating all internal dicts inside mydicts_1
    data_1st_stage=pd.concat([pd.Series(d[0]) for d in mydicts_1], axis=1).T
    
    # Defining rocket.first_stage.cores nested attribute new names 
    data_1st_stage.columns=['rocket.first_stage.cores.'+item for item in data_1st_stage.columns]

    # Same steps for attribute rocket.first_stage.payloads
    mydicts_2=upcoming_launches['rocket.second_stage.payloads']

    data_2nd_stage=pd.concat([pd.Series(d[0]) for d in mydicts_1], axis=1).T
    data_2nd_stage.columns=['rocket.second_stage.payloads.'+item for item in data_2nd_stage.columns]
    
    # Concatenating both UN-NESTED COLUMNS OBTAINED in the lines above
    final_upcoming=pd.concat([upcoming_launches[upcoming_launches.columns.tolist()[:28]],data_1st_stage,
                              upcoming_launches[upcoming_launches.columns.tolist()[30:34]],data_2nd_stage,
                              upcoming_launches[upcoming_launches.columns.tolist()[36:]]],axis=1)
    
    # Saving the dataframe as a CSV
    final_upcoming.to_csv(destination,index=False)
    
else:
    print("")
    print("  File ",destination)
    print("  Already exists")
    print("")
    print(">>  Please, continue with Starman Information Retrieve  <<")
    pass


# ## Retrieve Starman Information

urlstarman='https://api.spacexdata.com/v3/roadster'

response = requests.get(urlstarman)
result = response.json()

# Normalizing data retrieved from starman journey (The first launch with Falcon Heavy)
starman=json_normalize(result)

# Wrangling process to clean duplicates, just in case
starman=starman.drop_duplicates(['period_days'])

# If is the first time you run this code it will create a new CSV file
if not os.path.exists(destfolder+'/Space_X_Starman.csv'):
    starman.to_csv(destfolder+'/Space_X_Starman.csv',index=False)
else:
    # If not, it will load the stored CSV and compare with the most recent data we have retrieved
    data=pd.read_csv(destfolder+'/Space_X_Starman.csv')
    data.columns=starman.columns.tolist()
    datad=pd.concat([starman,data],axis=0,sort=True)
    datad=datad.drop_duplicates(['period_days'])
    datad.to_csv(destfolder+'/Space_X_Starman.csv',index=False)

# Saving the log of the script
log_doc=destfolder+'/log_crontab_spacex_data.txt'   
if not os.path.exists(log_doc):
    docodoc=open(log_doc,'w')
    docodoc.write('\n')
    docodoc.write('*****************************************\n')
    docodoc.write('\n')
    docodoc.write('           SPACEX_data.py LOG\n          \n')
    docodoc.write('\n')
    docodoc.write('*****************************************\n')
    docodoc.write('\n')
else:
    docodoc=open(log_doc,'a')

docodoc.write('---------------------\n')
docodoc.write('\n')
docodoc.write('SPACEX_data.py script last execution on '+datetime.datetime.now().isoformat()+' \n')
docodoc.write('\n')
docodoc.write('\n')
docodoc.close()
print("")
print("Successfully executed at ",datetime.datetime.now().isoformat())
print("")