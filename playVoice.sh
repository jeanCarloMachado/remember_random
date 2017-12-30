#!/usr/bin/env bash

message=${1:-$(cat /dev/stdin)}
output=/tmp/google.mp3
lang=${2:-en}

[ ! -z ${VERBOSE+x} ] && {
    echo "Transmofer this text in voice: $message"
}


wget -q -U Mozilla -O $output "http://translate.google.com/translate_tts?ie=UTF-8&total=1&idx=0&textlen=32&client=tw-ob&q=$message&tl=$lang"
mpv $output
