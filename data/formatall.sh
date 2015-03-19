#!/bin/bash
for i in {11..20}
do
  cd $i
  mkdir -p out
  cp ../proper.rb .
  ruby proper.rb
  for j in {00..23}
  do
    rm -rf $j
  done
  cp ../json_to_db.py out
  cd ..
done
