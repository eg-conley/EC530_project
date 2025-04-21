# python3 -m coverage run -m pytest -s
# tests made with ChatGPT
import os
import pytest

from database.models import create_table
from database.operations import create_doc, read_doc, edit_doc, delete_doc

# Use a temporary test database to isolate testing
TEST_DB = "tests.db"

create_table(TEST_DB)

def test_create_doc():
    filename = "test.txt"
    content = "Hello, World!"
    created_file = create_doc(TEST_DB, filename, content)
    assert created_file == True

def test_read_doc():
    filename = "test.txt"
    read_content = read_doc(TEST_DB, filename)
    assert read_content == "Hello, World!"

def test_edit_doc():
    filename = "edit.txt"
    content = "Original"
    new_content = "Updated"
    create_doc(TEST_DB, filename, content)

    edited_content = edit_doc(TEST_DB, filename, new_content)
    assert edited_content == True

    read_content = read_doc(TEST_DB, filename)
    assert read_content == "Updated"

def test_delete_doc():
    filename = "edit.txt"
    deleted_file = delete_doc(TEST_DB, filename)
    assert deleted_file is True
