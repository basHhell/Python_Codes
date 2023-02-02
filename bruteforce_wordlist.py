from itertools import product

#here i have not used any random module and it will give different products of my inputs.

print("Welcome to PASS CRACK")
name = input("Type NAME : \n")
last_name = input("Type LAST NAME : \n")
age = input("Type AGE : \n")
dob = input("Type DOB : \n")
addd = (name + last_name + age + dob)

for i in range(1,5):
    for j in product(addd,repeat=i):
        word="".join(j)
        p=open("password.txt","a")
        p.write(word)
        p.write("\n")

































