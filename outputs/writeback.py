# writeback.py writes any produced content back to a txt file
import os
def write_back(content):
    write_flag = input("Do you want to write this to a file? (y/n): ")
    if write_flag.lower() == "y":
        write_file_name = input("Enter the new file name: ")
        with open(write_file_name, "w") as file:
            return file.write(grade)