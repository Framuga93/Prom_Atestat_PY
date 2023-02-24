from Home_Work.PromAtest_PY.model.Repository import Repository


class Controller:

    def __init__(self, __repository):
        self.__repository = __repository

    def create_task(self, task, file_name, format_question):
        if format_question == 1:
            self.__repository.save_task_csv(self.__repository.create_task(task[0], task[1], task[2])
                                            , file_name)
        if format_question == 2:
            self.__repository.save_task_json(self.__repository.create_task(task[0], task[1], task[2])
                                             , file_name)
