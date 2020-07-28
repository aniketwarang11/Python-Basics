# dictionary is case sensetive
d1= {} #this is how we represent dictionary
d2 = {"Aniket":"Bike", "Aakash":"Car", "Ankita":"Bus", "Anant":"Train",
      "family":{"A":"Bike", "B":"Car", "C":"Bus", "D":"Train" }}
#print(d2["family"]["A"])
d2 ["Warang"] = "Surname" #this is like update fumction only but use update only.
"""
del d2["Warang"]
#print(d2)

d3 = d2.copy()
del d3 ["Aniket"]
print(d3)

d2.update({"Aniket1":"Rocket"})
print(d2)
"""

# a = list(d2)[0]
# print(a)
# print(d2)
x=d2.keys()
# print(x)
# y=len(x)
# for i in range(0,y) :
#       if list(d2)[i] == "Aniket":
#             del d2["Aniket"]
# print(d2)

# var = d2.values()
# print(var)
# print (d2.keys())
list = list()
var = d2.items()
print(var)
for item in var :
      if item == 'Bike' :
           print(item)


# if "Aniket" in d2:
#       del d2["Aniket"]
# print(d2)

#print(d2.items())
# d4 = {"Boy":"Bike", "Girl":"Car", "People":"Bus", "Public":"Train"}
# print ("who are you")
# x=input()
# y=x.capitalize()
# print ("You like", d4[y])
