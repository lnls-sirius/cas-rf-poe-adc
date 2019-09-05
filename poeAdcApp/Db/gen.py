#!/usr/bin/python3
from string import Template
adc = Template('''
record(stringin, "${ioc}:SaveName"){
    field(VAL,  "${ioc}.sav")
    field(PINI, "YES")
    field(DESC, "Autosave destination file")
}

record(waveform, "${ioc}:ADC0:Data-Mon"){
    field(PINI, "YES")
    field(DESC, "ADC0 Data")
    field(SCAN, "$$(SCAN=1 second)")
    field(DTYP, "stream")
    field(INP,  "@ADC.proto getData(ADC0) $$(PORT) $$(A)")
    field(FTVL, "DOUBLE")
    field(NELM, "4")
}
record(calc, "${ioc}:ADC0:Data-Mon_enbl"){
   field(CALC, "A#0")
   field(INPA, "${ioc}:ADC0:Data-Mon.STAT CP")
   field(INPB, "${ioc}:ADC0:Data-Mon CP")
}
record(waveform, "${ioc}:ADC1:Data-Mon"){
    field(PINI, "YES")
    field(DESC, "ADC1 Data")
    field(SCAN, "$$(SCAN=1 second)")
    field(DTYP, "stream")
    field(INP,  "@ADC.proto getData(ADC1) $$(PORT) $$(A)")
    field(FTVL, "DOUBLE")
    field(NELM, "4")
}
record(calc, "${ioc}:ADC1:Data-Mon_enbl"){
   field(CALC, "A#0")
   field(INPA, "${ioc}:ADC1:Data-Mon.STAT CP")
   field(INPB, "${ioc}:ADC1:Data-Mon CP")
}
record(waveform, "${ioc}:ADC2:Data-Mon"){
    field(PINI, "YES")
    field(DESC, "ADC2 Data")
    field(SCAN, "$$(SCAN=1 second)")
    field(DTYP, "stream")
    field(INP,  "@ADC.proto getData(ADC2) $$(PORT) $$(A)")
    field(FTVL, "DOUBLE")
    field(NELM, "4")
}
record(calc, "${ioc}:ADC2:Data-Mon_enbl"){
   field(CALC, "A#0")
   field(INPA, "${ioc}:ADC2:Data-Mon.STAT CP")
   field(INPB, "${ioc}:ADC2:Data-Mon CP")
}
record(waveform, "${ioc}:ADC3:Data-Mon"){
    field(PINI, "YES")
    field(DESC, "ADC3 Data")
    field(SCAN, "$$(SCAN=1 second)")
    field(DTYP, "stream")
    field(INP,  "@ADC.proto getData(ADC3) $$(PORT) $$(A)")
    field(FTVL, "DOUBLE")
    field(NELM, "4")
}
record(calc, "${ioc}:ADC3:Data-Mon_enbl"){
   field(CALC, "A#0")
   field(INPA, "${ioc}:ADC3:Data-Mon.STAT CP")
   field(INPB, "${ioc}:ADC3:Data-Mon CP")
}
''')

power = Template('''
record(ao, "${NAME}:${OFS}${N}-Mon"){
    field(PREC, "2")
    field(EGU,  "dB")
    field(VAL,  "0")
    field(PINI, "YES")
}
record(calc, "${NAME}${N}_ADC"){
    field(CALC, "(5.*A/4095.)*(${CTE})")
    field(INPA, "${ioc}:ADC${ADC}:Data-Mon.VAL[${CH}] CP MSS")
    field(DISV, "1")
    field(DISS, "INVALID")
    field(SDIS, "${ioc}:ADC${ADC}:Data-Mon_enbl")
}
record(calc, "${NAME}:${dBm}${N}_CALC"){
    field(CALC, "${p5}*(F**4) + ${p4}*(F**3) + ${p3}*(F**2) + ${p2}*F + ${p1}")
    field(INPF, "${NAME}${N}_ADC CP MSS")
    field(DISV, "1")
    field(DISS, "INVALID")
    field(SDIS, "${ioc}:ADC${ADC}:Data-Mon_enbl")
}
record(calc, "${NAME}:${dBm}${N}-Mon"){
    field(CALC, "(A>${MIN})?(A + B):(-Inf)")
    field(INPA, "${NAME}:${dBm}${N}_CALC CP MSS")
    field(INPB, "${NAME}:${OFS}${N}-Mon CP MSS")
    field(PREC, "2")
    field(EGU,  "dBm")
    field(DISV, "1")
    field(DISS, "INVALID")
    field(SDIS, "${ioc}:ADC${ADC}:Data-Mon_enbl")
}
record(calc, "${NAME}:${W}${N}-Mon"){
    field(CALC, "(10**(A/10))*(1/1000)")
    field(INPA, "${NAME}:${dBm}${N}-Mon CP MSS")
    field(PREC, "2")
    field(EGU,  "W")
    field(DISV, "1")
    field(DISS, "INVALID")
    field(SDIS, "${ioc}:ADC${ADC}:Data-Mon_enbl")
}
''')

