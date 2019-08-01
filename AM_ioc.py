# -*- coding: utf-8 -*-

from pcaspy import Driver, SimpleServer
from queue import Queue
import random
import threading
from AM_Classes import *
import os 
import time

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


Prefix = 'ADC'
PVs = {}
for j in range(4):		#construção das PVs
	x = str(j)
	PVs['0:CHANNEL' + x] = {"type" : "float", "prec" : 3, "unit" : "V",}
	PVs['1:CHANNEL' + x] = {"type" : "float", "prec" : 3, "unit" : "V",}
	PVs['2:CHANNEL' + x] = {"type" : "float", "prec" : 3, "unit" : "V",}
	PVs['3:CHANNEL' + x] = {"type" : "float", "prec" : 3, "unit" : "V",}


	
class My_Driver(Driver):

	def __init__ (self):
		Driver.__init__(self)
		
		self.queue = Queue()
		self.event = threading.Event()
		
		self.process_thread = threading.Thread(target = self.processThread)
		self.scan_thread = threading.Thread(target = self.scanThread)
		self.print_thread = threading.Thread(target = self.printThread)
		
		self.process_thread.setDaemon(True)
		self.scan_thread.setDaemon(True)
		self.print_thread.setDaemon(True)
		
		self.print_thread.start()
		self.process_thread.start()
		self.scan_thread.start()

	def printThread(self):
		n = 0
		while(True):
			input()
			print (n)
			n += 1
			time.sleep(1)
			
			
			
	def scanThread(self):
		while (True):
			self.queue.put(['READ'])
			self.event.wait(SCAN_PERIOD)
	
		
		
	def processThread(self):
	
		while (True):
		
			item = self.queue.get()
			if item == ['READ']:
			
				adc0_read = ADC0.read([0,1,2,3])
				adc1_read = ADC1.read([0,1,2,3])
				adc2_read = ADC2.read([0,1,2,3])
				adc3_read = ADC3.read([0,1,2,3])
				c0 = convert(adc0_read,5,0,1)
				c1 = convert(adc1_read,5,0,1)
				c2 = convert(adc2_read,5,0,1)
				c3 = convert(adc3_read,5,0,1)
				n=0
				for i in sorted(PVs):
					if n <= 3:
						self.setParam(i,float(c0[n]))
					elif n<=7:
						self.setParam(i,float(c1[n-4]))
					elif n<=11:
						self.setParam(i,float(c2[n-8]))
					elif n<=15:
						self.setParam(i,float(c3[n-12]))
					n += 1
					self.updatePVs()

				
			else:
				pass


				
				
if __name__ == "__main__":

	CAserver = SimpleServer()
	CAserver.createPV(Prefix, PVs)
	driver = My_Driver()

	while True:
		CAserver.process(0.1)
