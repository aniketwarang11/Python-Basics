# ls = []
# for i in range(100) :
#     if i%3 == 0 :
#         ls.append(i)
# print(ls)

#===============Using numbere comprehensions==================#
# ds = [i for i in range(100) if i%3 == 0]
# print(ds)


#===============Using dictionary comprehensions==================#
# di = {j :f"item{j}" for j in range(1,10001) if j%100 == 0}
# print(di)

# di = {j :f"item{j}" for j in range(5)}
# dt = {value:key for key,value in di.items()}
# print(di,"\n",dt)
#===============Using set comprehensions==================#

# dresses = {dress for dress in ["dress1","dress2","dress1","dress2","dress1","dress2","dress1","dress2"]}
# print(dresses)
# print(type(dresses))


#===============Using generator comprehensions==================#
#creating generator
# evens = (i for i in range(100) if i%2 == 0)
#
# for item in evens :
#     print(item)

# print ("Generating Comprehensions")
# num = input("Enter no of input")
#
# for i in range(num) :
#     inp = input("Enter item")
#     list.append(inp)

a = input("Enter 'n' for number comprehensions :- \nEnter 'd' for dictonary comprehensions :- \nEnter 's' for set comprehensions")
if a == 'n' :
    list1 = [i for i in range(100) if i%3 == 0]
    print(list1)
elif a == 'd' :
    pass
elif a == 's' :
    pass