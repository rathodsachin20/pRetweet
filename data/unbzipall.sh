#!/bin/bash
for i in {11..20}
do
  cd $i
  cp ../unbzip.sh .
  ./unbzip.sh
  cd ..
done
