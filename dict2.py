
PhoneBook = {}
print("\nEnter Names and Phone numbers :")
n=int(input("How many names?"))
for i in range(n) :
    name=input("Name:")
    p=int(input("How many phone numbers ?"))
    PhoneBook[name] = []
    for j in range(p):
        num=int(input("enter phone number:"))
        PhoneBook[name].append(num)
print(PhoneBook)
print("Enter details of name and phone number to be deleted:")

name= input("Enter name :")
number = int(input("Enter number :"))
if name in PhoneBook:
   PhoneBook[name].remove(number)

print(PhoneBook)