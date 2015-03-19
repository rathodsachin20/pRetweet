#!/bin/bash
for i in {01..31}
do
  cd $i
  ruby proper.rb
  for j in {00..23}
  do
    rm -rf $j
  done
  cp json_to_db.py out
  cd ..
done
