import random
from itertools import product

# here i have use random module so it will give more combination, and as i increase the range() it will give more combination

print("Welcome to PASS CRACK")
name = input("Type NAME : \n")
last_name = input("Type LAST NAME : \n")
age = input("Type AGE : \n")
dob = input("Type DOB : \n")
addd = (name + last_name + age + dob)

for x in range(10):
    for j in product(addd,repeat=x):
        chars_lst = list(addd)
        random.shuffle(chars_lst)

        word="".join(chars_lst)
        p = open("bruteforce110.txt","a")
        p.write(word)
        p.write("\n")
