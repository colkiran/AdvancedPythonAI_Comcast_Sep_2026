
# FL = None
# try:
#     FL = open("data.txt", "r")
#     data = FL.read()
#     print(data)
# except FileNotFoundError as f:
#         print(f)
# finally:
#     if FL is not None:
#         FL.close()
#     print("finally block code....")
#

try:
    with open("data.txt", "r") as FL:
        data = FL.read()
        print(data)
except FileNotFoundError as f:
    print(f)

