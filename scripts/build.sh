#!/bin/bash
set -exu
./gen-cal-sys.py
./gen-cav-pl-drv.py

pushd ../CalSysSup
cat SIA-CalSys.db | grep record | grep PwrdBm | grep Mon | grep -Po '(?<=")(.*?)(?="\){)' | sed 's/.*/&\.DESC/' >SIA-CalSys.req
cat SIA-CalSys.db | grep record | grep OFSdB | grep -Po '(?<=")(.*?)(?="\){)' >>SIA-CalSys.req
popd

# Booster Cal Sys (legacy scripts)
./gen-cal-sys-legacy.py > ../CalSysSup/BO-CalSys.db
pushd ../CalSysSup
cat BO-CalSys.db | grep record | grep PwrdBm | grep Mon | grep -Po  '(?<=")(.*?)(?="\){)' | sed 's/.*/&\.DESC/' > BO-CalSys.req
cat BO-CalSys.db | grep record | grep OFSdB | grep -Po  '(?<=")(.*?)(?="\){)' >> BO-CalSys.req
popd
