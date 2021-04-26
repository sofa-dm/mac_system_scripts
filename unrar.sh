#!/bin/bash
# Put script somewhere and add "source path/to/this/file.sh" to .bashrc file.
rar () {
   YELLOW='\033[0;33m'
   NC='\033[0m' # No Color

   echo "${YELLOW}To unrar file write filename.rar${NC} "
   read file
   unrar x $file
}