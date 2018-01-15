#!/usr/bin/env bash

ere_quote() {
    sed 's/[]\|$(){}?+*^]/\\&/g' <<< "$*"
}

openResult() {
    result=$(echo "$1" | head -n 1)
    file=$(head -n1 <<< $result | cut -d ':' -f1)
    line=$(head -n1 <<< $result | cut -d ':' -f2)
    gvim +$line $file
}


SEARCH_DIRECTORY=$WIKI_PATH
content=${1:-$(cat /dev/stdin)}
content=$(ere_quote "$content")

#search first 40 chars
remember=$(echo "$content" | cut -c1-40 )
result=$(grep -n "$remember"  -R $SEARCH_DIRECTORY)

[ ! -z "$result" ] && {
    openResult "$result"
    exit
}


#search last 40 chars
remember=$(echo "$content" | rev | cut -c1-40 | rev )
result=$(grep -n "$remember"  -R $SEARCH_DIRECTORY)

[ ! -z "$result" ] && {
    openResult "$result"
    exit
}


#search first 20 chars
remember=$(echo "$content" | cut -c1-20 )
result=$(grep -n "$remember"  -R $SEARCH_DIRECTORY)

[ ! -z "$result" ] && {
    openResult "$result"
    exit
}

#search last 20 chars
remember=$(echo "$content" | rev | cut -c1-20 | rev )
result=$(grep -n "$remember"  -R $SEARCH_DIRECTORY)

[ ! -z "$result" ] && {
    openResult "$result"
    exit
}


#search first 15 chars
remember=$(echo "$content" | cut -c1-15 )
result=$(grep -n "$remember"  -R $SEARCH_DIRECTORY)

[ ! -z "$result" ] && {
    openResult "$result"
    exit
}


#search last 15 chars
remember=$(echo "$content" | rev | cut -c1-15 | rev )
result=$(grep -n "$remember"  -R $SEARCH_DIRECTORY)

[ ! -z "$result" ] && {
    openResult "$result"
    exit
}


exit 1
