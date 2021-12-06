# cas-rf-poe-adc

This repository contains iocs for the adc/spi hardware developed by the RF group.
We start two systemd services, one for the IOC and another for a Python script that is used to get data in and out from the board.

```
        socket
[IOC] <--------> [.py] <---> [hardware]
```

# Requirements
The python script requires the module [Adafruit_BBIO](https://github.com/adafruit/adafruit-beaglebone-io-python.git).

Install it via pip or manually:

```bash
#  via pip
sudo apt-get update
sudo apt-get install build-essential python3-dev python3-pip -y
sudo pip3 install Adafruit_BBIO

# from the repository
sudo apt-get update
sudo apt-get install build-essential python3-dev python3-pip -y
git clone git://github.com/adafruit/adafruit-beaglebone-io-python.git
cd adafruit-beaglebone-io-python
sudo python3 setup.py install
```

[procServhttps](https://github.com/ralphlange/procServ) is required for runing the IOC.
```bash
apt-get install procserv
```

The following EPICS modules are used [configure/RELEASE](./configure/RELEASE): 
```
ASYN        = /opt/epics-R3.15.5/modules/asyn4-35
AUTOSAVE    = /opt/epics-R3.15.5/modules/autosave-R5-9
CALC        = /opt/epics-R3.15.5/modules/synApps/calc-R3-7-1
STREAM      = /opt/epics-R3.15.5/modules/StreamDevice-2.8.8

EPICS_BASE  = /opt/epics-R3.15.5/base
```

https://github.com/epics-base/epics-base

https://github.com/epics-modules/asyn

https://github.com/epics-modules/autosave

https://github.com/epics-modules/calc

https://github.com/paulscherrerinstitute/StreamDevice


## Beagle SPI PINs

**SPI(0,0)**

| ADC  |   GPIO  |
|------|---------|
| ADC0 | "P9_24" |
| ADC1 | "P9_26" |
| ADC2 | "P9_28" |
| ADC3 | "P9_30" |

```bash

config-pin P9_24 output
config-pin P9_26 output
config-pin P9_28 output
config-pin P9_30 output

config-pin P9.17 spi_cs
config-pin P9.18 spi
config-pin P9.21 spi
config-pin P9.22 spi_sclk
```

