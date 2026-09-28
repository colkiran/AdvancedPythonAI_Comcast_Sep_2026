
from pathlib import Path

# define the path
data_dir = Path("C:/Training/PycharmProjects/AdvPythonComcastSept2026/Day04")
file_path = data_dir / "employeeData.csv"

# check if the path exists
if file_path.exists():
    print(f"{file_path} exists!")

# Read the contents of the file
contents = file_path.read_text(encoding="utf-8")
print("file content\n", contents)

# write into a file
output_file = data_dir / "output.txt"
output_file.write_text("Processed information saved here....", encoding="utf-8")

for text_file in data_dir.glob("*.py"):
    print("Found :", text_file.name)
