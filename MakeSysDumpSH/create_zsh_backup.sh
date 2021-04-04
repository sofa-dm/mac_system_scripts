#!/bin/zsh

## To get executable rights use 
## chmod u+x startup.sh

echo 'Hello! Script will create backup of your config files and directories\nand put backup to Desktop.'
echo '- .zshrc - zsh config';
echo '- .vimrc - vim config';
echo '- .dircolors - colorized LS';
echo '- .hushlogin - do not show sal session in terminal';
echo '- .zaliases - my alieases';
echo '- .zprofile';

echo 'Press ENTER to continue'
read ok;

cd ~;
mkdir Desktop/zsh_backup_$(date +"%d-%m-%Y");

# Copy files
cp .zshrc Desktop/zsh_backup_$(date +"%d-%m-%Y");
cp .vimrc Desktop/zsh_backup_$(date +"%d-%m-%Y");
cp .hushlogin Desktop/zsh_backup_$(date +"%d-%m-%Y");
cp .zaliases Desktop/zsh_backup_$(date +"%d-%m-%Y");
cp .zprofile Desktop/zsh_backup_$(date +"%d-%m-%Y");

# Copy directores
mkdir Desktop/zsh_backup_$(date +"%d-%m-%Y")/.dircolors/;
cp -R .dircolors/* Desktop/zsh_backup_$(date +"%d-%m-%Y")/.dircolors/;

ls -l Desktop/zsh_backup_$(date +"%d-%m-%Y")/;

echo 'Completed'
read ok;


cd ~;
