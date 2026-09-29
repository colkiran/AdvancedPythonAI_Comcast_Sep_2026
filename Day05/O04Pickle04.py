
import pickle

data = {"name": "Virat", "age": 38, "runs": {'sri': 85, 'pak': 102, 'aus': 90} }

print(f"data :{data}")
print(type(data))

print("-" * 60)
# text based serialization
print(pickle.dumps(data, protocol=0))

print("-" * 60)
# protocol 4 - binary efficient
print(pickle.dumps(data, protocol=4))
