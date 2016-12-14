#!/bin/sh

if [ "$1" == "" ] 
then
  echo "Give Directory!"
  exit 1
fi


fromdir=$1
tmpfile=/tmp/$$


find "$fromdir/" -type d > "$tmpfile"

while read mydir
do
  newdir=`echo "$mydir" | tr -cd "[:alnum:][:space:]/.()#_\-\'"`
  if [ "$mydir" != "$newdir" ]
  then
    echo mv "$mydir" "$newdir"
    mv "$mydir" "$newdir"
  fi
done < "$tmpfile"


find "$fromdir/" -type f > "$tmpfile"

while read myfile
do
  newfile=`echo "$myfile" | tr -cd "[:alnum:][:space:]/.()#_\-\'"`
  if [ "$myfile" != "$newfile" ]
  then
    echo mv "$myfile" "$newfile"
    mv "$myfile" "$newfile"
  fi
done < "$tmpfile"


rm "$tmpfile"
