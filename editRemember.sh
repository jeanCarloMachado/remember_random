#!/usr/bin/env bash

ere_quote() {
    sed 's/[]\|$(){}?+*^]/\\&/g' <<< "$*"
}

content=${1:-$(cat /dev/stdin)}
content=$(ere_quote "$content")
remember=$(echo "$content" | cut -c1-20 )
result=$(ack "$remember"  $WIKI_PATH)

[ ! -z "$result" ] && {
    file=$(head -n1 <<< $result | cut -d ':' -f1)
    line=$(head -n1 <<< $result | cut -d ':' -f2)

    $EDITOR +$line $file
}
