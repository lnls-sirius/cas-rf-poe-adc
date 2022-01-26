#!../../bin/linux-arm/poeAdc

< envPaths

cd "${TOP}"

epicsEnvSet("P", "RA-RaSIA01")
epicsEnvSet("D", ":RF-RFCalSys")

dbLoadDatabase "dbd/poeAdc.dbd"
poeAdc_registerRecordDeviceDriver pdbbase

dbLoadRecords("db/SIA-CalSys.db", "PORT=L0,P=$(P),D=$(D),A=0,S=.1")

drvAsynIPPortConfigure("L0", "unix://$(TOP)/poeAdcSPI/unix-socket")

save_restoreSet_DatedBackupFiles(0)
save_restoreSet_NumSeqFiles(3)
save_restoreSet_SeqPeriodInSeconds(600)

set_requestfile_path("$(TOP)/db")
set_savefile_path("$(TOP)/autosave")
 
# Offsets
set_pass0_restoreFile("SIA-CalSys.sav")
set_pass1_restoreFile("SIA-CalSys.sav")

cd "${TOP}/iocBoot/${IOC}"
iocInit

create_monitor_set("$(TOP)/db/SIA-CalSys.req", 10, "TOP=$(TOP),P=$(P),D=$(D)")

#var streamDebug 1
