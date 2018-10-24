"""
I'm using ##---> to differentiate my comments from the assigments. 
Unless the code is useful for testing correctedness, in which case I leave it as ## 
When the question requires a verbal response, it is written between three '"'
"""

#1. Import the NUMPY package under the name np.
import numpy as np
## np.__version__ 

#2. Print the NUMPY version and the configuration.
print(np.version.version)
print('\n')
numpy.__config__


#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
a = np.random.random((2, 3, 5))

# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?
##---> RAND creates the array from given numbers inside the function
##---> aX names have been given for clarity to not interfere with the code
a2 = np.random.rand(2, 3, 5)

##---> sample([size]) 
a3 = np.random.random_sample((2, 3, 5))

a4 = np.random.ranf((2, 3, 5))

a5 = np.random.sample((2, 3, 5))

## tb randint (indicar hasta qué número)

#4. Print a.
print(a)
## print('\n\n')
## print(a2)
## print('\n\n')
## print(a3) 
## print('\n\n')
## print(a4)
## print('\n\n')
## print(a5)
print('\n')


#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"
b = np.ones((5, 2, 3)) 


#6. Print b.
print(b)
print('\n')


#7. Do a and b have the same size? How do you prove that in Python code?
print(a.size == b.size)
"""
Sí es verdad
"""
print('\n')

#8. Are you able to add a and b? Why or why not?
"""
Sip porque tienen el mismo tamaño. Se usasuman los elemntos como en un array normal. 
Se puede hacer con la función sum()
"""


#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".
##---> a is of shape (2, 3, 5), b shape is (5, 2, 3)
##---> We need to make axe 1 to 0, 2 to 1 and 0 to 3:
c = np.transpose(b, (1, 2, 0))
print('a= \n', a, '\n')
print('b= \n', b, '\n')
print('c= \n', c, '\n')


#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". 
##--> If we were asked for a total sum of the elements 
## (but I assume we are not, just that I saw somewhere that we had to use the sum fn: 
## d = np.sum((a, c))
## print('d= \n', d, '\n')

# But what we want is another array, so no sum fn here: 
d = a + c
print('d= \n', d, '\n')
##---> Works. 


#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.
print('a= \n', a, '\n')
print('d= \n', d, '\n')

##---> We are just adding 1 to each element, as d has been created with the `one` fn. 


#12. Multiply a and c. Assign the result to e.
e = a * c


#13. Does e equal to a? Why or why not?
print('a= \n', a, '\n')
print('c= \n', c, '\n')
print('e= \n', e, '\n')
e == a

##---> `a = e` because we are just multiplying `a` by one.


#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"
d_max, d_min, d_mean = np.amax(d), np.amin(d), np.mean(d)
d_max, d_min, d_mean
## print(d_max, d_min, d_mean)

#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.
f = np.empty((2, 3, 5))
##---> Use it with caution, as it doesn't initialze the values (unlike np.ceros)
##---> In Jupyter f takes the values of the previous array!
## print(f)



#16. Populate the values in f.
f = np.random.rand(2, 3, 5)

# For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
# If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
# If a value equals to d_mean, assign 50 to the corresponding value in f.
# Assign 0 to the corresponding value(s) in f for d_min in d.
# Assign 100 to the corresponding value(s) in f for d_max in d.
# In the end, f should have only the following values: 0, 25, 50, 75, and 100.
# Note: you don't have to use Numpy in this question.

f[d > d_mean] = 75
f[d < d_mean] = 25
f[d == d_min] = 0
f[d == d_mean] = 50
f[d == d_max] = 100

##---> No need to remove min, mean, and max values of the first two comparisons 
## as those values are assigned later - they will overwrite any previous given value


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
print('d= \n', d,'\n\n', 'f= \n', f)


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

##---> Tested options in Jupyter but none of them work. 

f[d > d_mean] = 'D'
f[d < d_mean] = 'B'
f[d == d_min] = ''
f[d == d_mean] = 50
f[d == d_max] = 100
