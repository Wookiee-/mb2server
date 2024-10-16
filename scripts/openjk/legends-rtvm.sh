#!/bin/bash

echo "Superleet startup script!"

status=1
while [ $status -ne 0 ]
do
		python legends-rtvrtm.py -c MBII/legends-rtvrtm.cfg -t 10

        status=$?


        if [ $status -ne 0 ]
        then
                date=`/bin/date`
                echo "Server crashed with status "$status" at "$date
		# ./legends-stop.sh
        fi
done

echo "Server exited peacefully"
