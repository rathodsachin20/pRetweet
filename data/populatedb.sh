#!/bin/bash
for i in {01..10}
do
    cd $i/out
    #mv json_to_db.py out
    #cd out
    python json_to_db.py
    #cd ..
    cd ../..
done
