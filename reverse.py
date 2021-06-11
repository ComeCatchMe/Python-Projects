def reverse(sentence):
    return sentence[::-1]

sample = reverse("123")
print(sample)

##

def type_checker(number):
    if(type(number) == int or type(number)== float):
        return True
    else:
        return False
my_string=type_checker("whatever")
print(my string)

##

def odd(lst):
    for number in lst:
        index = lst.count(number)
        if (index%2!=0):
            return(number)
        else:
            None

