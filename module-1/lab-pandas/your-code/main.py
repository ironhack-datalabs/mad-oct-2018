import pandas as pd
import numpy as np
url="./apple_store.csv"
data=pd.read_csv(url)
print(data.head(50))
print(data.dtypes)
print(len(data.columns))
print(data.columns)

# 1.How many apps are there in the data source?
print(len(data["track_name"]))

# 2.What is the average rating of all apps?
print(data.user_rating.mean())

#3. How many apps have an average rating no less than 4?
WRated=sum(data["user_rating"]>=4)
print(WRated)

# 4.How many genres are there in total for all the apps?
genres=set(data.prime_genre)
print(len(genres))

# 5.What are the top 3 genres that have the most number of apps?

genresApps= data.prime_genre.value_counts(sort=True)
print(genresApps.head(3))

# 6. Which genre is most likely to contain free apps

df=data[["prime_genre", "price"]][data.price==0]
genreFree= df.prime_genre.value_counts()
print(genreFree.head(1))

# 7. If a developer tries to make money by developing and selling Apple Store apps,
# in which genre should s/he develop the apps? Please assume all apps cost the same amount 
# of time and expense to develop.

appsPrice=data[["prime_genre", "price"]]
print(type(appsPrice))
a=appsPrice.groupby(["prime_genre"]).mean()
a=a.sort_values(["price"], ascending=False)
print(a.head(1))


#8. Bonus Question: What is the proportion of apps that don't have an English track_name?

import langdetect as ld
import langid as lg

b=data["track_name"]
c=[]
for i in b:
    c.append(list(lg.classify(str(i))))

dfc = pd.DataFrame(np.array(c), columns=['lan',"prob" ]) 
en=(sum(dfc["lan"]=="en")/len(dfc["lan"]))*100
print(en)