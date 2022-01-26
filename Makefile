# Makefile at top of application tree
TOP = .
include $(TOP)/configure/CONFIG

# Directories to build, any order
DIRS += configure
DIRS += $(wildcard *Sup)
DIRS += $(wildcard *App)
DIRS += $(wildcard *Top)
DIRS += $(wildcard iocBoot)

# The build order is controlled by these dependency rules:

# All dirs except configure depend on configure
$(foreach dir, $(filter-out configure, $(DIRS)), \
    $(eval $(dir)_DEPEND_DIRS += configure))

# Any *App dirs depend on all *Sup dirs
$(foreach dir, $(filter %App, $(DIRS)), \
    $(eval $(dir)_DEPEND_DIRS += $(filter %Sup, $(DIRS))))

# Any *Top dirs depend on all *Sup and *App dirs
$(foreach dir, $(filter %Top, $(DIRS)), \
    $(eval $(dir)_DEPEND_DIRS += $(filter %Sup %App, $(DIRS))))

# iocBoot depends on all *App dirs
iocBoot_DEPEND_DIRS += $(filter %App,$(DIRS))

# Add any additional dependency rules here:

include $(TOP)/configure/RULES_TOP

clean:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . -name '__pycache__' -exec rm -rf {} +

spi-restart:
	systemctl restart cas-rf-poe-adc.service

spi-start:
	systemctl restart cas-rf-poe-adc.service

spi-stop:
	systemctl restart cas-rf-poe-adc.service

spi-enable:
	systemctl enable cas-rf-poe-adc.service

spi-install: spi-start spi-enable
	cp -v services/cas-rf-poe-adc-spi.service /etc/systemd/system

restart-cal-sys-bo:
	systemctl restart cas-rf-poe-adc-ioc-BO-CalSys.service

install-cal-sys-bo:
	cp -v services/cas-rf-poe-adc-ioc-BO-CalSys.service /etc/systemd/system
	systemctl enable cas-rf-poe-adc-ioc-BO-CalSys.service
	systemctl start  cas-rf-poe-adc-ioc-BO-CalSys.service

status-cal-sys-bo:
	systemctl status cas-rf-poe-adc-ioc-BO-CalSys.service

stop-cal-sys-services:
	systemctl stop  cas-rf-calibration-module-ioc.service
	systemctl disable  cas-rf-calibration-module-ioc.service
