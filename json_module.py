
import json
data = '{"var1":"Harry","var2":"56"}'
# print(data)
parsed = json.loads(data)
print(parsed)

data2 =  {
    "channel_name": "CodeWithHArry",
    "cars" : ['bmw', 'audi a8', 'ferrari'],
    "fridge": ('roti',540),
    "isbad": False
}
jscomp = json.dumps(data2)
print(jscomp)