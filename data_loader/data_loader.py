#usr/bin/python3

import csv
import os

class DataSource(object):

    data = []
    file_extension = None
    supported_file_extensions = {".csv", ".tsv"}
    headers = []


    def get_file_extension_from_path(self):
        return self.file_path[-4:]


    def set_file_path(self, *args, **kwargs):
        file_path = None
        if args:
            file_path = args[0]
        elif kwargs:
            file_path = kwargs.values()["path"]

        return file_path


    def arguments_are_valid(self, *args, **kwargs):
        # check how many arguments we got
        if len(args) + len(kwargs.keys()) != 1:
            raise SyntaxError(f"Please provide one single argument. You provided {len(args)} args and {len(kwargs.keys())}"
            f" kwargs.\n {[arg for arg in args]}")
        # check if we got keyword arguments other than "path"
        if kwargs:
            if "path" not in kwargs:
                raise SyntaxError("Just provide the `path` argument.")
        return True


    def file_in_path_exists(self):
        # check if file exists
        if not os.path.isfile(self.file_path):
            raise ValueError(f"Path {self.file_path} doesn't exist.")
        return True
        

    def file_extension_is_supported(self):
        #check for file extension
        if self.get_file_extension_from_path() not in self.supported_file_extensions:
            raise ValueError(f"Received {self.file_path}. Please provide a file with any of the following extensions: {self.supported_file_extensions}")
        return True
        

    def validate_path(self):
        if self.file_in_path_exists() and self.file_extension_is_supported():
            return True
        

    def ingest_data(self):
        if self.file_extension == '.csv':
            return self.ingest_csv()
        elif self.file_extension == '.tsv':
            return self.ingest_tsv()


    def ingest_csv(self):
        csvdata = []
        with open(self.file_path, newline='\n') as csvfile:
            reader = csv.reader(csvfile, delimiter = ',')
            for row in reader:
                csvdata.append(row)
        return csvdata


    def ingest_tsv(self):
        tsvdata = []
        with open(self.file_path, newline='\n') as tsvfile:
            reader = csv.reader(tsvfile, delimiter = '\t')
            for row in reader:
                tsvdata.append(row)
        return tsvdata


    def get_data(self):
        return self.data


    def get_file_extension(self):
        return self.file_extension


    def get_headers(self):
        return self.headers

    def __init__(self, *args, **kwargs):
        if self.arguments_are_valid(*args, **kwargs):
            self.file_path = self.set_file_path(*args, **kwargs)
            if self.validate_path():
                self.file_extension = self.get_file_extension_from_path()
                self.data = self.ingest_data()
                if self.data != []:
                    self.headers = self.data[0]


