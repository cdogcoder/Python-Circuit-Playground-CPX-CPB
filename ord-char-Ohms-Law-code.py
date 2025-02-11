ohms_symbol = chr(ord("Ω"))
voltage = 5
current_in_milliamps = 20

print("?" + ohms_symbol, "=", str(voltage) + "V", "/", str(current_in_milliamps) + "mA")

current_in_amps = current_in_milliamps/1000
answer = voltage/current_in_amps

print(str(answer) + ohms_symbol, "=", str(voltage) + "V", "/", str(current_in_amps) + "A")

