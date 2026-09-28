
class ManagedFile:

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode


    def __enter__(self):
        self.file = open(self.filename, self.mode)
        print("File opened.....")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        print("File closed.....")

with ManagedFile("employeeData.csv", "r") as F:
    F.readline()
    for line in F.readlines():
        print(line)

