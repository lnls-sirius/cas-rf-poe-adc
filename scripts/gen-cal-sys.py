#!/usr/bin/env python
import argparse
from src.data import write_data, cal_sys_data

if __name__ == "__main__":
    args = argparse.ArgumentParser("Gen Calibration System Database")
    args.add_argument("--dest", default="../CalSysSup", help="destination directory")
    parsed = args.parse_args()

    write_data(parsed.dest, cal_sys_data)
