#!/bin/sh

for i in `seq 52 1 290`
do
  sleep 15
  echo ${i}
  sh download.sh ${i}
done