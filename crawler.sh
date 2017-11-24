#!/usr/bin/env bash

remove_empty_line() {
      sed '/^$/d'
}

[ -z ${CONFIG_FILE+x} ] && {
    CONFIG_FILE=~/.remember_config
}

config=$(cat $CONFIG_FILE)

tmp_file=$(echo "$config" | grep tmp_file | cut -d "=" -f2)
[ -f $tmp_file ] && {
    rm -rf $tmp_file
}
touch $tmp_file
chmod a+rw $tmp_file

namespaces=$(echo "$config" | cut -d '.' -f1 | uniq | grep -v global)
IFS='
'
for namespace in $namespaces
do

    file_path=$(echo "$config" | grep "$namespace\.file_path" | cut -d "=" -f2)
    separator=$(echo "$config" | grep "$namespace\.separator" | cut -d "=" -f2)

    if [[ $separator == 'new_line' ]]
    then
        for line in $(cat $file_path)
        do
            echo -e "$line|\c" >> $tmp_file
        done
    elif [[ $separator == 'three_dashes' ]]
    then
        content=$(cat $file_path | tr "\n" " " | sed "s/---/\\n/g" | tr -d "-" )

        for line in $content
        do
            echo -e "$line|\c" >> $tmp_file
        done
    elif [[ $separator == 'emphasis_blocks' ]]
    then
        content=$(grep -RPzoh "\n\*{3}[^\*]+\*{3}" $file_path/**/*.md  \
        | tr "\*\*\*" "|" )

        echo $content >> $tmp_file
    elif [[ $separator == 'marked_folds' ]]
    then
        content=$(grep -RPzoh "\{{3}[^\{\}]+\}{3}" $file_path/**/*.md  \
            | tr "\{\{\{" "|" | tr "\}\}\}" "|" )

        echo $content >> $tmp_file
    else
        echo "separator method ($method) not found"
        exit 1
    fi
done

sed -i "s/| |/|/g" $tmp_file
sed -i "s/||/|/g" $tmp_file
sed -i "s/||/|/g" $tmp_file
sed -i "s/||/|/g" $tmp_file
