def plus(n1, n2):
    return n1+n2
def negate(n1):
    return 0-n1
def abss(n1):
    if(n1>=0):
        return n1
    else:
        return negate(n1)
def minus(n1, n2):
    if(n1==n2):
        return 0
    elif(n1<n2):
        newN1=plus(n1, 1)
        return plus(minus(newN1, n2), 1)
    else:
        newN2=plus(n2,1)
        return plus(minus(n1, newN2), 1)
def times(n1, n2):
    if(n1==0 or n2==0):
        return 0
    elif(n1==1):
        return n2
    else:
        return plus(n2, times(calculator(n1, "minus", 1), n2))
def divide(n1, n2):
    if(n1==0):
        return 0
    elif(n1<n2):
        print("Not Divisible")
        exit()
    elif(n2==n1):
        return 1
    else:
        return plus(divide(calculator(n1, "minus", n2), n2), 1)
def remainder(n1, n2):
    if(n1<n2):
        return n1
    else:
        return remainder(calculator(n1, "minus", n2), n2)
def power(n1, n2):
    if(n2==0):
        return 1
    elif(n1==0):
        return 0
    else:
        return calculator(n1, "times", power(n1, calculator(n2, "minus", 1)))
def calculator(n1, operation, n2):
    if(operation=="plus"):
        return plus(n1, n2)
    elif(operation=="minus"):
        if(n1<n2):
            return negate(minus(n1, n2))
        elif(n1<0 and n2<0):
            return minus(abs(n2), abs(n1))
        else:
            return minus(n1, n2)
    elif(operation=="times"):
        n=times(abss(n1), abss(n2))
        if((n1<0 and n2<0) or (n1>=0 and n2>=0)):
            return n
        else:
            return negate(n)
    elif(operation=="divide"):
        if(n2==0):
            print("Divide by 0 Error")
            return
        n=divide(abss(n1), abss(n2))
        if((n1<0 and n2<0) or (n1>=0 and n2>0)):
            return n
        else:
            return negate(n)
    elif(operation=="remainder"):
        if(n1>=0 and n2>=0):
            return remainder(n1, n2)
        else:
            print("Invalid parameters, remainder requires two positive integers")
    elif(operation=="power"):
        if(n2<0):
            print("Invalid parameters, power in this calculator requires exponent to be a nonzero integer")
        else:
            return power(n1, n2)
    else:
        print("Invalid operation, valid operations are: plus, minus, times, divide, remainder, and power.")
        return
n1=int(input("First Integer: "))
operation=input("Operation: ")
n2=int(input("Second Integer: "))
print("The Result:")