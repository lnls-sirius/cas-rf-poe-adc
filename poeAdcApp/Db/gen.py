#!/usr/bin/python3
from string import Template
voltage = Template('''
record(calc, "${NAME}"){
    field(CALC, "(${CH}*A/4095.)*((${R_}+${R})/${R_})")
    field(INPA, "$(P)$(R):ADC${ADC}:Data-Mon.VAL[${CH}] CP MSS")
    field(EGU, "V")
    field(DESC, "${DESC}")
}
''')

defaults = { 'R_': 1., 'R':1., 'DESC':''}

readings = [
    {'ADC':'0', 'CH':'0', 'NAME':'$(P)$(R):ADC0:CH1:Voltage-Mon', 'template':voltage},
    {'ADC':'0', 'CH':'1', 'NAME':'$(P)$(R):ADC0:CH2:Voltage-Mon', 'template':voltage},
    {'ADC':'0', 'CH':'2', 'NAME':'$(P)$(R):ADC0:CH3:Voltage-Mon', 'template':voltage},
    {'ADC':'0', 'CH':'3', 'NAME':'$(P)$(R):ADC0:CH4:Voltage-Mon', 'template':voltage},

    {'ADC':'1', 'CH':'0', 'NAME':'$(P)$(R):ADC1:CH1:Voltage-Mon', 'template':voltage},
    {'ADC':'1', 'CH':'1', 'NAME':'$(P)$(R):ADC1:CH2:Voltage-Mon', 'template':voltage},
    {'ADC':'1', 'CH':'2', 'NAME':'$(P)$(R):ADC1:CH3:Voltage-Mon', 'template':voltage},
    {'ADC':'1', 'CH':'3', 'NAME':'$(P)$(R):ADC1:CH4:Voltage-Mon', 'template':voltage},

    {'ADC':'2', 'CH':'0', 'NAME':'$(P)$(R):ADC2:CH1:Voltage-Mon', 'template':voltage},
    {'ADC':'2', 'CH':'1', 'NAME':'$(P)$(R):ADC2:CH2:Voltage-Mon', 'template':voltage},
    {'ADC':'2', 'CH':'2', 'NAME':'$(P)$(R):ADC2:CH3:Voltage-Mon', 'template':voltage},
    {'ADC':'2', 'CH':'3', 'NAME':'$(P)$(R):ADC2:CH4:Voltage-Mon', 'template':voltage},

    {'ADC':'3', 'CH':'0', 'NAME':'$(P)$(R):ADC3:CH1:Voltage-Mon', 'template':voltage},
    {'ADC':'3', 'CH':'1', 'NAME':'$(P)$(R):ADC3:CH2:Voltage-Mon', 'template':voltage},
    {'ADC':'3', 'CH':'2', 'NAME':'$(P)$(R):ADC3:CH3:Voltage-Mon', 'template':voltage},
    {'ADC':'3', 'CH':'3', 'NAME':'$(P)$(R):ADC3:CH4:Voltage-Mon', 'template':voltage},
]

if __name__ == '__main__':
    db = ''
    with open('Conv.db', 'w+') as f:
        for reading in readings:
            db += reading['template'].safe_substitute(defaults, **reading)
        f.write(db)

