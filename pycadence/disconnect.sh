#!/bin/sh
kill -15 $(screen -ls | grep '[0-9]*\.ocean_simulation' | sed -E 's/\s+([0-9]+)\..*/\1/')