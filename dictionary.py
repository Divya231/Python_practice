dic={
    "name" : "divya",
    "age" : 23
}
# print(dic["name"])
# print(dic.keys())
# print(dic.values())

for key in dic.keys():
    print(key)
    print(f"the value corresponding to {key} is {dic[key]}")

for key in dic.values(): 
    print(key)
