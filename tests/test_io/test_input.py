# test_input.py

import unittest
from app.io.input import *
import os
import pandas

class TestInputFunctions(unittest.TestCase):

    def setUp(self):
        os.makedirs('data', exist_ok=True)

        self.text_file_path = 'test_input.txt'
        with open(self.text_file_path, 'w', encoding='utf-8') as file:
            file.write('Hello, world!\nI wrote something in this file.')

        self.csv_file_path = 'test_input.csv'
        df = pandas.DataFrame({'first': [1, 2], 'second': ['a', 'b']})
        df.to_csv(self.csv_file_path, index=False)

    def tearDown(self):
        os.remove(self.text_file_path)
        os.remove(self.csv_file_path)

    def test_read_file(self):
        content = read_file(self.text_file_path)
        self.assertEqual(content, 'Hello, world!\nI wrote something in this file.')

    def test_read_file_nonexistent(self):
        with self.assertRaises(FileNotFoundError):
            read_file('nonexistent.txt')

    def test_read_file_empty(self):
        empty_file_path = 'empty.txt'
        with open(empty_file_path, 'w', encoding='utf-8'):
            pass
        content = read_file(empty_file_path)
        self.assertEqual(content, '')
        os.remove(empty_file_path)

    def test_read_file_pandas(self):
        content = read_file_pandas(self.csv_file_path)
        expected_content = '   first second\n0      1      a\n1      2      b'
        self.assertEqual(content, expected_content)

    def test_read_file_pandas_nonexistent(self):
        with self.assertRaises(FileNotFoundError):
            read_file_pandas('nonexistent.csv')

    def test_read_file_pandas_empty(self):
        empty_csv_path = 'empty.csv'
        pandas.DataFrame().to_csv(empty_csv_path, index=False)
        content = read_file_pandas(empty_csv_path)
        self.assertEqual(content, 'Empty DataFrame')
        os.remove(empty_csv_path)

if __name__ == '__main__':
    unittest.main()