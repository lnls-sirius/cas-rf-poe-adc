#!/usr/bin/env python3
import argparse
from src.data import write_data, cav_pl_drv_data

if __name__ == "__main__":
    args = argparse.ArgumentParser("Gen Cav PL Drv Database")
    args.add_argument("--dest", default="../PlDrvSup", help="destination directory")
    parsed = args.parse_args()

    write_data(parsed.dest, cav_pl_drv_data)
