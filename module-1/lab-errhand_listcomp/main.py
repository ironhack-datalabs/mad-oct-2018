#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Example: 

eggs = (1,3,8,3,2)

my_listComprehension = [1/egg for egg in eggs]

print(my_listComprehension)


# In[74]:


#Insert here the module/library import statements 
import math, os, pandas as pd, random as rd, sys


# In[3]:


#1. Calculate the square number of the first 20 numbers. Use square as the name of the list.
# Remember to use list comprehensions and to print your results
square = [e*e for e in range(1,11)]
print(square)


# In[4]:


#2. Calculate the first 50 power of two. Use power_of_two as the name of the list.
# Remember to use list comprehensions and to print your results
power_of_two = [2**e for e in range(1,51)]
print(power_of_two)


# In[5]:


#3. Calculate the square root of the first 100 numbers. Use sqrt as the name of the list.
# You will probably need to install math library with pip and import it in this file.  
# Remember to use list comprehensions and to print your results
sqrt = [math.sqrt(e) for e in range(1,101)]
print(sqrt)


# In[6]:


#4. Create this list [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0]. Use my_list as the name of the list.
# Remember to use list comprehensions and to print your results
# my_list = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0]
my_list = [e for e in range(-10, 1)]
print(my_list)


# In[7]:


#5. Find the odd numbers from 1-100. Use odds as the name of the list. 
# Remember to use list comprehensions and to print your results
odds = [e for e in range(1, 101, 2)]
print(odds)


# In[8]:


#6. Find all of the numbers from 1-1000 that are divisible by 7. Use divisible_by_seven as the name of the list.
# Remember to use list comprehensions and to print your results
divisible_by_seven = [e for e in range(7, 1001, 7)]
print(divisible_by_seven)


# In[9]:


#7. Remove all of the vowels in a string. Hint: make a list of the non-vowels. Use non_vowels as the name of the list.
# Remember to use list comprehensions and to print your results
# You can use the following test string but feel free to modify at your convenience
teststring = 'Find all of the words in a string that are monosyllabic'
non_vowels = [e for e in teststring if e not in ('a', 'e', 'i', 'o', 'u')]
stNV = "".join(str(i) for i in non_vowels)
print(stNV)

#I have removed them but left a space,


# In[10]:


#8. Find the capital letters (and not white space) in the sentence 'The Quick Brown Fox Jumped Over The Lazy Dog'. 
# Use capital_letters as the name of the list.  
# Remember to use list comprehensions and to print your results


# In[11]:


sentence = 'The Quick Brown Fox Jumped Over The Lazy Dog'
capital_letters = [e for e in sentence if i.isupper()]
print(capital_letters)


# In[12]:


#9. Find all the consonants in the sentence 'The quick brown fox jumped over the lazy dog'.
# Use consonants as the name of the list.
# Remember to use list comprehensions and to print your results.
sentence = 'The quick brown fox jumped over the lazy dog'
consonants = [i for i in sentence if i not in ('a', 'e', 'i', 'o', 'u', ' ')] #últimas comillas para remover espacio
print(consonants)


# In[13]:


#10. Find the folders you have in your madrid-oct-2018 local repo. Use files as name of the list.  


# In[14]:


# Enter pwd in the terminal first to make sure what is your actual path:
[e for e in os.listdir('../../../') if os.path.isdir(os.path.join('../../../', e)) ]


# In[15]:


# Otras formas (quitar triple comillas para probarlas):

"""
# De la forma siguiente salen listados los directorios enteros, con sus padres, abuelos, suegros y cuñaos: 
files = [x for x in os.walk("/home/cmv/Desktop/IronHack/madrid-oct-2018")]
# Aparecen como tuplas de 3 elem, el primero de los cuales es el directorio desde la raíz. 

# Para que aparezca sólo el directorio seleccionamos el primer elem de la tupla:
files = [x[0] for x in os.walk("/home/cmv/Desktop/IronHack/madrid-oct-2018")]
print (files)
"""


# In[16]:


"""
# Problemática a explorar 1:
# Esto lo mete Arie y a él le funciona, pero a mí me da Invalid character in identifier, tanto en la barra de slash como poniendo
# /Users/cmv,    /home/cmv-UX430UAR ... quitando el slash y sus combinaciones. . 

path = “/home/cmv/Desktop/IronHack/madrid-oct-2018”
files = [p for p in os.listdir(path)]
print(files)
"""


# In[17]:


"""
# A explorar 2: 

for dirname, dirnames, filenames in os.walk('.'):
    # print path to all subdirectories first.
    for subdirname in dirnames:
        print(os.path.join(dirname, subdirname))    
"""


