# AutoTeacher AI 👩‍🏫

## Table of Contents
 1. [Overview](#overview)
 2. [Features](#features)
 3. [Command Options](#command-options)
 4. [Relevant File Structure](#relevant-file-structure)
 5. [How to Use](#how-to-use)
 6. [Future Improvements](#future-improvements)
 7. [Acknowledgements](#acknowledgements)

## Overview
Welcome to AutoTeacher AI, the portal where all of your document needs can be fulfilled. With AutoTeacher AI, gather inspiration for tests, study guides, and even grade papers with the type of the keyboard.

## Features
⬆️ Upload PDF, DOCX, or txt files you want to work on directly from your computer. You can read, edit, and delete all of the documents later on as needed. \
🔄 Auto-generate feedback on assignments, papers, and more. \
💯 Grade student assignments with added justification according to a given rubric. \
📝 Auto-generate tests with a given number of multiple choice, true or false, or fill in the blank questions. \
🧠 Create study material inluding flash cards or study guides.

## Command Options
 1. create <document_path> - Upload a PDF, DOCx, or .txt document directly from your computer
 2. read [document_name] - Read document
 3. edit [document_name] - Edit an existing document directly with input text
 4. delete [document_name] - Delete a document
 5. feedback [document_name] - Generate feedback for an existing document
 6. grade [document_name] [rubric_name] - Auto-grade an existing document
 7. generate [document_name] [content_type] [number] - Generate studying and testing material for an existing document
 8. content - Display content type you can generate
 9. list - Display all current documents
 10. help - Display this help message
 11. exit - Exit the application

## Relevant File Structure
EC530_project/ \
|-- analyzer/ \
&nbsp;&nbsp;&nbsp;  |-- cli.py #defines a simple, interactive cli for users \
&nbsp;&nbsp;&nbsp;  |-- feedback.py #generates feedback on the uploaded documents after they are analyzed \
&nbsp;&nbsp;&nbsp;  |-- generator.py #creates short quizzes, study guides, and other material \
&nbsp;&nbsp;&nbsp;  |-- grader.py #grades uploaded documents/responses \
&nbsp;&nbsp;&nbsp;  |-- llm.py #uses OpenAI's API to generate answers to the respective prompts \
&nbsp;&nbsp;&nbsp;  |-- parser.py #reads the documents (PDF, DOCX, txt)\
|-- database/ \
&nbsp;&nbsp;&nbsp;  |-- models.py #outlines the table schema for the files \
&nbsp;&nbsp;&nbsp;  |-- operations.py #defines CRUD operations for the documents the user will be uploading and analyzing \
|-- outputs/ \
&nbsp;&nbsp;&nbsp;  |-- writeback.py #writes any produced content back to a txt file \
|-- tests/ \
&nbsp;&nbsp;&nbsp;  |-- analyzer_test.py #tests analyzer file functions \
&nbsp;&nbsp;&nbsp;  |-- database_test.py #tests database file functions \
&nbsp;&nbsp;&nbsp;  |-- outputs_test.py #tests output file functions\
|--  main.py #runs the application and introduces a simple CLI\
|-- requirements.txt #lists the required packages

## How to Use
### Requirements
* Python 3.9 or newer
* The required packages are in the requirements.txt file

### Steps
 1. 
 2. 
 3. 
 4. 

### Example Uses
* command 1 `create`
>
* command 2 `read`
>
* command 3 `edit`
>
* command 4 `delete`
>
* command 5 `feedback`
>
* command 6 `grade`
>
* command 7 `generate`
>
* command 8 `generate`
>
* command `generate`
>
* `content`
>
* `list`
>
* `help`
>
* `exit`
>

## Future Improvements
* Build out UI and create better UX
* Support additional file types like .rtf, .md, etc

## Acknowledgements
* ChatGPT helped with file structure and generating tests, modified as needed
* OpenAI API: https://platform.openai.com/docs/overview
