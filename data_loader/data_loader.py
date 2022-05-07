#usr/bin/python3

import csv
import os

class DataSource(object):

    def load_csv(*args, **kwargs):

        # check how many arguments we got
        if len(args) + len(kwargs.keys()) != 1:
            raise SyntaxError("Please provide one single argument.")

        # check if we got keyword arguments other than "path"
        if kwargs:
            if "path" not in kwargs:
                raise SyntaxError("Please provide the `path` argument.")

        # name argument
        if args:
            path = args[0]
        else:
            path = kwargs.values()[0]

        #check for file extension
        if path[-4:] != ".csv":
            raise ValueError(f"Received {path}. Please provide a file with extension `.csv`.")

        # check if file exists
        if not os.path.isfile(path):
            raise ValueError(f"Path {path} doesn't exist.")


        data = []
        with open(path, newline='\n') as csvfile:
            reader = csv.reader(csvfile, delimiter = ',')
            for row in reader:
                data.append(row)
            
        return data


        


