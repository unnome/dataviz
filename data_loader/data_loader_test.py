#usr/bin/python3

import os
import unittest

from data_loader import DataSource


class TestDataSource(unittest.TestCase):
    

    def setUp(self):
        # create empty file
        empty_file_name = 'empty_file.csv'
        if os.path.isfile(empty_file_name):
            os.remove(empty_file_name)
        with open(empty_file_name, "w") as f:
            f.write("")

        # create file with no headers
        no_headers_file_name = 'no_headers_file.csv'
        if os.path.isfile(no_headers_file_name ):
            os.remove(no_headers_file_name)
        with open(no_headers_file_name, "w") as f:
            f.write("1")


    def tearDown(self):
        os.remove('empty_file.csv')
        os.remove('no_headers_file.csv')

    def test_DataSource_load_csv_fails_with_no_arguments(self):
        with self.assertRaises(SyntaxError):
            DataSource.load_csv()


    def test_DS_load_csv_fails_with_two_arguments(self):
        with self.assertRaises(SyntaxError):
            DataSource.load_csv("first_arg", "second_arg")


    def test_DS_load_csv_refuses_a_keyword_argument_that_isnt_path(self):
        with self.assertRaises(SyntaxError):
            DataSource.load_csv(not_path="just_one_arg")


    def test_DS_load_csv_refuses_to_open_txt_file(self):
        with self.assertRaises(ValueError):
            DataSource.load_csv("wrong_extension.txt")


    def test_DS_load_csv_alerts_for_nonexisting_file(self):
        with self.assertRaises(ValueError):
            DataSource.load_csv("non_existing_file.csv")


    def test_DS_load_csv_returns_empty_list_for_missing_file(self):
        data = DataSource.load_csv('empty_file.csv')
        self.assertEqual([], data)


    def test_DS_load_csv_returns_data_for_file_without_header(self):
        data = DataSource.load_csv('no_headers_file.csv')
        self.assertEqual([["1"]], data)
        
        
