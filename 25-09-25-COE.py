#!/usr/bin/env python
# coding: utf-8

# In[37]:


r=float(input())
def aoc(r):
    pai=3.14
    area=2*pai*(r**2)
    return area
aoc(r)



# In[42]:


def count_vowel():
    vowels="aeiouAEIOU"
    count=0
    consonents=0
    for i in a:
        if i in vowels:
            count=count+1
        else:
            consonents=consonents+1
    print("vowels are",count)
    print("consonents are",consonents)
a=input()
count_vowel()


# In[43]:


def lis():
    list=[]
    for i in li:
        if i%5==0:
            i=i-5
            list.append(i)
        else:
            list.append(i)
    print(list)
li=[30,42,56,70,45,35]
lis()


# In[45]:


def even_odd():
    a=[]
    b=[]
    for i in li:
        if li.index(i)%2==0:
            a.append(i)
        else:
            b.append(i)
    print("even index list:",a)
    print("odd index list:",b)
li=[23,24,45,67,99,54,20]
even_odd()
    


# In[49]:


def sum():
    es=0
    os=0
    for i in li:
        if i%2==0:
            es=es+li.index(i)
        else:
            os=os+li.index(i)
    print("Even sum of indexes is:",es)
    print("odd sum of indexes is:",os)
li=[20,35,45,30,60,75,85,45,25,40]
sum()
        


# In[50]:


def city():
    a=[]
    for i in li:
        if i[0]=="D" or i[0]=="d":
            a.append(i)
    print(a)
li=["Mumbai","Hyd","delhi","Dubai","Jaipur","Kolkata","Dadar","Danish"]
city()


# In[54]:


s={'Mumbai' : 50,'Hyd' : 40,'delhi' : 30,'dubai' : 20,'jaipur' : 100,'kol' : 350,'chennai' : 280,'dadar' : 200}
a=[]
for i,value in s.items():
    if value<100:
        a.append(i)
print(a)
        


# In[ ]:





# In[ ]:





# In[46]:


def even_odd():
    even_sum=0
    odd_sum=0
    for i in li:
        if i%2==0:
            even_sum=even_sum+i
        else:
            odd_sum=odd_sum+i
    print(even_sum)
    print(odd_sum)
li=[20,35,45,30,60,75,85,45,25,40]
even_odd()

