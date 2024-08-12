#!/bin/sh
cd "`dirname "$0"`"

running=`ps aux | grep duel-rtv.sh | grep -v grep | wc -l`
if [ $running -eq 0 ]
then
  screen -dmS duelrtv ./duel-rtv.sh
  echo "RTV started"
else
  echo "RTV is already running"
fi
