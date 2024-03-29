#!/usr/bin/env bash
#https://exercism.org/tracks/bash/exercises/error-handling/edit

# The goal of this exercise is to consider the number of arguments passed to your program.
# If there is exactly one argument,
# print a greeting message. Otherwise print an error message and exit with a non-zero status.

main() {
    num_args=$#
    if  (( num_args == 1 ))
    then
        echo "Hello, $1"
        return 0
    fi
    echo "Usage: error_handling.sh <person>"
    # is required fot testing because it checks the function state
    return 1
}

main "$@"

main "$@"