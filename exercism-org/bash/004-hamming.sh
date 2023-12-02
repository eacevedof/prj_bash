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

  #printf "%s | %s" "$str_sequence1" "$str_sequence2"; return 1;


  len_seq1=${#str_sequence1}
  len_seq2=${#str_sequence2}

  #printf "%s | %s" "$len_seq1" "$len_seq2"; return 1;

  if (( len_seq1 != len_seq2 ))
  then
    echo "wrong-length $len_seq1 != $len_seq2"
    return 1
  fi

  arr_sequence1=()
  arr_sequence2=()



  #error aqui no pudo partir el string en varios
  IFS= read -r -n1 -a arr_sequence1 <<< "$str_sequence1"
  IFS= read -r -n1 -a arr_sequence2 <<< "$str_sequence2"

  printf "%s " "${arr_sequence1[@]}"; return 1;


  printf "%s %s " "$len_seq1 $len_seq2"
  return 1



  hamming_distance=$(get_hamming_distance "${arr_sequence1[@]}" "${arr_sequence2[@]}")
  echo "distance: $hamming_distance"
  return 0
}


get_hamming_distance () {
  local arr_sequence1=("$1[@]")
  local arr_sequence1=("$2[@]")


  local distance=0
  local index=0

  for char1 in "${arr_sequence1[@]}"
  do
    char2="${arr_sequence2[index]}"
    if [[ "$char1" != "$char2"  ]]
    then
      distance=$((distance+1))
    fi
    index=$((index+1))
  done

  echo "$distance"
}

main "$@"