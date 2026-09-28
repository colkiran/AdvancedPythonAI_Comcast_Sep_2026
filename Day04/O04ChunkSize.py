
CHUNK_SIZE = 4096
with open("employeeData.csv", "rb") as FL:
    while chunk:= FL.read(CHUNK_SIZE):
        print(chunk)
