#1. Import the NUMPY package under the name np.
print("")
print(chr(27)+"[1;4;30m"+"NUMPY LAB"+chr(27)+"[0m"+"")
import numpy as np
print("")
print("  >> Numpy module Loaded")
print("")

#2. Print the NUMPY version and the configuration.
print("")
print(chr(27)+"[1;31m"+"NUMPY version: "+chr(27)+"[0m"+"")
print(np.version.version)
print("")
print("-------------------------")

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?
a=np.random.random((2,3,5))
a1=np.random.randint(-50,50,(2,3,5))
## For a2 we have to import the module string
import string
a2=np.random.choice(list(string.ascii_lowercase),(2,3,5))

#4. Print a.
print("")
print("np.random.random((2,3,5)) in FLoat Format: ")
print(a)
print("")
print("-------------------------")
print("")
print("Way 2 in INT Format: ")
print(a1)
print("")
print("-------------------------")
print("")
print("Way 3 in STRING Format: ")
print(a2)
print("")
print("-------------------------")

#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"
b=np.ones((5,2,3))

#6. Print b.
print("")
print("Ones 3-D Matrix: ")
print(b)
print("")
print("-------------------------")


#7. Do a and b have the same size? How do you prove that in Python code?
if np.size(a)==np.size(b):
        print(chr(27)+"[1;4;32m"+"YES, a and b have the same size    "+u'\u2713'+chr(27)+"[0m"+"") 
        print("But do they have the same shape?")
        if np.shape(a)==np.shape(b):
                print("")
                print(chr(27)+"[1;4;32m"+"YES, a and b have the same shape    "+u'\u2713'+u'\u2713'+chr(27)+"[0m"+"") 
                print("")
        else:
                print("")
                print(chr(27)+"[1;4;34m"+"NOOOOOO! Not the same shape"+chr(27)+"[1;31m"+"  X"+chr(27)+"[0m"+"") 
                print("")
else:
        print("")
        print(chr(27)+"[1;4;31m"+"Not even the same size  "+chr(27)+"[1;31m"+"  XX"+chr(27)+"[0m"+"") 
        print("")


#8. Are you able to add a and b? Why or why not?
if np.shape(a)==np.shape(b):
        print("")
        print(chr(27)+"[1;4;32m"+"You can add them because they have the same shape "+u'\u2713'+chr(27)+"[0m"+"") 
        print("")
        print(np.add(a,b))
else:
        print("")
        print(chr(27)+"[1;4;32m"+"You cannot add them because they have different shapes "+chr(27)+"[0m"+"") 
        print("")


#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".
print(np.shape(a))
print(np.shape(b))
if np.shape(a)==np.shape(np.transpose(b,(1,2,0))):
        c=np.transpose(b,(1,2,0))
        print("")
        print(chr(27)+"[1;4;32m"+"Adding a and b because b transposed has the same shape than a "+u'\u2713'+chr(27)+"[0m"+"") 
        print("")
        print(np.add(a,c))
        print("")
else:
        print("")
        print("Seems like b transposed does not have the same shape than a matrix. c matrix will be filled with 0")
        print("")
        c=np.zeros(np.shape(a))


#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?
print("")
print("10. Adding a to c")
if np.shape(a)==np.shape(c):
        print("")
        print("a and c have the shame shape so we can add them")
        print("")
        print("")
        d=np.add(a,c)
        print(d)
        print("")


#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.
print("")
print("11. Print a and d")
print("")
print(a)
print("")
print(d)
print("")
print("a is equal to a+1 because c (and b) where a ones matrixes")
print("the difference is just a group o ones matrixes")
print("")
print(np.subtract(d,a))
print("")


#12. Multiply a and c. Assign the result to e.
e=np.multiply(a, c)
print("")
print("12. Multiply a and c")
print("")
print(e)
print("")


#13. Does e equal to a? Why or why not?
print("")
print("13. e equal to a? ")
print("")
print(a==e)
print("")
print("e is equal to a because e multiplies a to c, so c is b transposed (b is a ones matrix)")
print("")


#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"
d_max=d.max()
d_min=d.min()
d_mean=d.mean()
print("")
print("14. Max: ",d_max," | Min: ",d_min," | Mean: ",d_mean)
print("")

#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.
f=np.empty(np.shape(d))
print("")
print("15. Empty array f")
print("")
print(f)
print("")


"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""
ff=f.copy()
print("")
print("16. Filling f array")
print("")
for i in range(np.shape(f)[0]):
    for j in range(np.shape(f)[1]):
        for k in range(np.shape(f)[2]):
            value=d[i,j,k]
            if value==d_min:
                f[i,j,k]=0
            if value>d_mean and value<d_max:
                f[i,j,k]=75
            if value==d_mean:
                f[i,j,k]=50
            if value==d_max:
                f[i,j,k]=100
            if value>d_min and value<d_mean:
                f[i,j,k]=25
print(f)
print("")

# There is also another way to obtain the same result
# using booleans arrays
f=ff
f[d==d_min]=0.0
f[d==d_max]=100.0
f[(d<d_mean)==(d>d_min)]=25.0
f[(d<d_max)==(d>d_mean)]=75.0
f[d==d_max]=100.0
print("")
print(f)
print("")

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
print("")
print("17. Printing d and f")
print("")
print(d)
print("")
print(f)
print("")
print("Min: ",d_min," | Max: ",d_max," | Mean: ",d_mean)
print("")


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
<<<<<<< HEAD
"""

# For his question we are going to use booleans arrays
f=f.astype(str)
f[f=='0.0']='A'
f[f=='25.0']='B'
f[f=='50.0']='C'
f[f=='75.0']='D'
f[f=='100.0']='E'
print("")
print("18. Bonus question")
print("")
print(f)
print("")
=======
"""
>>>>>>> e8c15488c1249b8cb82864ac797a4a8ed1d50c6a
