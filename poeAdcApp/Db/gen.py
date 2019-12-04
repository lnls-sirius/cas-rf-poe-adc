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
    field(LOLO, "0.3")
    field(LLSV, "INVALID")
}
record(calc, "${NAME}${N}_enbl"){
   field(CALC, "(A+B)#0")
   field(INPA, "${ioc}:ADC${ADC}:Data-Mon_enbl CP")
   field(INPB, "${NAME}${N}_ADC.STAT CP")
   field(INPC, "${NAME}${N}_ADC CP")
}
record(calc, "${NAME}:${dBm}${N}_CALC"){
    field(CALC, "${p5}*(F**4) + ${p4}*(F**3) + ${p3}*(F**2) + ${p2}*F + ${p1}")
    field(INPF, "${NAME}${N}_ADC CP MSS")
    field(DISV, "1")
    field(DISS, "INVALID")
    field(SDIS, "${NAME}${N}_enbl")
}
record(calc, "${NAME}:${dBm}${N}-Mon"){
    field(CALC, "(A>${MIN})?(A + B):(-Inf)")
    field(INPA, "${NAME}:${dBm}${N}_CALC CP MSS")
    field(INPB, "${NAME}:${OFS}${N}-Mon CP MSS")
    field(PREC, "2")
    field(EGU,  "dBm")
    field(DISV, "1")
    field(DISS, "INVALID")
    field(SDIS, "${NAME}${N}_enbl")
}
record(calc, "${NAME}:${W}${N}-Mon"){
    field(CALC, "(10**(A/10))*(1/1000)")
    field(INPA, "${NAME}:${dBm}${N}-Mon CP MSS")
    field(PREC, "2")
    field(EGU,  "W")
    field(DISV, "1")
    field(DISS, "INVALID")
    field(SDIS, "${NAME}${N}_enbl")
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
    field(PREC, "${PREC}")
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
record(calc,"${NAME}_raw"){
    field(CALC, "(5.*A/4095.)*(${CTE})")
    field(INPA, "${ioc}:ADC${ADC}:Data-Mon.VAL[${CH}] CP MSS")
    field(DISV, "1")
    field(DISS, "INVALID")
    field(SDIS, "${ioc}:ADC${ADC}:Data-Mon_enbl")
    field(PREC, "${PREC}")
}
# ((ADC${ADC}[$CH] - 0.5) / 0.4)
record(calc, "${NAME}"){
    field(CALC, "((A - 0.5)/0.4)")
    field(INPA, "${NAME}_raw CP MSS")
    field(PREC, "${PREC}")
    field(EGU,  "A")
    field(DISV, "1")
    field(DISS, "INVALID")
    field(SDIS, "${ioc}:ADC${ADC}:Data-Mon_enbl")
}
''')

bi_2 = Template('''
record(calc, "${NAME}_CALC"){
    field(CALC, "(A>1000)?1:0")
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

defaults = {'MIN':'-41.', 'CTE':'1.', 'DESC':'', 'W':'PwrW', 'dBm':'PwrdBm', 'OFS':'OFSdB', 'PREC':'4'}

dbs = [
    {'ioc':'SIA-CalSys',
    'readings' : [
        {'ADC':'0', 'CH':'0', 'N':'1',  'NAME':'RA-RaSIA01:RF-LLRFCalSys', 'template':power, 'p1':'45.68', 'p2':'-51.47', 'p3':'11.04', 'p4':'-3.75', 'p5':'0.2512'},
        {'ADC':'0', 'CH':'1', 'N':'2',  'NAME':'RA-RaSIA01:RF-LLRFCalSys', 'template':power, 'p1':'47.09', 'p2':'-53.66', 'p3':'12.17', 'p4':'-3.742', 'p5':'0.149'},
        {'ADC':'0', 'CH':'2', 'N':'3',  'NAME':'RA-RaSIA01:RF-LLRFCalSys', 'template':power, 'p1':'44.51', 'p2':'-47.16', 'p3':'5.411', 'p4':'-0.5061', 'p5':'-0.4482'},
        {'ADC':'0', 'CH':'3', 'N':'4',  'NAME':'RA-RaSIA01:RF-LLRFCalSys', 'template':power, 'p1':'45.09', 'p2':'-50.15', 'p3':'9.92', 'p4':'-3.278', 'p5':'0.1856'},

        {'ADC':'1', 'CH':'0', 'N':'5',  'NAME':'RA-RaSIA01:RF-LLRFCalSys', 'template':power, 'p1':'46.16', 'p2':'-51.47', 'p3':'10.21', 'p4':'-3.055', 'p5':'0.06204'},
        {'ADC':'1', 'CH':'1', 'N':'6',  'NAME':'RA-RaSIA01:RF-LLRFCalSys', 'template':power, 'p1':'45.19', 'p2':'-49.24', 'p3':'7.966', 'p4':'-1.979', 'p5':'-0.1082'},
        {'ADC':'1', 'CH':'2', 'N':'7',  'NAME':'RA-RaSIA01:RF-LLRFCalSys', 'template':power, 'p1':'47.47', 'p2':'-54.86', 'p3':'14.07', 'p4':'-4.903', 'p5':'0.3741'},
        {'ADC':'1', 'CH':'3', 'N':'8',  'NAME':'RA-RaSIA01:RF-LLRFCalSys', 'template':power, 'p1':'45.49', 'p2':'-50.17', 'p3':'7.643', 'p4':'-1.292', 'p5':'-0.3443'},

        {'ADC':'2', 'CH':'0', 'N':'9',  'NAME':'RA-RaSIA01:RF-LLRFCalSys', 'template':power, 'p1':'45.24', 'p2':'-50.03', 'p3':'9.681', 'p4':'-3.335', 'p5':'0.2122'},
        {'ADC':'2', 'CH':'1', 'N':'10', 'NAME':'RA-RaSIA01:RF-LLRFCalSys', 'template':power, 'p1':'44.04', 'p2':'-44.51', 'p3':'1.543', 'p4':'1.47', 'p5':'-0.7763'},
        {'ADC':'2', 'CH':'2', 'N':'11', 'NAME':'RA-RaSIA01:RF-LLRFCalSys', 'template':power, 'p1':'44.59', 'p2':'-48.98', 'p3':'8.901', 'p4':'-3.015', 'p5':'0.1688'},
        {'ADC':'2', 'CH':'3', 'N':'12', 'NAME':'RA-RaSIA01:RF-LLRFCalSys', 'template':power, 'p1':'45.84', 'p2':'-50.12', 'p3':'8.205', 'p4':'-1.859', 'p5':'-0.213'},

        {'ADC':'3', 'CH':'0', 'N':'13', 'NAME':'RA-RaSIA01:RF-LLRFCalSys', 'template':power, 'p1':'45.6', 'p2':'-49.76', 'p3':'7.374', 'p4':'-1.227', 'p5':'-0.3468'},
        {'ADC':'3', 'CH':'1', 'N':'14', 'NAME':'RA-RaSIA01:RF-LLRFCalSys', 'template':power, 'p1':'46.36', 'p2':'-52.73', 'p3':'11.62', 'p4':'-3.509', 'p5':'0.09841'},
        {'ADC':'3', 'CH':'2', 'N':'15', 'NAME':'RA-RaSIA01:RF-LLRFCalSys', 'template':power, 'p1':'44.82', 'p2':'-47.16', 'p3':'5.384', 'p4':'-0.8597', 'p5':'-0.2635'},
        {'ADC':'3', 'CH':'3', 'N':'16', 'NAME':'RA-RaSIA01:RF-LLRFCalSys', 'template':power, 'p1':'45.6', 'p2':'-51.55', 'p3':'11.61', 'p4':'-4.361', 'p5':'0.4268'},
    ]},
    {'ioc':'SIA-CavPlDrv',
         'readings': [
             {'ADC': '0', 'CH':'0', 'NAME':'RA-RaSIA01:RF-CavPlDrivers:VoltPos5V-Mon', 'template':voltage, 'CTE':'2.'},
             {'ADC':'0', 'CH':'1', 'NAME':'RA-RaSIA01:RF-CavPlDrivers:Current5V-Mon',  'template':current},
             {'ADC':'0', 'CH':'2', 'NAME':'RA-RaSIA01:RF-CavPlDrivers:VoltPos48V-Mon', 'template':voltage, 'CTE':res(90.9,10.)},

             {'ADC':'1', 'CH':'0', 'NAME':'RA-RaSIA01:RF-CavPlDrivers:Dr1Current-Mon', 'template':current},
             {'ADC':'1', 'CH':'1', 'NAME':'RA-RaSIA01:RF-CavPlDrivers:Dr1Enbl-Mon',    'template':bi_2,
                'ZNAM':'Enable','ONAM':'Disable'},
             {'ADC':'1', 'CH':'2', 'NAME':'RA-RaSIA01:RF-CavPlDrivers:Dr1Flt-Mon',     'template':bi,
                'ZNAM':'Fail',  'ONAM':'Normal'},
             {'ADC':'1', 'CH':'3', 'NAME':'SI-02SB:RF-P7Cav:Pl1Pos-Mon',               'template':voltage},

             {'ADC':'2', 'CH':'0', 'NAME':'RA-RaSIA01:RF-CavPlDrivers:Dr2Current-Mon', 'template':current},
             {'ADC':'2', 'CH':'1', 'NAME':'RA-RaSIA01:RF-CavPlDrivers:Dr2Enbl-Mon',    'template':bi_2,
                'ZNAM':'Enable', 'ONAM':'Disable'},
             {'ADC':'2', 'CH':'2', 'NAME':'RA-RaSIA01:RF-CavPlDrivers:Dr2Flt-Mon',     'template':bi,
                'ZNAM':'Fail', 'ONAM':'Normal'},
             {'ADC':'2', 'CH':'3', 'NAME':'SI-02SB:RF-P7Cav:Pl2Pos-Mon',               'template':voltage},
         ]
     },
    {
        'ioc':'LLRFLinPS01',
        'readings': [
            {
                'ADC':'0', 'CH':'0', 'NAME':'RA-RaBO01:RF-LLRFLinPS:VoltPos5V-Mon',  'template':voltage, 'CTE':res(10,20),
                'DESC': 'Tensão de saída da fonte de 5 Volts'
            },
            {
                'ADC':'0', 'CH':'1', 'NAME':'RA-RaBO01:RF-LLRFLinPS:VoltNeg5V-Mon',  'template':voltage, 'CTE':res(-10,20),
                'DESC': 'Tensão de saída da fonte de -5 Volts'
            },
            {
                'ADC':'0', 'CH':'2', 'NAME':'RA-RaSIA01:RF-CavPlDrivers:VoltPos48V-Mon', 'template':voltage, 'CTE':res(20,10),
                'DESC': 'Tensão de saída da fonte de 12 Volts'
            },
            {
                'ADC':'0', 'CH':'3', 'NAME':'RA-RaBO01:RF-LLRFLinPS:VoltPos3V3-Mon', 'template':voltage, 'CTE':'1',
                'DESC': 'Tensão de saída da fonte de 3.3 Volts'
            },

            {
                'ADC':'1', 'CH':'0', 'NAME':'RA-RaBO01:RF-LLRFLinPS:CurrentPos5V-Mon',  'template':current, 'CTE':'1',
                'DESC': 'Corrente de saída da fonte de 5 Volts'
            },
            {
                'ADC':'1', 'CH':'1', 'NAME':'RA-RaBO01:RF-LLRFLinPS:CurrentNeg5V-Mon',  'template':current, 'CTE':'1',
                'DESC': 'Corrente de saída da fonte de -5 Volts'
            },
            {
                'ADC':'1', 'CH':'2', 'NAME':'RA-RaBO01:RF-LLRFLinPS:CurrentPos12V-Mon', 'template':voltage, 'CTE':'1',
                'DESC': 'Corrente de saída da fonte de 12 Volts'
            },
            {
                'ADC':'1', 'CH':'3', 'NAME':'RA-RaBO01:RF-LLRFLinPS:CurrentPos3V3-Mon', 'template':voltage, 'CTE':'1',
                'DESC': 'Corrent de saída da fonte de 3.3 Volts'
            },
        ]
    },
    {
        'ioc':'LLRFLinPS02',
        'readings': [
            {
                'ADC':'0', 'CH':'0', 'NAME':'RA-RaSIA01:RF-LLRFLinPS:VoltPos5V-Mon',  'template':voltage, 'CTE':res(10,20),
                'DESC': 'Tensão de saída da fonte de 5 Volts'
            },
            {
                'ADC':'0', 'CH':'1', 'NAME':'RA-RaSIA01:RF-LLRFLinPS:VoltNeg5V-Mon',  'template':voltage, 'CTE':res(10,20),
                'DESC': 'Tensão de saída da fonte de -5 Volts'
            },
            {
                'ADC':'0', 'CH':'2', 'NAME':'RA-RaSIA01:RF-LLRFLinPS:VoltPos12V-Mon', 'template':voltage, 'CTE':res(20,10),
                'DESC': 'Tensão de saída da fonte de 12 Volts'
            },
            {
                'ADC':'0', 'CH':'3', 'NAME':'RA-RaSIA01:RF-LLRFLinPS:VoltPos3V3-Mon', 'template':voltage, 'CTE':'1',
                'DESC': 'Tensão de saída da fonte de 3.3 Volts'
            },

            {
                'ADC':'1', 'CH':'0', 'NAME':'RA-RaBO01:RF-LLRFLinPS:CurrentPos5V-Mon',  'template':current, 'CTE':'1',
                'DESC': 'Corrente de saída da fonte de 5 Volts'
            },
            {
                'ADC':'1', 'CH':'1', 'NAME':'RA-RaBO01:RF-LLRFLinPS:CurrentNeg5V-Mon',  'template':current, 'CTE':'1',
                'DESC': 'Corrente de saída da fonte de -5 Volts'
            },
            {
                'ADC':'1', 'CH':'2', 'NAME':'RA-RaBO01:RF-LLRFLinPS:CurrentPos12V-Mon', 'template':voltage, 'CTE':'1',
                'DESC': 'Corrente de saída da fonte de 12 Volts'
            },
            {
                'ADC':'1', 'CH':'3', 'NAME':'RA-RaBO01:RF-LLRFLinPS:CurrentPos3V3-Mon', 'template':voltage, 'CTE':'1',
                'DESC': 'Corrente de saída da fonte de 3.3 Volts'
            },
        ]
    },
    {
        'ioc':'LLRFSwPS01',
        'readings': [
            {
                'ADC':'0', 'CH':'0', 'NAME':'RA-RaBO01:RF-LLRFSwPS:VoltPos5V-Mon',  'template':voltage, 'CTE':res(10,20),
                'DESC': 'Tensão de saída da fonte de 5 Volts'
            },
            {
                'ADC':'0', 'CH':'1', 'NAME':'RA-RaBO01:RF-LLRFSwPS:VoltPos24V-Mon',  'template':voltage, 'CTE':res(49.9,10),
                'DESC': 'Tensão de saída da fonte de 24 Volts'
            },
            {
                'ADC':'0', 'CH':'2', 'NAME':'RA-RaBO01:RF-LLRFSwPS:VoltPos3V3-Mon', 'template':voltage, 'CTE':'1',
                'DESC': 'Tensão de saída da fonte de 3.3 Volts'
            },

            {
                'ADC':'1', 'CH':'0', 'NAME':'RA-RaBO01:RF-LLRFSwPS:CurrentPos5V-Mon',  'template':current, 'CTE':'1',
                    'DESC': 'Corrente de saída da fonte de 5 Volts'
            },
            {
                'ADC':'1', 'CH':'1', 'NAME':'RA-RaBO01:RF-LLRFSwPS:CurrentPos24V-Mon',  'template':current, 'CTE':'1',
                    'DESC': 'Corrente de saída da fonte de 24 Volts'
            },
            {
                'ADC':'1', 'CH':'2', 'NAME':'RA-RaBO01:RF-LLRFSwPS:CurrentPos3V3-Mon', 'template':voltage, 'CTE':'1',
                'DESC': 'Corrente de saída da fonte de 3.3 Volts'
            },
        ]
    },
    {
        'ioc': 'LLRFSwPS02',
        'readings': [
            {
                'ADC': '0', 'CH': '0', 'NAME': 'RA-RaSIA01:RF-LLRFSwPS:VoltPos5V-Mon', 'template': voltage,
                'CTE': res(10, 20),
                'DESC': 'Tensão de saída da fonte de 5 Volts'
            },
            {
                'ADC': '0', 'CH': '1', 'NAME': 'RA-RaSIA01:RF-LLRFSwPS:VoltPos24V-Mon', 'template': voltage,
                'CTE': res(49.9, 10),
                'DESC': 'Tensão de saída da fonte de 24 Volts'
            },
            {
                'ADC': '0', 'CH': '2', 'NAME': 'RA-RaSIA01:RF-LLRFSwPS:VoltPos3V3-Mon', 'template': voltage, 'CTE': '1',
                'DESC': 'Tensão de saída da fonte de 3.3 Volts'
            },
            {
                'ADC': '1', 'CH': '0', 'NAME': 'RA-RaSIA01:RF-LLRFSwPS:CurrentPos5V-Mon', 'template': current, 'CTE': '1',
                'DESC': 'Corrente de saída da fonte de 5 Volts'
            },
            {
                'ADC': '1', 'CH': '1', 'NAME': 'RA-RaSIA01:RF-LLRFSwPS:CurrentPos24V-Mon', 'template': current, 'CTE': '1',
                'DESC': 'Corrente de saída da fonte de 24 Volts'
            },
            {
                'ADC': '1', 'CH': '2', 'NAME': 'RA-RaSIA01:RF-LLRFSwPS:CurrentPos3V3-Mon', 'template': voltage, 'CTE': '1',
                'DESC': 'Corrente de saída da fonte de 3.3 Volts'
            },
        ]
    },
    {
        'ioc': 'SSASwPS01',
        'readings': [
            {
                'ADC': '0', 'CH': '0', 'NAME': 'RA-RaBO02:RF-SSASwPS:VoltPos5V-Mon', 'template': voltage,
                'CTE': res(10, 20),
                'DESC': 'Tensão de saída da fonte de 5 Volts'
            },
            {
                'ADC': '0', 'CH': '1', 'NAME': 'RA-RaBO02:RF-SSASwPS:VoltPos12V-Mon', 'template': voltage,
                'CTE': res(20, 10),
                'DESC': 'Tensão de saída da fonte de 24 Volts'
            },
            {
                'ADC': '0', 'CH': '2', 'NAME': 'RA-RaBO02:RF-SSASwPS:VoltNeg12V-Mon', 'template': voltage, 'CTE': res(20, 10),
                'DESC': 'Tensão de saída da fonte de 3.3 Volts'
            },
            {
                'ADC': '0', 'CH': '3', 'NAME': 'RA-RaBO02:RF-SSASwPS:SSAOn-Mon', 'template': voltage, 'CTE': '1',
                'DESC': 'Monitoramento Liga Módulos'
            },
            {
                'ADC': '1', 'CH': '0', 'NAME': 'RA-RaBO02:RF-SSASwPS:CurrentPos5V-Mon', 'template': current, 'CTE': '1',
                'DESC': 'Corrente de saída da fonte de 5 Volts'
            },
            {
                'ADC': '1', 'CH': '1', 'NAME': 'RA-RaBO02:RF-SSASwPS:CurrentPos12V-Mon', 'template': current, 'CTE': '1',
                'DESC': 'Corrente de saída da fonte de 24 Volts'
            },
            {
                'ADC': '1', 'CH': '2', 'NAME': 'RA-RaBO02:RF-SSASwPS:CurrentNeg12V-Mon', 'template': voltage, 'CTE': '1',
                'DESC': 'Corrente de saída da fonte de 3.3 Volts'
            },
        ]
    },
    {
        'ioc': 'SSASwPS02',
        'readings': [
            {
                'ADC': '0', 'CH': '0', 'NAME': 'RA-RaSIA02:RF-SSASwPS:VoltPos5V-Mon', 'template': voltage,
                'CTE': res(10, 20),
                'DESC': 'Tensão de saída da fonte de 5 Volts'
            },
            {
                'ADC': '0', 'CH': '1', 'NAME': 'RA-RaSIA02:RF-SSASwPS:VoltPos12V-Mon', 'template': voltage,
                'CTE': res(20, 10),
                'DESC': 'Tensão de saída da fonte de 24 Volts'
            },
            {
                'ADC': '0', 'CH': '2', 'NAME': 'RA-RaSIA02:RF-SSASwPS:VoltNeg12V-Mon', 'template': voltage, 'CTE': res(20, 10),
                'DESC': 'Tensão de saída da fonte de 3.3 Volts'
            },
            {
                'ADC': '0', 'CH': '3', 'NAME': 'RA-RaSIA02:RF-SSASwPS:SSAOn-Mon', 'template': voltage, 'CTE': '1',
                'DESC': 'Monitoramento Liga Módulos'
            },
            {
                'ADC': '1', 'CH': '0', 'NAME': 'RA-RaSIA02:RF-SSASwPS:CurrentPos5V-Mon', 'template': current, 'CTE': '1',
                'DESC': 'Corrente de saída da fonte de 5 Volts'
            },
            {
                'ADC': '1', 'CH': '1', 'NAME': 'RA-RaSIA02:RF-SSASwPS:CurrentPos12V-Mon', 'template': current, 'CTE': '1',
                'DESC': 'Corrente de saída da fonte de 24 Volts'
            },
            {
                'ADC': '1', 'CH': '2', 'NAME': 'RA-RaSIA02:RF-SSASwPS:CurrentNeg12V-Mon', 'template': voltage, 'CTE': '1',
                'DESC': 'Corrente de saída da fonte de 3.3 Volts'
            },
        ]
    },

]

if __name__ == '__main__':
    for data in dbs:
        db = ''
        with open(data['ioc'] + '.db', 'w+') as f:
            db += adc.safe_substitute(defaults, ioc=data['ioc'])
            for reading in data['readings']:
                db += reading['template'].safe_substitute(defaults, ioc=data['ioc'], **reading)
            f.write(db)

