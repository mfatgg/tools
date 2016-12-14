#!/bin/sh

for a in "$@"
do
  # delete trailing whitespace
  sed -i 's/[ \t]*$//' "$a"
  # replace tabs by 4 spaces
  sed -i 's/\t/    /g' "$a"
done
