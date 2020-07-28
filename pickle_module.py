import pickle

#Pickling a python object
# cars = ["Audi", "BMW", "Maruti suzuki"]
# file1 = "mycar.pkl"
# file1obj = open(file1, "wb")
# pickle.dump(cars,file1obj)
# file1obj.close()

#depickling a python object
file = "mycar.pkl"
fileobj = open(file,'rb')
mycar = pickle.load(fileobj)
print(mycar)

#pickle.loads() this function loads data from bytes string