# In[18]:


"""
# A explorar 3:

for subdirname in dirnames:
    print(os.path.join(dirname, subdirname))
    dir_path = os.path.dirname(os.path.realpath(__file__))
"""


# In[19]:


#11. Create 4 lists of 10 random numbers between 0 and 100 each. Use random_lists as the name of the list. 
## random.sample generates a list 
for i in range(0, 4): 
    random_lists = [e for e in rd.sample(range(0, 101), 10)]
    print(random_lists)


# In[20]:


"""
## Also, without CL: 
random_lists = [rd.randrange(1, 101) for i in range(10)]
print(my_randoms)
"""


# In[21]:


"""
## Both approaches cannot be combined: 
random_lists = [e for e in rd.randrange(0, 101), 10]
print(my_randoms)
"""


# In[23]:


#12. Flatten the following list of lists. Use flatten_list as the name of the output.
# Remember to use LCs and to print your results

list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]
flatten_list=[]
for i in range(0, 3): # or in list_of_lists
    flatten_list += [e for e in list_of_lists[i]]
print(flatten_list)


# In[65]:


#13. Convert the numbers of the following nested list to floats. Use floats as the name of the list. 
# Remember to use list comprehensions and to print your results.

list_of_lists = [['40', '20', '10', '30'], ['20', '20', '20', '20', '20', '30', '20'], ['30', '20', '30', '50', '10', '30', '20', '20', '20'], ['100', '100'], ['100', '100', '100', '100', '100'], ['100', '100', '100', '100']]
##> \ means you can go to a new line in your source code but have no effect on the program. \n means produce a new line as a character in a string.

""" list assignment index out of range. Why?
floats=[]
# for i in range(0, 6):
floats[0] = [float(e) for e in list_of_lists[0]]
print(floats)
# floats[0] = [float(e) for e in list_of_lists[i]]
#     print(list_of_lists[i]) #test
# print(floats)
"""

##> Or for a larger list that I don't want to count:
count = 0
for i in list_of_lists:
    floats[count] = [float(e) for e in list_of_lists[0]]
    count += 1
print(floats)

    


# In[71]:


#14. Handle the exception thrown by the code below by using try and except blocks. 
for i in ['a','b','c']:
    try:
        print i**2
    except:
        print("the function errored out")  
##> It is a syntax error. Maybe those have priority over try/except?


# In[72]:


#15. Handle the exception thrown by the code below by using try and except blocks. 
#Then use a finally block to print 'All Done.'
# Check in provided resources the type of error you may use. 

x = 5
y = 0

try:
    z = x/y
except: 
    print("Value error")
finally:
    print("All Done")


# In[73]:


#16. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 

abc=[10,20,20]
try:
    print(abc[3])
except: 
    print("Key error: Index out of bound")


# In[66]:


#17. Handle at least two kind of different exceptions when dividing a couple of numbers provided by the user. 
# Hint: take a look on python input function. 
# Check in provided resources the type of error you may use. 

x = input("Introduce the numerator")
y = input("Introduce the denominator")

if y==0  
    raise ValueError("Denominator can't be a cero")
else if math.isnan(x) or marth.isnan(y)
    raise TypeError("input has to be a number")
else: 
    print(x/y)


# In[66]:


#18. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 
try:
    f = open('testfile','r')
    f.write('Test write this')
except:
    print("IOError: file not found")
    


# In[66]:


#19. Handle the exceptions that can be thrown by the code below using try and except blocks. 
#Hint: the file could not exist and the data could not be convertable to int

try:
    fp = open('myfile.txt')
        line = f.readline()
        i = int(s.strip())
except:
    print("IOError")
    


# In[66]:


#20. The following function can only run on a Linux system. 
# The assert in this function will throw an exception if you call it on an operating system other than Linux. 
# Handle this exception using try and except blocks. 
# You will probably need to import sys 

def linux_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    print('Doing something.')


# Bonus Questions:

# You will need to make some research on dictionary comprehension to solve the following questions

#21.  Write a function that asks for an integer and prints the square of it. 
# Hint: we need to continually keep checking until we get an integer.
# Use a while loop with a try,except, else block to account for incorrect inputs.




# 22. Find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9). 
# Use results as the name of the list 




# 23. Define a customised exception to handle not accepted values. 
# You have the following user inputs and the Num_of_sections can not be less than 2.
# Hint: Create a class derived from the pre-defined Exception class in Python

Total_Marks = int(input("Enter Total Marks Scored: ")) 
Num_of_Sections = int(input("Enter Num of Sections: "))

