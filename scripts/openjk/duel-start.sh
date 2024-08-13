#!/bin/bash

echo "Superleet startup script!"

status=1
while [ $status -ne 0 ]
do
		screen -dmS mb2duel ./mbiided.i386 +set fs_game MBII +set dedicated 2 +set net_port 29071 +exec duel-server.cfg 
		screen -dmS duelrtv python duel-rtvrtm.py -c MBII/duel-rtvrtm.cfg -t 10
		
        status=$?


        if [ $status -ne 0 ]
        then
                date=`/bin/date`
                echo "Server crashed with status "$status" at "$date
        fi
done

echo "Server exited peacefully"
