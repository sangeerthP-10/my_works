import random

user_wins=0
computer_wins=0

options=["rock","paper","scissors"]
while True:
    user_input=input("typr Rock/Paper/scissors(q to quit)").lower()
    if user_input=='q':
        break
    if user_input not in options:
        print("invalid input")
        continue
    random_num=random.randint(0,2)
    computer_pick=options[random_num]
    print("computer : ",computer_pick)
    print("user : ",user_input)

    if user_input=="rock" and computer_pick=="scissors":
        print("you win")
        user_wins+=1
    elif user_input=="paper" and computer_pick=="rock":
        print("you win")
        user_wins+=1
    elif user_input=="scissors" and computer_pick=="paper":
        print("you win")
        user_wins+=1
    elif user_input==computer_pick:
        print("draw")
    else:
        print("you lose")
        computer_wins+=1


print("user score : ",user_wins)
print("comuter score : ",computer_wins)





 

