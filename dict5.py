print("Maximum messages per day")

n=int(input("Enter number of inputs: "))

msg_dict={}
for i in range(n):
    sender=input("Sender:")
    msg_dict[sender]={}
    no_of_days = int(input("How many days input ? :"))
    for j in range(no_of_days):
        day = input("Day:")
        msgs = int(input("Msgs: "))
        msg_dict[sender][day]=msgs

print("Input stored in dictonary :")
print(msg_dict)

required_day=input("Enter day for which max msgs needs to be displayed :")
tmp_max=0
for k,v in msg_dict.items() :
    if required_day in v:
        if tmp_max < int(v[required_day]) :
            tmp_max = int(v[required_day])

#print(tmp_max)

print("Details of person sending highest messages on ", required_day)
for i in msg_dict:
    if msg_dict[i].get(required_day) == tmp_max:        
        print( i, ":",  msg_dict[i])