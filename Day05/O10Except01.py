
# accept data from the user

try:
    # expecting a number input
    num = int(input("Enter a number :"))
    print(f"num :{num}")
except ValueError as v:
    print(v)

finally:
    print("code fromwq finally.....")

# num = int(input("Enter a number :"))
# print(num)