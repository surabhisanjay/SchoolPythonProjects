n=int(input("enter no of elements you want in each list"))
L=[]
M=[]
for i in range(n):
    valL=int(input("enter list 1 elements"))
    L.append(valL)
for i in range(n):
    valM=int(input("enter list 2 elements"))
    M.append(valM)
print(L,M)
N=[]
for i in range(n):
    N.append(M[i]+L[i])
print(N)