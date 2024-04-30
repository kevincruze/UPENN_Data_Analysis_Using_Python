#!/usr/bin/env python
# coding: utf-8

# ## Module 2
# 
# #### In this assignment, you will work on movie data from IMDB.
# - The data includes movies and ratings from the IMDB website
# - Data File(s): imdb.xlsx
# 
# #### Data file contains 3 sheets:
# - “imdb”: contains records of movies and ratings scraped from IMDB website
# - “countries”: contains the country (of origin) names
# - “directors”: contains the director names

# In[2]:


""" Q1: 
Load and read the 'imdb.xlsx' file. Read the 'imdb' sheet into a DataFrame, df.
"""

import pandas as pd

xls = pd.ExcelFile('imdb.xlsx')
df = xls.parse('imdb')

print(df) #for debugging purposes



""" Q2: 
Store the dimensions of the DataFrame as a tuple in a variable called 'shape' and print it.

Hint: A tuple is made up of comma separated values inside parenthesis.  e.g. (1, 2)
"""

shape = df.shape

print(shape) #for debugging



""" Q3: 
Store the column titles and the types of data in variables named 'columns' and 'dtypes', then print them.
"""

columns = df.columns

dtypes = df.dtypes

print(columns, dtypes)


""" Q4: 
Examine the first 10 rows of data; store them in a variable called first10
"""

first10 = df.head(10)

print(first10)



""" Q5: 
Examine the first 5 rows of data; store them in a variable called first5
"""

first5 = df.head()

print(first5)



""" Q6: 
Import the "directors" and "countries" sheets into their own DataFrames, df_directors and df_countries.
"""
df_directors = xls.parse('directors')

df_countries = xls.parse('countries')

print(df_directors, df_countries)




""" Q7: 
Check the "directors" sheet
1. Count how many records there are based on the "id" column. (To get the number of records per "id", 
   use the value_counts method.) Store the result in a variable named count.
2. Remove the duplicates from the directors dataframe and store the result in a variable called df_directors_clean.
"""

count = df_directors['id'].value_counts()

df_directors_clean = df_directors.drop_duplicates()

print(count, df_directors_clean)






