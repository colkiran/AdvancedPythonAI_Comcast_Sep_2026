
import pickle

data = {"name": "Patrick", "age": 30, "skills": ["Python", "C", "C++", "AI", "ML"]}

print(f"data :{data}")
print(type(data))

# Serialize the data (pickling)
with open("data.pkl", "wb") as F:
    pickle.dump(data, F)

# Deserialise the data (unpickling)
with open("data.pkl", "rb") as R:
    restored = pickle.load(R)

print(f"restored :{restored}")
