class Task:
    def __init__(self, task_id, header, task_text, create_date):
        self.__task_id = task_id
        self.header = header
        self.__task_text = task_text
        self.create_date = create_date

    def get_task_id(self):
        return self.__task_id

    def get_header(self):
        return self.header

    def get_task_text(self):
        return self.__task_text

    def get_date(self):
        return self.create_date

    def set_header(self, header):
        self.header = header

    def set_task_text(self, task_text):
        self.__task_text = task_text

