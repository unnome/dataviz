#usr/bin/python3

import csv
import os

class DataSource(object):

    data = []
    file_extension = None
    supported_file_extensions = {".csv", ".tsv"}


    def get_file_extension(self):
        return self.path[-4:]


    def path_is_validated(self,*args, **kwargs):
        # check how many arguments we got
        if len(args) + len(kwargs.keys()) != 1:
            raise SyntaxError(f"Please provide one single argument. You provided {len(args)} args and {len(kwargs.keys())}"
            f" kwargs.\n {[arg for arg in args]}")
        # check if we got keyword arguments other than "path"
        if kwargs:
            if "path" not in kwargs:
                raise SyntaxError("Just provide the `path` argument.")
            self.path = kwargs.values()["path"]

        if args:
            self.path = args[0]

        # check if file exists
        if not os.path.isfile(self.path):
            raise ValueError(f"Path {self.path} doesn't exist.")
        #check for file extension
        if self.get_file_extension() not in self.supported_file_extensions:
            raise ValueError(f"Received {self.path}. Please provide a file with any of the following extensions: {self.supported_file_extensions}")

        return self.path


    def ingest_data(self):
        if self.file_extension == '.csv':
            return self.ingest_csv()
        elif self.file_extension == '.tsv':
            return self.ingest_tsv()


    def ingest_csv(self):
        csvdata = []
        with open(self.path, newline='\n') as csvfile:
            reader = csv.reader(csvfile, delimiter = ',')
            for row in reader:
                csvdata.append(row)
        return csvdata


    def ingest_tsv(self):
        tsvdata = []
        with open(self.path, newline='\n') as tsvfile:
            reader = csv.reader(tsvfile, delimiter = '\t')
            for row in reader:
                tsvdata.append(row)
        return tsvdata


    def get_data(self):
        return self.data


    def get_extension(self):
        return self.data


    def __init__(self, *args, **kwargs):
        if self.path_is_validated(*args, **kwargs):
            self.file_extension = self.get_file_extension()
            self.data = self.ingest_data()


