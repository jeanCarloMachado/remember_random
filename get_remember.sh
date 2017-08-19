#!/usr/bin/env bash

config=$(cat config)
tmp_file=$(echo "$config" | grep tmp_file | cut -d "=" -f2)

get_remember() {
    total_remembers=0
    IFS='|'
    for i in $(cat $tmp_file)
    do
        total_remembers=$(( $total_remembers + 1 ))
    done

    show_index=$(./random 0 $total_remembers)
    counter=0
    for i in $(cat $tmp_file)
    do
        if [ $counter -eq $show_index ]
        then
            echo "$i"
        fi
        counter=$(( $counter + 1 ))
    done
}

while true
do
    result=$(get_remember)
    [[ ${#result} -ge 3  ]] && {
        echo "$result"
        exit
    }
done
