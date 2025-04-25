# tests made with ChatGPT and modified
import os
import builtins
from unittest import mock

from outputs.writeback import *

def test_write_back_yes(monkeypatch,capsys):
    test_filename = "response.txt"
    test_content = "Hello, world!"

    # mock input responses: first invalid input, then "y", then filename
    inputs = iter(["neither", "y", test_filename])
    monkeypatch.setattr(builtins, "input", lambda prompt: next(inputs))
    written_content = write_back(test_content)

    # check file created and its content
    captured = capsys.readouterr()
    assert "Please enter either 'y' or 'n'" in captured.out

    test_path = os.path.join("outputs", test_filename)
    assert written_content == len(test_content)
    assert os.path.exists(test_path)
    with open(test_path, "r") as f:
        assert f.read() == test_content

    # clean up
    os.remove(test_path)


def test_write_back_no(monkeypatch):
    test_filename = "output.txt"
    test_content = "This won't be saved"

    # mock input to decline writing
    monkeypatch.setattr(builtins, "input", lambda prompt: "n" if "write this" in prompt else test_filename)
    written_content = write_back(test_content)

    # should return None and not create a file
    assert written_content is None