list = []
list_item = int(input("Enter no of item you want in list :- "))
i = 1
for i in range(i,list_item+1):
    item = int(input(f"Enter {i} item :- "))
    list.append(item)
print(list)
list.reverse()
print(list)
list[::-1]
print(list)

for i in range (int(len(list)/2)):
    temp = list[i]
    list[i] = list[len(list)-i]
    list[len(list)-i] = temp

print(list)