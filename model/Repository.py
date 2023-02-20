import pandas as pd


class Repository:

    # def __init__(self, file_operation):
    #     self.file_operation = file_operation

    def create_task(self, header, task_text, create_date):
        task_to_list = [{'header': header, 'task text': task_text, 'date': create_date}]
        df = pd.DataFrame(task_to_list)
        return df

    def save_task_csv(self, df, file_name):
        df.to_csv(file_name)

    def save_task_json(self, task, file_name):
        task.to_json(file_name)

    def find_task(self, data_frame, find_by, find_name):
        task = data_frame[data_frame[find_by] == find_name]
        print(task)
        return task

    def update_task(self, data_frame, find_function):
        task = find_function(data_frame, )
