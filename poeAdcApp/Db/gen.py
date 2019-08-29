#!/usr/bin/python3
from string import Template
voltage = Template('''
record(calc, "${NAME}"){
    field(CALC, "(${CH}*A/4095.)*(${CTE})")
    field(INPA, "$(P)$(R):ADC${ADC}:Data-Mon.VAL[${CH}] CP MSS")
    field(EGU, "V")
    field(DESC, "${DESC}")
}
''')

#Descrição Lógica Nome EP
#Monitoramento da Tensão de Saída do Detector de Potência 1RA-RaSIA01:LLRFCalSys:PwrdBm1-Mon
#Monitoramento da Tensão de Saída do Detector de Potência 2RA-RaSIA01:LLRFCalSys:PwrdBm2-Mon
#Monitoramento da Tensão de Saída do Detector de Potência 3RA-RaSIA01:LLRFCalSys:PwrdBm3-Mon
#Monitoramento da Tensão de Saída do Detector de Potência 4RA-RaSIA01:LLRFCalSys:PwrdBm4-Mon
        
#Descrição Lógica Nome EP
#Monitoramento da Tensão de Saída do Detector de Potência 5RA-RaSIA01:LLRFCalSys:PwrdBm5-Mon
#Monitoramento da Tensão de Saída do Detector de Potência  RA-RaSIA01:LLRFCalSys:PwrdBm6-Mon
#Monitoramento da Tensão de Saída do Detector de Potência  RA-RaSIA01:LLRFCalSys:PwrdBm7-Mon
#Monitoramento da Tensão de Saída do Detector de Potência  RA-RaSIA01:LLRFCalSys:PwrdBm8-Mon
                                
#Descrição Lógica Nome EP
#Monitoramento da Tensão de Saída do Detector de Potência 9RA-RaSIA01:LLRFCalSys:PwrdBm9-Mon
#Monitoramento da Tensão de Saída do Detector de Potência 1RA-RaSIA01:LLRFCalSys:PwrdBm10-Mon
#Monitoramento da Tensão de Saída do Detector de Potência 1RA-RaSIA01:LLRFCalSys:PwrdBm11-Mon
#Monitoramento da Tensão de Saída do Detector de Potência 1RA-RaSIA01:LLRFCalSys:PwrdBm12-Mon
                                                                        
#Descrição Lógica Nome ES
#Monitoramento da Tensão de Saída do Detector de Potência 1RA-RaSIA01:LLRFCalSys:PwrdBm13-Mon
#Monitoramento da Tensão de Saída do Detector de Potência 1RA-RaSIA01:LLRFCalSys:PwrdBm14-Mon
#Monitoramento da Tensão de Saída do Detector de Potência 1RA-RaSIA01:LLRFCalSys:PwrdBm15-Mon
#Monitoramento da Tensão de Saída do Detector de Potência 1RA-RaSIA01:LLRFCalSys:PwrdBm16-Mon

def res(R, R_):
    return str(((R_+R)/R_))

defaults = {'CTE':'1', 'DESC':''}

