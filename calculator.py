def plus(n1, n2):
    return n1+n2
    
def minus(n1, n2):
    return n1-n2
​
def times(n1, n2):
    return n1*n2
​
def divide(n1, n2):
    return n1/n2
​
def remainder(n1, n2):
    return n1%n2
​
def power(n1, n2):
    return n1**n2
​
def calculator(n1, operation, n2):
    if(operation=="plus"):
        return plus(n1, n2)
    elif(operation=="minus"):
        return minus(n1, n2)
    elif(operation=="times"):
        return times(n1, n2)
    elif(operation=="divide"):
        return divide(n1, n2)
    elif(operation=="remainder"):
        return remainder(n1, n2)
    elif(operation=="power"):
        return power(n1, n2)
    else:
        print("Invalid operation, valid operations are: plus, minus, times, divide, remainder, and power.")
        return
​
n1=int(input("First Number: "))
operation=input("Operation: ")
n2=int(input("Second Number: "))
print("The Result: "+str(calculator(n1, operation, n2)))