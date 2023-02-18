from model.FileOperation import FileOperation
from model.Repository import Repository

class Main:
    if __name__ == "__main__":
        fo = FileOperation()
        file_name = 'test.csv'
        # print(fo.read_all_lines(file_name))
        ro = Repository(fo)
        ro.create_task('fsfsdf','dfdsfds','11.22.3231',file_name)


