#!/usr/bin/env bash
# This script prints a string 10 times except for the 9th time

i=1
while [ $i -ne 11 ];
do
    if [ $i -eq 9 ]; then
	echo 'Best School'
	echo 'Hi'
    else
	echo 'Best School'
    fi
    ((i++))
done
