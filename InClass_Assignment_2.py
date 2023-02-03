#!/usr/bin/env python
# coding: utf-8

# In[7]:


n=int(input("enter the number "))
#upper Triangle
for i in range(n):
    for j in range(i + 1):
        print('*', end="")
    print()
# lower triangle
for i in range(n):
    for j in range(n - i - 1):
        print('*', end="")
    print()


# In[3]:


my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
l = my_list[1::2]
print(l)


# In[4]:


x = [23, 'Python', 23.98]
lst=[]
print(x)
for l in x:
    lst.append(type(l))
print(lst)


# In[5]:


Sample_List= [1,2,3,3,3,3,4,5]

def uniquefunction(lst):
    unique_list=[]
    for x in Sample_List:
        if x not in unique_list:
            unique_list.append(x)
    print("Unique List ",unique_list)

uniquefunction(Sample_List)


# In[6]:


st= 'The quick Brow Fox&'
upperCount=0
LowerCount=0
for element in range(0, len(st)):
    if st[element].isupper():
        upperCount=upperCount+1
    elif st[element].islower():
        LowerCount=LowerCount+1
    elif st[element].isspace():
        LowerCount=LowerCount
        upperCount=upperCount
    else:
        LowerCount=LowerCount
        upperCount=upperCount
print("No. of Upper-case characters: ",upperCount)
print("No. of Lower-case Characters: ",LowerCount)


# In[ ]:




