# oh soldier prettify my folder
import  os
def soldirer (path, file, formt) :
    os.chdir(path)
    i = 1
    files = os.listdir(path)
    with open (file) as f :
        filelist = f.read().split("\n")

    for file in files :
        if file not in filelist :
            os.rename(file, file.capitalize())
        if os.path.splitext(file)[1] == formt:
            os.rename(file, f"{i}{format}")
            i += 1

soldirer(r"D:\DBZ movies",
          r"C:/Users/Aniket/PycharmProjects/PythonProject1/exe.txt",  ".png")