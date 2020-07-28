file1 = open("harrydiet.txt")
try :
    file2 = open("harryexerciseq.txt")
    # file2 = open("harryexercise.txt")

except Exception as e :
    print(e)

else :
    print("there is no exception ")

finally:
    # file2.close()
    file1.close()
    print("Run Any Way")
