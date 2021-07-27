from string import Template

adc = Template(
    """
record(stringin, "${ioc}:SaveName"){
    field(VAL,  "${ioc}.sav")
    field(PINI, "YES")
    field(DESC, "Autosave destination file")
}

record(waveform, "${ioc}:ADC0:Data-Mon"){
    field(PINI, "YES")
    field(DESC, "ADC0 Data")
    field(SCAN, "$$(S=1) second")
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
    field(SCAN, "$$(S=1) second")
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
    field(SCAN, "$$(S=1) second")
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
    field(SCAN, "$$(S=1) second")
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
"""
)

power = Template(
    """
record(ao, "${NAME}:${OFS}${N}-Mon"){
    field(PREC, "2")
    field(EGU,  "dB")
    field(VAL,  "0")
    field(PINI, "YES")
}
record(calc, "${NAME}${N}_ADC"){
    field(CALC, "(5.*A/4095.)*(${CTE})")
    field(INPA, "${ioc}:ADC${ADC}:Data-Mon.VAL[${CH}] CP MSS")
    field(EGU,  "V")
    field(PREC, "2")
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
    field(PREC, "2")
    field(EGU,  "dBm")
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
"""
)

voltage = Template(
    """
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
"""
)

raw = Template(
    """
record(ai, "${NAME}"){
    field(INP,  "${ioc}:ADC${ADC}:Data-Mon.VAL[${CH}] CP MSS")
    field(PREC, "3")
    field(DISV, "1")
    field(DISS, "INVALID")
    field(SDIS, "${ioc}:ADC${ADC}:Data-Mon_enbl")
}

"""
)

current = Template(
    """
record(calc,"${NAME}_raw"){
    field(CALC, "(5.*A/4095.)*(${CTE})")
    field(INPA, "${ioc}:ADC${ADC}:Data-Mon.VAL[${CH}] CP MSS")
    field(DISV, "1")
    field(DISS, "INVALID")
    field(SDIS, "${ioc}:ADC${ADC}:Data-Mon_enbl")
}
# ((ADC${ADC}[$CH] - 0.5) / 0.4)
record(calc, "${NAME}"){
    field(CALC, "((A - 0.5)/0.4)")
    field(INPA, "${NAME}_raw CP MSS")
    field(PREC, "3")
    field(EGU,  "A")
    field(DISV, "1")
    field(DISS, "INVALID")
    field(SDIS, "${ioc}:ADC${ADC}:Data-Mon_enbl")
}
"""
)

bi_2 = Template(
    """
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
"""
)
bi = Template(
    """
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
"""
)
