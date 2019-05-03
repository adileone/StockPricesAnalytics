
# coding: utf-8

# In[ ]:


import datetime
startTime = datetime.now()


# In[1]:


dataFrame = spark.read.format('csv').option('header','true').option('inferSchema','true').option('mode','DROPMALFORMED').load("file:///media/alessandro/storage/big_data-primoProgetto/dataset/historical_stock_prices.csv")


# In[2]:


dataFrame.printSchema()


# In[3]:


dataFrame.show(2,truncate= True)


# In[23]:


dataFrame.count() 


# In[4]:


df = dataFrame.filter((dataFrame.date < '2018-01-01') & (dataFrame.date > '1998-01-01'))


# In[67]:


df.count()


# In[5]:


df = df.select('ticker','close', 'volume', 'date')


# In[6]:


df.show(2)


# In[16]:


from pyspark.sql import functions as F

df1 = df.groupBy('ticker').agg((100*(F.last(df.close)-F.first(df.close))/F.first(df.close)).alias('percentageIncrease'),
                               F.min(df.close).alias('min_close'), 
                               F.max(df.close).alias('max_close'), 
                               F.mean(df.volume).alias('avg_volume'))


# In[25]:


final = df1.orderBy(df1['percentageIncrease'].desc())


# In[26]:


final.show(10)


# In[ ]:


print('Exec Time: ')
print(datetime.now() - startTime)

