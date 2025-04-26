# tests made with ChatGPT and modified
# feedback.py tests

# python -m coverage run -m pytest -s
# python coverage report -m

import os
from analyzer.feedback import *
from unittest.mock import patch, MagicMock
os.environ["OPENAI_API_KEY"] = "test-key"

@patch("analyzer.feedback.client.chat.completions.create")
def test_provide_feedback(mock_create):
    # mock a valid OpenAI-style response
    mock_response = MagicMock()
    mock_response.choices = [MagicMock(message=MagicMock(content="Feedback"))]
    mock_create.return_value = mock_response

    # call the function
    content = "Student document"
    response = provide_feedback(content)

    # verify
    assert response == "Feedback"
    mock_create.assert_called_once()
