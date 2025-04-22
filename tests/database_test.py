# python3 -m coverage run -m pytest -s
# tests made with ChatGPT
import os
import pytest
import sqlite3

from database.models import create_table
from database.operations import create_doc, read_doc, edit_doc, delete_doc

# Use a temporary test database to isolate testing
TEST_DB = "tests.db"

# test working cases
create_table(TEST_DB)

def test_create_doc():
    created_file = create_doc(TEST_DB, "test.txt", "Hello, World!")
    assert created_file == True

def test_read_doc():
    read_content = read_doc(TEST_DB, "test.txt")
    assert read_content == "Hello, World!"

def test_edit_doc():
    create_doc(TEST_DB, "edit.txt", "Original")
    edited_content = edit_doc(TEST_DB, "edit.txt", "Updated")
    assert edited_content == True

    read_content = read_doc(TEST_DB, "edit.txt")
    assert read_content == "Updated"

def test_delete_doc():
    deleted_file = delete_doc(TEST_DB, "edit.txt")
    assert deleted_file is True


# test error cases
def fail_connect(*args, **kwargs):
    raise sqlite3.DatabaseError("Simulated DB error")

def test_create_table_exception(monkeypatch, capsys):
    monkeypatch.setattr(sqlite3, "connect", fail_connect)
    create_table("fake.db")
    captured = capsys.readouterr()
    assert "Error creating table: Simulated DB error" in captured.out

def test_create_doc_exception(monkeypatch):
    monkeypatch.setattr(sqlite3, "connect", fail_connect)
    created_file = create_doc(TEST_DB, "fail.txt", "Test content")
    assert created_file is False

def test_read_doc_exception(monkeypatch):
    monkeypatch.setattr(sqlite3, "connect", fail_connect)
    read_content = read_doc(TEST_DB, "fail.txt")
    assert read_content is False

def test_edit_doc_exception(monkeypatch):
    monkeypatch.setattr(sqlite3, "connect", fail_connect)
    edited_content = edit_doc(TEST_DB, "fail.txt", "new content")
    assert edited_content is False

def test_delete_doc_exception(monkeypatch):
    monkeypatch.setattr(sqlite3, "connect", fail_connect)
    deleted_file = delete_doc(TEST_DB, "fail.txt")
    assert deleted_file is False

def test_delete_doc_nonexistent():
    deleted_file = delete_doc(TEST_DB, "doesnotexist.txt")
    assert deleted_file is False
