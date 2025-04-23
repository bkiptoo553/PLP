"""
File Read & Write Challenge 🖋️: 
    Create a program that reads a file and writes a modified version to a new file.
Error Handling Lab 🧪: 
    Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
"""
def read_write_program():
    file_name = input("Enter your file name: ")

    try:
        file = open(file_name, "r")
        file_data = file.read()

        print(file_data)

        modified_data = file_data.upper()

        print(modified_data)

        new_file_name = input("Enter new file name: ")

        new_file = open(new_file_name, "w")
        new_file_data = new_file.write(modified_data)

    except FileNotFoundError:
        print("File is not available !")

    finally:
        file.close()

read_write_program()