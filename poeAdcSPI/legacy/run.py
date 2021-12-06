#!/usr/bin/python
import argparse
import logging
import os
import time


def config_pins():
    os.system("config-pin P9_17 spi_cs")  # CS
    os.system("config-pin P9_18 spi")  # DI
    os.system("config-pin P9_21 spi")  # DO
    os.system("config-pin P9_22 spi_sclk")  # CLK

    os.system("config-pin P9_14 out")  # Relay

    os.system("config-pin P9_24 out")  # ADC 1
    os.system("config-pin P9_26 out")  # ADC 2


def config_logger():
    logging.basicConfig(
        level=logging.DEBUG if args.debug else logging.INFO,
        format="%(asctime)-15s [%(levelname)s] %(message)s",
        datefmt="%d/%m/%Y %H:%M:%S",
    )


def parse_args():
    parser = argparse.ArgumentParser(
        description="RF calibration module SPI interface",
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


if __name__ == "__main__":
    args = parse_args()
    config_logger()
    logger = logging.getLogger()
    logger.info("Sleep for 30 seconds")

    time.sleep(30)

    config_pins()

    from server import Comm

    comm = Comm(args.unix_socket_path)
    comm.serve()
