import datetime

import pandas as pd


class View:

    def __init__(self, controller):
        self.controller = controller

    def show_menu(self):
        command = input('__________________________________________________\n'
                        'Welcome to notebook, please take your choose:\n'
                        '__________________________________________________\n'
                        'CREATE task\n'
                        'FIND task\n'
                        'UPDATE task\n'
                        'DELETE task\n'
                        'Exit program\n'
                        '__________________________________________________\n')
        if command == 'create':
            header = input('Insert header: ')
            task_text = input('Insert task_text: ')
            create_date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
            task = [header, task_text, create_date]

            format_question = int(input('What format you like?\n'
                                        '1. CSV\n'
                                        '2. JSON\n'))
            if format_question == 1:
                file_name = input('Insert file name: ') + '.csv'
                self.controller.create_task(task, file_name, format_question)

            if format_question == 2:
                file_name = input('Insert file name: ') + '.json'
                self.controller.create_task(task, file_name, format_question)
        if command == 'find':
            file_name = input('Insert file name with format (Example: task.csv): ')
