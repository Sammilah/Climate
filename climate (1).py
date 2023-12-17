#!/usr/bin/env python
# coding: utf-8

# # World Temparature Dataset

# In[2]:


# Importing Necessary Libraries

import pandas as pd


# In[3]:


import matplotlib.pyplot as plt


# In[4]:


import seaborn as sbn


# In[32]:


get_ipython().system('pip install numpy')


# In[5]:


import numpy as np


# In[6]:


# Importing the dataset


temp_data = pd.read_csv(r"C:\Users\Administrator\Desktop\python projects\world_temps.cleaned.csv")


# # Data viewing
# 

# In[6]:


# Chenking the first five rows of the dataset

temp_data.head()


# In[7]:


# Checking the last Row or the dataset

temp_data.tail()


# In[8]:


# To displays the random n number of rows in the sample data


temp_data.sample(6)


# In[9]:


# to display the sample data's rows and columns

temp_data.shape


# # Statistics

# In[10]:


#  performing statistics like average, min/max, and quartiles on your data.

temp_data.describe


# In[18]:


# To get information about the various data types used and the non-null count of each column.

temp_data.info()


# # Data Cleaning

# In[11]:


# Identifying the missing values in the dataframe.

temp_data.isnull()


# In[12]:


# Removing the rows containing missing values in any column.

temp_data.dropna()


# # Data Selection 
# 

# In[13]:


# writing a code that will retrieve all data from  African countries

# Create a DataFrame
african_countries = temp_data[temp_data['Continent'] == 'Africa']

# Filter the data for countries in the African continent

print(african_countries)


# In[22]:


# Calculate the average climate for each year
average_climate = african_countries.iloc[:, 3:].mean(axis=0)

# Display the result
print(average_climate)


# In[38]:


# Create a line plot
plt.plot(average_climate.index, average_climate.values, marker='o')



# Add labels and title
plt.xlabel('Year')
plt.ylabel('Average Climate')
plt.title('Average Climate in African Countries (1961-2022)')


# Display the plot
plt.show()


# In[17]:


# Writimg a code to retrieve all the data from Europe

European_Countries = temp_data[temp_data['Continent'] =='Europe']

print (European_Countries )


# In[26]:


# Avarrage temp for European Countries

Avarage_temp = European_Countries.iloc[:, 3:].mean(axis=0)

print(Avarage_temp)


# In[39]:


# Ploting a line grapgh for the european avarage climate per year

plt.plot(Avarage_temp.index, Avarage_temp.values, marker='o')

plt.xlabel('Year')
plt.ylabel('Avarage temperature')
plt.title('Avarage European temperature from 1961 to 2022')

plt.show()
           


# In[46]:


# Retrieving Asian temp_Data


Asian_Countries = temp_data[temp_data['Continent'] =='Asia']


print (Asian_Countries)


# In[49]:


# Finding for Avarage temperature across conties in Asia

avarage_temp = Asian_Countries.iloc[:, 3:].mean(axis=0)

print (avarage_temp)


# In[51]:


# Ploting a Grapgh To represend the data

plt.plot(avarage_temp.index, avarage_temp.values, marker='o')



plt.xlabel('Year')
plt.ylabel('Temperature')
plt.title('Asian temperature from 1961 to 2022')

plt.show()


# In[9]:


# Retrieving North Amrican Data

north_america = temp_data[temp_data['Continent'] == 'North America']


print(north_america)


# In[11]:


# Finding Avarage North American Temp

avarage_temp = north_america.iloc[:, 3:].mean(axis=0)

print(avarage_temp)


# In[15]:


# Ploting a Line graph to 

plt.plot(avarage_temp.index, avarage_temp.values, marker='o')


plt.xlabel('Year')
plt.ylabel('Temperature')
plt.title('North American Temperature from 1961 to 2022')

plt.show


# In[17]:


# Retriving data from North American Counries

south_american= temp_data[temp_data['Continent'] == 'South America']

print (south_american)


# In[18]:


# Finding avarage temp for South America

avarage_temp = south_american.iloc[:, 3:].mean(axis=0)

print(avarage_temp)


# In[19]:


# Graph representation of the data

plt.plot(avarage_temp.index, avarage_temp.values, marker='o')


plt.xlabel('Year')
plt.ylabel('Temperature')
plt.title('South American temperature data from 1961 to 2022')


plt.show


# In[20]:


# Retrieving Oceania Data

oceania_temp = temp_data[temp_data['Continent'] == 'Oceania']

print(oceania_temp)


# In[22]:


# Finding the avarage temp of Oceania


avarage_temp = oceania_temp.iloc[:, 3:].mean(axis=0)


print(avarage_temp)


# In[23]:


# Graphical reprisentation of the data

plt.plot(avarage_temp.index, avarage_temp.values, marker= 'o')

plt.xlabel('Year')
plt.ylabel('Temperature')
plt.title('Oceania Temperature from 1961 to 2022')

plt.show


# In[24]:


# World wide Temp

world_wide = temp_data[temp_data['Continent'] == 'Worldwide']


print(world_wide)


# In[41]:


# Creating a list of continenst


continents = ['Africa', 'Europe', 'North America', 'South America', 'Oceania', 'Asia']

print(continents)


# In[49]:


# Create subplots to compare the trends
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(15, 8))
fig.suptitle('Average Temperature Trends by Continent (1961-2022)', fontsize=16)


    # Filter data for each continent
    Continent_data = temp_data[temp_data['Continent'] == 'continent']
    
    # Calculate the average temperature for each year
    average_temp = continent_data.iloc[:, 3:].mean(axis=0)
    
    # Calculate the average temperature in batches of 10 years
    average_temp_10_years = average_temp.groupby(average_temp.index // 10 * 10).mean()
    
    # Plotting
    row, col = divmod(i, 3)
    axes[row, col].plot(average_temp_10_years.index, average_temp_10_years.values, marker='o')
    axes[row, col].set_title(continent)
    axes[row, col].set_xlabel('Year')
    axes[row, col].set_ylabel('Average Temperature')

# Adjust layout
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Show the plot
plt.show()

 


# In[2]:


get_ipython().system(' pip install pandoc')


# In[ ]:




