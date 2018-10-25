print("Lab-Pandas October 25, new push")
print("")

import pandas as import pdb

#1. Import the PANDAS package under the name pd. Import the NUMPY package under the name np
import pandas as pd

#2. Define a variable called `url` that contains the path to the csv file you downloaded. 
# Alternatively, you can also assign the hyperlink value to `url`.
url="https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/data-static/data/apple_store.csv"
print("Lets define the URL")
print("For an file stored in the folder or a tree folder we can use some tools from os package or use the function list_csv_files")
print("This function give us a list of CSV files inside a folder tree. Very usefull for huge file storages")
print("")
print("First thing: Printing URL  ")
print(" >> "+url)

def list_csv_files(startpath):
    gd=[]
    for root, dirs, files in os.walk(startpath):
        for f in files:
            fn,ext=os.path.splitext(f)
            if ext=='.csv' or ext=='.CSV':
                a=root+"/"+f
                a=a.replace('\\','/')
                gd.append(a)
    return gd

# Importing os for the os.getcwd function
import os
foldpath=os.getcwd().replace('\\','/')
filesg=list_csv_files(foldpath)
print("In our case the first file is the file we are using for this task")
print(filesg[0])

#3. Using Pandas' `read_csv()` method, import the csv file at the url above. 
# Assign the returned value to a variable called `data`.
# Note: you can omit the `sep` parameter for `read_csv()` because the csv file uses the default separator of ",".
data=pd.read_csv(url)

#4. Print the first 5 rows of `data` to see what the data look like.
# A data analyst usually does this to have a general understanding about what the data look like before digging deep.
data.head(5)

"""
          id                                         track_name  size_bytes      ...       user_rating  user_rating_ver   prime_genre
0  281656475                                    PAC-MAN Premium   100788224      ...               4.0              4.5         Games
1  281796108                          Evernote - stay organized   158578688      ...               4.0              3.5  Productivity
2  281940292    WeatherBug - Local Weather, Radar, Maps, Alerts   100524032      ...               3.5              4.5       Weather
3  282614216  eBay: Best App to Buy, Sell, Save! Online Shop...   128512000      ...               4.0              4.5      Shopping
4  282935706                                              Bible    92774400      ...               4.5              5.0     Reference
"""


#5.  Print the summary (info) of the data.
data.info()

"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 7197 entries, 0 to 7196
Data columns (total 9 columns):
id                  7197 non-null int64
track_name          7197 non-null object
size_bytes          7197 non-null int64
price               7197 non-null float64
rating_count_tot    7197 non-null int64
rating_count_ver    7197 non-null int64
user_rating         7197 non-null float64
user_rating_ver     7197 non-null float64
prime_genre         7197 non-null object
dtypes: float64(3), int64(4), object(2)
memory usage: 506.1+ KB
"""


#6 Print the number of columns in the data.
print(chr(27)+"[1;34m"+"Number of colums in data: "+str(len(data.columns))+chr(27)+"[0m"+"")
"""
9
"""


#7. Print all column names.
for item in data.columns:
    print(item)
print("")
print("or")
print("")
print(data.columns)
"""
Index([u'id', u'track_name', u'size_bytes', u'price', u'rating_count_tot',
       u'rating_count_ver', u'user_rating', u'user_rating_ver',
       u'prime_genre'],
      dtype='object')
"""


# Now that we have a general understanding of the data, we'll start working on the challenge questions.

# Q1: How many apps are there in the data source?
#8. Print the # of observations of the data.
# Your code should return the number 7197.
print("")
print("> Available apps: "+str(len(set(data['track_name']))))
print("")

# Q2: What is the average rating of all apps?
#9. First, read the `user_rating` column into a varialbe named `user_rating`.
user_rating=data['user_rating'].mean()

#10. Now you can calculate the average of the `user_rating` data.
# Your code should return 3.526955675976101
print("Avg user rating for all apps available: "+str(user_rating))
print("")
print("The result above can be rounded to 1 decimal only")
print("")
print("Avg user rating for all apps available: "+str(np.round(user_rating,1)))


# Q3: How many apps have an average rating no less than 4?

#11. First, filter `user_rating` where its value >= 4. 
# Assign the filtered dataframe to a new variable called `user_rating_high`.
user_rating_high=data[data['user_rating']>=4]

#12. Now obtain the length of `user_rating_high` which should return 4781.
print(" Number of apps with an avg user rate equal or over 4: "+str(len(user_rating_high)))

# Of course you don't have to define `user_rating_high` because you only use it once.
# You can directly print the length of the filtered dataframe if you want.
print(" or ")
print(" Number of apps with an avg user rate equal or over 4: "+str(len(data[data['user_rating']>=4])))

# Q4: How many genres are there in total for all the apps?

#12. Define a new varialbe named `genres` that contains the `prime_genre` column of `data`.
prime_genre=data['prime_genre']

#13. Google for how to obtain unique values of a dataframe column. 
# Print the length of the unique values of `genres`. Your code should return 23.
print("Number of genres for all aps: "+str(len(set(prime_genre))))
print("or")
print("Number of genres for all aps: "+str(len(set(data['prime_genre']))))


# Q5: What are the top 3 genres that have the most number of apps?

"""
14. What you want to do is to count the number of occurrences of each unique genre values.
 Because you already know how to obtain the unique genre values, you can of course count the # of apps of each genre one by one.
 However, Pandas has a convient function to let you count all values of a dataframe column with a single command.
 Google for "pandas count values" to find the solution. Your code should return the following:
