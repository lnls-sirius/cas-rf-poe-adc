#!../../bin/linux-arm/poeAdc
< envPaths

cd "${TOP}"

epicsEnvSet("P", "RA-RaBO01:RF-LLRFCalSys")

dbLoadDatabase "dbd/poeAdc.dbd"
poeAdc_registerRecordDeviceDriver pdbbase

drvAsynIPPortConfigure("P1", "unix://$(TOP)/poeAdcSPI/unix-socket")

dbLoadRecords("db/BO-CalSys.db","PORT=P1,P=$(P),A=0")

set_savefile_path("$(TOP)/autosave")
 
# Offsets
set_pass0_restoreFile("$(P).sav")
set_pass1_restoreFile("$(P).sav")

cd "${TOP}/iocBoot/${IOC}"
iocInit

cd "${TOP}"
create_monitor_set("$(TOP)/db/BO-CalSys.req", 10, "TOP=$(TOP), SAVENAMEPV=$(P):SaveName")
