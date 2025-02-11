ohms_symbol = chr(ord("Ω"))
voltage = float(input("Enter a voltage value: ")
current_in_milliamps = float(input("Enter a current value (in milliamps): ")

print("?" + ohms_symbol, "=", str(voltage) + "V", "/", str(current_in_milliamps) + "mA")

current_in_amps = current_in_milliamps/1000
answer = voltage/current_in_amps

print(str(answer) + ohms_symbol, "=", str(voltage) + "V", "/", str(current_in_amps) + "A")
print("A circuit with a voltage of", str(voltage)+"V", "and a current of", str(current_in_milliamps)+"mA", "will require a resistor of", str(answer)+ohms_symbol)
