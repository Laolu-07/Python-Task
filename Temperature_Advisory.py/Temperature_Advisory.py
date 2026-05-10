def temperature_advisory(temp, unit='C', threshold=55):
if unit.upper() == 'C':
   converted_temp = (temp * 9/5) + 32
