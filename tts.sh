#!/bin/bash 

STRINGNUM=0

while [[ $# -gt 1 ]] 
do
key="$1"
case $key in
    -l|--lang)
    LANG="$2"
    shift
    ;;
    -m|--message)
    INPUT="$2"
    shift
    ;;
    *)
    ;;
esac
shift
done
 
ary=($INPUT)
for key in "${!ary[@]}" 
  do
    SHORTTMP[$STRINGNUM]="${SHORTTMP[$STRINGNUM]} ${ary[$key]}"
    LENGTH=$(echo ${#SHORTTMP[$STRINGNUM]})
    if [[ "$LENGTH" -lt "100" ]]; then
      SHORT[$STRINGNUM]=${SHORTTMP[$STRINGNUM]}
    else
      STRINGNUM=$(($STRINGNUM+1))
      SHORTTMP[$STRINGNUM]="${ary[$key]}"
      SHORT[$STRINGNUM]="${ary[$key]}"
    fi
done
 
for key in "${!SHORT[@]}"
  do
    NEXTURL=$(echo ${SHORT[$key]} | xxd -plain | tr -d '\n' | sed 's/\(..\)/%\1/g')
    mpg123 "http://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q=$NEXTURL&tl=$LANG"
done
