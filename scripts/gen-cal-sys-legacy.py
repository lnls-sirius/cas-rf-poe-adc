#!/usr/bin/env python3
from string import Template

wf = Template(
    """
record(stringin, "$(P):SaveName"){
    field(VAL,  "$(P).sav")
    field(PINI, "YES")
    field(DESC, "Autosave destination file")
}

record(waveform, "${PV_VALS}"){
    field(DTYP, "stream")
    field(SCAN, ".5 second")
    field(DTYP, "stream")
    field(INP,  "@BO-CalSys.proto getData $(PORT) $(A)")
    field(FTVL, "FLOAT")
    field(NELM, "17")
}

record(calc, "${PV_VALS}_enbl"){
   field(CALC, "A#0")
   field(INPA, "${PV_VALS}.STAT CP")
   field(INPB, "${PV_VALS} CP")
}

"""
)

"""
:param PV:
:param PV_VALS:
:param N:
:param MIN:
:param p5:
:param p4:
:param p3:
:param p2:
:param p1:
"""
adc = Template(
    """
record(calc, "${PV}${N}_ADC"){
    field(CALC, "((A/10)/4095.)*5.")
    field(INPA, "${PV_VALS}.VAL[${N}] CP MSS")
    field(EGU,  "V")
    field(PREC, "2")

    field(LOLO, "0.3")
    field(LLSV, "INVALID")
}

record(calc, "${PV}${N}_enbl"){
   field(CALC, "(A+B)#0")
   field(INPA, "${PV}${N}_ADC.STAT CP")
   field(INPB, "${PV_VALS}_enbl CP")

   field(INPC, "${PV}${N}_ADC CP") # Rec process
}

record(calc, "${PV}${N}_CALC"){
    field(CALC, "A*(F**4) + B*(F**3) + C*(F**2) + D*F + E")
    field(INPA, "${p5}")
    field(INPB, "${p4}")
    field(INPC, "${p3}")
    field(INPD, "${p2}")
    field(INPE, "${p1}")
    field(EGU,  "dBm")
    field(PREC, "2")

    field(INPF, "${PV}${N}_ADC CP MSS")
    
    field(DISV, "1")
    field(DISS, "INVALID")
    field(SDIS, "${PV}${N}_enbl")
}

record(ao, "${PV_OFS}${N}-Mon"){
    field(PREC, "2")
    field(EGU,  "dB")
    field(VAL,  "0")
    field(PINI, "YES")
}

record(calc, "${PV}${N}-Mon"){
    field(CALC, "(A>${MIN})?(A + B):(-Inf)")
    field(INPA, "${PV}${N}_CALC CP MSS")
    field(INPB, "${PV_OFS}${N}-Mon CP MSS")
    field(PREC, "2")
    field(EGU,  "dBm")
    field(DISV, "1")
    field(DISS, "INVALID")
    field(SDIS, "${PV}${N}_enbl")
}

record(calc, "${PV_W}${N}-Mon"){
    field(CALC, "(10**(A/10))*(1/1000)")
    field(INPA, "${PV}${N}-Mon CP MSS")
    field(PREC, "2")
    field(EGU,  "W")
    field(DISV, "1")
    field(DISS, "INVALID")
    field(SDIS, "${PV}${N}_enbl")
}
"""
)

on_off = Template(
    """
record(mbbi, "${PV_STAT}"){
    field(INP, "${PV_VALS}.VAL[0] CP MSS")

    field(ZRVL, "0")
    field(ONVL, "1")

    field(ZRST, "Off")
    field(ONST, "On")
}
"""
)


