"""#9.rotates the elements of a list 
W=int(input("enter the no  of elements "))
L=[]
for i in range(W):
    Q=int(input("enter the list element"))
    L.append(Q)
print(L)
for i in range(3):#i=0
    L[i-1]=L[i]
    
print(L)
#10.fibonacci series 
n=int(input("enter which term you want"))
Q=[0,1]
for i in range(n):
    nextnum=Q[-2]+Q[-1]
    Q.append(nextnum)
print(Q[n-1])
print(Q)

#11.print the length of the longest string in the list of strings strlst
w=int(input("enter no of strings"))
strlst=[]
for i in range(w):
    q=input("enter list element")
    strlst.append(q)
longest=""
for i in range(w):
    if len(longest)<len(strlst[i]):
        longest=strlst[i]
print(longest)
#12.
lst = [ ]
for i in range(len(num)) :
      fraction = num[ i ] / denum[ i ]
      lst.append( fraction )

lst.sort()
print("Smallest fraction = ",lst[ 0 ]
#13.WAP to display the maximum and minimum values of a specified range of indexes
q=eval(input("enter the list"))
start=int(input("enter the start index value"))
stop=int(input("enter the stop index value"))
R=q[start:stop]
print(R)
#14.write a program to move all the duplicate values in a list to the end of the list
lst = eval(input("Enter a list :-"))
dup = [ ]
n = 1
while n < len(lst):
      for i in lst :
            if lst.count( i ) != 1 :
                  lst.remove( i )
                  dup.append(i)
      n += 1

lst.sort()
print("New list :- ",lst + dup)"""
#15.WAP to compare 2 equal sized lists and print the first index where they differ
Q=eval(input("enter the first list"))
R=eval(input("enter the second list"))
for i in range(len(Q)):
    if Q[i]!=R[i]:
        print(i)
        break


        