Games            3862
Entertainment     535
Education         453
Name: prime_genre, dtype: int64
"""
genres=pd.DataFrame(np.c_[np.unique(data['prime_genre'],return_counts=True)],columns=['Genre','Counts']).sort_values('Counts',ascending=False)
genres.head(3)


# Q6. Which genre is most likely to contain free apps?
"""
15. First, filter `data` where the price is 0.00. Assign the filtered data to a new variable called `free_apps`.
 Then count the values in `free_apps`. Your code should return:
Games                2257
Entertainment         334
Photo & Video         167
Social Networking     143
Education             132
Shopping              121
Utilities             109
Lifestyle              94
Finance                84
Sports                 79
Health & Fitness       76
Music                  67
Book                   66
Productivity           62
News                   58
Travel                 56
Food & Drink           43
Weather                31
Navigation             20
Reference              20
Business               20
Catalogs                9
Medical                 8
Name: prime_genre, dtype: int64
"""
free=data[data['price']==0]
free_apps=pd.DataFrame(np.c_[np.unique(free['prime_genre'],return_counts=True)],columns=['Genre','Count'])
free_apps=(free_apps.sort_values('Count',ascending=False)).reset_index(drop=True)
print("The genre most likely to have free apps is: "+free_apps['Genre'][0]+" with "+str(free_apps['Count'][0])+" counts")
free_apps


"""
16. Now you can calculate the proportion of the free apps in each genre based on the 
 value counts you obtained in the previous two steps. Challenge yourself by achieving 
 that with one line of code. The output should look like:
Shopping             0.991803
Catalogs             0.900000
Social Networking    0.856287
Finance              0.807692
News                 0.773333
Sports               0.692982
Travel               0.691358
Food & Drink         0.682540
Lifestyle            0.652778
Entertainment        0.624299
Book                 0.589286
Games                0.584412
Music                0.485507
Photo & Video        0.478510
Utilities            0.439516
Navigation           0.434783
Weather              0.430556
Health & Fitness     0.422222
Business             0.350877
Productivity         0.348315
Medical              0.347826
Reference            0.312500
Education            0.291391
Name: prime_genre, dtype: float64
The numbers are interesting, aren't they?
"""
# For calculation purpouse I order both data frames to have the same Genre Order
f0=free_apps.sort_values('Genre') 
g0=genres.sort_values('Genre')
relation=pd.DataFrame(np.c_[np.asarray(f0['Count'])/np.asarray(g0['Count']),g0['Genre']],columns=['Proportion','Genre']).sort_values('Proportion',ascending=False)
relation


"""
Q7. If a developer tries to make money by developing and selling Apple Store apps, 
 in which genre should s/he develop the apps? Please assume all apps cost the same 
 amount of time and expense to develop.
We will leave this question to you. There are several way to solve it. Ideally your
 output should look like below:
    average_price              genre
21       8.776087            Medical
11       5.116316           Business
4        4.836875          Reference
6        4.835435              Music
1        4.330562       Productivity
15       4.124783         Navigation
16       4.028234          Education
12       1.916444   Health & Fitness
20       1.790536               Book
7        1.647621          Utilities
2        1.605417            Weather
18       1.552381       Food & Drink
14       1.473295      Photo & Video
0        1.432923              Games
8        1.120370             Travel
10       0.953070             Sports
13       0.889701      Entertainment
17       0.885417          Lifestyle
22       0.799000           Catalogs
19       0.517733               News
5        0.421154            Finance
9        0.339880  Social Networking
3        0.016311           Shopping
But if that's too difficult it's ok. You pass this test as long as you find out the most
 expensive app genre is "Medical".
"""
pr=np.zeros(len(genres))
ik=-1 # Counter
for item in genres['Genre']:
    ik=ik+1
    pr[ik]=round((data[data['prime_genre']==item]['price']).mean(),3)
genres['avg_price']=pr
genres=genres.sort_values('avg_price',ascending=False).reset_index(drop=True)
genres[['avg_price','Genre']]


# Bonus question: What is the proportion of apps that don't have an English `track_name`?
"""
Tip: You can install `langdetect` (https://pypi.org/project/langdetect/) with `pip`, 
 then use `langdetect.detect()` to detect the language of a string. Also, you may need to 
 decode the string with `utf8` if the string is not based on the ASCII encoding. Otherwise 
 `langdetect.detect()` may throw errors.
"""
from langdetect import detect
count=0
for item in data['track_name']:
    try:
        lenguage=detect(item)
        if lenguage=='en':
            count=count+1
            if count%100==0:
                print ("Accumulative Number of apps in ENG:",count," >> ",item)
    except:
        print("")
        print(chr(27)+"[1;31m"+"** AN ERROR HAS OCURRED WHILE TRYING TO GET THE APP LANGUAGE, SKIPPING TO THE NEXT ONE **"+chr(27)+"[0m"+"")
        print("")
        pass
print("")
print(" Total Apps in Englis (en): ",str(count)," , in % > ",str(round(count*100/len(data['track_name']),2)))
print("")
print("##################################################################################################")
print("")
print(" Apps not in English (en): ",str(len(data['track_name'])-count))
print(" Apps not in English (en) %: ",str(round((len(data['track_name'])-count)*100/len(data['track_name']),2)))
print("")
print(".________________________________________________________.")
print("|                                                        |")
print("|  Thanks in advance for your Feedback! ;)               |")
print("|                                                        |")
print("|                                       Ivan Cernicharo  |")
print("|________________________________________________________|")