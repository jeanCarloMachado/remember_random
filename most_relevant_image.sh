#!/bin/bash

tmp-file() {
echo /tmp/$(date "+%Y-%m-%d_%H-%I-%S")
}

remote=$(image_search.js  "$1" | head -n 1)
tmp_file=$(tmp-file)
wget $remote -q -o /dev/null -O $tmp_file
printf $tmp_file
