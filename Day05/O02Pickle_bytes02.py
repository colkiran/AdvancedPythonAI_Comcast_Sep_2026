
import pickle

numbers = list(range(1, 11))
print(f"numbers :{numbers}")
print(type(numbers))

print("-" * 60)

# serialize to bytes
serialized = pickle.dumps(numbers)
print(serialized)

print("-" * 60)
# deserialize from bytes
restored = pickle.loads(serialized)
print(f"restored :{restored}")
