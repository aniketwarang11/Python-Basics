#list = [["Aniket",24], ["Anant",56], ["Aakash",21]]
#print (list[0],list[1],list[2]) #this is goof for small list contaning 3-4 items only
#d1 = dict(list)
#print(d1)
"""
for item , age in d1.items() :
    print(item," age is :- ",age)
"""

#to get key only
"""
for item in d1 : 
    print(item)

"""
list2 = [1,"aa",2,"ee",10,"tt",23]

#for item in list2 :
#   if type(item) == int and item > 6:
#      print(item)


for item in list2 :
    if str(item).isnumeric() and item >=6 :
        print(item)
