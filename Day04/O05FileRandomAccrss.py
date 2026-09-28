
with open("employeeData.csv", "rb") as FL:
    print(FL.tell())
    FL.read(500)
    print(FL.tell())
    pos = FL.seek(600, 1)
    print(f"Position :{pos}")
    pos = FL.seek(-10, 2)
    print(f"Position :{pos}")
