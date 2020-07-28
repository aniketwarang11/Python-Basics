import time
k=0
initial = time.asctime(time.localtime(time.time()))
print(initial)
while (k<10):
    print("hii")
    time.sleep(3)
    k+=1
print ("while loop ran in " ,time.time()-initial,"Seconde")
initial1 = time.time()
for i in range (10) :
    print("hello")
print ("for loop ran in " ,time.time()-initial1,"Seconde")

# var = time.time()
# var1 =time.localtime(var)
# var2 = time.asctime(var1)
#  #this is same as
#localtime = time.asctime(time.localtime(time.time()))
#
# print(var2)
#
#print(localtime)