voltage = Template('''
record(calc, "${NAME}"){
    field(CALC, "(5.*A/4095.)*(${CTE})")
    field(INPA, "${ioc}:ADC${ADC}:Data-Mon.VAL[${CH}] CP MSS")
    field(EGU, "V")
    field(DESC, "${DESC}")
    field(DISV, "1")
    field(DISS, "INVALID")
    field(SDIS, "${ioc}:ADC${ADC}:Data-Mon_enbl")
}
''')

raw = Template('''
record(ai, "${NAME}"){
    field(INP,  "${ioc}:ADC${ADC}:Data-Mon.VAL[${CH}] CP MSS")
    field(PREC, "3")
    field(DISV, "1")
    field(DISS, "INVALID")
    field(SDIS, "${ioc}:ADC${ADC}:Data-Mon_enbl")
}

''')

current = Template('''
# ((ADC${ADC}[$CH] - 0.5) / 0.4)
record(calc, "${NAME}"){
    field(CALC, "(A - 0.5)/0.4")
    field(INPA, "${ioc}:ADC${ADC}:Data-Mon.VAL[${CH}] CP MSS")
    field(PREC, "3")
    field(EGU,  "A")
    field(DISV, "1")
    field(DISS, "INVALID")
    field(SDIS, "${ioc}:ADC${ADC}:Data-Mon_enbl")
}

''')

bi = Template('''
record(calc, "${NAME}_CALC"){
    field(CALC, "(A>2.5)?1:0")
    field(INPA, "${ioc}:ADC${ADC}:Data-Mon.VAL[${CH}] CP MSS")
    field(DISV, "1")
    field(DISS, "INVALID")
    field(SDIS, "${ioc}:ADC${ADC}:Data-Mon_enbl")
}
record(bi, "${NAME}"){
    field(DTYP, "Raw Soft Channel")
    field(INP,  "${NAME}_CALC CP MSS")
    field(ZNAM, "${ZNAM}")
    field(ONAM, "${ONAM}")
    field(DISV, "1")
    field(DISS, "INVALID")
    field(SDIS, "${ioc}:ADC${ADC}:Data-Mon_enbl")
}
''')

def res(R, R_):
    return str(((R_+R)/R_))

defaults = {'MIN':'-41.', 'CTE':'1.', 'DESC':'', 'W':'PwrW', 'dBm':'PwrdBm', 'OFS':'OFSdB'}

