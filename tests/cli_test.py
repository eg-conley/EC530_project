# # tests made with ChatGPT and modified
# from unittest.mock import patch
# import io
# import sys
# from analyzer.cli import *
#
# # Test for the "help" command
# @patch("builtins.input", return_value="help")
# @patch("sys.stdout", new_callable=io.StringIO)  # Capture printed output
# def test_help_command(mock_stdout, mock_input):
#     application_cli()  # Call the CLI method
#     output = mock_stdout.getvalue()
#
#     # Check if help message is printed
#     assert "Available commands:" in output
#     assert "create <document_path>" in output
#
# # Test for the "exit" command
# @patch("builtins.input", return_value="exit")
# @patch("sys.stdout", new_callable=io.StringIO)
# def test_exit_command(mock_stdout, mock_input):
#     with patch("builtins.exit") as mock_exit:
#         application_cli()
#         mock_exit.assert_called_once()  # Ensure exit was called
#
# # Test for the "list" command when there are documents in the database
# @patch("builtins.input", return_value="list")
# @patch("sys.stdout", new_callable=io.StringIO)
# @patch("database.operations.list_doc", return_value=[("doc1.txt",), ("doc2.txt",)])
# @patch("database.operations.count_doc", return_value=(2,))
# def test_list_documents(mock_count, mock_list, mock_stdout, mock_input):
#     application_cli()  # Simulate user input
#     output = mock_stdout.getvalue()
#
#     assert "2 documents:" in output
#     assert "doc1.txt" in output
#     assert "doc2.txt" in output
#
# # Test for the "create" command (mocking the file loading)
# @patch("builtins.input", return_value="create doc1.txt")
# @patch("sys.stdout", new_callable=io.StringIO)
# @patch("analyzer.parser.load_document", return_value="Document content here")
# @patch("database.operations.create_doc")
# def test_create_document(mock_create, mock_load, mock_stdout, mock_input):
#     application_cli()
#     mock_create.assert_called_once_with("test.db", "doc1.txt", "Document content here")
#     output = mock_stdout.getvalue()
#     assert "Document created successfully." in output  # Ensure proper output after creation
#
# # Test for the "edit" command (mocking file content edit)
# @patch("builtins.input", side_effect=["edit doc1.txt", "New content for doc1.txt"])
# @patch("sys.stdout", new_callable=io.StringIO)
# @patch("analyzer.parser.read_doc", return_value="Old content")
# @patch("database.operations.edit_doc")
# def test_edit_document(mock_edit, mock_read, mock_stdout, mock_input):
#     application_cli()
#     mock_edit.assert_called_once_with("test.db", "doc1.txt", "New content for doc1.txt")
#     output = mock_stdout.getvalue()
#     assert "Document edited successfully." in output
#
# # Test for the "feedback" command (mocking feedback generation)
# @patch("builtins.input", return_value="feedback doc1.txt")
# @patch("sys.stdout", new_callable=io.StringIO)
# @patch("analyzer.parser.read_doc", return_value="This is the document content.")
# @patch("analyzer.feedback.provide_feedback", return_value="Feedback: Improve grammar.")
# @patch("outputs.writeback.write_back")
# def test_feedback_command(mock_writeback, mock_feedback, mock_read, mock_stdout, mock_input):
#     application_cli()
#     mock_feedback.assert_called_once_with("This is the document content.")
#     mock_writeback.assert_called_once_with("Feedback: Improve grammar.")
#     output = mock_stdout.getvalue()
#     assert "Feedback: Improve grammar." in output
#
# # Test for the "grade" command (mocking grading)
# @patch("builtins.input", side_effect=["grade doc1.txt rubric.txt"])
# @patch("sys.stdout", new_callable=io.StringIO)
# @patch("analyzer.parser.read_doc", return_value="This is the student essay.")
# @patch("analyzer.grader.grade_document", return_value="Score: 8/10. Needs improvement in argument strength.")
# @patch("outputs.writeback.write_back")
# def test_grade_command(mock_writeback, mock_grade, mock_read, mock_stdout, mock_input):
#     application_cli()
#     mock_grade.assert_called_once_with("This is the student essay.", "This is the rubric content.")
#     mock_writeback.assert_called_once_with("Score: 8/10. Needs improvement in argument strength.")
#     output = mock_stdout.getvalue()
#     assert "Score: 8/10" in output
#
# # Test for the "generate" command (mocking content generation)
# @patch("builtins.input", side_effect=["generate doc1.txt mc 5"])
# @patch("sys.stdout", new_callable=io.StringIO)
# @patch("analyzer.parser.read_doc", return_value="This is the document content for generating MC questions.")
# @patch("analyzer.generator.create_mc", return_value="Mocked MC Questions")
# @patch("outputs.writeback.write_back")
# def test_generate_mc_command(mock_writeback, mock_create_mc, mock_read, mock_stdout, mock_input):
#     application_cli()
#     mock_create_mc.assert_called_once_with("This is the document content for generating MC questions.", "5")
#     mock_writeback.assert_called_once_with("Mocked MC Questions")
#     output = mock_stdout.getvalue()
#     assert "Mocked MC Questions" in output
#
