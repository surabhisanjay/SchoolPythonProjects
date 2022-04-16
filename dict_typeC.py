"""#1.enter names of employees and salaries as input and store them in a dictionary
n=int(input("enter no of employees"))
Q={}
for i in range(n):
    emp_name=input("enter employee's name")
    sal=int(input("enter salary of employee"))
    Q.update({ emp_name:sal })
print(Q)

#2.count the number of times a character appears in a given string 
R=input("enter the string")
count=0
for i in R:
    if i=="r":
        count+=1
    else:
        pass
print(count)

#3.WAP to convert a number into their words 
 
"""
#4.WAP to enter the team name and how many games a team has won store it in a dict. 
E=int(input("enter the no of teams in your tournament "))
A={}
V=[]
for i in range(E):
    t=input("enter the team name")
    w=int(input("no of wins"))
    l=int(input("no of losses"))
    V.append(w)
    V.append(l)
    A.update({t:V})
    V=[]
print(A)

In=input("enter team name")
O=A.get(In)
Y=0
for i in O:
    Y+=i
    
win_prcnt=(O[1]/Y)*100
print("the teams winning percentage is ",win_prcnt,"%")

