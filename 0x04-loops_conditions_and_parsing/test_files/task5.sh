#!/usr/bin/env bash
# This script prints a string 10 times but prints another at
# the 4th and 8th iterations

i=1
while [ $i -ne 11 ];
do
    if [ $i -eq 4 ]; then
	echo 'bad luck'
    elif [ $i -eq 8 ]; then
	echo 'good luck'
    else
	echo 'Best School'
    fi
    ((i++))
done
