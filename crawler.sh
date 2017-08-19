#!/usr/bin/env bash

config=$(cat config)

tmp_file=$(echo "$config" | grep tmp_file | cut -d "=" -f2)
[ -f $tmp_file ] && {
    rm -rf $tmp_file
}
touch $tmp_file

namespaces=$(echo "$config" | cut -d '.' -f1 | uniq | grep -v global)
IFS='

'
for namespace in $namespaces
do

    file_path=$(echo "$config" | grep "$namespace\.file_path" | cut -d "=" -f2)
    separator=$(echo "$config" | grep "$namespace\.separator" | cut -d "=" -f2)


    for line in $(cat $file_path)
    do
        echo -e "$line|\c" >> $tmp_file
    done
done



