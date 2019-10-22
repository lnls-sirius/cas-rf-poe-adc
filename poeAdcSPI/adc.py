#!/usr/bin/python3
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
        tamanho = len(channels)
        
        #Envio de setup inicial
        GPIO.output(self.port,0)
        self.spi.xfer2([0x83,0x10])
        GPIO.output(self.port,1)
        
        _channels = channels[:]
        _channels.append(channels[tamanho-1]+1)
        for i in _channels:
            GPIO.output(self.port, 0)
            data = self.spi.xfer2([0x83 + (4)*i, 0x10])
            GPIO.output(self.port, 1)
            calc = (data[0]&0x0F)*256 + data[1]
            if calc > (4096):
                calc = 0
            saida.append(calc)
        return saida[1:]
            
