import json

def write_json(data , filename="employer.json"):
    with open(filename , "w") as f:
        json.dump(data , f , indent=4)

with open ("employer.json") as json_file:
    data =  json.load(json_file)
    temp =  data["employ"]
    y = {"id": "3" , "name":"bob" , "designation": "boss"}
    temp.append(y)

write_json(data)




