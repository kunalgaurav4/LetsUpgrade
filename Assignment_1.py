#!/usr/bin/env python
# coding: utf-8

# # List and it'default functions
# 

# In[5]:


bicycles = ['trek', 'cannondale', 'redline', 'specialized']

print(bicycles)


# In[6]:


# Accessing Elements in a List
print(bicycles[0])


# In[8]:


# Modifying Elements in a List
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)


# In[10]:


motorcycles[0] = 'ducati'
print(motorcycles)


# In[12]:


# Adding Elements to a List

motorcycles.append('ducati')
print(motorcycles)


# In[13]:


# Removing Elements from a List

# Removing an Item Using the del Statement
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)


# In[14]:


del motorcycles[1]
print(motorcycles)


# In[16]:


# Removing an Item Using the pop() Method

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)


# In[17]:


# Removing an Item by Value

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)


# In[8]:


# Sorting a List Permanently with the sort() Method

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)


# In[9]:


cars.sort(reverse=True)
print(cars)


# In[12]:


print(len(cars))


# In[11]:


list = [{1, 2}, ('a'), ['1.1', '2.2']]

# clearing the list
list.clear()

print('List:', list)


# In[14]:


avenger = ['IronMan','SpiderMan','Hawk','CaptainAmerica']
avenger.reverse()
print(avenger)


# In[ ]:




