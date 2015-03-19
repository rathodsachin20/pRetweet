#!/bin/bash

URL_BASE="https://archive.org/download/archiveteam-json-twitterstream-2012/twitter-stream-2012-01-"
for i in `seq 2 9`;
do
    URL=$URL_BASE'0'$i'.zip'
    echo "URL:"$URL
    wget --no-check-certificate $URL
    echo "DONE.\n"
done
for i in `seq 10 31`;
do
    URL=$URL_BASE$i'.zip'
    echo "URL:"$URL
    wget --no-check-certificate $URL
    echo "DONE.\n"
done
