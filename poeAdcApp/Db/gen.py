#!/usr/bin/python3
from string import Template
voltage = Template('''
record(calc, "${NAME}"){
    field(CALC, "(5.*A/4095.)*(${CTE})")
    field(INPA, "$(P)$(R):ADC${ADC}:Data-Mon.VAL[${CH}] CP MSS")
    field(EGU, "V")
    field(DESC, "${DESC}")
}
''')

def res(R, R_):
    return str(((R_+R)/R_))

defaults = {'CTE':'1', 'DESC':''}

dbs = [
    {'ioc':'SIA-CalSys.db',
    'readings' : [
        {'ADC':'0', 'CH':'0', 'NAME':'RA-RaSIA01:RF-LLRFCalSys:PwrdBm1-Mon', 'template':voltage},
        {'ADC':'0', 'CH':'1', 'NAME':'RA-RaSIA01:RF-LLRFCalSys:PwrdBm2-Mon', 'template':voltage},
        {'ADC':'0', 'CH':'2', 'NAME':'RA-RaSIA01:RF-LLRFCalSys:PwrdBm3-Mon', 'template':voltage},
        {'ADC':'0', 'CH':'3', 'NAME':'RA-RaSIA01:RF-LLRFCalSys:PwrdBm4-Mon', 'template':voltage},

        {'ADC':'1', 'CH':'0', 'NAME':'RA-RaSIA01:RF-LLRFCalSys:PwrdBm5-Mon', 'template':voltage},
        {'ADC':'1', 'CH':'1', 'NAME':'RA-RaSIA01:RF-LLRFCalSys:PwrdBm6-Mon', 'template':voltage},
        {'ADC':'1', 'CH':'2', 'NAME':'RA-RaSIA01:RF-LLRFCalSys:PwrdBm7-Mon', 'template':voltage},
        {'ADC':'1', 'CH':'3', 'NAME':'RA-RaSIA01:RF-LLRFCalSys:PwrdBm8-Mon', 'template':voltage},

        {'ADC':'2', 'CH':'0', 'NAME':'RA-RaSIA01:RF-LLRFCalSys:PwrdBm9-Mon', 'template':voltage},
        {'ADC':'2', 'CH':'1', 'NAME':'RA-RaSIA01:RF-LLRFCalSys:PwrdBm10-Mon', 'template':voltage},
        {'ADC':'2', 'CH':'2', 'NAME':'RA-RaSIA01:RF-LLRFCalSys:PwrdBm11-Mon', 'template':voltage},
        {'ADC':'2', 'CH':'3', 'NAME':'RA-RaSIA01:RF-LLRFCalSys:PwrdBm12-Mon', 'template':voltage},

        {'ADC':'3', 'CH':'0', 'NAME':'RA-RaSIA01:RF-LLRFCalSys:PwrdBm13-Mon', 'template':voltage},
        {'ADC':'3', 'CH':'1', 'NAME':'RA-RaSIA01:RF-LLRFCalSys:PwrdBm14-Mon', 'template':voltage},
        {'ADC':'3', 'CH':'2', 'NAME':'RA-RaSIA01:RF-LLRFCalSys:PwrdBm15-Mon', 'template':voltage},
        {'ADC':'3', 'CH':'3', 'NAME':'RA-RaSIA01:RF-LLRFCalSys:PwrdBm16-Mon', 'template':voltage},
    ]},
    {'ioc':'SIA-CavPlDrv.db',
        'readings' : [
        {'ADC':'0', 'CH':'0', 'NAME':'RA-RaSIA01:RF-CavPlDrivers:VoltPos5V-Mon',  'template':voltage},
        {'ADC':'0', 'CH':'1', 'NAME':'RA-RaSIA01:RF-CavPlDrivers:Current5V-Mon',  'template':voltage},
        {'ADC':'0', 'CH':'2', 'NAME':'RA-RaSIA01:RF-CavPlDrivers:VoltPos48V-Mon', 'template':voltage, 'CTE':res(90.9,10.)},

        {'ADC':'1', 'CH':'0', 'NAME':'RA-RaSIA01:RF-CavPlDrivers:Dr1Current-Mon', 'template':voltage},
        {'ADC':'1', 'CH':'1', 'NAME':'RA-RaSIA01:RF-CavPlDrivers:Dr1Enbl-Sts',    'template':voltage},
        {'ADC':'1', 'CH':'2', 'NAME':'RA-RaSIA01:RF-CavPlDrivers:Dr1Flt-Mon',     'template':voltage},
        {'ADC':'1', 'CH':'3', 'NAME':'SI-03SP:RF-P5Cav:Pl1Pos-Mon',               'template':voltage},

        {'ADC':'2', 'CH':'0', 'NAME':'RA-RaSIA01:RF-CavPlDrivers:Dr2Current-Mon', 'template':voltage},
        {'ADC':'2', 'CH':'1', 'NAME':'RA-RaSIA01:RF-CavPlDrivers:Dr2Enbl-Sts',    'template':voltage},
        {'ADC':'2', 'CH':'2', 'NAME':'RA-RaSIA01:RF-CavPlDrivers:Dr2Flt-Mon',     'template':voltage},
        {'ADC':'2', 'CH':'3', 'NAME':'SI-03SP:RF-P5Cav:Pl2Pos-Mon',               'template':voltage},
    ]},
]

if __name__ == '__main__':
    for data in dbs:
        db = ''
        with open(data['ioc'], 'w+') as f:
            for reading in data['readings']:
                db += reading['template'].safe_substitute(defaults, **reading)
            f.write(db)

