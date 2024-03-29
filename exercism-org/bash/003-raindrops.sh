#!/usr/bin/env bash
#https://exercism.org/tracks/bash/exercises/raindrops/edit

# The rules of raindrops are that if a given number:
#has 3 as a factor, add 'Pling' to the result.
#has 5 as a factor, add 'Plang' to the result.
#has 7 as a factor, add 'Plong' to the result.
#does not have any of 3, 5, or 7 as a factor, the result should be the digits of the number.

# el doble parentesis se usa para operaciones aritmeticas
is_3_factored() {
  (( $1 % 3 == 0 )) && return 0 || return 1
}

is_5_factored() {
  (( $1 % 5 == 0 )) && return 0 || return 1
}

is_7_factored() {
  (( $1 % 7 == 0 )) && return 0 || return 1
}

main() {
  result=""
  number="$1"
  if (( $1 % 3 == 0 )); then
    result="Pling"
  fi
  if (( $1 % 5 == 0 )); then
    result="${result}Plang"
  fi
  if (( $1 % 7 == 0 )); then
    result+="Plong"
  fi
  if [[ -z "$result" ]]; then
    result=$number
  fi
  echo "$result"
}

main "$@"