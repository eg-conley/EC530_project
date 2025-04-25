# tests made with ChatGPT and modified
# grader.py tests

# python -m coverage run -m pytest -s
# python coverage report -m

from analyzer.grader import *
from unittest.mock import patch, MagicMock

@patch("analyzer.grader.client.chat.completions.create")
def test_grade_document(mock_create):
    # mock a valid OpenAI-style response
    mock_response = MagicMock()
    mock_response.choices = [MagicMock(message=MagicMock(content="Grade"))]
    mock_create.return_value = mock_response

    # call the function
    content = "Student document"
    rubric = "Rubric"
    response = grade_document(content, rubric)

    # verify
    assert response == "Grade"
    mock_create.assert_called_once()
