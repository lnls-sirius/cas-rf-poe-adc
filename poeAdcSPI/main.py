#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
from Adafruit_BBIO.SPI import SPI
import Adafruit_BBIO.GPIO as GPIO
import math
import time
from Classes import *
import os

spi = SPI(0,0)
spi.msh = 2000000
spi.mode = 1


os.system('config-pin P9.17 spi_cs')
os.system('config-pin P9.18 spi')
os.system('config-pin P9.21 spi')
os.system('config-pin P9.22 spi_sclk')

ADC1 = ADC("P9_24",spi)
ADC2 = ADC("P9_26",spi)


while(1):
    
	adc1_read = ADC1.read([0,1,2,3])
	adc2_read = ADC2.read([0,1,2,3])
	time.sleep(.1)
	os.system('clear')
	print('*-----------------------------------------------*')
	print('ADC1')
	print('Valor s/ conversao: ', adc1_read)
	print ('Valor convertido: ',convert(adc1_read,5,0,1))
	print('*-----------------------------------------------*')
	print('ADC2')
	print('Valor s/ conversao: ', adc2_read)
	print('Valor convertido: ',convert(adc2_read,5,0,1))
	print('*-----------------------------------------------*')
	

spi.close()



