import datetime
import pandas as pd


class Repository:

    def __init__(self, file_operation):
        self.file_operation = file_operation



    def create_task(self):
        header = input('Insert header: ')
        task_text = input('Insert task_text: ')
        create_date = datetime.datetime.now().strftime("%d/%m/%Y")
        task = [{'header': header, 'task text': task_text, 'date': create_date}]
        df = pd.DataFrame(task)
        return df

    def save_task_csv(self, df, file_name):
        self.file_operation.save_csv(file_name, df)

    def save_task_json(self, df, file_name):
        self.file_operation.save_json(file_name, df)

    def find_task(self, df):
        find_by_question = input('Find by\n'
                                 'ID\n'
                                 'header\n'
                                 'date\n')
        find_name = input('Input: ')
        if find_by_question == 'ID':
            find_name = int(find_name)
        task = df.loc[df[find_by_question] == find_name]
        return task

    def update_task(self, df, file_name):
        task = self.find_task(df)
        index_odject = task.index
        task_index = index_odject[0]
        what_update = input('What you want to update\n'
                            'header\n'
                            'task text\n'
                            'whole task\n')
        update_task = input('Input: ')
        df.at[task_index, what_update] = update_task
        df.to_csv(file_name, index=False)

    def delete_task(self, df, file_name):
        task = self.find_task(df)
        index_odject = task.index
        task_index = index_odject[0]
        sure_question = input('Are you sure:\n'
                              'yes\n'
                              'no\n')
        if sure_question == 'yes':
            df.drop(labels=[task_index], axis=0, inplace=True)
            df.to_csv(file_name, index=False)