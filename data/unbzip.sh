#!/bin/bash
# Run in one folder up the folders containing .bz2 files
dirlist=$(find $1 -mindepth 1 -maxdepth 1 -type d)
for dir in $dirlist
do
    echo $dir
    cd $dir
    bzip2 -d *.bz2
    cd ..
done
