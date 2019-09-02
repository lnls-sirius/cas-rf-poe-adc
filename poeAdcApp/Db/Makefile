TOP=../..
include $(TOP)/configure/CONFIG

DB += SIA-CalSys.db
DB += SIA-CalSys.req
DB += SIA-CavPlDrv.db
# DB += SIA-CavPlDrv.req
DB += ADC.proto

.PHONY: db
db :
	./gen.py
	cat SIA-CalSys.db | grep record | grep PwrdBm | grep Mon | grep -Po  '(?<=")(.*?)(?="\){)' | sed 's/.*/&\.DESC/' > SIA-CalSys.req
	cat SIA-CalSys.db | grep record | grep OFSdB | grep -Po  '(?<=")(.*?)(?="\){)' >> SIA-CalSys.req
	# cat SIA-CavPlDrv.db | grep record | grep PwrdBm | grep Mon | grep -Po  '(?<=")(.*?)(?="\){)' | sed 's/.*/&\.DESC/' > SIA-CavPlDrv.req
	# cat SIA-CavPlDrv.db | grep record | grep OFSdB | grep -Po  '(?<=")(.*?)(?="\){)' >> SIA-CavPlDrv.req

#----------------------------------------
#  ADD RULES AFTER THIS LINE
include $(TOP)/configure/RULES
