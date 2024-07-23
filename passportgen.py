import random
char="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
number="0123456789"
symbol="!@#$%^&*()_+"
password=char+number+symbol
count=int(input("enter how many password you want"))
length=int(input("enter the length"))

for x in range(1,count):
 x="".join(random.sample(password,length))
 print(x)


