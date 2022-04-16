M={1:"A",2:"B",3:"C"}
U=[]
for i in M:
    U.append(M.get(i))
print(U)
O=[]
for i in M:
    O.append(i)

P={}
for i in range(len(M)):
    P.update({U[i]:O[i]})
print(P)

