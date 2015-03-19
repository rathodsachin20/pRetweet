#!/bin/bash
for i in {11..20}
do
    cd $i/out
    cp ../../json_to_db.py .
    #cd out
    python json_to_db.py
    #cd ..
    cd ../..
done
