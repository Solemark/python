with open("file1.csv", "r") as f1, open("file2.csv", "r") as f2:
    file1 = f1.readlines()
    file2 = f2.readlines()

for line in file1:
    if line not in file2:
        print(f"line: {line}\ndoes not exist in file2!")
    else:
        print("these files match!")
