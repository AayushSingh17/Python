# API is a set of rules that allows one software applications to interact with another

# A web api is accessed over the internet using http request and response and the data is return in Json format.

# Methods....


#JSON...
# (JavaScript Object Notation)
# It is a light data format used to exchange data between web clients and server and very similar to dictionary


import json
# data = {'name': 'Aayush', 'Age': 19}
# json_str = json.dumps(data) #convert dict to json..
# print(json_str)

# json_data = {'name': 'Aayush', 'Age': 19}
# json_str = json.loads(json_data) #convert json to dict...
# print(data["name"]) #Output : Aayush

x = {
    "Name" : "Aayush",
    "Age" : "19",
    "Married" : True,
    "Divorced" : False,
    "Children" : None,
    "Pets": "Sheru",
    "Cars": [
        {"Model": "BMW R8", "MPG": 30.6},
        {"Model": "Mercedes Benz", "MPG": 70.6},
    ]
}

print(json.dumps(x))
print(x["Cars"][1]["Model"])

