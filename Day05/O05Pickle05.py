
import pickle

numbers = list(range(10, 101, 10))
print(f"numbers :{numbers}")
print(type(numbers))

print("-" * 60)

# shared references
# mylist[0]  and mylist[1] points to the same object in memory
mylist = [numbers, numbers]

serialized = pickle.dumps(mylist)
print(f"serialized :{serialized}")

print("-" * 60)
restored = pickle.loads(serialized)
print(f"restored :{restored}")
print(restored[0] is restored[1])
