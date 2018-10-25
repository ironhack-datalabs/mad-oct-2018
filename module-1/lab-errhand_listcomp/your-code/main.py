#Example: 

eggs = (1,3,8,3,2)

my_listComprehension = [1/egg for egg in eggs]

print(my_listComprehension)

#Insert here the module/library import statements 

import os,random,sys


#1. Calculate the square number of the first 20 numbers. Use square as the name of the list.
# Remember to use list comprehensions and to print your results

square=[e**2 for e in range(20)]
print(square)


#2. Calculate the first 50 power of two. Use power_of_two as the name of the list.
# Remember to use list comprehensions and to print your results

power_of_two=[2**e for e in range(50)]
print(power_of_two)


#3. Calculate the square root of the first 100 numbers. Use sqrt as the name of the list.
# You will probably need to install math library with pip and import it in this file.  
# Remember to use list comprehensions and to print your results

sqrt=[e**0.5 for e in range(100)]
print(ssqrt)


#4. Create this list [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0]. Use my_list as the name of the list.
# Remember to use list comprehensions and to print your results

my_list=[e-10 for e in range(11)]
print(my_list)


#5. Find the odd numbers from 1-100. Use odds as the name of the list. 
# Remember to use list comprehensions and to print your results

odds=[e for e in range(1,101) if e%2!=0]
print(odds)


#6. Find all of the numbers from 1-1000 that are divisible by 7. Use divisible_by_seven as the name of the list.
# Remember to use list comprehensions and to print your results

divisible_by_7=[e for e in range(1,1001) if e%7==0]
print(divisible_by_7)


#7. Remove all of the vowels in a string. Hint: make a list of the non-vowels. Use non_vowels as the name of the list.
# Remember to use list comprehensions and to print your results
# You can use the following test string but feel free to modify at your convenience

teststring = 'Find all of the words in a string that are monosyllabic'
non_voewls=''.join([e for e in teststring if e not in 'aeiouAEIOU'])
print(non_voewls)


#8. Find the capital letters (and not white space) in the sentence 'The Quick Brown Fox Jumped Over The Lazy Dog'. 
# Use capital_letters as the name of the list.  
# Remember to use list comprehensions and to print your results

str_cap='The Quick Brown Fox Jumped Over The Lazy Dog'
capital_letters=[e for e in str_cap if e.isupper()]
print(capital_letters)


#9. Find all the consonants in the sentence 'The quick brown fox jumped over the lazy dog'.
# Use consonants as the name of the list.
# Remember to use list comprehensions and to print your results.

str_cons='The quick brown fox jumped over the lazy dog'
consonants=''.join([e for e in str_cons if not e in 'aeiouAEIOU'])
print(consonants)


#10. Find the folders you have in your madrid-oct-2018 local repo. Use files as name of the list.  
# You will probably need to import os library and some of its modules. You will need to make some online research.
# Remember to use list comprehensions and to print your results.

files=[e for e in os.listdir('../../../') if os.path.isdir(os.path.join('../../../',e))]
print(files)


#11. Create 4 lists of 10 random numbers between 0 and 100 each. Use random_lists as the name of the list. 
#You will probably need to import random module
# Remember to use list comprehensions and to print your results

random_lists=[random.sample(range(1, 100), 10) for f in range(4)]
print(random_lists)


#12. Flatten the following list of lists. Use flatten_list as the name of the output.
# Remember to use list comprehensions and to print your results

list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]
flatten_list=[y for x in list_of_lists for y in x]
print(flatten_list)


#13. Convert the numbers of the following nested list to floats. Use floats as the name of the list. 
# Remember to use list comprehensions and to print your results.

list_of_lists = [['40', '20', '10', '30'], ['20', '20', '20', '20', '20', '30', '20'], \
['30', '20', '30', '50', '10', '30', '20', '20', '20'], ['100', '100'], ['100', '100', '100', '100', '100'], \
['100', '100', '100', '100']]

