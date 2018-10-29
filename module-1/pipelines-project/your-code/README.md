# Pipelines Project October 29, 2018
____
## Introduction
Today is the Day of days. We face the uncertainty of being eated by a **shark** on every corner of out planet. Sharks are evil creatures that plans the dommination of our world. Do you remember DOOM Meat Balls throwing fire projectiles? Sharks are worse than this case, even more $&!*^!% than Dolphins.<br><br>
The main purpouse of this pipeline is to warn you about the Areas of a selected country that you want to visit and practice surf.<br><br>
With this ojective in mind, we will use as Dataset one of [Global_Shark_Attacks](https://www.kaggle.com/teajay/global-shark-attacks) from **Kaggle database**.<br><br>
Finally we will deliver you an overview of which area you should not visit.<br>

___
## How to Run the workflow
To run the analysis just type the next line of code:<br>
```
$ python3 main_ivan.py
```
Before running it, I recommend you to read the whole README.md
<br><br>
I have run an analysis for USA, MEXICO and AUSTRALIA. You can find the results in **Output/** folder.
<br>

___
## Step 0 - Locate the dataset
First step consists on creaating a function able to locate all files with an specific file format inside a folder tree.<br><br>
The function will ask us which format we want to look for inside our folder tree.<br><br>
This step needs you to have installed **os** module in your python 3 library. Code below helps you with the necessary code to install this module:<br>
```
$ pip3 install os
```
To run the function to locate all files and return a list of then just run the next code:
```
list_files(startpath)
```
This function will have an input cell for you to define the dataset format.<br>
This function is not called directly in the workflow but its called by function **acquire_data()** from Step #1.<br>

___
## Step 1 - Load data
Once we have listed our files, next step consists on reading the data. Here we can select which file we want to analyze.<br>
We can call load data function as follows:<br>
```
data=acquire_data()
```
Is not necessary to define ny input parameter. The function will ask for defining input parameters once called.<br>
**Files** will be atomatically loaded from folder:<br>
```
./global-shark-attack-incidents
```
<br>

___
## Step 2 - Filter data
When asked to define your format file, please use **csv** format. It is important to remember this because right now there are not any other kind of file.<br><br>
This step consists on filtering data for a specific country. Remember that this workflow pretends to advice you about how frequent is to be attacked by a shark in a detemined Country.<br><br>
Here we will call wrangle as follows:
```
filtered,country=wrangle(data)
```
Where **data** is the dataframe obtained in Step #1<br><br>
This function first cleans all rows for Counttry Attribute with nan values. Then it filter the data for an input Country defined by the user.<br><br>
The function will ask the user which country does he want to analyze.<br><br>
I invite you to test this function and its error messages :wink: <br>

___
## Step 3 - Analyze data
Next step in the workflow is to run a small analysis of shark attack frequency.<br><br>
To achieve this goal I have defined the next function:<br>
```
fatal,iunjured,activity=analyze(filtered)
```
This function analyzes the **filtered** dataframe, from Step #2, for injured and fatal registers. It also returns the number of Shark attacks by Activity developed by each registred victim. Only the TOP 5 all 3 Dataframes. <br>

___
## Step 4 - Reporting
Once we have obtained the 3 analyzed, fatal, injured and activity resulting dataframes, we procced to plot these results. Remember, just the TOP 5 Areas or Activities, depending on the dataframe analysis.<br><br>
To run this last step you can just execut the following command:<br>
```
reporting(fatal,injured,activity)
```
No need of defining as input the country, for titles issues. This function will be take the global variable country obtained in Step #2 for this purpouse.<br><br>
Deliverable are 3 images for Fatal Casualities, Injured cases and a brief review of the most dangerous activities to do before being attack by an **evil** shark.<br>

___
## Step 5 - Defining Pipelines
In the following box code you will find how to define the pipelines to get the precisse workflow I have developed for Shark Attack Evaluation: <br>
```
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
```
<br>

___
___
## Last words
Do not hesitate to contact or comment the repository if you think there could be improvements to do in it.<br>
Thank you very much for your time!<br>
___
___