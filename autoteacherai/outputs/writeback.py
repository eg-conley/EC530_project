# writeback.py writes any produced content back to a txt file
import os
def write_back(content):
    while True:
        write_flag = input("Do you want to write this to a file? (y/n): ")
        if write_flag in {"y", "n"}:
            break
        else:
            print("Please enter either 'y' or 'n'")

    if write_flag.lower() == "y":
        write_file_name = input("Enter the new file name: ")
        file_path = os.path.join("documents", write_file_name)
        with open(file_path, "w") as file:
            return file.write(content)
    else:
        return None