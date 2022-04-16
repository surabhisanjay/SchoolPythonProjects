#Q2
Q=[0,0,1]#initial list
R=int(input("To Print the series till nth value \n enter value of n :"))#taking user input 
for i in range(R-3):           #traversing through the list R-3 no of times because there are already 3 nos
    nextval=Q[-1]+Q[-2]+Q[-3]  #summing the last 3 numbers in the list to create the next element
    Q.append(nextval)          #appending this value to the list 

print(Q)