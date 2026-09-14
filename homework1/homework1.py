# File: homework1.py

# Variables and Data Types
a = 10
print(a)
print(type(a)) # a is an integer

b = 1.5
print(b)
print(type(b)) # b is a floating point number

c = 3j
print(c)
print(type(c)) # c is an imaginary (and complex) number

d = "hello" 
print(d)
print(type(d)) # d is a string

e = [1, 2, 3]
print(e)
print(type(e)) # e is a list/array, which is a collection of data types

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) # f is a dictionary, 

g = (1, 2)
print(g)
print(type(g)) # g is a tuple, which is an immutable collection of data types

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) # h is a list/array

i = True
print(i)
print(type(i)) # i is a boolean, true or false value

f = None
print(f)
print(type(f)) # f is a NoneType, a special empty data type

k = [True, "blue", 12]
print(k)
print(type(k)) # k is a list/array

l = str(14)
print(l)
print(type(l)) # l is a string

m = 1e4
print(m)
print(type(m)) # m is a floating point number

'''
1. How many different data types did you find?

    8 data types: integer, float, complex, string, list/array, dictionary, tuple, boolean, NoneType

2. List all the data types you found.

    integer, float, complex, string, list/array, dictionary, tuple, boolean, NoneType

3. What variables have the same data types?

    b and m are both floats, e, h, and k are lists/arrays, and d and l are strings.

4. What was the data type of l? Why is it not an integer? What does str() do?

    l is a string because str(x) takes the input x and converts it to a string, regardless of data type.

5. Look up one more data type not given above. Repeat the same procedure.

'''

set = {a, b, c}
print(set)
print(type(set)) # set is a set, which is an unordered collection of data types

#Booleans
print(10 > 9) # True, 10 is greater than 9
print(10 == 9) # False, 10 does not equal 9
print(10 <= 9) # False, 10 is not less than or equal to 9
print(bool("abc")) # True, the boolean values of some non-empty data types are True. String is non-empty.
print(bool(123)) # True, Integer is non-empty
print(bool(["apple", "cherry", "banana"])) # True, list is non-empty
print(bool(True)) # True, True is truthy
print(bool(False)) # False, False is falsy
print(bool(0)) # False, 0 is falsy
print(bool("")) # False, empty string is falsy
print(bool(" ")) # True, non-empty string is truthy
print(bool(())) # False, empty tuple is falsy
print(bool([])) # False, empty list is falsy
print(bool({})) # False, empty set is falsy
print(bool(True and False)) # False, and requires both values to be True
print(bool(True and True)) # True, and requires both values to be True
print(bool(False and False)) # False, and requires both values to be True
print(bool(True or False)) # True, or requires at least one value to be True
print(bool(True or True)) # True, or requires at least one value to be True
print(bool(False or False)) # False, or requires at least one value to be True
print(bool(not(False))) # True, not negates the boolean value. The negation of false is true
print(bool(not(True))) # False, the negation of true is false

'''
1. What pattern do you notice about expressions returning True or False?

Empty data types are falsy, while non-empty data types are truthy. Otherwise, booleans obey normal logic.

2. Which expression surprised you about its result?

At frist, the empty data types being fasly surprised me since it is a bit of a nuance.

'''

# 3. Create an expression, not given above, that will return True. Why is it True?

print(bool(2j)) # True, 2j is a non-empty complex number, which is truthy

# 4. Create an expression, not given above, that will return False. Why is it False?

print(bool(None)) # False, None is falsy

#Operators

