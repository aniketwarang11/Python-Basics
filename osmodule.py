import os
# print(dir(os))
# print(os.getcwd())
# os.chdir("C://")
# print(os.getcwd())
# f = open("harrydiet.txt")
#========to see files in C drive========#
print(os.listdir("C://"))

#print(os.listdir())
#============to create folder in corrent direcory =========#
#os.mkdir("This")

#=======to create folder with one folder inside it =====#
#os.makedirs("This/That")

#=====to rename any file====#
#os.rename("change.txt", "aakash.txt")

#======= to read environment variable ======#
#print(os.environ.get("path"))

#====== to join path =======#
#print(os.path.join("C:/","/harry.txt"))

#=====to check whether file exist or not====#
#print(os.path.exists("C:/"))
# print(os.path.isdir("C:/"))