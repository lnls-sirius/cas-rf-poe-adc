#!../../bin/linux-arm/poeAdc
< envPaths

cd "${TOP}"

epicsEnvSet("P", "RA-RaBO01")
epicsEnvSet("D", ":RF-LLRFCalSys")

dbLoadDatabase "dbd/poeAdc.dbd"
poeAdc_registerRecordDeviceDriver pdbbase

drvAsynIPPortConfigure("P1", "unix://$(TOP)/poeAdcSPI/unix-socket")

dbLoadRecords("db/BO-CalSys.db","PORT=P1,P=$(P),D=$(D),A=0")

save_restoreSet_DatedBackupFiles(0)
save_restoreSet_NumSeqFiles(3)
save_restoreSet_SeqPeriodInSeconds(600)

set_requestfile_path("$(TOP)/db")
set_savefile_path("$(TOP)/autosave")

# Offsets
set_pass0_restoreFile("BO-CalSys.sav")
set_pass1_restoreFile("BO-CalSys.sav")

cd "${TOP}/iocBoot/${IOC}"
iocInit

cd "${TOP}"
create_monitor_set("$(TOP)/db/BO-CalSys.req", 10, "TOP=$(TOP), P=$(P),D=$(D)")

#var streamDebug 1
