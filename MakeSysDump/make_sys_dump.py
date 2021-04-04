#!/usr/local/bin/python3
import os
import shutil
import pathlib
from datetime import datetime

dt = str(datetime.now()).split(' ')
backup_name = 'backup_from_' + dt[0] + '_' + dt[1].split('.')[0].rstrip(':').replace(':', '-')[:-3]
print(backup_name)

current_path = '/Users/dm/Dev/mac_system_scripts/MakeSysDump'

pathlib.Path(f"{current_path}/backups/{backup_name}").mkdir(parents=True, exist_ok=True)

# Copy Files
# .zaliases, .dircolors, .hushlogin, .vimrc, .zcompdump, .zprofile, .zsh_history, .zshrc
#
print(shutil.copyfile('/Users/dm/.zaliases', f"{current_path}/backups/{backup_name}/.zaliases"))
print(shutil.copyfile('/Users/dm/.hushlogin', f"{current_path}/backups/{backup_name}/.hushlogin"))
print(shutil.copyfile('/Users/dm/.vimrc', f"{current_path}/backups/{backup_name}/.vimrc"))
print(shutil.copyfile('/Users/dm/.zcompdump', f"{current_path}/backups/{backup_name}/.zcompdump"))
print(shutil.copyfile('/Users/dm/.zprofile', f"{current_path}/backups/{backup_name}/.zprofile"))
print(shutil.copyfile('/Users/dm/.zshrc', f"{current_path}/backups/{backup_name}/.zshrc"))


# Copy directory
shutil.copytree('/Users/dm/.dircolors', f"{current_path}/backups/{backup_name}/.dircolors", ignore=shutil.ignore_patterns(".*"))






