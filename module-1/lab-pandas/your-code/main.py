# Alberto García Cobo

# # Lab | Pandas Deep Dive

# imports
import pandas as pd

# cargamos datos
path_file = "apple_store.csv"
data = pd.read_csv(path_file)
print(data.head(10))

# ## How many apps are there in the data source?

print(data.describe())
print(data.dtypes)


# eliminamos duplicados
data = data.drop_duplicates()
len_diff_data = len(data.track_name)
print('There are {} different apps'.format(len_diff_data))

# ### What is the average rating of all apps?

# sobre user_rating
avg_rating_mean = data.user_rating.mean()
print('The average rating of all apps is {}'.format(avg_rating_mean))


# ### How many apps have an average rating no less than 4?

avg_rating = data.user_rating
avg_rating_higher_4 = avg_rating[avg_rating >= 4]
print('The number of apps with average rating no less than 4 is {}'.format(len(avg_rating_higher_4)))

"""
con métodos de pandas se ejecutaría más rápido
(data.user_rating >= 4).sum()
"""

# ### How many genres are there in total for all the apps?

diff_genres = data.prime_genre.drop_duplicates()
print('The number of different genres is {}'.format(len(diff_genres)))


# ### What are the top 3 genres that have the most number of apps?

genres = data.prime_genre
unique_genres = genres.value_counts()
print('Top 3 genres that have the most number of apps: ')
print(unique_genres.head(3))


# ### Which genre is most likely to contain free apps?

# free apps -> price = 0.00
free_apps = data.prime_genre[data.price == 0.00]
genre_most_likely_free = free_apps.value_counts().head(1)
print('The genre most likely to contain free apps is {}'.format(genre_most_likely_free))


# ### If a developer tries to make money by developing and selling Apple Store apps, in which genre should s/he develop the apps? Please assume all apps cost the same amount of time and expense to develop.

genre_prices = data[['prime_genre', 'price']]
top = genre_prices.groupby('prime_genre').mean().sort_values(by=['price'], ascending=False)
top


print(top.head(1))


# ### Bonus Question: What is the proportion of apps that don't have an English track_name?

# https://pypi.org/project/langdetect/
# !pip3 install langdetect

from langdetect import detect

no_eng = 0
total = 0

for name in data.track_name: 
    try:  
        res = detect(name) != 'en'        
    except: 
        pass
    else: 
        total += 1
        if res: 
            no_eng += 1
    # print((name))
        

print('the proportion of apps that do not have an English track_name is {}%'.format(str(100*no_eng/total)))


