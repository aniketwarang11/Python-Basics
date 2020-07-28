list1 = ["Bhindi","Aloo","Chopsticks","Chowmint"]
# i=1
# for item in list1 :
#     if i%2 != 0 :
#         print(f"Jarvis please buy {item}")
#     i+=1

for index,item in enumerate(list1):
    if index%2 == 0 :
        print(f"Jarvis please buy {item}")