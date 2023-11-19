#!/usr/bin/env bash
#https://exercism.org/tracks/bash/exercises/error-handling/edit

# The goal of this exercise is to consider the number of arguments passed to your program.
# If there is exactly one argument,
# print a greeting message. Otherwise print an error message and exit with a non-zero status.

main() {
    num_args=$#
    if [[ $num_args -lt 1 ]] || [[ $num_args -gt 1 ]]; then
        echo "Usage: error_handling.sh <person>"
        return
    fi
    echo "Hello, $1"
}

main "$@"