# def function_name_print (a,b,c,d,e) :
#     print(a,b,c,d,e)
#     def funargs () :
#         print(args[0])
#function_name_print("Aniker","Anant","Warang","Ankita","Aakash")
vehical = {"car":"lambo", "Bike":"Pulzar", "Bus":"Best" } #this is dictionary
family = ["Aniker","Anant","Warang","Ankita","Aakash"] # list
normal = "family members" # normal
#we have to pass normal argument first then args and then kwargs
def functargs (normal,*args,**kwargs):
    print(normal)
    for item in args :
        print (item)
    for key,value in kwargs.items(): # .item() is used to get value of vehicle in pair
        print(f"{key} is a {value}" ) #f stringnis used


functargs(normal,*family,**vehical)