#!/usr/bin/env bash

echo "edit remmember"
ere_quote() {
    sed 's/[]\|$(){}?+*^]/\\&/g' <<< "$*"
}

content=${1:-$(cat /dev/stdin)}
content=$(ere_quote "$content")
remember=$(echo "$content" | cut -c1-20 )
result=$(grep -n "$remember"  -R $WIKI_PATH)

[ -z "$result" ] && {
    echo "No match found"
    exit 1
}
echo "Found match"
result=$(echo "$result" | head -n 1)

file=$(head -n1 <<< $result | cut -d ':' -f1)
line=$(head -n1 <<< $result | cut -d ':' -f2)
gvim +$line $file
