# cli.py defines a simple, interactive cli for users

# display available commands
def print_help():
    print("\nAvailable commands:")
    print(" create <document_path>          - Description")
    print(" read <document_path>            - Description")
    print(" edit <document_path>            - Description")
    print(" delete <document_path>          - Description")
    print(" feedback <document_path>        - Description")
    print(" grade [document_path]           - Description")
    print(" generate [document_path]        - Description")
    print(" help                            - Show this help message")
    print(" exit                            - Exit the application\n")

def application_cli():
    print("\n---- Welcome to AutoTeacher AI ----")
    print("Type 'help' for available commands.\n")

    while True:
        try:
            user_input = input("> ").strip()
            if not user_input:
                continue

            # parse the input command
            parts = user_input.split(maxsplit=1)
            command = parts[0].lower() # gets first word from input

            if command == "exit":
                break

            elif command == "help":
                print_help()

        except KeyboardInterrupt:
            print("\nExiting...")
            exit(0)
        except Exception as e:
            print(f"Error: {e}")