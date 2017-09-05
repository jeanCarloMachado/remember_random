#!/usr/bin/env bash
[ -z ${CONFIG_FILE+x} ] && { CONFIG_FILE=~/.remember_config
}

BASEDIR=$(dirname "$0")


config=$(cat $CONFIG_FILE)
tmp_file=$(echo "$config" | grep tmp_file | cut -d "=" -f2)
tmp_file_content=$(cat $tmp_file)

[[ ! -f "$tmp_file" ]]  || [[ -z $tmp_file_content ]] && {
    echo "tmp_file invalid"
    exit 1
}

get_remember() {
    total_remembers=0
    IFS='|'
    for i in $tmp_file_content
    do
        total_remembers=$(( $total_remembers + 1 ))
    done

    show_index=$($BASEDIR/random 0 $total_remembers)
    counter=0
    for i in $tmp_file_content
    do
        if [[ $counter -eq $show_index ]]
        then
            echo "$i"
        fi
        counter=$(( $counter + 1 ))
    done
}

while true
do
    result=$(get_remember)
    [[ ${#result} -le 3  ]] && {
        continue
    }

    result_hash=$(echo "$result" | md5sum | cut -d ' ' -f1)
    [[ -f "/home/jean/.config/remember_random/$result_hash" ]] && {

        [[ $(random 0 100) -le 75 ]]  && {
            continue
        }
    }

    echo "$result"
    exit
done
