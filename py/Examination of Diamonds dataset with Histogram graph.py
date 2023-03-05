#!/usr/bin/env python
# coding: utf-8

# # Examination of Diamonds dataset with Histogram graph

# In[2]:


import seaborn as sns
diamonds = sns.load_dataset('diamonds')
df=diamonds.copy()
df.head()

import warnings
warnings.filterwarnings('ignore')


# ### Graph-1

# In[3]:


sns.distplot(df.price,kde=False);


# The histogram is used to give the distribution of numerical and continuous variables. The operating logic divides the continuous variable into certain intervals and reflects the frequencies at these intervals. In other words, it allows us to learn about intervals and make inferences.

# ### Graph-2

# In[4]:


get_ipython().run_line_magic('pinfo', 'sns.distplot')


# In[5]:


sns.distplot(df.price,bins=1000,kde=False);


# We added the bins parameter in our histogram and assigned its value as 1000. This value
# has increased the precision in our ranges.

# ### Graph-3

# In[6]:


sns.distplot(df.price);


# histogram plot with probability density function

# ### Graph-5

# In[7]:


sns.distplot(df.price,hist=False);


# By setting the "hist" parameter to "False", only the dense graph is plotted.

# ### Graph-6

# In[8]:


sns.kdeplot(df.price,shade=True);


# The density graph is filled by entering the "shade" parameter as True.

# # Histogram and Density Crossovers

# ### Graph-7

# In[9]:


(sns
 .FacetGrid(df,
             hue="cut",
             height=5,
             xlim=(0,10000))
 .map(sns.kdeplot,"price",shade=True)
 .add_legend()
);


# When we examine Graph-6, it is seen that the density of the graph is skewed to the left. Under normal conditions, we want our graph to be in accordance with a normal distribution. That is, the middle point is skewed as the peak-shaped bulging corners are descended. We will examine the reason for this left skew in Graph-7. The "cut" variable is added to it. The cut variable refers to the qualities. When we look at the skewness, we see that the reason is due to the "Ideal" class. In fact, the "Ideal" class is where our top quality diamonds are. In other words, we expect the prices of the "Ideal" class to be high, but as it is seen, it was not like that. The majority of the "Ideal" class is distributed between 0-2000 dollars. After the price variable passed 6000, the frequencies of the categories converged.

# ### Graph-8

# In[10]:


sns.catplot(x="cut",y="price",hue="color",kind="point",data=df);


# We observe the effects of two categorical variables at different levels of "price". The fact that the categories of the "color" variable in the "Ideal" class are distributed at different levels means that an information is conveyed in the fold change via color.

# In[ ]:




