name = input("Enter your name: ")
def method_name():
    Question = input("enter your question:" " ")
    return Question

Question = method_name()
answer=""
import random
random_numbers = random.randint(1, 9)
print(random_numbers)

if random_numbers == 1:
    answer="-> Yes difinately."
elif random_numbers == 2:
    answer="-> It's decidely so."
elif random_numbers == 3:
    answer="-> Without a doubt."
elif random_numbers == 4:
     answer="-> Reply hazy, try again."
elif random_numbers == 5:
     answer="-> Ask again later."
elif random_numbers == 6:
     answer="-> Better not tell you now."
elif random_numbers == 7:
     answer="-> My sources say no."
elif random_numbers == 8:
     answer="-> Outlook not so good."
elif random_numbers == 9:
     answer="-> Very doubtful."

print(name + " " "asks:" + Question)
print("Magic 8-ball's answer:" + answer)






