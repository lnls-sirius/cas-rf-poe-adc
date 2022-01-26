#!/usr/bin/env python3
import argparse
from src.data import write_data, cal_sys_data

if __name__ == "__main__":
    args = argparse.ArgumentParser("Gen Calibration System Database")
    args.add_argument("--dest", default="../CalSysSup", help="destination directory")
    parsed = args.parse_args()

    for data in cal_sys_data:
        write_data(parsed.dest, data)
