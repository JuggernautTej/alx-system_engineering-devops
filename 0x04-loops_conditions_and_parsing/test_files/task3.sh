#!/usr/bin/env bash
# This script uses the until loop to print a string 10 times

i=0
until [ $i -eq 10 ]; do
    echo 'Best School'
    ((i++))
done
