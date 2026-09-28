
import marshal
data = {'name': 'Mohammed Ali', 'age': 78, 'city': 'Los Angeles'}

print(f"data :{data}")
print(type(data))
print("-" * 60)

# dumps - returns byte object stored in variable bytes
bytes = marshal.dumps(data)
print("After Seriazation :", bytes)
print(type(bytes))

print("-" * 60)
# loads - converts bytes objects into values
new_data = marshal.loads(bytes)
print("After Deserialization :",  new_data)
print(type(new_data))