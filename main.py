from model.FileOperation import FileOperation
from model.Repository import Repository
from view.view import View
from controller.Controller import Controller


class Main:
    if __name__ == "__main__":
        fo = FileOperation()
        file_name = 'test.csv'
        # print(fo.read_all_lines(file_name))
        ro = Repository()
        co = Controller(ro)
        vw = View(co)
        vw.show_menu()

