#!/bin/sh
process_name="[0-9]*\.$1"
kill -15 $(screen -ls | grep $process_name | sed -E 's/\s+([0-9]+)\..*/\1/')