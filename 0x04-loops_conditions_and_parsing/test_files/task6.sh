#!/usr/bin/env bash
# This script displays numbers from 1 to 20 and prints a
# string aafter the 4th, 9th and 17th loops

i=1
while [ $i -le 20 ];
do
    echo "$i"
    case $i in
	4)
	    echo "bad luck from China"
	    ;;
	9)
	    echo "bad luck from Japan"
	    ;;
	17)
	    echo "bad luck from Italy"
	    ;;
    esac
    ((i++))
done
