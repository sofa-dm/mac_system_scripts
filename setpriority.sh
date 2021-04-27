#!/bin/bash
# Put script somewhere and add "source path/to/this/file.sh" to .bashrc file.
rar () {
    # Function to set proccess priority using <PID>
    YELLOW='\033[0;33m'
    NC='\033[0m' # No Color

    echo ""

    read port
    lsof -n -i4TCP:$port

   echo "${YELLOW}To unrar file write filename.rar${NC} "
   read file
   unrar x $file
}

read v
case $v in
1)
    echo "Creating file $v"
    # touch $v
    ;;
2)
    echo "Creating dir $v"
    # mkdir $2
    ;;
*)
    echo "Wrong value!"
esac