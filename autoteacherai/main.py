# main.py runs the application and introduces a simple CLI
from autoteacherai.analyzer.cli import *

def main():
    try:
        application_cli()
    except Exception as e:
        print(f'Error: {e}')

main()