# AutoTeacher AI 👩‍🏫

## Table of Contents
 1. [Overview](#overview)
 2. [Features](#features)
 3. [Command Options](#command-options)
 4. [File Structure](#relevant-file-structure)
 5. [How to Use](#how-to-use)
 6. [Future Improvements](#future-improvements)
 7. [Acknowledgements](#acknowledgements)

## Overview
Welcome to AutoTeacher AI, the portal where all of your document needs can be fulfilled. With AutoTeacher AI, gather inspiration for tests, study gyudes, 

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
&nbsp;&nbsp;&nbsp;  |-- cli.py \
&nbsp;&nbsp;&nbsp;  |-- feedback.py \
&nbsp;&nbsp;&nbsp;  |-- generator.py \
&nbsp;&nbsp;&nbsp;  |-- grader.py \
&nbsp;&nbsp;&nbsp;  |-- llm.py \
&nbsp;&nbsp;&nbsp;  |-- parser.py \
|-- database/ \
&nbsp;&nbsp;&nbsp;  |-- models.py \
&nbsp;&nbsp;&nbsp;  |-- operations.py \
|-- outputs/ \
&nbsp;&nbsp;&nbsp;  |-- writeback.py \
|-- tests/ \
&nbsp;&nbsp;&nbsp;  |-- analyzer_test.py \
&nbsp;&nbsp;&nbsp;  |-- database_test.py \
&nbsp;&nbsp;&nbsp;  |-- outputs_test.py \
|--  main.py \
|-- requirements.txt 

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
* Command 1
>
 
## Future Improvements
* Build out UI and create better UX
* Support additional file types like .rtf, .md, etc

## Acknowledgements
* ChatGPT helped with file structure and generating tests, modified as needed
* OpenAI API: https://platform.openai.com/docs/overview
