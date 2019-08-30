TOP=../..
include $(TOP)/configure/CONFIG

DB += SIA-CalSys.db
DB += SIA-CavPlDrv.db
DB += ADC.db
DB += ADC.proto

include $(TOP)/configure/RULES
.PHONY: db
db :
	./gen.py
#----------------------------------------
#  ADD RULES AFTER THIS LINE

