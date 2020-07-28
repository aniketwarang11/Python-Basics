num = ["2","3","4","6"]
#map always return an onjet so
num = list(map(int,num))# then the string will be converted in int format
# for i in range(len(num)) :
#     num [i] = int(num[i])
num[2] =  num[2] + 1
# print(num[2] )
# def sq(a):
#     return a*a
# number = [7,8,9,10,11,12]
# square = list(map(sq,number))
# print(square)


# number = [7,8,9,10,11,12]
# square = list(map(lambda a:a*a,number))
# print(square)

# def square (a) :
#     return a*a
#
# def cube (a) :
#     return a*a*a
#
# func = [square, cube]
# # number = [7, 8, 9, 10, 11, 12]
# for i in range(5) :
#     val = list(map(lambda x:x(i),func)) #x is function who return x(i) where x can be any function
#     print(val)
#=============== FILTER =================#
# list1 = [1,2,3,4,5,6,7,8,9,10]
# def is_grater_5(num):
#     return num>5
# gt_than_5 = list(filter(is_grater_5,list1))
# print(gt_than_5)
#================ REDUCE ==================#

from functools import reduce
list1 = [1,2,3,4,5]
prod = reduce(lambda x,y:x*y,list1)
print(prod)
# num =0
# for i in list1 :
#     num= num + i
# print(num)

