#!/bin/bash


main() {
    cookie_by_name "$1"
}

cookie_by_name() {
    name=$1
    if [ -z "$name" ]; then
        echo "One for you, one for me."
    else
        echo "One for $name, one for me."
    fi
}

main "$1"