"""#3.Write a program that reverses a list of integers (in place).
L1=[1,2,3,4,5]
L2=[6,7,8,9,10]
L3=L1[:5]+L2[:5]
print(L3)
#4.ask user to enter a list of elements from 1 to 12 into a list 
Q=[]
for i in range(4):
    W=int(input("enter the number"))
    Q.append(W)
for a in range(4):
    if Q[a] > 10:
        Q[a]=10
    else:
        pass
print(Q)
#5
w=int(input("which number do you want to check"))
Q=[1,2,4,5,7]
for i in range(len(Q)):
    if Q[i]==w:
        print("it is present")
        print("it is located at the index",i)
    else:
        pass
#7 ask user to enter a list of strings and remove the first letter of every string
W=int(input("enter no of words in the list"))
Q=[]
for i in range(W):
    wrd=input("enter the string")
    Q.append(wrd)
for i in range(W):
    Q[i]=Q[i][1:]
print(Q)
import math
#7.create using for loop
#1.a list containing integers through 0 to 49
Intlst=[]
for i in range(0,49):
    Intlst.append(i+1)
print(Intlst)
#2. A list containing the squares of the integers from 1 through 50
sqrlst=[]
for a in range(1,51):
    sqrlst.append(math.pow(a,2))
print(sqrlst)
#3.a,bb,ccc,dddd,eeee.........z*26
a=[]
for i in range(1,27):
    a = a+ [chr(96+i)*i]
print(a)"""