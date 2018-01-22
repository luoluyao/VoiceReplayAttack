#!/bin/sh


count=30
i=0
while [ "$i" -lt "$count" ]
do
	echo Inter y or times
	read next
	if [ "$next" = "y" ]; then
		i=$((i+1))
	else
		i=$next
	fi
	python kws_cch.py
	mkdir wav_${i}
	cp log/* wav_${i}
done



#if [ "$#" = 1 ]; then
#	times="$1"
#	python kws_cch.py
#	mkdir wav_${times}
#	cp log/* wav_${times}
#else
#	echo need a argument
#fi

exit 0
