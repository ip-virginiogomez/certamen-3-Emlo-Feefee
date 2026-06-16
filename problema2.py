ventas = [
    [15000, 7000, 7500],
    [20000, 8000, 12000],
    [40000, 2500, 30000]
]
mayorventas = 0

for vendedor in ventas:
    totventas = 0
    for venta in vendedor:
        totventas += venta
    if totventas > mayorventas:
        mayorventas = totventas
        mejorvend = vendedor
    if totventas < 30000:
        print(f"El {ventas.index(vendedor)+1}° vendedor tuvo un bajo desempeño con un total de ${totventas} en ventas.")
    else:
        print(f"El {ventas.index(vendedor)+1}° vendedor sumó un total de ${totventas} en ventas.")
print(f"El vendedor con mejor rendimiento fue el {ventas.index(mejorvend)+1}°, con un total de ${mayorventas} en ventas.")