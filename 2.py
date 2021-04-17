isSorted=False
count=0
def sortList(a):
    global count
    global isSorted
    n=len(a)
    if (count%n==0 and isSorted==True):
        count=0
        return
    elif(count%n==0):
        isSorted=True
    if(a[count%n]>a[(count+1)%n]):
        isSorted=False
        temp=a[count%n]
        a[count%n]=a[(count+1)%n]
        a[(count+1)%n]=temp
    if(count%n==n-2):
        count+=1
    count+=1
    sortList(a)
​
a=[56,23,43,65,-50,90,-43,54,76]
sortList(a)
​
print(a)