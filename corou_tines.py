# def searcher ():
#     import time
#     book = "This is book of aniket and code with aniket"
#     time.sleep(4)
#
#     while True :
#         text = (yield)
#         if text in book :
#             print("Your text is in the book")
#         else:
#             print("Your text is not in the book")
#
# search = searcher()
# print("Search Started")
# next(search)
# print("Next mehod running")
# search.send("aniket")
# search.close()
# input("press any key")
# search.send("book")
# input("press any key")
# search.send("an")
# input("press any key")
# search.send("ggh")


file1 = open("corou.txt")
def challenge () :
    while True:
        file1 = open("corou.txt")
        text = (yield)
        if text in file1.read():
            print("Your text is in the file")
        else:
            print("Your text is not in the file")


chall = challenge()
print("search started")
next(chall)
chall.send("aniket")
