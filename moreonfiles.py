a = open("aniket.txt")
#print(a.tell()) # tells where is your pointer
print(a.readline())
#print(a.tell())
a.seek(0)  # this will reset the pointer
print(a.readline())
#print(a.tell())
a.close()