from random import randint
print("Welcome to Lottery numbers generator.")
import time
time.sleep(3)
print("Pleas enter how many random numbers would you like to have: ")

user_answer = int(raw_input("Enter the number: "))
import random

counting_list=[]

for i in range (user_answer):

    counting_list.append(random.randrange(1,101,1))

print (counting_list)
print("END")
import time
time.sleep(5)
