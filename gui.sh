#!/bin/bash

data=$(cat /dev/stdin)

notify-send "$data"

comand=$({echo Menu; echo -e "Increase\nDecrease\nClose" | dzen2 -l 4 -m h -p)

echo $comand


