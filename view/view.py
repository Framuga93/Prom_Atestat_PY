class View:

    def __init__(self, controller):
        self.controller = controller

    def show_menu(self):
        while True:
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

                format_question = int(input('What format you like?\n'
                                            '1. CSV\n'
                                            '2. JSON\n'))

                if format_question == 1:
                    file_name = input('Insert file name: ') + '.csv'
                    self.controller.create_task(file_name, format_question)

                if format_question == 2:
                    file_name = input('Insert file name: ') + '.json'
                    self.controller.create_task(file_name, format_question)

            if command == 'find':
                task = self.controller.find_task(self.get_file_name())
                print(f'______________________'
                      f'\n{task}\n'
                      f'______________________')

            if command == 'update':
                self.controller.update_task(self.get_file_name())

            if command == 'delete':
                self.controller.del_task(self.get_file_name())

            if command == 'exit':
                print('Bye bye')
                break

            else:
                print('Incorrect COMMAND\n'
                      'Try again!\n')

    def get_file_name(self):
        return input('Insert file name with format (Example: task.csv): ')
