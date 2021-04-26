#!/bin/bash
# Put script somewhere and add "source path/to/this/file.sh" to .bashrc file.
killport () {
   echo 'What port to kill ?'
   read port
   lsof -n -i4TCP:$port
   echo 'Write <PID> of the process.'
   read pid
   kill -9 $pid
}