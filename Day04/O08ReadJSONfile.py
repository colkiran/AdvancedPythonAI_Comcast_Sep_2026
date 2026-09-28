"""
load - load is used to read the JSON document from a file
loads - loads will convert the json string into python dictionary
"""


import json

JFR = open("books.json", "r")
jsonfile = json.load(JFR)

# print(jsonfile)
for book in jsonfile['books']:
    print(book['name'])
    print("-" * len(book['name']))
    for k, v in book.items():
        print(k, "=>", v)
    print('-' * 60)

print('-' * 60)
# loads
empdata = '{"name": "Michael", "age": 35, "desig": "MGR", "Dept": "Finance", "location": "Delhi"}'
print(f"empdata :{empdata}")
print(type(empdata))
print('-' * 60)

res = json.loads(empdata)
print(f"res :{res}")
print(type(res))
