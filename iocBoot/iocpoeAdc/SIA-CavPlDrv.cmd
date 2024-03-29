#!../../bin/linux-arm/poeAdc

## You may have to change poeAdc to something else
## everywhere it appears in this file

< envPaths

cd "${TOP}"

dbLoadDatabase "dbd/poeAdc.dbd"
poeAdc_registerRecordDeviceDriver pdbbase

dbLoadRecords("db/SIA-CavPlDrv.db", "PORT=L0,A=0,S=.1")

drvAsynIPPortConfigure("L0", "unix://$(TOP)/poeAdcSPI/unix-socket")

cd "${TOP}/iocBoot/${IOC}"
iocInit

#var streamDebug 1
