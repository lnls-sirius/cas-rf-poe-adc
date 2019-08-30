#!../../bin/linux-arm/poeAdc

## You may have to change poeAdc to something else
## everywhere it appears in this file

< envPaths

epicsEnvSet("P","Test")
epicsEnvSet("R","")

cd "${TOP}"

dbLoadDatabase "dbd/poeAdc.dbd"
poeAdc_registerRecordDeviceDriver pdbbase

dbLoadRecords("db/ADC.db",  "P=$(P),R=$(R),PORT=L0,A=0,SCAN=0.1 second,SCAN=.1 second")
dbLoadRecords("db/SIA-CalSys.db", "P=$(P),R=$(R),PORT=L0,A=0")

drvAsynIPPortConfigure("L0", "unix://$(TOP)/poeAdcSPI/unix-socket")

cd "${TOP}/iocBoot/${IOC}"
iocInit

#var streamDebug 1
