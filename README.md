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
💻 Upload PDF, DOCX, or txt files you want to work on directly from your computer. You can read, edit, and delete all of the documents later on as needed. \
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
&nbsp;&nbsp;&nbsp;  |-- parser.py #reads the documents (PDF, DOCX, txt) \
|-- database/ \
&nbsp;&nbsp;&nbsp;  |-- models.py #outlines the table schema for the files \
&nbsp;&nbsp;&nbsp;  |-- operations.py #defines CRUD operations for the documents the user will be uploading and analyzing \
|-- documents/ \
&nbsp;&nbsp;&nbsp;  |-- Countries_of_the_World.pdf #sample pdf file \
&nbsp;&nbsp;&nbsp;  |-- Layers_of_the_Ocean_Rubric.pdf #sample pdf file \
&nbsp;&nbsp;&nbsp;  |-- Layers_of_the_Ocean_.docx #sample docx file \
&nbsp;&nbsp;&nbsp;  |-- Water_Cycle #sample txt file \
|-- documents.db #database preloaded with some example documents \
|-- outputs/ \
&nbsp;&nbsp;&nbsp;  |-- writeback.py #writes any produced content back to a txt file \
|-- tests/ \
&nbsp;&nbsp;&nbsp;  |-- analyzer_test.py #tests analyzer file functions \
&nbsp;&nbsp;&nbsp;  |-- database_test.py #tests database file functions \
&nbsp;&nbsp;&nbsp;  |-- outputs_test.py #tests output file functions\
|--  main.py #runs the application and introduces a simple CLI\
|-- requirements.txt #lists the required packages
|-- tests.db #database required for test files

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
* Initial startup entering database to use `[database_name].db`
> <img width="607" alt="image" src="https://github.com/user-attachments/assets/955a01f1-f787-4789-8d70-2b2d94469da3" />
* `create <document_path>`
> <img width="426" alt="image" src="https://github.com/user-attachments/assets/8271af5f-27c7-4dcd-abec-6710ffc33175" />
* `read [document_name]`
> <img width="815" alt="Screenshot 2025-04-25 at 12 51 36 AM" src="https://github.com/user-attachments/assets/cac8e9a2-7153-4b97-94b4-14e17142b8be" />
* `edit [document_name]` (directly type new content)
> <img width="500" alt="image" src="https://github.com/user-attachments/assets/aa5edaa0-82c9-4e81-9fe1-bf0a3988c5d2" />
* `delete [document_name]`
> <img width="430" alt="image" src="https://github.com/user-attachments/assets/ebb1312a-6687-4aa1-a94c-580797f513ab" />
* `feedback [document_name]`
> <img width="1377" alt="Screenshot 2025-04-25 at 12 59 56 AM" src="https://github.com/user-attachments/assets/d1111275-b670-48a4-a65e-8bf553e1f18f" />
> . . .
> <img width="1373" alt="Screenshot 2025-04-25 at 1 01 05 AM" src="https://github.com/user-attachments/assets/712e2aa9-9254-4a15-88f0-ebc3e5610ad4" />
* `grade [document_name] [rubric_name]`
> <img width="1374" alt="Screenshot 2025-04-25 at 1 04 22 AM" src="https://github.com/user-attachments/assets/ef33fba2-4f1c-4a73-86ab-044c8df47d05" />
* `generate [document_name] [content_type] [number] `
> <img width="982" alt="image" src="https://github.com/user-attachments/assets/ca5abf79-1bab-4484-bbef-a0915626acca" />
> <img width="1176" alt="Screenshot 2025-04-25 at 1 07 57 AM" src="https://github.com/user-attachments/assets/62a2ca49-920a-4184-a00a-62677fdbd05e" />
> <img width="1375" alt="Screenshot 2025-04-25 at 1 08 42 AM" src="https://github.com/user-attachments/assets/20c5d09f-4028-43f7-b38d-99b2e4c9fe32" />
* `content`
> <img width="547" alt="Screenshot 2025-04-25 at 12 56 14 AM" src="https://github.com/user-attachments/assets/455e88a9-7dc3-4144-8667-242a1003e2ed" />
* `list`
> <img width="256" alt="image" src="https://github.com/user-attachments/assets/f92235dd-c6d6-470d-8f34-879a07531029" />
* `help`
> <img width="961" alt="image" src="https://github.com/user-attachments/assets/5ab27ae9-9e62-42fe-b9f7-cab98e982186" />
* `exit`
> <img width="501" alt="Screenshot 2025-04-25 at 1 06 18 AM" src="https://github.com/user-attachments/assets/deb3a70e-48ae-4ddf-bfc4-ff3731a3a30a" />


## Future Improvements
* Build out UI and create better UX
* Support additional file types like .rtf, .md, etc

## Acknowledgements
* ChatGPT helped with file structure and generating tests, modified as needed
* OpenAI API: https://platform.openai.com/docs/overview
