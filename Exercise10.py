#use pickle and requests module
#use request module to download iris dataset
import json
import  requests
import pickle
#url = 'https://archive.isc.uci.edu/ml/machine-learning-databases/iris/iris.data'
data_set = requests.get("https://archive.iCS.uci.edu/ml/machine-learning-databases/iris/iris.data").text
#print(data_set)

l1 = data_set.split("\n")
print(l1)

l2 = [item.split(",") for item in l1 if len(item)!=0]
print(l2)
# with open("myiris.pkl", "wb") as f :
#     pickle.dump(l2, f)

# with open("myiris.pkl", "rb") as f :
#     print(pickle.load(f))