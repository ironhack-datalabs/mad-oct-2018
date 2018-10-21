# codewars

# https://www.codewars.com/kata/insert-dashes
'''
Write a function insertDash(num)/InsertDash(int num) that will insert dashes ('-') between each 
two odd numbers in num. For example: if num is 454793 the output should be 4547-9-3. Don't count 
zero as an odd number.

insert_dash(454793) ->'4547-9-3'

def list_in_to_string(lista): 
    res = ""
    for x in lista: 
        res += str(x)
    return res
'''

def insert_if_needed(n1, n2): 
    res = False
    if n1%2 != 0 and n2%2 != 0: 
        res = True
    return res    

def insert_dash(num):
    res = []
    cad = str(num)
    for i in range(len(cad)-1): 
        res.append(cad[i])
        if insert_if_needed(int(cad[i]), int(cad[i+1])): 
            res.append('-')
    res.append(cad[-1]) 
    print(res)
    return ''.join(res)


# https://www.codewars.com/kata/thinkful-logic-drills-red-and-bumpy/train/python
'''
You're playing a game with a friend involving a bag of marbles. In the bag are ten marbles:

    1 smooth red marble
    4 bumpy red marbles
    2 bumpy yellow marbles
    1 smooth yellow marble
    1 bumpy green marble
    1 smooth green marble

You can see that the probability of picking a smooth red marble from the bag is 1 / 10 or 0.10 
and the probability of picking a bumpy yellow marble is 2 / 10 or 0.20.

The game works like this: your friend puts her hand in the bag, chooses a marble (without looking 
at it) and tells you whether it's bumpy or smooth. Then you have to guess which color it is before 
she pulls it out and reveals whether you're correct or not.

You know that the information about whether the marble is bumpy or smooth changes the probability 
of what color it is, and you want some help with your guesses.

Write a function color_probability() that takes two arguments: a color ('red', 'yellow', or 'green') 
and a texture ('bumpy' or 'smooth') and returns the probability as a decimal fraction accurate to 
two places.

The probability should be a string and should discard any digits after the 100ths place. 
For example, 2 / 3 or 0.6666666666666666 would become the string '0.66'. Note this is different 
from rounding.

As a complete example, color_probability('red', 'bumpy') should return the string '0.57'.
'''

def color_probability(color, texture):
    # Your code goes here.
    PROBABILITIES = {
        'smooth': ['red', 'yellow', 'green'], 
        'bumpy': ['red', 'red', 'red', 'red','yellow', 'yellow', 'green']
    }
    res = PROBABILITIES[texture].count(color)/len(PROBABILITIES[texture])
    return str(int(res*100)/100)


# https://www.codewars.com/kata/weird-matrix-multiplication/train/python

"""
Hello Codewarriors,

In this exercise you will have to multiply 2 numpy matrices (2d numpy arrays) in the following way:

    Take each element of the first matrix and multiply by the second matrix
    Place the resulting matrices in the same order as elements of the first matrix.

Important: use Numpy arrays as input and as output

If arrays with wrong shape (not 2d) or arrays with zero shape (shape=(0, 0)) are passed as an input, 
please return None

Examples:

I. A = [[2]]

B = [[1, 2], [3, 4]]

AB = [[2, 4], [6, 8]]

II. A = [[2, 3]]

B = [[40], [50]]

AB = [[80, 120], [100, 150]]

III. A = [[0, 1], [2, 3]]

B = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]

AB = [[ 0, 0, 0, 1, 1, 1], [ 0, 0, 0, 1, 1, 1], [ 0, 0, 0, 1, 1, 1], [ 0, 0, 0, 1, 1, 1], [ 2, 2, 2, 3, 3, 3], [ 2, 2, 2, 3, 3, 3], [ 2, 2, 2, 3, 3, 3], [ 2, 2, 2, 3, 3, 3]]

IV. A = [[1, 2], [3, 4]]

B = [[10, 20, 30], [40, 50, 60]]

AB = [[ 10, 20, 30, 20, 40, 60], [ 40, 50, 60, 80, 100, 120], [ 30, 60, 90, 40, 80, 120], [120, 150, 180, 160, 200, 240]]
"""

# https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.block.html
import numpy as np
def weird_mul(A, B):
    AB = []
    if 0 in A.shape or 0 in B.shape or A.ndim != 2 or B.ndim != 2: 
        return None
    
    for fila in A: 
        ABfila = []
        for elemento in fila: 
            ABfila.append(elemento*B)  
        ABfila = np.hstack(ABfila)
        AB.append(ABfila)
    AB = np.vstack(AB) 
    return AB

