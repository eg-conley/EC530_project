# tests made with ChatGPT and modified
# generator.py tests

# python -m coverage run -m pytest -s
# python coverage report -m

# tests made with ChatGPT and modified
# generator.py tests

import os
from autoteacherai.analyzer.generator import *
from unittest.mock import patch, MagicMock
os.environ["OPENAI_API_KEY"] = "test-key"


@patch("autoteacherai.analyzer.generator.client.chat.completions.create")
def test_create_mc(mock_create):
    # mock a valid OpenAI-style response
    mock_response = MagicMock()
    mock_response.choices = [MagicMock(message=MagicMock(content="MC Questions"))]
    mock_create.return_value = mock_response

    # call the function
    content = "Document"
    number = 3
    response = create_mc(content, number)

    # verify
    assert response == "MC Questions"
    mock_create.assert_called_once()

@patch("autoteacherai.analyzer.generator.client.chat.completions.create")
def test_create_tf(mock_create):
    # mock a valid OpenAI-style response
    mock_response = MagicMock()
    mock_response.choices = [MagicMock(message=MagicMock(content="TF Questions"))]
    mock_create.return_value = mock_response

    # call the function
    content = "Document"
    number = 3
    response = create_tf(content, number)

    # verify
    assert response == "TF Questions"
    mock_create.assert_called_once()

@patch("autoteacherai.analyzer.generator.client.chat.completions.create")
def test_create_fill(mock_create):
    # mock a valid OpenAI-style response
    mock_response = MagicMock()
    mock_response.choices = [MagicMock(message=MagicMock(content="Fill in blank Questions"))]
    mock_create.return_value = mock_response

    # call the function
    content = "Document"
    number = 3
    response = create_fill(content, number)

    # verify
    assert response == "Fill in blank Questions"
    mock_create.assert_called_once()

@patch("autoteacherai.analyzer.generator.client.chat.completions.create")
def test_create_fc(mock_create):
    # mock a valid OpenAI-style response
    mock_response = MagicMock()
    mock_response.choices = [MagicMock(message=MagicMock(content="Flashcards"))]
    mock_create.return_value = mock_response

    # call the function
    content = "Document"
    number = 3
    response = create_fc(content, number)

    # verify
    assert response == "Flashcards"
    mock_create.assert_called_once()

@patch("autoteacherai.analyzer.generator.client.chat.completions.create")
def test_create_sg(mock_create):
    # mock a valid OpenAI-style response
    mock_response = MagicMock()
    mock_response.choices = [MagicMock(message=MagicMock(content="Study guide"))]
    mock_create.return_value = mock_response

    # call the function
    content = "Document"
    response = create_sg(content)

    # verify
    assert response == "Study guide"
    mock_create.assert_called_once()