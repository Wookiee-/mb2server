#!/bin/bash

PID=$(pgrep -f "python automessage.py")

if [ -n "$PID" ]
then
    kill $PID
    echo "Auto Message Plugin stopped. PID: $PID"
else
    echo "Auto Message Plugin is not running."
fi
