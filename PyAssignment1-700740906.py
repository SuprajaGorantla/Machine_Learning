#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[22]:


import statistics
ages = [19,22,19,24,20,25,26,24,25,24]

#1.1 Sort the list and find the min and max age
ages.sort() #soring the ages
min_age = min(ages) #minimum age would be the first element in sorted ages
max_age = max(ages) #maximum age would be the last element in sorted ages
print(" min_age = " , min_age , " max_age =" , max_age)


#1.2 Add the min age and the max age again to the list
ages.append(min_age) #adding min_age
ages.append(max_age) #adding max_age
print("ages = ", ages)


#1.3 Find the median age (one middle item or two middle items divided by two)
mid_value = len(ages) // 2 #finding the length for list and dividing by 2
median = (ages[mid_value] + ages[~mid_value]) / 2 # using negative in list to count items from the end and get average
print("median age = ", median)

     
#1.4 Find the average age (sum of all items divided by their number)
sum = 0 #assingning value 0 to varible named sum
length = len(ages)
for i in ages: #running for loop for list
    sum = sum + i # adding every element to sum and storing the value in sum
print("sum = ", sum/length)

#1.5 Find the range of the ages (max minus min)
ages.sort() #soring the ages
min_age = min(ages) #minimum age would be the first element in sorted ages
max_age = max(ages) #maximum age would be the last element in sorted ages
range_ages = max_age - min_age #max age minus min age gives range
print("range_ages = ", range_ages)



# In[23]:


#Create an empty dictionary called dog
dog={}#dict()
#Add name, color, breed, legs, age to the dog dictionary
dog["name"]="Rolo"
dog["color"]="grey"
dog["breed"]="Little Lion Dog"
dog["legs"]="shot"
dog["age"]="2 yrs"
print("Dog Dictionary =",dog)
#Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student={
  "first_name": "Supraja",
  "last_name": "Gorantla",
  "gender": "feMale",
  "age": 23,
  "marital status": "Single",
  "skills": ["Java", "HTML", "CSS"],
  "country": "United States",
  "city": "Denton",
  "address": "Apt no:1234, random Street",
}
#Get the length of the student dictionary
print(len(student))
#Get the value of skills and check the data type, it should be a list
student["skills"] 
print(student["skills"])
print(type(student["skills"]))
#Modify the skills values by adding one or two skills
student["skills"] =["Java", "HTML", "CSS", "Python", "SQL"]
print(student["skills"])
#Get the dictionary keys as a list
print(list(student.keys()))
#Get the dictionary values as a list
print(list(student.values()))


# In[24]:


#3.1 Create a tuple containing names of your sisters and your brothers
sisters = ('srilekha' , 'supriyaa')
brothers = ('siddu','srikanth')
print("sisters = ", sisters, ", brothers = ", brothers)

#3.2 Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers
print("siblings = ", siblings)


#3.3 How many siblings do you have?
siblings_count = len(siblings)
print("siblings_count = ", siblings_count)

#3.4 Modify the siblings tuple and add the name of your father and mother and 
# assign it to family_members
siblings = list(siblings) #converting tuple to list to Modify
siblings.append("ram") #adding father name
siblings.append("kaveri") #adding mother name
family_members = tuple(siblings) #coverting list into tuple again and assingning
print("family_members = ", family_members)


# In[25]:


it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'} 
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
#Find the length of the set it_companies
print(len(it_companies))
#Add 'Twitter' to it_companies
it_companies.add("Twitter")
print(it_companies)
#Insert multiple IT companies at once to the set it_companies
addcomp=["TCS","Infosys"]
it_companies.update(addcomp)
print(it_companies)
#Remove one of the companies from the set it_companies
it_companies.discard("Infosys")
print(it_companies)
#What is the difference between remove and discard
#join A and B
print(A.union(B))
#Find A intersection B
print(A.intersection(B))
#Is A subset of B
subAB= A.issubset(B)
print(subAB)
#Are A and B disjoint sets
print(A.isdisjoint(B))
C=A.union(B)
D=B.union(A)
print(A.symmetric_difference(B))
del it_companies
del A
del B
ages=set(age)
print(type(ages))


# In[26]:


#5.1 Calculate the area of a circle and assign the value to a variable name of _area_of_circle_
radius = 30
pi = 3.141592653589793238
_area_of_circle_ = pi*radius*radius
print("area of circle = ", _area_of_circle_)


#5.2 Calculate the circumference of a circle and assign the value to a variable name of
#_circum_of_circle_
_circum_of_circle_ = 2*pi*radius
print(" _circum_of_circle_ = ", _circum_of_circle_)


#5.3 Take radius as user input and calculate the area
r = int(input("enter radius: "))
print(" area = ", pi*r*r)


# In[27]:


#6 How many unique words have been used in the sentence? Use the split methods and set
#to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people" #given sentence
ans = set(sentence.split(" ")) #splitting the given sentence where there is a space and adding them to set(sets does not have duplicate values so every value is unique).
print("unique words = ", ans)


# In[28]:


print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")


# In[29]:


radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius %d is %d meters square."%(radius, area))


# In[18]:


n=int(input("enter number of students ="))
lbs=[]
kgs=[]
lb=0.453592
for x in range(n):
    #print(x)
    a=int(input("enter weight in lbs:"))
    lbs.append(a)
for y in lbs:
    #print(x)
    b=y*lb
    kgs.append(b)
print(kgs)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[6]:





# In[ ]:





# In[ ]:




