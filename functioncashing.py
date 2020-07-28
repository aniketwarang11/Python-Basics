import  time
from functools import lru_cache


# @lru_cache(maxsize=3)
# def somework(n) :
#     time.sleep(n)
#     return  n
#
# if __name__ == "__main__" :
#     print("now running work done")
#     somework(3)
#     somework(1)
#     somework(2)
#     somework(4)
#     print("Done...calling again")
#     somework(3)
#     print("Called again")

cach_value = int (input("Enter no of previous calls you want to cach :- "))

@lru_cache(maxsize=cach_value)
def playing (n) :
    time.sleep(n)

print("Playing")
playing(3)
playing(4)
print("waited for 2 calls")
playing(2)
print("third call")
playing(4)
print("did't wait for 4 sec")





