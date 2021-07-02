#!/usr/bin/env python
# coding: utf-8

# ## Marketing Analytics

# In[1]:


from IPython.display import Image
Image(filename='marketing.png', width=500, height=200)


# ### Introduction
# This notebook will accomplish the following task:
# 
# #### Overall goal:
# You're a marketing analyst and you've been told by the Chief Marketing Officer that recent marketing campaigns have not been as effective as they were expected to be. You need to analyze the data set to understand this problem and propose data-driven solutions.
# 
# #### Section 01: Exploratory Data Analysis
# 
# Are there any null values or outliers? How will you wrangle/handle them?
# Are there any variables that warrant transformations?
# Are there any useful variables that you can engineer with the given data?
# Do you notice any patterns or anomalies in the data? Can you plot them?
# Which marketing campaign is most successful?
# 
# #### Section 02: Statistical Analysis
# Please run statistical tests in the form of regressions to answer these questions & propose data-driven action recommendations to your CMO. Make sure to interpret your results with non-statistical jargon so your CMO can understand your findings.
# 
# What factors are significantly related to the number of store purchases?
# Does US fare significantly better than the Rest of the World in terms of total purchases?
# Your supervisor insists that people who buy gold are more conservative. Therefore, people who spent an above average amount on gold in the last 2 years would have more in store purchases. Justify or refute this statement using an appropriate statistical test
# Fish has Omega 3 fatty acids which are good for the brain. Accordingly, do "Married PhD candidates" have a significant relation with amount spent on fish? What other factors are significantly related to amount spent on fish? (Hint: use your knowledge of interaction variables/effects)
# Is there a significant relationship between geographical regional and success of a campaign?
# 
# #### Section 03: Data Visualization
# Please plot and visualize the answers to the below questions.
# 
# What does the average customer look like for this company?
# Which products are performing best?
# Which channels are underperforming?

# In[13]:


import pandas as pd
pd.options.display.max_columns = None
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# In[3]:


df = pd.read_csv('marketing_data.csv')
df.head()


# In[4]:


# Removing white spaces from column names.
df.columns = df.columns.str.replace(' ', '')


# In[5]:


# Removing $ sign from Income field.
df['Income'] = df['Income'].str.replace('$', '')
df['Income'] = df['Income'].str.replace(',', '').astype('float')
df.head()


# ### Section 01: Exploratory Data Analysis

# #### Are there any null values or outliers? How will you wrangle/handle them?

# In[6]:


# Yes there are some null values. There are a 24 null values in the Income field.
# We can handle handle these null values by either dropping rows of data in the other fields so they match up with the 
# Income field or we can take take the average income and replace the missing values with that value.
df.describe(include='all')


# #### Are there any variables that warrant transformations?

# 

# #### Are there any useful variables that you can engineer with the given data?

# In[ ]:





# #### Do you notice any patterns or anomalies in the data? Can you plot them? Which marketing campaign is most successful?

# In[ ]:





# #### Which marketing campaign is most successful?
# 
# It would be the response campaign as 15% of customers accept an offer from that campaign.

# In[38]:


objects = ('Response', 'Cmp2', 'Cmp4', 'Cmp3', 'Cmp1')
y_pos = np.arange(len(objects))
performance = [15,13.3,7.5,7.3,6.5]

plt.bar(y_pos, performance, align='center', alpha=0.5,  color='royalblue')
plt.xticks(y_pos, objects)
plt.xlabel('Campaign')
plt.ylabel('Percent of Customers')
plt.title('Campaigns by Percent of Customers Who Accept an Offer')
# plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.9)
plt.show()


# In[7]:


# Calculating the percent of customers who accepted an offer after the last campaign. Here we can see that it's 15% 
# This is the most successful campaign.
df['Response'].value_counts(normalize=True)


# In[8]:


# Calculating the percent of customers who accepted an offer after the first campaign. Here we can see that it's 6.5%
df['AcceptedCmp1'].value_counts(normalize=True)


# In[9]:


# Calculating the percent of customers who accepted an offer after the second campaign. Here we can see that it's 13.3%
df['AcceptedCmp2'].value_counts(normalize=True)


# In[10]:


# Calculating the percent of customers who accepted an offer after the third campaign. Here we can see that it's 7.3%
df['AcceptedCmp3'].value_counts(normalize=True)


# In[11]:


# Calculating the percent of customers who accepted an offer after the fourth campaign. Here we can see that it's 7.5%
df['AcceptedCmp4'].value_counts(normalize=True)


# ### Section 02: Statistical Analysis
# Please run statistical tests in the form of regressions to answer these questions & propose data-driven action recommendations to your CMO. Make sure to interpret your results with non-statistical jargon so your CMO can understand your findings.
# 
# What factors are significantly related to the number of store purchases?
# Does US fare significantly better than the Rest of the World in terms of total purchases?
# Your supervisor insists that people who buy gold are more conservative. Therefore, people who spent an above average amount on gold in the last 2 years would have more in store purchases. Justify or refute this statement using an appropriate statistical test
# Fish has Omega 3 fatty acids which are good for the brain. Accordingly, do "Married PhD candidates" have a significant relation with amount spent on fish? What other factors are significantly related to amount spent on fish? (Hint: use your knowledge of interaction variables/effects)
# Is there a significant relationship between geographical regional and success of a campaign?

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ### Section 03: Data Visualization
# Please plot and visualize the answers to the below questions.
# 
# What does the average customer look like for this company?
# Which products are performing best?
# Which channels are underperforming?

# #### What does the average customer look like for this company?

# In[ ]:





# #### Which products are performing best?

# In[ ]:





#  #### Which channels are underperforming?

# In[ ]:




