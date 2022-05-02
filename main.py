import random
decision = []
print("Enter your QUESTION")
q = input()
num1 = input("Enter first option:\n")
num2 = input("Enter second option:\n")
num3 = input("Enter third option:\n")
num4 = input("Enter fourth option:\n")
num5 = input("Enter fifth option:\n")

decision.extend([num1, num2, num3, num4, num5])
result = random.choice(decision)
print(f"The option you should select is {result.upper()}")