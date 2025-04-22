# main.py runs the application and introduces a simple CLI
from analyzer import *
from analyzer.cli import *
from database.models import *

def main():
    try:
        # set up database first
        db_name = input("Enter the name of the database: ")
        create_table(db_name)

        # activate cli
        application_cli()
    except Exception as e:
        print(f'Error: {e}')

main()