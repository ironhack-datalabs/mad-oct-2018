import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns


def listing_files(startpath):
    """
    This programm retrieve a list of available files in our actual root tree for a specific file format
    """
    print("")
    print(" # USE CSV AS DEFAULT #")
    formatfile=input("Please define your format file: ")
    return [os.path.join(root,f) for root,dirs,files in os.walk(startpath) for f in files if f.endswith(formatfile.lower())]


def acquire_data():
    """
    This function will retrieve the valuable data for this case study
    It will ask you wich document index do you want to analyze (via printed 
    info in you screen). It will automattically stop the programm if your input
    is not in the indexes list. You are suposse to be smart enough to define 
    your input as an integer
    """
    files=listing_files('./')
    counter=-1
    print("")
    print("Available files: ")
    if files!=[]:
        for item in files:
            counter+=1
            print("Index: ",counter," >> ",item)
    else:
        print("Index:       >>      ")
    print("")
    try:
        if files==[]:
            raise ValueError
        index_dat=int(input("Please define your file index showed above: "))
        if index_dat not in range(len(files)):
            raise ImportError
    except ImportError:
        print(chr(27)+"[1;31m"+("INT not in indexes list").upper()+chr(27)+"[0m"+"")
    except ValueError:
        print(chr(27)+"[1;31m"+"NO FILES FOUND FOR THE FILE FORMAT YOU HAVE DEFINED ABOVE"+chr(27)+"[0m"+"")
    else:
        print("")
        print(chr(27)+"[1;32m"+"Successfully loaded  "+u'\u2713'+chr(27)+"[0m"+"")
        print("")
        return pd.read_csv(files[index_dat],encoding = "ISO-8859-1")


def wrangle(df):
    """
    This function first cleans all rows for Counttry Attribute with nan values
    Then it filter the data for an input Country defined by the user
    """
    df=df.dropna(subset=['Country']) # First nan values removal
    list_countries=df['Country'].unique()
    country_in='MARS'
    counter=0
    try:
        while country_in.upper() not in list_countries:
            print("")
            country_in=input("Iteration >> %s | Which country do you want to analyze (use lowercase)?: " %counter)
            print("")
            counter+=1
            if counter==5:
                raise IOError
            if country_in.upper() in list_countries and len(df[df['Country']==country_in.upper()])<10:
                counter=0
                print('Not enough registers for %s' %country_in)
                country_in='MARS'
    except IOError:
        print("")
        print(chr(27)+"[1;31m"+("I am bored of you pulling my leg").upper()+chr(27)+"[0m"+"")
        print("AGUR!")
        print("")
    else:
        return df[df['Country']==country_in.upper()],country_in.upper()


def analyze(df):
    """
    This function analyzes the data of a dataframe for injured and fatal registers
    It also returns the number of Shark attacks by Activity, The TOP 10
    """
    df=df.dropna(subset=['Fatal (Y/N)']) # First we delete all rows with this attribute equal to NaN
    fatal_count=(df[df['Fatal (Y/N)']=='Y'])['Area'].value_counts().reset_index()
    fatal_count.columns=['Area','Count']
    if len(fatal_count)>5:
        fatal_count=fatal_count[:5]
    injured_count=(df[df['Fatal (Y/N)']=='N'])['Area'].value_counts().reset_index()
    injured_count.columns=['Area','Count']
    if len(injured_count)>5:
        injured_count=injured_count[:5]
    activity_count=df['Activity'].value_counts()
    if len(activity_count)>5:
        activity_count=activity_count[:5]
    activity_count=activity_count.reset_index()
    activity_count.columns=['Activity','Count']
    return fatal_count,injured_count,activity_count


def reporting(fatal,injured,activity):
    
    destination=os.path.join(os.getcwd(),'Output')
    if not os.path.exists(destination):
        os.mkdir(destination)
        
    fig=plt.figure(figsize=(15,7))

    sns.barplot(data=fatal, x='Area', y='Count')
    title = ('Top 5 Areas by Fatalities for %s' %country).replace(' ','_')
    plt.title(title + "\n", fontsize=16)
    
    final=os.path.join(destination,title)
    fig.savefig(final + '.png')
    

    fig=plt.figure(figsize=(15,7))

    sns.barplot(data=injured, x='Area', y='Count')
    title = ('Top 5 Areas by Injured registers for %s' %country).replace(' ','_')
    plt.title(title + "\n", fontsize=16)
    
    final=os.path.join(destination,title)
    fig.savefig(final + '.png')
    

    fig=plt.figure(figsize=(15,7))

    sns.barplot(data=activity, x='Activity', y='Count')
    title = ('Top 5 Dangerous Activities for %s' %country).replace(' ','_')
    plt.title(title + "\n", fontsize=16)
    
    final=os.path.join(destination,title)
    fig.savefig(final + '.png')


if __name__ == '__main__':
    print("==============================================")
    print("|                                            |")
    print("|     Running main_ivan.py version 1.0       |")
    print("|____________________________________________|")
    print("")
    data=acquire_data()
    filtered,country=wrangle(data)
    fatal,injured,activity=analyze(filtered)
    reporting(fatal,injured,activity)
    print("")
    print("              ANALYSIS FINISHED               ")
    print("")
    print("         GOOD LOOK AND GODSPEED YOU           ")
    print("")
    print("______________________________________________")
    print("|                                            |")
    print("|          Created by Ivan Cernicharo Ortiz  |")
    print("|        Data Analytics Bootcamp - IronHack  |")
    print("|                                            |")
    print("==============================================")
    print("")