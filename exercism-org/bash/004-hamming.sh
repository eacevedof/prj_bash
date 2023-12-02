#!/usr/bin/env bash

# https://exercism.org/tracks/bash/exercises/hamming

# hamming distance

main () {
  num_args=$#
  if (( num_args != 2 ))
  then
    echo "num_args: $num_args"
    return 1
  fi

  str_sequence1="$1"
  str_sequence2="$2"
  if [[ -z $str_sequence1 || -z $str_sequence2 ]]
  then
    echo "empty-sequence $str_sequence1 | $str_sequence2"
    return 1
  fi

  IFS=""
  read -ra arr_sequence1 <<< "$str_sequence1"
  read -ra arr_sequence2 <<< "$str_sequence2"

  len_seq1=${#arr_sequence1[@]}
  len_seq2=${#arr_sequence2[@]}

  if (( len_seq1 != len_seq2 ))
  then
    echo "wrong-length $len_seq1 != $len_seq2"
    return 1
  fi

  hamming_distance=$(get_hamming_distance arr_sequence1 arr_sequence2)
  echo "$hamming_distance"
  return 0
}


get_hamming_distance () {
  arr_sequence1=$1
  arr_sequence1=$2

  local distance=0
  for char1 in "${arr_sequence1[@]}"; do
    index=$((index+1))
    char2="${arr_sequence2[index]}"
    if [[ "$char1" != "$char2"  ]]
    then
      distance=$((distance+1))
    fi
  done
  echo "$distance"
}

main "$@"