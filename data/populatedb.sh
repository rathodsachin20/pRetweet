#!/bin/bash
for i in {01..31}
do
  cd $1
  mv json_to_db.py out
  cd out
  python json_to_db.py
  cd ..
  cd ..
done
