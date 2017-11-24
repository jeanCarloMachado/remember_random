#!/usr/bin/env bash

content=${1:-$(cat /dev/stdin)}
search=""
for term in $content
do
search="$search%20$term"
done

$BROWSER "http://www.google.com/search?q=$search"

