#!../../bin/linux-arm/poeAdc

< envPaths

cd "${TOP}"

dbLoadDatabase "dbd/poeAdc.dbd"
poeAdc_registerRecordDeviceDriver pdbbase

dbLoadRecords("db/SIA-CalSys.db", "PORT=L0,A=0,S=.1")

drvAsynIPPortConfigure("L0", "unix://$(TOP)/poeAdcSPI/unix-socket")

set_savefile_path("$(TOP)/autosave")
 
# Offsets
set_pass0_restoreFile("SIA-CalSys.sav")
set_pass1_restoreFile("SIA-CalSys.sav")

cd "${TOP}/iocBoot/${IOC}"
iocInit

create_monitor_set("$(TOP)/db/SIA-CalSys.req", 10, "TOP=$(TOP), SAVENAMEPV=SIA-CalSys:SaveName")

#var streamDebug 1
