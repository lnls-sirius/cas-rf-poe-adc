#!../../bin/linux-arm/poeAdc

## You may have to change poeAdc to something else
## everywhere it appears in this file

< envPaths

cd "${TOP}"

epicsEnvSet("P", "RA-RaSIA01")
epicsEnvSet("D", "RF-LLRFSwPS")

dbLoadDatabase "dbd/poeAdc.dbd"
poeAdc_registerRecordDeviceDriver pdbbase

dbLoadRecords("db/LLRFSwPS.db", "PORT=L0,A=0,P=$(P),D=$(D),S=.1")

drvAsynIPPortConfigure("L0", "unix://$(TOP)/poeAdcSPI/unix-socket")

cd "${TOP}/iocBoot/${IOC}"
iocInit

#var streamDebug 1
