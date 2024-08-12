#!/bin/sh

running=`ps aux | grep duel-rtv.sh | grep -v grep | wc -l`
if [ $running -eq 0 ]
then
  echo "RTV is not currently running"
else
  killall duel-rtv.sh
  echo "RTV stopped"
fi
