#def fibonacci(i):
#    if i == 0:
#        return 0
#    if i == 1:
#        return 1
#    else:
#        return fibonacci(i-2) + fibonacci(i-1)

#for x in range(13):
#    print(fibonacci(x))



#def fibonacci(x):
#  if (x==1) or (x==2):
#    return 1
#  elif (x==0):
#    return 0
#  else :
#    return fibonacci(x-1)+fibonacci(x-2)
#print(fibonacci(7))


def sequence(n,x, Fibo):
    if (n<x):
        Fibo = Fibo  +  str(fibonacci_sequence(n+1))
        n+=1
        return sequence(n,x, Fibo)
    else:
        return Fibo

Length = int(input("Length of desired Fibonacci sequence: "))
print("The first " + str(Length) + "numbers in your sequence are:" + sequence(n = 0, x = Length - 1, Fibo = str(fibonacci_sequence(0))))