# Homework 4
#3: Lists

food = ['sushi', 'burgers', 'pasta', 'ice cream', 'tuna']
print("food[1]")
print("food[-1]")
food.append('pizza')
food.insert(0,'apple')
food.remove('pasta')
print(len(food))
for i in range(len(food)):
    print(food[i].upper())
food2 = food[0::len(food)-1]
print(food2)
if 'potato' in food:
    print ("A potato!")
else:
    print ("No potato!")

numbers = []
for i in range(0,21):
    numbers.append(i)
def get_first_15(numbers):
    return numbers[0:15]
print(get_first_15(numbers))
def get_every_fifth(numbers):
    return numbers[::5]
print(get_every_fifth(get_first_15(numbers)))
def reverse_and_stride(numbers):
    return numbers[::-3]
print(reverse_and_stride(get_every_fifth(get_first_15(numbers))))

list1 = [1,2,3]
list2 = [4,5,6]
list3 = [7,8,9]
matrix = [list1,list2,list3]
print(matrix[2])
print(matrix[1][1])
matrix.append([10,11,12])

def sum_nested(matrix):
    n = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[1])):
            n += matrix[i][j]
    return n
print(sum_nested(matrix))
x = 0
for i in range(12):
    x += i + 1
print(x)

def matirx_nxn(n):
    matrix = []
    k = 1
    for i in range(n):
        row = []
        for j in range(n):
            row.append(k)
            k += 1
        matrix.append(row)
    return matrix
print(matirx_nxn(5))
M5 = matirx_nxn(5)

def multiples_of_3_swap(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] % 3 == 0:
                matrix[i][j] = "?"
    return matrix
M5_swap = multiples_of_3_swap(M5)
print(M5_swap)


'''
Traceback (most recent call last):
  File "/Users/jamesspear/Desktop/PythonDecal/JamesSpear/homework4/homework4.py", line 73, in <module>
    M5_swap = multiples_of_3_swap(M5)
  File "/Users/jamesspear/Desktop/PythonDecal/JamesSpear/homework4/homework4.py", line 69, in multiples_of_3_swap
    if matrix[i][j] % 3 == 0:
TypeError: not all arguments converted during string formatting

There was an issue with the order.
'''

def sum_nested_swap(matrix):
    n = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != "?":
                n += matrix[i][j]
    return n

print(sum_nested_swap(M5_swap))

#4: Dictionaries
ages = {"Katie": 30, "Miriam": 42, "Safia": 25, "Mira": 48}
print(ages["Katie"])
ages["Mira"] = 100
ages["Milana"] = 52
del ages["Miriam"]
for name in ages:
    print(name, ages[name])

print(matirx_nxn(7))