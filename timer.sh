#!/bin/bash
# Put script somewhere and add "source path/to/this/file.sh" to .bashrc file.
# Usage example: timer 1
# Timer for 1 minute
timer() {
    sleep $(echo "$1 * 60" | bc)
    say "AAAAAAAAAAAAAAA"
}
