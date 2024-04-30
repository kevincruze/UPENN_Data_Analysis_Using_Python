#!/usr/bin/env python
# coding: utf-8

# ## Module 3
# 
# #### In this assignment, you will continue working on the movie data from IMDB.
# - The data includes movies and ratings from the IMDB website
# - Data File(s): imdb.xlsx
# 
# #### Data file contains 3 sheets:
# - “imdb”: contains records of movies and ratings scraped from IMDB website
# - “countries”: contains the country (of origin) names
# - “directors”: contains the director names

# In[1]:




# Loading the data
import pandas as pd

xls = pd.ExcelFile('imdb.xlsx')
df = xls.parse('imdb')
df_directors = xls.parse('directors')
df_countries = xls.parse('countries')

print("Data Loading Finished.")



""" Q1: 
Join three Dataframes: df, df_directors, and df_countries with an inner join.
Store the joined DataFrames in df.

Here are the steps:
1. Merge df with df_countries and assign it df
2. Merge df with df_directors and assign it to df again
There might be errors if the merge is not in this order, so please be careful.

"""

df = pd.merge (left=df, right=df_countries, how="inner", left_on="country_id", right_on="id")
df = pd.merge (left=df, right=df_directors, how="inner", left_on="director_id", right_on="id")
#del df['id_x']
#del df['id_y']


# After the join, the resulting Dataframe should have 12 columns.
df.shape



""" Q2: 
Save the first ten rows of movie titles in a variable called first10, then print it
"""

first10 = df['movie_title'].head(10)

first10



""" Q3: 
There's an extra character at the end of each movie title. 
Remove it from the data using str.replace.
And print the first ten rows of movie titles again. 
"""

df["movie_title"] = df["movie_title"].str.replace('Ê','')

df.head(10)





""" Q4:
Who is the director with the most movies? First get the number of movies per "director_name", then save the director's name
and count as a series of length 1 called "director_with_most"
"""

director = df['director_name'].value_counts()

director_with_most = director.head(1)

print(director_with_most)




"""Q5:
Save all of this director's movies and their ratings in a variable called all_movies_ratings, then print this variable.
(The director with the most movies you got from the last question.)
"""

all_movies_ratings = df[df["director_name"] == "Christopher Nolan"]

all_movies_ratings = all_movies_ratings[["movie_title", "imdb_score"]]

all_movies_ratings



"""Q6:
Recommend a **random** movie that has a rating of over 8.3. 
Store the random recommendation in a variable called "rand_goodmovie".
What is the title and imdb_score of your recommendation?
 
Here are the steps:
1. Query the data ('df' DataFrame) for movies with a rating over 8.3 (imdb_score > 8.3)
2. Create a random integer index location to get a single movie recommendation
3. Save the random movie recommendation in a DataFrame called 'rand_goodmovie'
4. Save the title of the random movie recommendation in a variable "random_title" and print it
5. Save the imdb_score of the random movie recommendation in a variable "random_imdb_score" and print it

"""

import random
random.seed(0)

validmovie = df[df["imdb_score"] > 8.3]

rand_int = random.randint(0, len(validmovie) - 1)
rand_goodmovie = validmovie[rand_int : rand_int + 1]

random_title = rand_goodmovie['movie_title']

random_imdb_score = rand_goodmovie['imdb_score']

print(random_title)
print(random_imdb_score)





