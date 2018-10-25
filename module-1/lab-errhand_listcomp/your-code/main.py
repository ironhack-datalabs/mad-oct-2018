# #Example:
#
# eggs = (1,3,8,3,2)
#
# my_listComprehension = [1/egg for egg in eggs]
#
# print(my_listComprehension)

#Insert here the module/library import statements 
import numpy as np



#1. Calculate the square number of the first 20 numbers. Use square as the name of the list.
# Remember to use list comprehensions and to print your results
square = [i**2 for i in range(20)]
print(square)



#2. Calculate the first 50 power of two. Use power_of_two as the name of the list.
# Remember to use list comprehensions and to print your results
power_of_two = [2**i for i in range(50)]
print(power_of_two)


#3. Calculate the square root of the first 100 numbers. Use sqrt as the name of the list.
# You will probably need to install math library with pip and import it in this file.
# Remember to use list comprehensions and to print your results
sqrt = [np.sqrt(i) for i in range(100)]
print(sqrt)




#4. Create this list [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0]. Use my_list as the name of the list.
# Remember to use list comprehensions and to print your results
my_list = [i for i in range(-10,1)]
print(my_list)



#5. Find the odd numbers from 1-100. Use odds as the name of the list.
# Remember to use list comprehensions and to print your results
odds = [i for i in range(1,100,2)]
print(odds)


#6. Find all of the numbers from 1-1000 that are divisible by 7. Use divisible_by_seven as the name of the list.
# Remember to use list comprehensions and to print your results
divisible_by_seven = [i for i in range(1,1000) if i%7 == 0]
print(divisible_by_seven)



#7. Remove all of the vowels in a string. Hint: make a list of the non-vowels. Use non_vowels as the name of the list.
# Remember to use list comprehensions and to print your results
# You can use the following test string but feel free to modify at your convenience
vowels = ["a","e","i","o","u"]
teststring = 'Find all of the words in a string that are monosyllabic'
without_vowels = [i for i in teststring if i not in vowels]
with_out_vowels = "".join(without_vowels)
print(with_out_vowels)



#8. Find the capital letters (and not white space) in the sentence 'The Quick Brown Fox Jumped Over The Lazy Dog'.
# Use capital_letters as the name of the list.
# Remember to use list comprehensions and to print your results
teststring2 = 'The Quick Brown Fox Jumped Over The Lazy Dog'
Capital_letters = [i for i in teststring2 if i.isupper()]
print(Capital_letters)


#9. Find all the consonants in the sentence 'The quick brown fox jumped over the lazy dog'.
# Use consonants as the name of the list.
# Remember to use list comprehensions and to print your results.
teststring3 = 'The quick brown fox jumped over the lazy dog.'
consonants = set([i for i in teststring3 if i not in vowels])
print(consonants)


#10. Find the folders you have in your madrid-oct-2018 local repo. Use files as name of the list.
# You will probably need to import os library and some of its modules. You will need to make some online research.
# Remember to use list comprehensions and to print your results.
import os
path = "/Users/arie/Desktop/IronHack/Repositorio Ejercicios 1  /madrid-oct-2018"
files = [p for p in os.listdir(path)]
print(files)


#11. Create 4 lists of 10 random numbers between 0 and 100 each. Use random_lists as the name of the list.
#You will probably need to import random module
# Remember to use list comprehensions and to print your results
import random


random_list = [(random.sample(range(0, 100), 10)) for i in range(4)]
print(random_list)



#12. Flatten the following list of lists. Use flatten_list as the name of the output.
# Remember to use list comprehensions and to print your results

list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]
flatten_list = [e2 for e1 in list_of_lists for e2 in e1]
print(flatten_list)



#13. Convert the numbers of the following nested list to floats. Use floats as the name of the list.
# Remember to use list comprehensions and to print your results.

list_of_lists = [['40', '20', '10', '30'], ['20', '20', '20', '20', '20', '30', '20'], \
['30', '20', '30', '50', '10', '30', '20', '20', '20'], ['100', '100'], ['100', '100', '100', '100', '100'], \
['100', '100', '100', '100']]

floats = [list(map(float,e)) for e in list_of_lists]
print(floats)


#14. Handle the exception thrown by the code below by using try and except blocks.
for i in ['a','b','c']:
    try:
        print (i**2)
    except:
        print("a,b and c must be an integer or a float")



#15. Handle the exception thrown by the code below by using try and except blocks.
#Then use a finally block to print 'All Done.'
# Check in provided resources the type of error you may use.

x = 5
y = 0
try:
    z = x/y
except:
    print("el valor en el denominador no puede ser 0")



#16. Handle the exception thrown by the code below by using try and except blocks.
# Check in provided resources the type of error you may use.

abc=[10,20,20]
try:
    print(abc[3])
except IndexError:
    print("el valor indicado esta fuera del indice, recuerde que la primera posicion es 0")



#17. Handle at least two kind of different exceptions when dividing a couple of numbers provided by the user.
# Hint: take a look on python input function.
# Check in provided resources the type of error you may use.

numerador = input("Introduce el numerador : ")
denominador = input("Introduce otro denominador: ")

try:
    numerador/denominador

except ValueError:
    print("El denominador tiene que ser distinto a 0")

except TypeError :
    print("El valor que se inserte debe ser un int o un float ")

#18. Handle the exception thrown by the code below by using try and except blocks.
# Check in provided resources the type of error you may use.

try:
    f = open('testfile','r')
    f.write('Test write this')

except FileNotFoundError :
    print("No existe ningun directorio con nombre 'testfile' ")


#19. Handle the exceptions that can be thrown by the code below using try and except blocks.
#Hint: the file could not exist and the data could not be convertable to int

try:
    f = open('myfile.txt')
except:
    print("No existe ningun archivo llamado 'myfile'")
try:
    line = f.readline()
    i = int(s.strip())
except:
    print("Los strings no se pueden convertir a tipo int, verificar aparte que la variable a la que se "
    
    "le esta aplicando el metodo exista")


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

def cuadrado():

    input_e = input("Introduzca un numero entero para calcular el cuadrado de el: ")
    try:
        input_e ** 2
    except:
        print("Debes introducir un numero entero")
    while type(input_e) != "int":
        input_e = input("Introduzca un numero entero para calcular el cuadrado de el: ")
        input_e =

cuadrado()
# # 22. Find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9).
# # Use results as the name of the list
#
#
#
#
# # 23. Define a customised exception to handle not accepted values.
# # You have the following user inputs and the Num_of_sections can not be less than 2.
# # Hint: Create a class derived from the pre-defined Exception class in Python
#
# Total_Marks = int(input("Enter Total Marks Scored: "))
# Num_of_Sections = int(input("Enter Num of Sections: "))
#
#
