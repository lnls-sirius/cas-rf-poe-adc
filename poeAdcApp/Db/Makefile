TOP=../..
include $(TOP)/configure/CONFIG

DB += ADC.db
DB += Conv.db

DB += ADC.proto

include $(TOP)/configure/RULES
.PHONY: db
db :
	./gen.py
#----------------------------------------
#  ADD RULES AFTER THIS LINE

