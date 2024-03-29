#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse
import logging
import os
import time

from server import Comm


def config_pins():

    os.system("config-pin P9.17 spi_cs")
    os.system("config-pin P9.18 spi")
    os.system("config-pin P9.21 spi")
    os.system("config-pin P9.22 spi_sclk")


def parse_args():

    parser = argparse.ArgumentParser(
        description="RF POE ADC module",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--unix-socket-path",
        dest="unix_socket_path",
        help="UNIX socket address.",
        default="./unix-socket",
    )
    parser.add_argument("--debug", action="store_true")
    return parser.parse_args()


def config_logger():
    logging.basicConfig(
        level=logging.DEBUG if args.debug else logging.INFO,
        format="%(asctime)-15s [%(levelname)s] %(message)s",
        datefmt="%d/%m/%Y %H:%M:%S",
    )


if __name__ == "__main__":

    args = parse_args()

    config_logger()

    logger = logging.getLogger()
    logger.info("Sleep for 30 seconds")
    time.sleep(30)

    config_pins()

    comm = Comm(args.unix_socket_path)
    comm.serve()
