import unittest
from io import StringIO
from unittest.mock import patch
from main import run_test

class TestRunTest(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_run_test_prints_message(self, mock_stdout):
        run_test()
        self.assertEqual(mock_stdout.getvalue().strip(), "Running to test")

if __name__ == '__main__':
    unittest.main()
