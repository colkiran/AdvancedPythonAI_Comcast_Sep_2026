
gender = {}
with open("employeeData.csv", "r") as FL:
    # data = FL.read()
    for line in FL.readlines():
        gen = line.split(",")[4]
        gen = gen.rstrip("\n")
        if gen not in gender:
            gender[gen] = 1
        else:
            gender[gen] += 1

print(gender)
