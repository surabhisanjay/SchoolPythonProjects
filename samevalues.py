W={1:2,2:3,3:3,4:2}
L=[]
for i in W:
    L.append(W.get(i))
U=0
for i in L:
    if L.count(i)>1:
        U=L.count(i)
if U==0:
    print("No keys have the same values")
else:
    print(U,"keys have same values")


       

    