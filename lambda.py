# Lambda function are one liner function
# they are also called as Anonymous function

# def add ( a,b) :
#     return a+b
# # minus is a function and x and y are variable
# minus = lambda x,y : x-y
# print(minus(4,5))


# def a_func (a) :
#     return a[1]
a = [[1,4],[5,6],[8,23]]
a.sort(key=lambda x:x[1]) #sort function always takes function as a key and permanentli change the list
# there is also function as sorted(list,key = ....,reverse = ......)
#this function dosent change the list but return the sorted list
print(a)

#while working with dectonary we use .get() method
#def funct() :
#  return dictionary_name.get('value')

