
class Repository:

    def __init__(self, file_operation):
        self.file_operation = file_operation

    def create_task_csv(self, header, task_text, create_date, csv_file_name):
        data_frame = self.file_operation.read_all_lines(csv_file_name)
        data_frame.loc[len(data_frame.index)] = [header, task_text, create_date]
        data_frame.to_csv(csv_file_name, index=False)

