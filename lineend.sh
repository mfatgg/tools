#!/bin/sh

for a in "$@"
do
  sed -i 's/\x0D$//' "$a"
done
