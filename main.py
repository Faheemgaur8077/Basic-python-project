'''
Write a python program capable of playing this game with the user.
'''

import random
'''
1 for snake
-1 for water
0 for gun
'''
computer = random.choice([-1, 0, 1])
youstr = input("Please enter your choice:")
youDict = {"s":1, "w": -1, "g": 0}
reversedict ={1:"snake", -1:"water", 0:"gun"} # we took reversedict because it is able to convert s, w, g, into i, -1, and 0

you = youDict[youstr]
# by now we have 2 numbers (variables), computer and you

print(f"You chose {reversedict[you]}\nComputer chose {reversedict[computer]}")

if(computer == you):
    print("its a draw")

else:
    if(computer== 1 and you == -1): # computer-you = 1 -(-1) = 2
        print("Computer win!")

    elif(computer== 1 and you==0): # 1-0 = 1
        print("You win!")

    elif(computer== -1 and you == 1):# -1-1 = -2
        print("You win!")

    elif(computer== -1 and you==0): # -1-0 = -1
        print("Computer win!")

    elif(computer== 0 and you == 1): # 0-1 = -1
        print("Computer win!")

    elif(computer== 0 and you == -1): # 0-(-1) = 1
        print("You win!")

    else:
        print("Something went wrong!")