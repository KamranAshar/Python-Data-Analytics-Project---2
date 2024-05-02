#!/usr/bin/env python
# coding: utf-8

# # Working on Cars Data Set real project with python

# The Data of different car is given with their specifications.
# This data is availabe as a CSV file.
# 
# We are going to analyze this data set ushing the Pandas DataFrame.

# In[4]:


import pandas as pd


# In[7]:


car = pd.read_csv('cars.csv')
car


# -  Finding all Null values in the dataset. 
# If there is any null value in any colum, then we will fill it with the mean of that column.

# In[8]:


car.isnull()


# In[11]:


car.isnull().sum()


# - Checking what are the different types of Brand are there in our dataset.
# What is the count (Occurence) of each brand in the data?

# In[13]:


car.head(2)


# In[14]:


car['Car Brand'].value_counts()


# - By using filtering method.
# - Analyzing all the records where the country is indonesia or china.

# In[17]:


car[car['Country'].isin(['China','Indonesia'])]


# - By using filtering method. 
# - Analyzing all the records (rows) where Manufacturing date is above 2004.

# In[21]:


car[car['Year of Manufacture'] > 2004]


# - Removing unwanted records
# - Removeing records where manufacturing year is lower then 2004

# In[26]:


car[~(car['Year of Manufacture'] < 2004)]

