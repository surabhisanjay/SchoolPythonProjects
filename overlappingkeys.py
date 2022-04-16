M={1:2,2:3,3:4,5:6}
N={1:2,"A":"B",2:3,8:9}
I=[]
for i in M:
    if i in N:
        I.append(i)
    else:
        pass
print(I)
