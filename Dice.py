import random
import time

min = 1
max = 6
again = "yes"
t = 3
while again == "yes" or again =="y":
    print("Dice is rolling .... ")
    time.sleep(t)
    x = random.randint(min , max)
    print(x)
    again = input("roll dice again?")
    if again == 'yes':
        print(x)
    else:
        print("okieee bye")

