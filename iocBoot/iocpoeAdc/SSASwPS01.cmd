#!../../bin/linux-arm/poeAdc

## You may have to change poeAdc to something else
## everywhere it appears in this file

< envPaths

cd "${TOP}"

epicsEnvSet("P", "RA-RaBO02")
epicsEnvSet("D", "RF-SSASwPS")

dbLoadDatabase "dbd/poeAdc.dbd"
poeAdc_registerRecordDeviceDriver pdbbase

dbLoadRecords("db/SSASwPS01.db", "PORT=L0,A=0,P=$(P),D=$(D),S=.1")

drvAsynIPPortConfigure("L0", "unix://$(TOP)/poeAdcSPI/unix-socket")

cd "${TOP}/iocBoot/${IOC}"
iocInit

#var streamDebug 1