dbs = [
    {'ioc':'ioc1.db',
    'readings' : [
        {'ADC':'0', 'CH':'0', 'NAME':'RA-RaSIA01:LLRFCalSys:PwrdBm1-Mon', 'template':voltage},
        {'ADC':'0', 'CH':'1', 'NAME':'RA-RaSIA01:LLRFCalSys:PwrdBm2-Mon', 'template':voltage},
        {'ADC':'0', 'CH':'2', 'NAME':'RA-RaSIA01:LLRFCalSys:PwrdBm3-Mon', 'template':voltage},
        {'ADC':'0', 'CH':'3', 'NAME':'RA-RaSIA01:LLRFCalSys:PwrdBm4-Mon', 'template':voltage},

        {'ADC':'1', 'CH':'0', 'NAME':'RA-RaSIA01:LLRFCalSys:PwrdBm5-Mon', 'template':voltage},
        {'ADC':'1', 'CH':'1', 'NAME':'RA-RaSIA01:LLRFCalSys:PwrdBm6-Mon', 'template':voltage},
        {'ADC':'1', 'CH':'2', 'NAME':'RA-RaSIA01:LLRFCalSys:PwrdBm7-Mon', 'template':voltage},
        {'ADC':'1', 'CH':'3', 'NAME':'RA-RaSIA01:LLRFCalSys:PwrdBm8-Mon', 'template':voltage},

        {'ADC':'2', 'CH':'0', 'NAME':'RA-RaSIA01:LLRFCalSys:PwrdBm9-Mon ', 'template':voltage},
        {'ADC':'2', 'CH':'1', 'NAME':'RA-RaSIA01:LLRFCalSys:PwrdBm10-Mon', 'template':voltage},
        {'ADC':'2', 'CH':'2', 'NAME':'RA-RaSIA01:LLRFCalSys:PwrdBm11-Mon', 'template':voltage},
        {'ADC':'2', 'CH':'3', 'NAME':'RA-RaSIA01:LLRFCalSys:PwrdBm12-Mon', 'template':voltage},

        {'ADC':'3', 'CH':'0', 'NAME':'RA-RaSIA01:LLRFCalSys:PwrdBm13-Mon', 'template':voltage},
        {'ADC':'3', 'CH':'1', 'NAME':'RA-RaSIA01:LLRFCalSys:PwrdBm14-Mon', 'template':voltage},
        {'ADC':'3', 'CH':'2', 'NAME':'RA-RaSIA01:LLRFCalSys:PwrdBm15-Mon', 'template':voltage},
        {'ADC':'3', 'CH':'3', 'NAME':'RA-RaSIA01:LLRFCalSys:PwrdBm16-Mon', 'template':voltage},
    ]},
    {'ioc':'ioc2.db',
    'readings' : [
        {'ADC':'0', 'CH':'0', 'NAME':'$(P)$(R):ADC1:CH1:Voltage-Mon', 'template':voltage},
        {'ADC':'0', 'CH':'1', 'NAME':'RA-RaSIA01:LLRFCalSys:PwrdBm2-Mon', 'template':voltage},
        {'ADC':'0', 'CH':'2', 'NAME':'RA-RaSIA01:LLRFCalSys:PwrdBm3-Mon', 'template':voltage},
        {'ADC':'0', 'CH':'3', 'NAME':'RA-RaSIA01:LLRFCalSys:PwrdBm4-Mon', 'template':voltage},

        {'ADC':'1', 'CH':'0', 'NAME':'RA-RaSIA01:LLRFCalSys:PwrdBm5-Mon', 'template':voltage},
        {'ADC':'1', 'CH':'1', 'NAME':'RA-RaSIA01:LLRFCalSys:PwrdBm6-Mon', 'template':voltage},
        {'ADC':'1', 'CH':'2', 'NAME':'RA-RaSIA01:LLRFCalSys:PwrdBm7-Mon', 'template':voltage},
        {'ADC':'1', 'CH':'3', 'NAME':'RA-RaSIA01:LLRFCalSys:PwrdBm8-Mon', 'template':voltage},

        {'ADC':'2', 'CH':'0', 'NAME':'RA-RaSIA01:LLRFCalSys:PwrdBm9-Mon ', 'template':voltage},
        {'ADC':'2', 'CH':'1', 'NAME':'RA-RaSIA01:LLRFCalSys:PwrdBm10-Mon', 'template':voltage},
        {'ADC':'2', 'CH':'2', 'NAME':'RA-RaSIA01:LLRFCalSys:PwrdBm11-Mon', 'template':voltage},
        {'ADC':'2', 'CH':'3', 'NAME':'RA-RaSIA01:LLRFCalSys:PwrdBm12-Mon', 'template':voltage},

        {'ADC':'3', 'CH':'0', 'NAME':'RA-RaSIA01:LLRFCalSys:PwrdBm13-Mon', 'template':voltage},
        {'ADC':'3', 'CH':'1', 'NAME':'RA-RaSIA01:LLRFCalSys:PwrdBm14-Mon', 'template':voltage},
        {'ADC':'3', 'CH':'2', 'NAME':'RA-RaSIA01:LLRFCalSys:PwrdBm15-Mon', 'template':voltage},
        {'ADC':'3', 'CH':'3', 'NAME':'RA-RaSIA01:LLRFCalSys:PwrdBm16-Mon', 'template':voltage},
    ]},
]

if __name__ == '__main__':
    for data in dbs:
        db = ''
        with open(data['ioc'], 'w+') as f:
            for reading in data['readings']:
                db += reading['template'].safe_substitute(defaults, **reading)
            f.write(db)

