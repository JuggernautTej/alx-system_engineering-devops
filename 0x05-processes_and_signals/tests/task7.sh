#!/bin/usr/env bash
# trap it all

i="To infinity and beyond"
j="I am invincible!!!"
trap 'echo $j' SIGTERM
while true;
do
    echo "$i"
    sleep 2
done