#3.3.1 Arithmetic Operators
print(10 + 5) # adds 10 and 5, returns 15
print(10 - 5) # subtracts 5 from 10, returns 5
print(2 * 4) # multiplies 2 and 4, returns 8
print(6 / 3) # divides 6 by 3, returns 2.0, as a floating point number
print(5 % 2) # returns the remainder of 5 divided by 2, which is 1
print(3 ** 2) # raises 3 to the power of 2, returns 9
print(15 // 2) # divides 15 by 2 and returns the integer part of the result, which is 7

#3.3.2 Comparison Operators
print(5 == 2) # checks if 5 is equal to 2, returns False
print(10 != 10) # checks if 10 is not equal to 10, returns False
print(2 < 5) # checks if 2 is less than 5, returns True
print(12 > 5) # checks if 12 is greater than 5, returns True
print(5 <= 6) # checks if 5 is less than or equal to 6, returns True
print(1 >= 10) # checks if 1 is greater than or equal to 10, returns False

#3.3.3 Assignment Operators
x = 5
print(x)
x += 5 # adds 5 to x and assigns the result to x
print(x)
x -= 4 # subtracts 4 from x and assigns the result to x
print(x)
x *= 3 # multiplies x by 3 and assigns the result to x
print(x)

#3.3.4 Logical Operators
#1. What does the operator and do? Write an expression that results in True. Write an expression that results in False.
# The and operator returns True if both expressions are True, and False otherwise.
print(True and True)
print(True and False)

#2. What does the operator or do? Write an expression that results in True. Write an expression that results in False.
# The or operator returns True if at least one of the expressions is True, and False if both expressions are False.
print(True or False)
print(False or False)

#3. What does the operator not do? Write an expression that results in True. Write an expression that results in False.
# The not operator negates the boolean value of an expression. The negation of True is False, and the negation of False is True.
print(not(False))
print(not(True))

'''
1. What is the difference between / and //?
The normal division operator, /, returns a float, where as // returns the integer part of the float result.
2. What is the difference between % and //?
The % operator returns the remainder of the division, while // returns the integer part of the division.
3. What operator would you use to calculate the remainder when dividing two numbers? Give an example.
You would use the % operator to find x (mod y). For example, 9 % 7 is 9 (mod 7), which is 2.
4. How do assignment operators work?
Assignment operators perform an operation on a variable and then assign the result onto a variable (which may or may not be the same variable).
'''

#Strings
my_string = "hello"
print(my_string) # prints the string "hello"
print(my_string[0]) # prints the first character in my_string, which is "h"
print(my_string[1]) # prints the second character in my_string, which is "e"
print(my_string[2]) # prints the third character in my_string, which is "l"
print(my_string[3]) # prints the fourth character in my_string, which is "l"
print(my_string[4]) # prints the fifth character in my_string, which is "o"
print(my_string[-1]) # prints the last character in my_string, which is "o"
print(my_string[1:3]) # prints the second and third, but not fourth, characters concatonated together in my_string, which is "el"
print(my_string[0:5:2]) # prints every other character in my_string concatonated togehter, starting with the first character, which is "hlo"
print(len(my_string)) # prints the length of the string, or number of chracters, as an integer, which is 5
print(type(len(my_string)))
print(my_string + "goodbye") # prints the concatonation of my_string and "goodbye", which is "hellogoodbye"
print(my_string * 7) # prints my_string concatonated with itself 7 times, which is "hellohellohellohellohellohellohello"

'''
1. Define the term slicing. For which of the manipulations did you slice your string?

Slicing extracts a substring from a string, usually denoted by [start:end:step]. This was done for the 2nd-9th manipulations of my_string.

'''

#2. Call the following, describe the result:
name = "Oski"
print("Hello, my name is", name) # The result is a string which concatonates the first string in the print statement with the second string, saved as a varaible here. Also, there is a space between the two strings added by the print statement.

#3. Call the following, describe the result.
name = "Oski"
print(f"Hello, my name is {name}") # The result is identical to the one above.

'''
4. What is the difference between the two last print statements?
Hint: Look up f-strings.

f-strings (formatted string literals) embed expressions inside strings using {}. The difference between the two print statements is that the second embes the string varaible name inside without an extra space like the comma.
'''

'''
Terminal Commands:
1. cd, changes directories, cd Desktop
2. ls, lists the contents of the current directory, ls Desktop
3. ls -a, lists the contents of the current directory, including hidden files, ls -a Desktop
4. mkdir, creates a new directory in the current directory, mkdir PythonDecal
5. cat, displays the contents of a file, cat homework1.py
6. pwd, prints the current directory path, pwd PythonDecal
7. cd .., changes directory to the parent directory, cd .. PythonDecal
8. cd ., changes directory to the current directory, cd . PythonDecal
9. cd ∼, changes directory to the home directory, cd ∼ PythonDecal
10. cp, copies a file or directory and lets you move or rename the copy, cp homework1.py homework1_copy.py
11. mv, moves or renames a file or directory to a specified location, mv homework1_copy.py /Desktop
12. rm (be careful with this one), removes a file or directory, rm homework1_copy.py
13. clear, clears the terminal screen, clear
14. grep, searches for a specific string in a file, grep "search_term" homework1.py

Questions:
1. Look up 3 other commands not present. Define and explain how to use them on the command line.

touch, creates a new empty file, touch newfile.txt
nano, opens a text editor in the terminal to edit a file, nano newfile.txt
pbcopy, copies the contents of a file to the clipboard, pbcopy < newfile.txt

2. What is the difference between ls and ls -a?

ls -a shows hidden files as well, where as ls does not.

3. What is a hidden file?

Hidden files usually start with a period and are not shown in the terminal by default.

4. Look up 3 other flags (e.g., -a was a flag for the ls command). Define and explain how to use them on the command line.

ls -l, lists the contents of a directory in long format, showing permissions, ownership, size, and modification date, ls -l Desktop
open -a, opens a file or directory in the default application, open -a TextEdit newfile.txt
rm -f, forcefully removes a file or directory without prompting for confirmation, rm -f newfile.txt

'''