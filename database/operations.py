# operations.py defines CRUD operations for the documents the user will be uploading and analyzing
import sqlite3

# CRUD API functions that interact with the database
# create document
def create_doc(db_name, filename, content):
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute("INSERT OR REPLACE INTO documents (filename, content) VALUES (?, ?)", (filename, content))
        conn.commit()
        cursor.close()
        print(f"Document {filename} has been created")
        return True
    except Exception as e:
        print(f"Error creating {filename}: {e}")
        return False

# read document
def read_doc(db_name, file_name):
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT content FROM documents WHERE filename = ?", (file_name, ))
        conn.commit()
        content = cursor.fetchone()
        cursor.close()
        if content[0]:
            return content[0]
    except Exception as e:
        print(f"Error reading {file_name}: {e}")
        return False

# edit document
def edit_doc(db_name, file_name, new_content):
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute("UPDATE documents SET content = ? WHERE filename = ?", (new_content, file_name))
        conn.commit()
        cursor.close()
        print(f"Document {file_name} has been updated")
        return True
    except Exception as e:
        print(f"Error editing {file_name}: {e}")
        return False

# delete document
def delete_doc(db_name, filename):
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM documents WHERE filename = ?", (filename,))
        deleted = cursor.rowcount > 0
        conn.commit()
        cursor.close()
        if deleted:
            print(f"Document {filename} has been deleted")
            return True
        else:
            print(f"Document {filename} not found, nothing deleted")
            return False
    except Exception as e:
        print(f"Error deleting {filename}: {e}")
        return False