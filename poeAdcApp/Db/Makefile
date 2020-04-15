TOP=../..
include $(TOP)/configure/CONFIG

DB += SIA-CalSys.db
DB += SIA-CalSys.req
DB += SIA-CavPlDrv.db
DB += LLRFLinPS01.db
DB += LLRFLinPS02.db
DB += LLRFSwPS01.db
DB += LLRFSwPS02.db
DB += SSASwPS01.db
DB += SSASwPS02.db

DB += ADC.proto

include $(TOP)/configure/RULES

.PHONY: db
db :
	./build.sh
#----------------------------------------
#  ADD RULES AFTER THIS LINE

