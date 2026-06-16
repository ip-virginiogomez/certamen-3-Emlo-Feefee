edad = int(input("Ingrese su edad:"))

membresia = " "

while not(membresia == "S" or membresia == "N"):
    membresia = input("¿Cuenta con tarjeta de socio? (S/N)")
    if not(membresia == "S" or membresia == "N"):
        print("Valor incorrecto. Responda correctamente, por favor.")
        
monto = int(input("Ingrese el monto de su compra en pesos:"))

if (monto > 10000) and ((edad == 60) or (membresia == "S")):
    monto = monto * 0.85
    print(f"Usted cuenta con el descuento. Su monto a pagar es de ${monto}.")
else:
    print(f"Usted no cuenta con descuento. Su monto a pagar es de ${monto}")