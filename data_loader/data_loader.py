#usr/bin/python3

import csv
import os

class DataSource(object):

    data = []

    def path_is_validated(self,*args, **kwargs):
        # check how many arguments we got
        if len(args) + len(kwargs.keys()) != 1:
            raise SyntaxError(f"Please provide one single argument. You provided {len(args)} args and {len(kwargs.keys())}"
            f" kwargs.\n {[arg for arg in args]}")
        # check if we got keyword arguments other than "path"
        if kwargs:
            if "path" not in kwargs:
                raise SyntaxError("Just provide the `path` argument.")

        if args:
            self.path = args[0]
        else:
            self.path = kwargs.values()["path"]

        # check if file exists
        if not os.path.isfile(self.path):
            raise ValueError(f"Path {self.path} doesn't exist.")
        #check for file extension
        if self.path[-4:] != ".csv":
            raise ValueError(f"Received {self.path}. Please provide a file with extension `.csv`.")

        return self.path


    def ingest_csv(self, path):
        csvdata = []
        with open(path, newline='\n') as csvfile:
            reader = csv.reader(csvfile, delimiter = ',')
            for row in reader:
                csvdata.append(row)
            
        return csvdata


    def __init__(self, *args, **kwargs):
        if self.path_is_validated(*args, **kwargs):
            self.data = self.ingest_csv(self.path)


    def get_data(self):
        return self.data
