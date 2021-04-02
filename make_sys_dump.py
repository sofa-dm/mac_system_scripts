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

    def __init__(self, *args):
        for i in args:
            print(i)

    @staticmethod
    def set_config():  # path is full path to home directory
        # todo: Uncomment message below. Home directory setting automatically
        # home_directory = input('Where is your home directory? e.g. /Users/dm\n')
        home_directory = '/Users/dm'
        file_dir = os.getcwd()
        os.chdir(home_directory)
        if os.path.exists(home_directory):
            os.chdir(home_directory)
            os.getcwd()
            cwd = os.getcwd()  # Get the current working directory
            print("Home directory is: {0}".format(cwd))  # Print the current working directory
            # Check if configuration file already exists in the script root directory.
            if os.path.exists(f'{file_dir}/make_sys_dump.conf'):
                print('Configuration file already exists. What do we do?\n'
                      'overwrite - to rewrite file\nnothing - break program\n'
                      'use_current - use current .conf file\n'
                      'show conf file')
                # todo: поменять инпут
                # user_input = input()
                user_input = 'use_current'
                if user_input == 'overwrite':
                    # create conf file as new
                    with open(f'{file_dir}/make_sys_dump.conf', 'w+') as f:
                        f.write(f'[make sys dump config file]\n'
                                f'home_directory: {home_directory}')
                elif user_input == 'show conf file':
                    with open(f'{file_dir}/make_sys_dump.conf', 'r') as f:
                        print(f.read())
                else:
                    pass
            else:  # create new file if directory is not exists
                with open(f'{file_dir}/make_sys_dump.conf', 'w+') as f:
                    f.write(f'[make sys dump config file]\n'
                            f'home_directory: {home_directory}')

        else:
            print('Home directory is not set')

    @staticmethod
    def create_backup(self):
        while True:
            user_input = input('Do you want to create backups when new files uploaded? [y, n) ?')
            if user_input == '':
                pass

    def __copy_to_dir(self, where_to):
        # print(self.kwargs)
        # todo:
        pass


# print('hello again')

files_directories = {'.zshrc', '.vimrc', '.aliases', '.zsh_history'}

files = FileManager(files_directories)
files.set_config()
# Get the current working directory
# cwd = os.getcwd()

# Print the current working directory
# print("Current working directory: {0}".format(cwd))
