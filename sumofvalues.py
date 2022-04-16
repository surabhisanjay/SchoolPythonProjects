D1={1:[1,2,3],2:[4,5,3]}
D2={}
sum_val=0
for i in D1:
    Y=D1.get(i)
    for j in range(len(Y)):
        sum_val+=Y[j]
        D2.update({i:sum_val})
    sum_val=0
print(D2)