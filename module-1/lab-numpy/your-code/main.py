#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1. Import the NUMPY package under the name np.
import numpy as np


# In[2]:


#2. Print the NUMPY version and the configuration.

# version
print(np.__version__)


# In[3]:


# configuration
print(np.__config__.show())


# In[4]:


#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?
a = np.random.random((2, 3, 5))
print(a)


# In[5]:


a = np.random.randint(5, size=(2, 3, 5))
print(a)


# In[6]:


a = np.random.rand(2, 3, 5)
print(a)


# In[7]:


#4. Print a.
print(a)


# In[8]:


#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"
b = np.random.random((5, 2, 3)) # está mal. hay que usar np.ones((5, 2, 3))


# In[9]:


#6. Print b.
print(b)


# In[10]:


#7. Do a and b have the same size? How do you prove that in Python code?

'''
Yes
'''
print(a.size == b.size)


# In[11]:


#8. Are you able to add a and b? Why or why not?

'''
No
a dimension is different than b dimension
'''
print(a.shape == b.shape)


# In[12]:


print(a.shape)


# In[13]:


print(b.shape)


# In[14]:


#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

# https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.transpose.html
# seleccionamos el orden de las dimensiones
c = b.transpose(1, 2, 0)
print(c.shape)


# In[15]:


print(a.shape)


# In[16]:


#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?
'''
Sí
'''
d = np.add(a, c)
print(d)


# In[17]:


#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.
'''
values in a are between (0, 1)
values in d are between (0, 2) because its values are sum from random values between (0, 1) 
2 x (0, 1) = (0, 2)
'''
print(a)


# In[18]:


print(d)


# In[19]:


#12. Multiply a and c. Assign the result to e.
e = np.multiply(a, c)
print(e)


# In[20]:


#13. Does e equal to a? Why or why not?
'''
e is not equal to a. 
the only way e would be equal to a would be if one of them were a matrix composed only by 1's
'''
print(e == a)


# In[21]:


#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"
d_max = np.amax(d)
d_min = np.amin(d)
d_mean = np.mean(d)
print(d_max, d_min, d_mean)


# In[22]:


#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

f = np.empty([2, 3, 5])
print(f)


# In[23]:


"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""

'''
# https://docs.scipy.org/doc/numpy-1.15.0/reference/arrays.nditer.html
for fi, di in zip(np.nditer(f), np.nditer(d)):
    print(fi, di)
    if di == d_max: 
        fi = 100
    elif di == d_min: 
        fi = 0
    elif di == d_mean: 
        fi = 50
    elif d_mean > di > d_min: 
        fi = 25
    else: 
        fi = 75
'''

f[d == d_max] = 100.
f[(d<d_max)==(d>d_mean)] = 75.
f[d == d_mean] = 50.
f[(d<d_mean)==(d>d_min)] = 25.
f[d == d_min] = 0.

'''
f[d==d_min]=0.0
f[d==d_max]=100.0
f[(d<d_mean)==(d>d_min)]=25.0
f[(d<d_max)==(d>d_mean)]=75.0
f[d==d_max]=100.0
'''
print(f)


# In[24]:



"""
#17. Print d and f. Do you have your expected f?
For instance, if your d is:
array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

Your f should be:
array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],

       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])
"""
'''
I get what is expected
'''
print(d), print(f)


# In[25]:


"""
#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
Again, you don't need Numpy in this question.
"""
DIC = {0.: "A", 
       25.: "B", 
       50.: "C", 
       75.: "D", 
       100.: "E"}

res = []

for x in np.nditer(d): 
    # print(f[i, j, k])
    if x == d_max: 
        res.append(DIC[100.])
    elif x == d_min: 
        res.append(DIC[0.])
    elif x == d_mean: 
        res.append(DIC[50.])
    elif d_mean >x > d_min: 
        res.append(DIC[25.])
    else: 
        res.append(DIC[75.])

f = np.array(res).reshape((2, 3, 5))
print(f)
    

