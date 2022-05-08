#usr/bin/python3

import os
import unittest

from data_loader import DataSource


class TestDataSource(unittest.TestCase):
    

    def setUp(self):
        # create empty csv file
        empty_file_name = 'empty_file.csv'
        if os.path.isfile(empty_file_name):
            os.remove(empty_file_name)
        with open(empty_file_name, "w") as f:
            f.write("")

        # create csv file with one row
        one_row_file_name = 'one_row_file.csv'
        if os.path.isfile(one_row_file_name ):
            os.remove(one_row_file_name)
        with open(one_row_file_name, "w") as f:
            f.write("1")

        # create csvfile with two rows
        two_rows_file_name = 'two_rows_file.csv'
        if os.path.isfile(two_rows_file_name ):
            os.remove(two_rows_file_name)
        with open(two_rows_file_name, "w") as f:
            f.write("first row\n")
            f.write("second row")

        # create csvfile with two rows two cols
        two_rows_two_cols_name = 'two_rows_two_cols_file.csv'
        if os.path.isfile(two_rows_two_cols_name ):
            os.remove(two_rows_two_cols_name)
        with open(two_rows_two_cols_name, "w") as f:
            f.write("1-1,1-2\n")
            f.write("2-1,2-2")

        # create tsvfile with two rows two cols
        tsv_two_rows_two_cols_name = 'tsv_two_rows_two_cols_file.tsv'
        if os.path.isfile(tsv_two_rows_two_cols_name ):
            os.remove(tsv_two_rows_two_cols_name)
        with open(tsv_two_rows_two_cols_name, "w") as f:
            f.write("1-1\t1-2\n")
            f.write("2-1\t2-2")


    def tearDown(self):
        os.remove('empty_file.csv')
        os.remove('one_row_file.csv')
        os.remove('two_rows_file.csv')
        os.remove('two_rows_two_cols_file.csv')
        os.remove('tsv_two_rows_two_cols_file.tsv')


    def test_DataSource_ingest_csv_fails_with_no_arguments(self):
        with self.assertRaises(SyntaxError):
            DataSource()


    def test_DS_ingest_csv_fails_with_two_arguments(self):
        with self.assertRaises(SyntaxError):
            DataSource("first_arg", "second_arg")


    def test_DS_ingest_csv_refuses_a_keyword_argument_that_isnt_path(self):
        with self.assertRaises(SyntaxError):
            DataSource(not_path="just_one_arg")


    def test_DS_ingest_csv_refuses_to_open_txt_file(self):
        with self.assertRaises(ValueError):
            DataSource("wrong_extension.txt")


    def test_DS_ingest_csv_alerts_for_nonexisting_file(self):
        with self.assertRaises(ValueError):
            DataSource("non_existing_file.csv")


    def test_DS_ingest_csv_returns_empty_list_for_missing_file(self):
        data = DataSource('empty_file.csv').get_data()
        self.assertEqual([], data)


    def test_DS_ingest_csv_returns_data_for_file_with_one_row_one_col(self):
        data = DataSource('one_row_file.csv').get_data()
        self.assertEqual([["1"]], data)
        

    def test_DS_ingest_csv_returns_data_for_file_with_two_rows_one_col(self):
        data = DataSource('two_rows_file.csv').get_data()
        self.assertEqual([["first row"],["second row"]], data)


    def test_DS_ingest_csv_returns_data_for_file_with_two_rows_two_cols(self):
        data = DataSource('two_rows_two_cols_file.csv').get_data()
        self.assertEqual([["1-1", "1-2"],["2-1", "2-2"]], data)


    def test_DS_ingest_tsv_returns_data_for_file_with_two_rows_two_cols(self):
        data = DataSource('tsv_two_rows_two_cols_file.tsv').get_data()
        self.assertEqual([["1-1", "1-2"],["2-1", "2-2"]], data)


    def test_DS_get_file_extension_returns_file_extension(self):
        file_extension = DataSource('two_rows_two_cols_file.csv').get_file_extension()
        self.assertEqual('.csv', file_extension)
        file_extension = DataSource('tsv_two_rows_two_cols_file.tsv').get_file_extension()
        self.assertEqual('.tsv', file_extension)


    def test_DS_get_column_headers_returns_first_row_of_data(self):
        ds = DataSource('two_rows_two_cols_file.csv')
        data = ds.get_data()
        headers = ds.get_headers()
        self.assertEqual(['1-1', '1-2'], headers)