floats=[[float(y) for y in x] for x in list_of_lists]
print(floats)


#14. Handle the exception thrown by the code below by using try and except blocks. 

for i in ['a','b','c']:
    try:
        print(i**2)
    except Exception as e:
        print(e)


#15. Handle the exception thrown by the code below by using try and except blocks. 
#Then use a finally block to print 'All Done.'
# Check in provided resources the type of error you may use. 

x = 5
y = 0
try:
    z = x/y
except Exception as e:
    print(e)


#16. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 

abc=[10,20,20]
try:
    print(abc[3])
except Exception as e:
    print(e)


#17. Handle at least two kind of different exceptions when dividing a couple of numbers provided by the user. 
# Hint: take a look on python input function. 
# Check in provided resources the type of error you may use. 

def division_x(a,b):
    if (type(a)!=str and type(b)!=str) and b!=0:
        return(a/b)
    elif (type(a)==str or type(b)==str):
        print("Error: a and b must be float or int type")
    elif b==0:
        print("Error: b must be major than 0")

division_x('a',5)

division_x(5,'a')

division_x(5,0)


#18. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 

try:
    f = open('testfile','r')
    f.write('Test write this')
except Exception as e:
    print(e)


#19. Handle the exceptions that can be thrown by the code below using try and except blocks. 
#Hint: the file could not exist and the data could not be convertable to int

try:
    fp = open('myfile.txt')
    line = f.readline()
    i = int(s.strip())
except Exception as e:
    print(e)


#20. The following function can only run on a Linux system. 
# The assert in this function will throw an exception if you call it on an operating system other than Linux. 
# Handle this exception using try and except blocks. 
# You will probably need to import sys 

def linux_interaction():
    try:
        assert ('linux' in sys.platform), "Function can only run on Linux systems."
        print('Doing something.')
        print('Everything is fine, You do not have any WINDOWS virus in your OS')
    except Exception as e:
        print(e)
        print("RUN FOR YOUR LIFE!")


# Bonus Questions:

# You will need to make some research on dictionary comprehension to solve the following questions

#21.  Write a function that asks for an integer and prints the square of it. 
# Hint: we need to continually keep checking until we get an integer.
# Use a while loop with a try,except, else block to account for incorrect inputs.

def function_square_integer(counter=0):
    while 1:
        print("--------------------------------------------------")
        counter+=1
        integer=input('Iteration %s | Define the integer you want to obtain its square: ' %counter)
        try:
            int(float(integer))
        except:
            print("")
            print("FUNCTION DOES NOT ACCEPT STR FORMAT!")
            print("")
        else:
            try:
                if int(float(integer))!=float(integer):
                    raise TypeError
            except TypeError:
                print("")
                print("You must define the input as INT type")
                print()
                print("Your actual data type is: ",type(float(integer)))
                print("")
            else:
                return int(integer)**2
                break


# 22. Find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9). 
# Use results as the name of the list 

results=[]
for f in range(1,1001):
    # we make a list of the digits that the number f is divisible for
    g=['' if f%e!=0 else e for e in range(2,10)]
    # Define a counter for digits different to ''
    count=0
    for item in g:
        if item!='':
            count+=1
    if count!=0:
        results.append(f)


# 23. Define a customised exception to handle not accepted values. 
# You have the following user inputs and the Num_of_sections can not be less than 2.
# Hint: Create a class derived from the pre-defined Exception class in Python

class HowManyTimesHaveToExplainThatINTisMandatory(Exception):
   """Why the hell you keep trying inputing values types different from INT?"""
   pass

###########################################################

try:
    Total_Marks = int(input("Enter Total Marks Scored: ")) 
    Num_of_Sections = int(input("Enter Num of Sections: "))
except:
    #print(HowManyTimesHaveToExplainThatINTisMandatory(Exception))
    print("Why the hell you keep trying inputing values types different from INT?")