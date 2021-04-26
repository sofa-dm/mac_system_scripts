#!/bin/bash
# Put script somewhere and add "source path/to/this/file.sh" to .bashrc file.
killport () {
   YELLOW='\033[0;33m'
   NC='\033[0m' # No Color

   printf "${YELLOW}What port to kill ?${NC} "
   read port
   lsof -n -i4TCP:$port
   printf "${YELLOW}Write <PID> of the process.${NC} "
   read pid
   kill -9 $pid
}