screen -ls legends | grep -E '\s+[0-9]+\.' | awk -F ' ' '{print $1}' | while read s; do screen -XS $s quit; done
pkill -9 mbiided.i386
rm MBII/legends-games.log
