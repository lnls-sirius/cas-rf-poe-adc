#!/usr/bin/python3
import os 
from AM_Classes import *

os.system('config-pin P9.17 spi_cs')
os.system('config-pin P9.18 spi')
os.system('config-pin P9.21 spi')
os.system('config-pin P9.22 spi_sclk')

spi = SPI(0,0)    #definindo porta spi 0, modo 0
spi.msh = 2000000 #definindo velocidade de comunicação
spi.mode = 1

ADC0 = ADC("P9_24", spi)
ADC1 = ADC("P9_26", spi)
ADC2 = ADC("P9_28", spi)
ADC3 = ADC("P9_30", spi)
SCAN_PERIOD = 0.001

adc0_read = ADC0.read([0,1,2,3])
adc1_read = ADC1.read([0,1,2,3])
adc2_read = ADC2.read([0,1,2,3])
adc3_read = ADC3.read([0,1,2,3])
#c0 = convert(adc0_read,5,0,1)
#c1 = convert(adc1_read,5,0,1)
#c2 = convert(adc2_read,5,0,1)
#c3 = convert(adc3_read,5,0,1)
while True:
    print(adc0_read, adc1_read, adc2_read, adc3_read)
