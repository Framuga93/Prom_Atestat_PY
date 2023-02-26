from os import path
import pandas as pd


class Controller:

    def __init__(self, __repository):
        self.__repository = __repository

    def create_task(self, file_name, format_question):
        if format_question == 1:
            self.__repository.save_task_csv(self.__repository.create_task(), file_name)
        if format_question == 2:
            self.__repository.save_task_json(self.__repository.create_task(), file_name)

    def find_task(self, file_name):
        df = self.get_df(file_name)
        task = self.__repository.find_task(df)
        return task

    def update_task(self, file_name):
        df = self.get_df(file_name)
        self.__repository.update_task(df, file_name)

    def get_df(self,file_name):
        format_file = path.splitext(file_name)[1]
        df = pd.DataFrame()
        if format_file == '.csv':
            df = pd.read_csv(file_name)
        if format_file == '.json':
            df = pd.read_json(file_name)
        return df

    def del_task(self, file_name):
        df = self.get_df(file_name)
        self.__repository.delete_task(df, file_name)