#!/bin/sh
isargsok=1
# while [[ "$isargsok" -eq 1 ]]; # ok
while (( isargsok )); #ok
do
  echo $isargsok
  exit
done

# import utils.hs
. "$thisdir/utils.sh"
