# cas-rf-poe-adc

## Beagle SPI PINs

**SPI(0,0)**

| ADC | GPIO |
|-----|------|
| ADC0 | "P9_24" |
| ADC1 | "P9_26" |
| ADC2 | "P9_28" |
| ADC3 | "P9_30" |

```bash

config-pin P9_24 output
config-pin P9_26 output
config-pin P9_28 output
config-pin P9_30 output

config-pin P9.17 spi_cs
config-pin P9.18 spi
config-pin P9.21 spi
config-pin P9.22 spi_sclk
```

