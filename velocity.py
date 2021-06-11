velocity1 = int(input("enter velocity1 :"))
velocity2 = int(input("enter velocity2 :"))

duration1 = int(input("enter duration1 :"))
duration2 = int(input("enter duration2 :"))

if velocity1 * duration1 > velocity2 * duration2:
    print("first object is faster")
    print(velocity1 * duration1)

elif velocity1 * duration1 == velocity2 * duration2:
    print(velocity1 * duration1 + "=" + velocity2 * duration2)

else:
    print("second object is faster")
    print(velocity2 * duration2)
