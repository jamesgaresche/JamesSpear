#3: Print Functions
#3.1
def say_Goodbye(name):
    print("Goodbye", name)
#3.2
def circle_area(radius):
    print(3.141592653589793238*(radius**2))

#4: Return Functions
#4.1
def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

#5: Conditionals
#5.1
temp = [15, 14, 17, 20, 23, 28, 20]
def weather(list):
    return [max(list),min(list)]
#5.2
def is_weekend(n):
    if n == 6 or n == 7:
        return True
    else:
        return False
#5.3
def fuel_eff(distance,gallons):
    return distance/gallons
#5.4
def encryptor(n):
    last_digit = n % 10
    power = 10**(len(str(n))-1)
    return (last_digit*power)+(n//10)
print(encryptor(312746))

#6: Loops
#6.1
def exponentiate(x,y):
    const = x
    for i in range(1,y):
        x *= const
    return x
print(exponentiate(2,3))
#6.2
def min(list):
    for i in range(0,len(list)):
        count = 0
        for j in range(0,len(list)):
            if list[i] < list[j]:
                count += 1
                if count == len(list) - 1:
                    return list[i]

L1 = [3,6,4,9,1,8,0]
print(min(L1))

def max(list):
    for i in range(0,len(list)):
        count = 0
        for j in range(0,len(list)):
            if list[i] > list[j]:
                count += 1
                if count == len(list) - 1:
                    return list[i]

print(max(L1))

def min2(list):
    minval = list[0]
    index = 0
    while index < len(list):
        if list[index] < minval:
            minval = list[index]
        index += 1
    return minval

def max2(list):
    maxval = list[0]
    index = 0
    while index < len(list):
        if list[index] > maxval:
            maxval = list[index]
        index += 1
    return maxval

print(min2(L1))
print(max2(L1))

#6.3
def sum_of_digits(n):
    digits = len(str(n))
    sum = 0
    for i in range(0,digits):
        add = n % (10**(i+1))
        add = add//(10**i)
        sum += add
    return sum

n = 1997
result = sum_of_digits(n)
print(sum_of_digits(n))

print(f"The result of the sum of digits function (6.1) applied 6.1 to {n} is {result}")