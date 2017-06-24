def isInteger(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def AskForNumber(Ask):
    while True:
        s = input (Ask)
        if isInteger(s):
            return int(s)
        else:
            print ("Sorry that is not a number")


num1 = int(input("What is your first number?"))
num2 = int(input("What is your second number?"))
num3 = 0
math = input("What do you want to do with the numbers? (multiply, divide, add, subtract, powers)")
if math == "add":
    num3 = num1 + num2
    print(str(num3) + " is the answer! Thank you.")
if math == "subtract":
    num3 = num1 - num2
    print(str(num3) + " is the answer! Thank you.")
if math == "multiply":
    num3 = num1 * num2
    print(str(num3) + " is the answer! Thank you.")
if math == "divide":
    num3 = num1 / num2
    print(str(num3) + " is the answer! Thank you.")
if math == "powers":
    num3 = num1 ** num2
    print(str(num3) + " is the answer! Thank you.")
try_again = input("Would you like to try again?(y/n)")
if try_again = "y":
    
if try_again = "n":
    break
