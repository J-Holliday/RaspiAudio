#!/bin/sh

# example:
# $ ./rokuon.sh 0

if [ $# -ne 2 ];then
				echo "arg1:output filename, arg2: audio input device number" 1>&2
				echo "Please try to 'arecord -l'."
				exit 1
fi

arecord -f S16_LE -D hw:$2,0 $1
