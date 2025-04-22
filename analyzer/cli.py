# cli.py defines a simple, interactive cli for users
import os
from database.operations import *

# display available commands
def print_help():
    print("\nAvailable commands:")
    print(" create <document_path>                              - Upload a PDF, DOCx, or .txt document directly from your computer")
    print(" read [document_name]                                - Read document")
    print(" edit [document_name]                                - Edit an existing document")
    print(" delete [document_name]                              - Delete a document")
    print(" feedback [document_name]                            - Generate feedback for an existing document")
    print(" grade [document_name]                               - Auto-grade an existing document")
    print(" generate [document_name] [content_type] [number]    - Generate studying and testing material for an existing document.")
    print(" content                                             - Display content type you can generate.")
    print(" help                                                - Display this help message")
    print(" exit                                                - Exit the application")

def print_content():
    print("\nAvailable content types:")
    print(" mc                  - Multiple choice questions and answers")
    print(" tf                  - True or false questions and answers")
    print(" fill                - Fill in the blank questions and answers")
    print(" fc                  - Flashcards with answers")
    print(" sg                  - Study guide with answers (will always get 1)")

def application_cli():
    print("\n---- Welcome to AutoTeacher AI ----")
    while True:
        try:
            db_name = input("Enter the database you are using in the format [db_name].db: ")
            if not os.path.isfile(db_name):
                raise FileNotFoundError("Database file does not exist.")
            break
        except Exception as e:
            print(f"{e} Try another one.")
    print("Type 'help' for available commands.\n")

    while True:
        try:
            user_input = input("> ").strip()
            if not user_input:
                continue

            # parse the input command
            parts = user_input.split(maxsplit=1)
            command = parts[0].lower() # gets first word from input

            # choose correct function based on input
            if command == "exit":
                break

            elif command == "help":
                print_help()

            elif command == "create":
                if len(parts) < 2:
                    print("Please specify a document name.")
                    continue
                load_parts = parts[1].split(maxsplit=1)
                file_name = load_parts[0]
                create_doc(db_name, file_name, "Default file content")

            elif command == "read":
                if len(parts) < 2:
                    print("Please specify a document name.")
                    continue
                load_parts = parts[1].split(maxsplit=1)
                file_name = load_parts[0]
                read_content = read_doc(db_name,file_name)
                if read_content:
                    print(f"Content: {read_content}")

            elif command == "edit":
                if len(parts) < 2:
                    print("Please specify a document name.")
                    continue
                load_parts = parts[1].split(maxsplit=1)
                file_name = load_parts[0]
                edit_doc(db_name,file_name,"Edited file content")

            elif command == "delete":
                if len(parts) < 2:
                    print("Please specify a document name.")
                    continue
                load_parts = parts[1].split(maxsplit=1)
                file_name = load_parts[0]
                delete_doc(db_name,file_name)

            elif command == "feedback":
                return True

            elif command == "grade":
                return True

            elif command == "generate":
                return True

            elif command == "content":
                print_content()

            else:
                print(f"Unknown command: {command}. Type 'help' for available commands.")

        except KeyboardInterrupt:
            print("\nExiting...")
            exit(0)
        except Exception as e:
            print(f"Error: {e}")