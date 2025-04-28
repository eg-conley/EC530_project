# cli.py defines a simple, interactive cli for users
from autoteacherai.database.operations import *
from autoteacherai.analyzer.parser import *
from autoteacherai.analyzer.feedback import *
from autoteacherai.analyzer.grader import *
from autoteacherai.analyzer.generator import *
from autoteacherai.outputs.writeback import *

# display available commands
def print_help():
    print("\nAvailable commands:")
    print(" create <document_path>                              - Upload a PDF, DOCx, or .txt document directly from your computer")
    print(" read [document_name]                                - Read document")
    print(" edit [document_name]                                - Edit an existing document directly with input text")
    print(" delete [document_name]                              - Delete a document")
    print(" feedback [document_name]                            - Generate feedback for an existing document")
    print(" grade [document_name] [rubric_name]                 - Auto-grade an existing document")
    print(" generate [document_name] [content_type] [number]    - Generate studying and testing material for an existing document.")
    print(" content                                             - Display content type you can generate.")
    print(" list                                                - Display all current documents")
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
            print(f"{e} Try another database.")
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
                print("Exiting...")
                exit(0)

            elif command == "help":
                print_help()

            elif command == "create":
                if len(parts) < 2:
                    print("Please specify a document name.")
                    continue
                load_parts = parts[1].split(maxsplit=1)
                file_path = load_parts[0]
                document_name = os.path.basename(file_path)
                file_content = load_document(file_path)
                create_doc(db_name, document_name, file_content)

            elif command == "read":
                if len(parts) < 2:
                    print("Please specify a document name.")
                    continue
                load_parts = parts[1].split(maxsplit=1)
                file_name = load_parts[0]
                read_content = read_doc(db_name,file_name)
                if read_content:
                    print(f"{read_content}")

            elif command == "edit":
                if len(parts) < 2:
                    print("Please specify a document name.")
                    continue
                load_parts = parts[1].split(maxsplit=1)
                file_name = load_parts[0]
                new_content = input("Directly enter the new content of the document: ")
                edit_doc(db_name,file_name,new_content)

            elif command == "delete":
                if len(parts) < 2:
                    print("Please specify a document name.")
                    continue
                load_parts = parts[1].split(maxsplit=1)
                file_name = load_parts[0]
                delete_doc(db_name,file_name)

            elif command == "feedback":
                if len(parts) < 2:
                    print("Please specify a document name.")
                    continue
                load_parts = parts[1].split(maxsplit=1)
                file_name = load_parts[0]
                file_content = read_doc(db_name,file_name)
                if file_content:
                    feedback = provide_feedback(file_content)
                    print(feedback)
                    write_back(feedback)

            elif command == "grade":
                if len(parts) < 2:
                    print("Please specify a document name and rubric document name.")
                    continue
                # get file content
                load_parts = parts[1].split(maxsplit=1)
                file_name = load_parts[0]
                file_content = read_doc(db_name,file_name)
                # get rubric content
                load_parts_2 = load_parts[1].split(maxsplit=1)
                rubric_name = load_parts_2[0]
                rubric_content = read_doc(db_name,rubric_name)
                if file_content and rubric_content:
                    grade = grade_document(file_content, rubric_content)
                    print(grade)
                    write_back(grade)

            elif command == "generate":
                if len(parts) < 2:
                    print("Please specify a document name, content type, and number.")
                    continue
                # get file content
                load_parts = parts[1].split(maxsplit=1)
                file_name = load_parts[0]
                file_content = read_doc(db_name, file_name)
                # get content type
                load_parts_2 = load_parts[1].split(maxsplit=1)
                content_type = load_parts_2[0]
                # get number
                load_parts_3 = load_parts_2[1].split(maxsplit=1)
                number = load_parts_3[0]
                if file_content and content_type and number:
                    if content_type == "mc":
                        mc = create_mc(file_content,number)
                        print(mc)
                        write_back(mc)
                    elif content_type == "tf":
                        tf = create_tf(file_content,number)
                        print(tf)
                        write_back(tf)
                    elif content_type == "fill":
                        fill = create_fill(file_content,number)
                        print(fill)
                        write_back(fill)
                    elif content_type == "fc":
                        fc = create_fc(file_content,number)
                        print(fc)
                        write_back(fc)
                    elif content_type == "sg":
                        sg = create_sg(file_content)
                        print(sg)
                        write_back(sg)
                    else:
                        print("Content type not supported.")

            elif command == "content":
                print_content()

            elif command == "list":
                count = count_doc(db_name)
                print(f"{count[0]} documents: ")
                documents = list_doc(db_name)
                # only print first 10
                for doc in documents:
                    print(doc[0])
                if (count[0] > 10):
                    print("...")

            else:
                print(f"Unknown command: {command}. Type 'help' for available commands.")

        except KeyboardInterrupt:
            print("\nExiting...")
            exit(0)
        except Exception as e:
            print(f"Error: {e}")