#Author: Adrian LaCour
#Date: 9/26/2018
#Description: This program takes in a lambda term and displays it as a tree
#Usage: To run the program, execute the script, and then type
#       test("x"), where x is the tuple expression.
#       Example: test(l(l(a(a(0,l(3)),a(l(0),0)))))


#The lambda functions help to change the input expression into a tree nested tuple
def l(x) : return ('l',x)

def a(x,y) : return ('a',x,y)

#Change the nested tuples into a nested list
def listIt(inputTuple):
    return list(map(listIt, inputTuple)) if isinstance(inputTuple, (list, tuple)) else inputTuple

#casts all of the list variables as type str, for use in printing
def castList(x):
     if isinstance(x, list):
         return list(map(castList, x))
     else:
         return str(x)

#Print out the given input, as it has already been converted into an usable format
def printList(inputList, level = 0):
    print('    ' * (level - 1) + '|___' * (level > 0) + inputList[0])
    for l in inputList[1:]:
        if type(l) is list:
            printList(l, level + 1)
        else:
            print('    ' * level + '|___' + l)

#Test function to run the program
def test(n):
    inputTuple = n
    inputList = listIt(inputTuple)
    inputList = castList(inputList)
    printList(inputList)
