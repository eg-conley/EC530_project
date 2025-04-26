# tests made with ChatGPT and modified
# llm.py tests

# python -m coverage run -m pytest -s
# python coverage report -m

import pytest, os
from analyzer.llm import ask_llm
from unittest.mock import patch, MagicMock

os.environ["OPENAI_API_KEY"] = "test-key"

@patch("analyzer.llm.client.chat.completions.create")
def test_ask_llm(mock_create):
    # mock response
    mock_response = MagicMock()
    mock_response.choices = [MagicMock(message=MagicMock(content="Response"))]
    mock_create.return_value = mock_response

    # call the function
    prompt = "Prompt"
    response = ask_llm(prompt)

    # verify
    assert response == "Response"
    mock_create.assert_called_once_with(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

def test_ask_llm_invalid_input():
    with pytest.raises(TypeError, match="Prompt must be a string"):
        ask_llm(1)