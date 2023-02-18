import pandas as pd

class FileOperation:
    def read_all_lines(self, file_name):
        return pd.read_csv(file_name, delimiter=",")


