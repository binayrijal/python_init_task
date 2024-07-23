
import random

ans=input("do you want to play?")
if ans.lower()!="yes":
    quit()
print("welcome to the quiz")
questions=['''what is your name?''','''how old are you?''','''what is your father name?''','''what is your country name?''']
for x in range(1,4):
 qnum=int(input("enter no between 1 to 4  "))

 if qnum==1:
    print(questions[0])
    ans1=input("enter answer  ")
    if(ans1.lower()=="binay"):
     print("correct!")
    
 elif qnum==2:
    print(questions[1])
    ans2=input("enter answer ")
    if(ans2.lower()==""):
        print("correct!")
    
 elif qnum==3:
    print(questions[2])
    ans3=input("enter answer")
    if(ans3.lower()==""):
        print("correct!")
 elif qnum==4:
    print(questions[3]) 
    ans4=input("enter answer")
    if(ans4.lower()==""):
        print("correct!") 

 elif qnum>4:
     print("sorry you choose wrong question number")            


