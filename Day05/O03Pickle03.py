
import pickle

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person("Sachin", 53)

# Serailize
data = pickle.dumps(person)

# Deserialize
restored = pickle.loads(data)
print(f"restored :{restored.name, restored.age}")
