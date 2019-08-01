#!/usr/bin/python3
# -*- coding: utf-8 -*-
import logging
import os
import socket

from Adafruit_BBIO.SPI import SPI
from adc import ADC

logger = logging.getLogger()

class ResponseType():
    NO_RESPONSE = 'NO_RESPONSE'
    EXCEPTION   = 'EXCEPTION'
    UNSUPPORTED_COMMAND = 'UNSUPPORTED_COMMAND'

class Comm():
    def __init__(self, unix_socket_path, *args, **kwargs):
        self.unix_socket_path = unix_socket_path
        self.connection = None
        self.welcome_socket = None

        spi = SPI(0,0)
        spi.msh = 2000000
        spi.mode = 1

        self.ADC0 = ADC("P9_24", spi)
        self.ADC1 = ADC("P9_26", spi)
        self.ADC2 = ADC("P9_28", spi)
        self.ADC3 = ADC("P9_30", spi)

    def serve(self):
        try:
            if os.path.exists(self.unix_socket_path):
                logger.warning('Unix socket {} already exist'.format(self.unix_socket_path))
                os.unlink(self.unix_socket_path)

            if self.welcome_socket != None:
                logger.warning('Welcome socket already istantiated')

            self.welcome_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
            self.welcome_socket.bind(self.unix_socket_path)
            os.system('chown iocuser:ioc {}'.format(self.unix_socket_path))

            logger.info('Unix socket created at {}'.format(self.unix_socket_path))
            self.welcome_socket.listen(1)

            while True:
                logger.info('Unix welcome socket listening')
                connection, client_address = self.welcome_socket.accept()
                logger.info('Client {} connected'.format(client_address))

                connection.settimeout(30)

                self.handle_connection(connection)
        except:
            logger.exception('Comm exception')
        finally:
            self.welcome_socket.close()
            os.remove(self.unix_socket_path)
            logger.info('Comm server shutdown')
            self.welcome_socket = None

    def handle_connection(self, connection):
        try:
            while True:
                command = connection.recv(1024).decode('utf-8')
                if command   == 'ADC0:DATA?':
                    response = str(ADC0.read([0,1,2,3]))
                elif command == 'ADC1:DATA?':
                    response = str(ADC1.read([0,1,2,3]))
                elif command == 'ADC2:DATA?':
                    response = str(ADC2.read([0,1,2,3]))
                elif command == 'ADC3:DATA?':
                    response = str(ADC3.read([0,1,2,3]))
                else:
                    response = ResponseType.UNSUPPORTED_COMMAND

                connection.sendall('{}\r\n'.format(response).encode('utf-8'))
                logger.debug('Command {} Length {}'.format(command, response))
        except:
            logger.exception('Connection exception')
        finally:
            logger.warning('Connection closed')
            connection.close()

