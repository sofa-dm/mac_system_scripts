import os


class FileManager:
    """
    Args:
        # todo: дописать аргументы
    Methods:
        obj_name.help() - show docstring
        obj_name.howto() - show how to use program

    Private methods:
        # todo: дописать аргументы
    """
    def __init__(self, *kwargs):
        for i, v in kwargs:
            print(i, v)

    @staticmethod
    def __set_config(self, path):  # where path is full path to home directory
        where_to = ''
        pass

    def copy_to_dir(self, where_to):
        # print(self.kwargs)
        # todo:
        pass

    def __is_exists(self, path_to_file):
        pass





print('hello again')

files_directories = {'zshrc': '', 'vimrc': ''}

files = FileManager()

# Get the current working directory
cwd = os.getcwd()

# Print the current working directory
print("Current working directory: {0}".format(cwd))

home_directory = '/Users/dm'

os.chdir(home_directory)


# Get the current working directory
cwd = os.getcwd()

# Print the current working directory
print("Current working directory: {0}".format(cwd))














