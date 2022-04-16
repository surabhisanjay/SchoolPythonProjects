#1.Separate the names of the customers from the email address, store them in a list L(L=[Jitin,Jagruth].
d1={"Jitin":"xyz@gmail.com","Jagruth":"pq@yahoo.com"}
L1=d1.keys()
L=[]
for i in L1:
    L.append(i)
print(L)
#2.Create a new dictionary d2, with names in the list as keys and length of the name as the value.
d2={}
for i in L:
    d2[i]=len(i)
print(d2)
#3.If the length is greater than five replace the name.
d3={}
for i in d2:
    while count>1:
    if d2[i]>5:
        newname=input("enter the new name")
        d3[newname]=len(newname)
        count+=1
print(d3)
