#!/usr/bin/env bash
filename="/Users/Quan_Lam/repos/personal/automations/time-track.log"
dt=$(date '+%d/%m/%Y %H:%M:%S');
message=$"${dt}"
echo $message >> $filename
