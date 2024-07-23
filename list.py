thislist=["apple","banana","cherry","dragonfruit","mango"]
print(thislist[:3])
print(thislist[-3:-1])
thislist[1:3]=["why","you","do","this"]
print(thislist)
thatlist=[]
for x in thislist:
    thatlist.append(x)
print(thatlist) 
thatlist[1:5]=["banana","cherry"]
print(thatlist) 
thatlist.insert(2,"papaya")
print(thatlist)
thatlist.append("last fruit") 
print(thatlist)
thatlist.extend(thislist)
print(thatlist)
thatlist.remove("last fruit")
print(thatlist) 
thatlist.pop(7)
print(thatlist)
del thatlist[7]
print(thatlist)
thislist.clear()
print(thislist)
i=0
while(i<len(thatlist)):
    print(thatlist[i])
    i+=1
newlist=["one","two","three","four","v"]
updatelist=[x   if x!="v" else "five" for x in newlist ]
print(updatelist) 

  
    


  
