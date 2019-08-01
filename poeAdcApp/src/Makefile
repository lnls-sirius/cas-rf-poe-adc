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

# Include dbd files from all support applications:
#poeAdc_DBD += xxx.dbd

# Add all the support libraries needed by this IOC
#poeAdc_LIBS += xxx

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

