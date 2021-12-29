
## https://pythonprogramminglanguage.com/python-json/ 
import json

class Student:
    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self.password = password

pythonObj = Student(1,'ashley','123456')

# Convert Python object to JSON object
jsonObj = json.dumps(pythonObj.__dict__)
print(jsonObj)

print("\n==========================================================================")

j = json.loads('{"password": "123456", "id": 1, "name": "ashley"}')
pythonObj = Student(**j)

print(pythonObj.id)
print(pythonObj.name)
print(pythonObj.password)