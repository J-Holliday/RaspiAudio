#!/bin/sh

commname="/home/pi/workspace/raspi-audio/downloads/aquestalkpi/AquesTalkPi"
while true
do
	count=$(ps ax -o command | grep "$commname" | grep -v "^grep" | wc -l)
	if [ "$count" -eq 0 ]; then
		./newsStation/call.py
		ps a
	fi
done

