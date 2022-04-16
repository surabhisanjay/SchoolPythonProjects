E = {}
num = int(input("Enter the number of Employees:"))

print("Number of Employees to be entered is: ", num)
for a in range(num):
    eno = int(input('Enter Employee no. '))
    ename=input("enter employee name:  ")
    E[eno]=ename
print("Printing the Employee details - in Ascending order of Employee number", E)
sorted_employees = E.keys()
sorted_employees =  sorted(sorted_employees)
for key in sorted_employees:
    print("Emplyee No:", key, "-", "Employee Name: ", E[key])