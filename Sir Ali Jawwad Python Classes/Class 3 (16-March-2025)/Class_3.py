# 1- Operators

# 1) Arithmetic Operators: +, -, *, /, %, **

# num1 = 5
# num2 = 2

# print(f"num1 + num2 = {num1 + num2}") # Addition
# print(f"num1 - num2 = {num1 - num2}") # Substraction
# print(f"num1 * num2 = {num1 * num2}") # Multiplication
# print(f"num1 / num2 = {num1 / num2}") # Divistion Float
# print(f"num1 // num2 = {num1 // num2}") # Floor Division
# print(f"num1 % num2 = {num1 % num2}") # Modulus
# print(f"num1 ** num2 = {num1 ** num2}") # Exponentiation


# 2) Assignment Operators: =, +=, -=, *=, /=, %=, **=

# num3 = 10 # Assign
# print(f"num3 = {num3}")

# num3 += 5 # Addition and Assign
# print(f"num3 += 5 = {num3}")

# num3 -= 3 # Subtraction and Assign
# print(f"num3 -= 3 = {num3}")

# num3 *= 2 # Multiplication and Assign
# print(f"num3 *= 2 = {num3}")

# num3 /= 4 # Division and Assign Float
# print(f"num3 /= 4 = {num3}")

# num3 //= 3 # Floor Division and Assign
# print(f"num3 //= 3 = {num3}")

# num3 %= 2 # Modulus and Assign
# print(f"num3 %= 2 = {num3}")

# num3 **= 3 # Exponentiation and Assign
# print(f"num3 **= 3 = {num3}")


# 3) Comparison (Relational) Operators

num4 = 10

print(f"num4 == 10: {num4 == 10}") # True, Equal

print(f"num4 != 10: {num4 != 10}") # False, Not Equal

print(f"num4 > 5: {num4 > 5}") # Ture, Greater than

print(f"num4 < 5: {num4 < 5}") # False, Less than

print(f"num4 >= 5: {num4 >= 5}") # True, Greater than or Equal

print(f"num4 <= 5: {num4 <= 5}") # False, Less than or Equal

# 4) Logical Operators

# Logical AND (&&)

print(f"(num4 > 5) && (num4 <= 10): {(num4 > 5) and (num4 <= 10)}") # True, Both conditions are True

# Logical OR (||)

print(f"(num4 > 5) || (num4 > 15): {(num4 > 5) or (num4 > 15)}") # True, At least one condition is True

# Logical NOT (!)

print(f"not (num4 > 5): {not (num4 > 5)}") # False, num4 is not greater than 5

# 5) Identify Operators

a: list = [1, 2, 3]
b: list = [1, 2, 3]
c: list = a

print("a is c     =  ",a is c) # True  (same object, sharing same memmory space)
print("a is b     =  ",a is b) # False (different objects, seperate memmory space)
print("a == b     =  ", a == b) # True  (same values, different memmory space but having same values)

print("a is not b =  ", a is not b)  # True  (True because of different memmory space, although having same memmory space)

# 6) Membership Operators

my_list = [1, 2, 3, 4, 5]

print(f"2 in my_list: {2 in my_list}") # True
print(f"6 in my_list: {6 in my_list}") # False