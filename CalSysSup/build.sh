#!/bin/bash
set -e
set -x
python3 gen.py
cat SIA-CalSys.db | grep record | grep PwrdBm | grep Mon | grep -Po  '(?<=")(.*?)(?="\){)' | sed 's/.*/&\.DESC/' > SIA-CalSys.req
cat SIA-CalSys.db | grep record | grep OFSdB | grep -Po  '(?<=")(.*?)(?="\){)' >> SIA-CalSys.req
