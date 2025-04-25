# # tests made with ChatGPT and modified
# import os
# import pytest
# import docx
# import fitz  # PyMuPDF
# from unittest.mock import MagicMock, patch
#
#
#
# # parser.py tests
# from analyzer.parser import *
#
# def test_load_txt(tmp_path):
#     content = "Hello from a .txt file!"
#     txt_path = tmp_path / "test.txt"
#     txt_path.write_text(content)
#
#     assert load_document(str(txt_path)) == content
#     assert extract_text_from_txt(str(txt_path)) == content
#
#
# def test_load_docx(tmp_path):
#     content = "Hello from a .docx file!"
#     docx_path = tmp_path / "test.docx"
#
#     # Create DOCX file
#     doc = docx.Document()
#     doc.add_paragraph(content)
#     doc.save(docx_path)
#
#     assert load_document(str(docx_path)) == content
#     assert extract_text_from_docx(str(docx_path)) == content
#
#
# def test_load_pdf(tmp_path):
#     content = "Hello from a PDF file!"
#     pdf_path = tmp_path / "test.pdf"
#
#     # Create a simple PDF file using PyMuPDF
#     doc = fitz.open()
#     page = doc.new_page()
#     page.insert_text((72, 72), content)
#     doc.save(pdf_path)
#     doc.close()
#
#     # Extract and verify
#     extracted = load_document(str(pdf_path))
#     assert content in extracted
#     assert content in extract_text_from_pdf(str(pdf_path))
#
# def test_load_unsupported_file(tmp_path):
#     fake_path = tmp_path / "test.xyz"
#     fake_path.write_text("some data")
#
#     with pytest.raises(ValueError, match=r"Unsupported file extension.*"):
#         load_document(str(fake_path))
#
#
#
# # llm.py tests
# # from analyzer.llm import ask_llm
# #
# # @patch("llm.client.chat.completions.create")
# # def test_ask_llm(mock_create):
# #     # Setup mock response
# #     mock_response = MagicMock()
# #     mock_response.choices = [MagicMock(message=MagicMock(content="Mocked response"))]
# #     mock_create.return_value = mock_response
# #
# #     # Call the function
# #     prompt = "What is the capital of France?"
# #     response = ask_llm(prompt)
# #
# #     # Assertions
# #     assert response == "Mocked response"
# #     mock_create.assert_called_once_with(
# #         model="gpt-4-turbo",
# #         messages=[{"role": "user", "content": prompt}]
# #     )
# #
# # def test_ask_llm_invalid_input():
# #     with pytest.raises(TypeError):
# #         ask_llm(None)  # Or pass an int, list, etc.
#
#
#
# # grader.py tests
# from analyzer.grader import *
#
# @patch("grader.ask_llm")
# def test_grade_document(mock_ask_llm):
#     content = "This is the student's essay about climate change."
#     rubric = "Clarity, Argument strength, Use of evidence, Grammar"
#
#     # Define what the mock should return
#     mock_response = "Score: 8/10. The essay was clear and well-argued, but lacked strong evidence."
#     mock_ask_llm.return_value = mock_response
#
#     # Call the function
#     result = grade_document(content, rubric)
#
#     # Assertions
#     assert result == mock_response
#     mock_ask_llm.assert_called_once_with(
#         f"Grade this student essay based on the following rubric: {rubric}.\n"
#         f"Give a score out of 10 and explain your reasoning:\n{content}"
#     )
#
# @patch("grader.ask_llm")
# def test_grade_document_empty_input(mock_ask_llm):
#     mock_ask_llm.return_value = "Score: 0/10. No content provided."
#     result = grade_document("", "")
#     assert "0/10" in result
#
#
#
# # generator.py tests
# from analyzer.generator import *
#
# @patch("generator.ask_llm")
# def test_create_mc(mock_ask_llm):
#     mock_ask_llm.return_value = "Mocked MC questions"
#     content = "Photosynthesis is a process..."
#     number = 3
#
#     result = create_mc(content, number)
#     assert result == "Mocked MC questions"
#     mock_ask_llm.assert_called_once_with(
#         f"Based on the following content, generate {number} multiple choice questions with answers:\n{content}"
#     )
#
# @patch("generator.ask_llm")
# def test_create_tf(mock_ask_llm):
#     mock_ask_llm.return_value = "Mocked TF questions"
#     content = "The heart pumps blood..."
#     number = 2
#
#     result = create_tf(content, number)
#     assert result == "Mocked TF questions"
#     mock_ask_llm.assert_called_once_with(
#         f"Based on the following content, generate {number} true or false questions with answers:\n{content}"
#     )
#
# @patch("generator.ask_llm")
# def test_create_fill(mock_ask_llm):
#     mock_ask_llm.return_value = "Mocked fill-in-the-blank"
#     content = "Gravity is a force that..."
#     number = 4
#
#     result = create_fill(content, number)
#     assert result == "Mocked fill-in-the-blank"
#     mock_ask_llm.assert_called_once_with(
#         f"Based on the following content, generate {number} fill in the blank questions with answers:\n{content}"
#     )
#
# @patch("generator.ask_llm")
# def test_create_fc(mock_ask_llm):
#     mock_ask_llm.return_value = "Mocked flashcards"
#     content = "Newton's Laws of Motion..."
#     number = 5
#
#     result = create_fc(content, number)
#     assert result == "Mocked flashcards"
#     mock_ask_llm.assert_called_once_with(
#         f"Based on the following content, generate {number} flashcard terms with answers:\n{content}"
#     )
#
# @patch("generator.ask_llm")
# def test_create_sg(mock_ask_llm):
#     mock_ask_llm.return_value = "Mocked study guide"
#     content = "The Cold War was a period of..."
#
#     result = create_sg(content)
#     assert result == "Mocked study guide"
#     mock_ask_llm.assert_called_once_with(
#         f"Based on the following content, generate 1 study guide with answers:\n{content}"
#     )
#
#
#
# # feedback.py tests
# from analyzer.feedback import *
#
# @patch("feedback.ask_llm")
# def test_provide_feedback(mock_ask_llm):
#     mock_ask_llm.return_value = "Mocked feedback: Great structure but needs grammar improvements."
#     content = "This is a sample student essay that has some grammar issues."
#
#     result = provide_feedback(content)
#
#     # Assert returned value is mocked response
#     assert result == "Mocked feedback: Great structure but needs grammar improvements."
#
#     # Assert correct prompt was constructed
#     mock_ask_llm.assert_called_once_with(
#         f"You are an experienced teacher. Provide constructive feedback on this document:\n{content}"
#     )
