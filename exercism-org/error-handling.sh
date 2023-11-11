#!/usr/bin/env bash
#https://exercism.org/tracks/bash/exercises/error-handling/edit

# The goal of this exercise is to consider the number of arguments passed to your program.
# If there is exactly one argument,
# print a greeting message. Otherwise print an error message and exit with a non-zero status.

main() {
    cookies_for "$1"
}

hello() {
    persons="$1"
    if [ -z "$name" ]; then
        echo "Usage: error_handling.sh <person>"
    else
        echo "Hello, $persons"
    fi
}

main "$@"