#!/usr/bin/python
# -*- coding: utf-8 -*-
import Adafruit_BBIO.GPIO as GPIO

class ADC:
    
    #inicializa com PORT sendo uma das portas onde estao ADC1, ADC2, ADC3 e ADC4
    def __init__(self, PORT, SPI):
        #Configurações iniciais
        self.spi = SPI
        self.port = PORT
        GPIO.setup(self.port, GPIO.OUT)
        GPIO.output(self.port,1)
        
        #Configuração do ADC
        GPIO.output(self.port,0)
        self.spi.xfer2([0xff,0xff])
        GPIO.output(self.port,1)
        
        #Envio de setup inicial
        GPIO.output(self.port,0)
        self.spi.xfer2([0x83,0x10])
        GPIO.output(self.port,1)
    

    def __str__(self):
        return "ADC localizado porta: " + self.port
        
        
    def read(self,channels):
        " Retorna valor medido pelo ADC (Valor de 0 4095) "
        saida = []
        if type(channels) == list:
            tamanho = len(channels)
            
            _channels = channels[:]
            _channels.append(channels[tamanho-1]+1)
            for i in _channels:
                GPIO.output(self.port, 0)
                data = self.spi.xfer2([0x83 + (4)*i, 0x10])
                GPIO.output(self.port, 1)
                calc = (data[0] - (i-1)*(16)) * (256) + data[1]
                if calc > (4096):
                    calc = 0
                saida.append(calc)
            return saida[1:]
        else:
            c = channels
            for i in range(2):
                GPIO.output(self.port,0)
                data = self.spi.xfer2([0x83+(4)*c,0x10])
                GPIO.output(self.port,1)
            calc = (data[0] - (c)*(16)) * (256) + data[1]
            if calc > 4096:
                calc = 0
            saida = (calc)
            return saida
            
''' 
        
def convert(ADC,Vref,R,R_):
    "ADC é o valor a ser convertido, R e R_ são os resistores que variam na PCB,VCC é a tensão máxima"
    "Para referencia com o esquemático: R* = R e R** = R_"
    
    if type(ADC) == list:
        s = []
        for i in ADC:
            x = i*Vref/4095.0
            y = (x * (R+R_))/R_
            y = "{0:.2f}".format(y,2)
            s.append(y)
        return s
        
    else:
        x = ADC*Vref/4095.0
        y = (x * (R+R_))/R_
        y = "{0:.2f}".format(y,2)
        return y
		

def value(channels, R1= [], R2= [], R3= [], R4= [], R5= [], R6= [], R7= [], R8 = []):
	lista = R1+R2+R3+R4+R5+R6+R7+R8
	if type(channels) == list:
		if (len(lista)/2) != len(channels):
			print("Please insert the Resistors values [R, R_]. R* = R & R** = R_")
'''        
