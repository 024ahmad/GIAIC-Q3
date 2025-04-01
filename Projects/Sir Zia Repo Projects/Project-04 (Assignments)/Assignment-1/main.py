# user1 = input("Enter first number: ")
# if user1.isdigit():
#     user1 = int(user1)
# else:
#     print("Invalid input")
#     exit()

# user2 = input("Enter second number: ")
# if user2.isdigit():
#     user2 = int(user2)
# else:
#     print("Invalid input")
#     exit()

# print(user1 + user2)

def calculate(num1, num2, operator):
    user1 = input("Enter first number: ")
    user2 = input("Enter second number: ")
    if user1.isdigit() and user2.isdigit():
        num1 = int(user1)
        num2 = int(user2)
        if operator == "+":
            return num1 + num2
         elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        elif operator == "/":
            return num1 / num2
    else:
        print("Invalid input")

    
    else:
        return "Invalid operator"

print(calculate(5,12,"*"))