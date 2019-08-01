#!/usr/bin/python
import argparse
import logging
import os
import time

from server import Comm

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='RF POE ADC module',
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--unix-socket-path', dest='unix_socket_path', help='UNIX socket address.', default='./unix-socket')
    parser.add_argument('--debug', action='store_true')
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO, format='%(asctime)-15s [%(levelname)s] %(message)s',
        datefmt='%d/%m/%Y %H:%M:%S')
    logger = logging.getLogger()
    logger.info('Sleep for 30 seconds')
    time.sleep(30)

    os.system('config-pin P9.17 spi_cs')
    os.system('config-pin P9.18 spi')
    os.system('config-pin P9.21 spi')
    os.system('config-pin P9.22 spi_sclk')

    comm = Comm(args.unix_socket_path)
    comm.serve()

