#!/bin/sh

# example:
# $ ./rokuon.sh 0

if [ $# -ne 1 ];then
				echo "Input Device-Number of Audio  as an argument." 1>&2
				echo "Please try to 'arecord -l'."
				exit 1
fi

arecord -f S16_LE -D hw:$1,0 record.wav