dbs = [
    {'ioc':'SIA-CalSys',
    'readings' : [
        {'ADC':'0', 'CH':'0', 'N':'1',  'NAME':'RA-RaSIA01:RF-LLRFCalSys', 'template':power, 'p1':'0', 'p2':'1', 'p3':'0', 'p4':'0', 'p5':'0'},
        {'ADC':'0', 'CH':'1', 'N':'2',  'NAME':'RA-RaSIA01:RF-LLRFCalSys', 'template':power, 'p1':'0', 'p2':'1', 'p3':'0', 'p4':'0', 'p5':'0'},
        {'ADC':'0', 'CH':'2', 'N':'3',  'NAME':'RA-RaSIA01:RF-LLRFCalSys', 'template':power, 'p1':'0', 'p2':'1', 'p3':'0', 'p4':'0', 'p5':'0'},
        {'ADC':'0', 'CH':'3', 'N':'4',  'NAME':'RA-RaSIA01:RF-LLRFCalSys', 'template':power, 'p1':'0', 'p2':'1', 'p3':'0', 'p4':'0', 'p5':'0'},

        {'ADC':'1', 'CH':'0', 'N':'5',  'NAME':'RA-RaSIA01:RF-LLRFCalSys', 'template':power, 'p1':'0', 'p2':'1', 'p3':'0', 'p4':'0', 'p5':'0'},
        {'ADC':'1', 'CH':'1', 'N':'6',  'NAME':'RA-RaSIA01:RF-LLRFCalSys', 'template':power, 'p1':'0', 'p2':'1', 'p3':'0', 'p4':'0', 'p5':'0'},
        {'ADC':'1', 'CH':'2', 'N':'7',  'NAME':'RA-RaSIA01:RF-LLRFCalSys', 'template':power, 'p1':'0', 'p2':'1', 'p3':'0', 'p4':'0', 'p5':'0'},
        {'ADC':'1', 'CH':'3', 'N':'8',  'NAME':'RA-RaSIA01:RF-LLRFCalSys', 'template':power, 'p1':'0', 'p2':'1', 'p3':'0', 'p4':'0', 'p5':'0'},

        {'ADC':'2', 'CH':'0', 'N':'9',  'NAME':'RA-RaSIA01:RF-LLRFCalSys', 'template':power, 'p1':'0', 'p2':'1', 'p3':'0', 'p4':'0', 'p5':'0'},
        {'ADC':'2', 'CH':'1', 'N':'10', 'NAME':'RA-RaSIA01:RF-LLRFCalSys', 'template':power, 'p1':'0', 'p2':'1', 'p3':'0', 'p4':'0', 'p5':'0'},
        {'ADC':'2', 'CH':'2', 'N':'11', 'NAME':'RA-RaSIA01:RF-LLRFCalSys', 'template':power, 'p1':'0', 'p2':'1', 'p3':'0', 'p4':'0', 'p5':'0'},
        {'ADC':'2', 'CH':'3', 'N':'12', 'NAME':'RA-RaSIA01:RF-LLRFCalSys', 'template':power, 'p1':'0', 'p2':'1', 'p3':'0', 'p4':'0', 'p5':'0'},

        {'ADC':'3', 'CH':'0', 'N':'13', 'NAME':'RA-RaSIA01:RF-LLRFCalSys', 'template':power, 'p1':'0', 'p2':'1', 'p3':'0', 'p4':'0', 'p5':'0'},
        {'ADC':'3', 'CH':'1', 'N':'14', 'NAME':'RA-RaSIA01:RF-LLRFCalSys', 'template':power, 'p1':'0', 'p2':'1', 'p3':'0', 'p4':'0', 'p5':'0'},
        {'ADC':'3', 'CH':'2', 'N':'15', 'NAME':'RA-RaSIA01:RF-LLRFCalSys', 'template':power, 'p1':'0', 'p2':'1', 'p3':'0', 'p4':'0', 'p5':'0'},
        {'ADC':'3', 'CH':'3', 'N':'16', 'NAME':'RA-RaSIA01:RF-LLRFCalSys', 'template':power, 'p1':'0', 'p2':'1', 'p3':'0', 'p4':'0', 'p5':'0'},
    ]},
    {'ioc':'SIA-CavPlDrv',
        'readings' : [
        {'ADC':'0', 'CH':'0', 'NAME':'RA-RaSIA01:RF-CavPlDrivers:VoltPos5V-Mon',  'template':voltage},
        {'ADC':'0', 'CH':'1', 'NAME':'RA-RaSIA01:RF-CavPlDrivers:Current5V-Mon',  'template':current},
        {'ADC':'0', 'CH':'2', 'NAME':'RA-RaSIA01:RF-CavPlDrivers:VoltPos48V-Mon', 'template':voltage, 'CTE':res(90.9,10.)},

        {'ADC':'1', 'CH':'0', 'NAME':'RA-RaSIA01:RF-CavPlDrivers:Dr1Current-Mon', 'template':current},
        {'ADC':'1', 'CH':'1', 'NAME':'RA-RaSIA01:RF-CavPlDrivers:Dr1Enbl-Sts',    'template':bi,  'ZNAM':'Enable', 'ONAM':'Disable'},
        {'ADC':'1', 'CH':'2', 'NAME':'RA-RaSIA01:RF-CavPlDrivers:Dr1Flt-Mon',     'template':bi,  'ZNAM':'Fail',   'ONAM':'Normal'},
        {'ADC':'1', 'CH':'3', 'NAME':'SI-03SP:RF-P5Cav:Pl1Pos-Mon',               'template':voltage},

        {'ADC':'2', 'CH':'0', 'NAME':'RA-RaSIA01:RF-CavPlDrivers:Dr2Current-Mon', 'template':current},
        {'ADC':'2', 'CH':'1', 'NAME':'RA-RaSIA01:RF-CavPlDrivers:Dr2Enbl-Sts',    'template':bi, 'ZNAM':'Enable', 'ONAM':'Disable'},
        {'ADC':'2', 'CH':'2', 'NAME':'RA-RaSIA01:RF-CavPlDrivers:Dr2Flt-Mon',     'template':bi, 'ZNAM':'Fail',   'ONAM':'Normal'},
        {'ADC':'2', 'CH':'3', 'NAME':'SI-03SP:RF-P5Cav:Pl2Pos-Mon',               'template':voltage},
    ]},
]

if __name__ == '__main__':
    for data in dbs:
        db = ''
        with open(data['ioc'] + '.db', 'w+') as f:
            db += adc.safe_substitute(defaults, ioc=data['ioc'])
            for reading in data['readings']:
                db += reading['template'].safe_substitute(defaults, ioc=data['ioc'], **reading)
            f.write(db)