def generate_bo_cal_sys():
    PV_VALS = "RA-RaBO01:RF-RFCalSys:Vals"
    PV_STAT = "RA-RaBO01:RF-RFCalSys:StatusCalOn"
    PV = "RA-RaBO01:RF-RFCalSys:PwrdBm"
    PV_W = "RA-RaBO01:RF-RFCalSys:PwrW"
    PV_OFS = "RA-RaBO01:RF-RFCalSys:OFSdB"
    MIN = "-41.0"

    defaults = {
        "MIN": MIN,
        "PV": PV,
        "PV_VALS": PV_VALS,
        "PV_OFS": PV_OFS,
        "PV_W": PV_W,
        "PV_STAT": PV_STAT,
    }

    # WF
    print(wf.safe_substitute(defaults))

    # On/Off
    kwargs = {"N": 0}
    print(on_off.safe_substitute(defaults, **kwargs))

    # Power Readings
    # Channel 1 (ADC PCB 1, CH1)
    kwargs = {
        "N": 1,
        "p1": 26.307,
        "p2": 7.6581,
        "p3": -53.648,
        "p4": 26.107,
        "p5": -4.6759,
    }
    print(adc.safe_substitute(defaults, **kwargs))

    # Channel 2 (ADC PCB 1, CH1)
    kwargs = {
        "N": 2,
        "p1": 29.637,
        "p2": -2.9709,
        "p3": -39.974,
        "p4": 18.446,
        "p5": -3.1204,
    }
    PV_VALS = "RA-RaBO01:RF-RFCalSys:Vals"
    PV_STAT = "RA-RaBO01:RF-RFCalSys:StatusCalOn"
    PV = "RA-RaBO01:RF-RFCalSys:PwrdBm"
    PV_W = "RA-RaBO01:RF-RFCalSys:PwrW"
    PV_OFS = "RA-RaBO01:RF-RFCalSys:OFSdB"
    MIN = "-41.0"

    defaults = {
        "MIN": MIN,
        "PV": PV,
        "PV_VALS": PV_VALS,
        "PV_OFS": PV_OFS,
        "PV_W": PV_W,
        "PV_STAT": PV_STAT,
    }

    # WF
    print(wf.safe_substitute(defaults))

    # On/Off
    kwargs = {"N": 0}
    print(on_off.safe_substitute(defaults, **kwargs))

    # Power Readings
    # Channel 1 (ADC PCB 1, CH1)
    kwargs = {
        "N": 1,
        "p1": 26.307,
        "p2": 7.6581,
        "p3": -53.648,
        "p4": 26.107,
        "p5": -4.6759,
    }
    print(adc.safe_substitute(defaults, **kwargs))

    # Channel 2 (ADC PCB 1, CH1)
    kwargs = {
        "N": 2,
        "p1": 29.637,
        "p2": -2.9709,
        "p3": -39.974,
        "p4": 18.446,
        "p5": -3.1204,
    }
    print(adc.safe_substitute(defaults, **kwargs))

    # Channel 3 (ADC PCB 1, CH2)
    kwargs = {
        "N": 3,
        "p1": 23.264,
        "p2": 17.234,
        "p3": -65.181,
        "p4": 32.361,
        "p5": -5.9411,
    }
    print(adc.safe_substitute(defaults, **kwargs))

    # Channel 4 (ADC PCB 1, CH3)
    kwargs = {
        "N": 4,
        "p1": 29.996,
        "p2": -2.412,
        "p3": -41.851,
        "p4": 20.226,
        "p5": -3.6413,
    }
    print(adc.safe_substitute(defaults, **kwargs))

    # Channel 5 (ADC PCB 1, CH4)
    kwargs = {
        "N": 5,
        "p1": 24.592,
        "p2": 13.793,
        "p3": -60.338,
        "p4": 29.492,
        "p5": -5.3428,
    }
    print(adc.safe_substitute(defaults, **kwargs))

    # Channel 6 (ADC PCB 1, CH5)
    kwargs = {
        "N": 6,
        "p1": 23.949,
        "p2": 15.762,
        "p3": -62.507,
        "p4": 30.325,
        "p5": -5.4278,
    }
    print(adc.safe_substitute(defaults, **kwargs))

    # Channel 7 (ADC PCB 1, CH6)
    kwargs = {
        "N": 7,
        "p1": 25.86,
        "p2": 9.2711,
        "p3": -56.011,
        "p4": 27.684,
        "p5": -5.077,
    }
    print(adc.safe_substitute(defaults, **kwargs))

    # Channel 8 (ADC PCB 1, CH7)
    kwargs = {
        "N": 8,
        "p1": 26.347,
        "p2": 6.0158,
        "p3": -49.13,
        "p4": 22.541,
        "p5": -3.8038,
    }
    print(adc.safe_substitute(defaults, **kwargs))

    # Channel 9 (ADC PCB 2, CH0)
    kwargs = {
        "N": 9,
        "p1": 24.396,
        "p2": 12.915,
        "p3": -57.398,
        "p4": 26.944,
        "p5": -4.6637,
    }
    print(adc.safe_substitute(defaults, **kwargs))

    # Channel 10 (ADC PCB 2, CH1)
    kwargs = {
        "N": 10,
        "p1": 26.928,
        "p2": 5.7414,
        "p3": -50.567,
        "p4": 24.195,
        "p5": -4.2941,
    }
    print(adc.safe_substitute(defaults, **kwargs))

    # Channel 11 (ADC PCB 2, CH2)
    kwargs = {
        "N": 11,
        "p1": 24.27,
        "p2": 13.93,
        "p3": -59.559,
        "p4": 28.652,
        "p5": -5.1056,
    }
    print(adc.safe_substitute(defaults, **kwargs))

    # Channel 12 (ADC PCB 2, CH3)
    kwargs = {
        "N": 12,
        "p1": 23.393,
        "p2": 17.506,
        "p3": -65.01,
        "p4": 31.765,
        "p5": -5.7288,
    }
    print(adc.safe_substitute(defaults, **kwargs))

    # Channel 13 (ADC PCB 2, CH4)
    kwargs = {
        "N": 13,
        "p1": 25.407,
        "p2": 10.57,
        "p3": -56.513,
        "p4": 27.402,
        "p5": -4.9173,
    }
    print(adc.safe_substitute(defaults, **kwargs))

    # Channel 14 (ADC PCB 2, CH5)
    kwargs = {
        "N": 14,
        "p1": 26.805,
        "p2": 6.3015,
        "p3": -50.449,
        "p4": 23.956,
        "p5": -4.2051,
    }
    print(adc.safe_substitute(defaults, **kwargs))

    # Channel 15 (ADC PCB 2, CH6)
    kwargs = {
        "N": 15,
        "p1": 24.922,
        "p2": 10.916,
        "p3": -56.348,
        "p4": 27.076,
        "p5": -4.7969,
    }
    print(adc.safe_substitute(defaults, **kwargs))

    # Channel 16 (ADC PCB 2, CH7)
    kwargs = {
        "N": 16,
        "p1": 20.502,
        "p2": 25.687,
        "p3": -73.787,
        "p4": 35.747,
        "p5": -6.3593,
    }
    print(adc.safe_substitute(defaults, **kwargs))
    print(adc.safe_substitute(defaults, **kwargs))

    # Channel 3 (ADC PCB 1, CH2)
    kwargs = {
        "N": 3,
        "p1": 23.264,
        "p2": 17.234,
        "p3": -65.181,
        "p4": 32.361,
        "p5": -5.9411,
    }
    print(adc.safe_substitute(defaults, **kwargs))

    # Channel 4 (ADC PCB 1, CH3)
    kwargs = {
        "N": 4,
        "p1": 29.996,
        "p2": -2.412,
        "p3": -41.851,
        "p4": 20.226,
        "p5": -3.6413,
    }
    print(adc.safe_substitute(defaults, **kwargs))

    # Channel 5 (ADC PCB 1, CH4)
    kwargs = {
        "N": 5,
        "p1": 24.592,
        "p2": 13.793,
        "p3": -60.338,
        "p4": 29.492,
        "p5": -5.3428,
    }
    print(adc.safe_substitute(defaults, **kwargs))

    # Channel 6 (ADC PCB 1, CH5)
    kwargs = {
        "N": 6,
        "p1": 23.949,
        "p2": 15.762,
        "p3": -62.507,
        "p4": 30.325,
        "p5": -5.4278,
    }
    print(adc.safe_substitute(defaults, **kwargs))

    # Channel 7 (ADC PCB 1, CH6)
    kwargs = {
        "N": 7,
        "p1": 25.86,
        "p2": 9.2711,
        "p3": -56.011,
        "p4": 27.684,
        "p5": -5.077,
    }
    print(adc.safe_substitute(defaults, **kwargs))

    # Channel 8 (ADC PCB 1, CH7)
    kwargs = {
        "N": 8,
        "p1": 26.347,
        "p2": 6.0158,
        "p3": -49.13,
        "p4": 22.541,
        "p5": -3.8038,
    }
    print(adc.safe_substitute(defaults, **kwargs))

    # Channel 9 (ADC PCB 2, CH0)
    kwargs = {
        "N": 9,
        "p1": 24.396,
        "p2": 12.915,
        "p3": -57.398,
        "p4": 26.944,
        "p5": -4.6637,
    }
    print(adc.safe_substitute(defaults, **kwargs))

    # Channel 10 (ADC PCB 2, CH1)
    kwargs = {
        "N": 10,
        "p1": 26.928,
        "p2": 5.7414,
        "p3": -50.567,
        "p4": 24.195,
        "p5": -4.2941,
    }
    print(adc.safe_substitute(defaults, **kwargs))

    # Channel 11 (ADC PCB 2, CH2)
    kwargs = {
        "N": 11,
        "p1": 24.27,
        "p2": 13.93,
        "p3": -59.559,
        "p4": 28.652,
        "p5": -5.1056,
    }
    print(adc.safe_substitute(defaults, **kwargs))

    # Channel 12 (ADC PCB 2, CH3)
    kwargs = {
        "N": 12,
        "p1": 23.393,
        "p2": 17.506,
        "p3": -65.01,
        "p4": 31.765,
        "p5": -5.7288,
    }
    print(adc.safe_substitute(defaults, **kwargs))

    # Channel 13 (ADC PCB 2, CH4)
    kwargs = {
        "N": 13,
        "p1": 25.407,
        "p2": 10.57,
        "p3": -56.513,
        "p4": 27.402,
        "p5": -4.9173,
    }
    print(adc.safe_substitute(defaults, **kwargs))

    # Channel 14 (ADC PCB 2, CH5)
    kwargs = {
        "N": 14,
        "p1": 26.805,
        "p2": 6.3015,
        "p3": -50.449,
        "p4": 23.956,
        "p5": -4.2051,
    }
    print(adc.safe_substitute(defaults, **kwargs))

    # Channel 15 (ADC PCB 2, CH6)
    kwargs = {
        "N": 15,
        "p1": 24.922,
        "p2": 10.916,
        "p3": -56.348,
        "p4": 27.076,
        "p5": -4.7969,
    }
    print(adc.safe_substitute(defaults, **kwargs))

    # Channel 16 (ADC PCB 2, CH7)
    kwargs = {
        "N": 16,
        "p1": 20.502,
        "p2": 25.687,
        "p3": -73.787,
        "p4": 35.747,
        "p5": -6.3593,
    }
    print(adc.safe_substitute(defaults, **kwargs))


if __name__ == "__main__":
    generate_bo_cal_sys()
