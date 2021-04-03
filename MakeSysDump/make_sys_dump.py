import os
import shutil
import os

# function to copy full directory

def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

with open('/Users/dm/Dev/mac_system_scripts/MakeSysDump/make_sys_dump.conf', 'r') as conf:
    conf = conf.read()

    # parse conf file to dictionary {'home_directory': '/usr/dm/dev'}
    conf = conf.split('\n')[1:]
    conf_dict = {}
    for i in conf:
        parameter = i.split(':')
        if len(parameter) == 2:
            conf_dict[parameter[0]] = parameter[1].lstrip().rstrip()

# generate full path to file: home_path+fle_name
conf_dict['files_to_copy'] = [conf_dict['home_directory'] + '/' + file_path.lstrip().rstrip() for file_path in conf_dict['files_to_copy'].split(',')]

print(conf_dict['files_to_copy'])

# copying files
for file in conf_dict['files_to_copy']:
    home_dir = conf_dict['home_directory']
    backup_folder = conf_dict['backups_folder']
    # copy
    print(os.path.exists(conf_dict['backups_folder'] + '/' + file))
    shutil.copy(file, conf_dict['backups_folder'])
    shutil.copytree(file, conf_dict['backup_folder'], ignore=shutil.ignore_patterns(".*"))

print(conf_dict['home_directory'])






