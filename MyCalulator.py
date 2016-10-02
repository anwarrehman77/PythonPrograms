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


n1 = AskForNumber("What is the first number?")
n2 = AskForNumber("What is the second number?")
math = input ("Do you want to Add, Subtract, Multiply, Divide or do Powers?")
if math == "add":
    print (n1+n2)
if math == "subtract":
    print (n1-n2)
if math == "multiply":
    print (n1*n2)
if math == "divide":
    print (n1/n2)
if math == "powers":
    print (n1**n2)
