#!/bin/sh
csh
source /home/install/cshrc
kill -15 $(screen -ls | grep '[0-9]*\.ocean_simulation' | sed -E 's/\s+([0-9]+)\..*/\1/')
screen -S ocean_simulation -d -m  
ocean
