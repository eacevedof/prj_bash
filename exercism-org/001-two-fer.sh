#!/usr/bin/env bash

main() {
    # cuando entra "John Smith"
    # si se pasa $1 => John
    # sino "$1" => "John Smith"
    cookies_for "$1"
}

cookies_for() {
    name="$1"
    if [ -z "$name" ]; then
        echo "One for you, one for me."
    else
        echo "One for $name, one for me."
    fi
}

# two-fer.sh "John Smith" "Mary Ann"
main "$@"