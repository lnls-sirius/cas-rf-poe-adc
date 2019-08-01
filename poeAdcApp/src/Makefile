TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC = poeAdc
# poeAdc.dbd will be created and installed
DBD += poeAdc.dbd

# poeAdc.dbd will be made up from these files:
poeAdc_DBD += base.dbd

poeAdc_DBD += asSupport.dbd
poeAdc_DBD += calcSupport.dbd
poeAdc_DBD += asyn.dbd
poeAdc_DBD += stream.dbd
poeAdc_DBD += drvAsynIPPort.dbd
 
poeAdc_LIBS += autosave
poeAdc_LIBS += stream
poeAdc_LIBS += asyn
poeAdc_LIBS += calc

# poeAdc_registerRecordDeviceDriver.cpp derives from poeAdc.dbd
poeAdc_SRCS += poeAdc_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
poeAdc_SRCS_DEFAULT += poeAdcMain.cpp
poeAdc_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#poeAdc_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Finally link to the EPICS Base libraries
poeAdc_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

