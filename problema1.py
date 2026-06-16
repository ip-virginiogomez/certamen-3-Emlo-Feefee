velocidades = []
velmax = 0
promvel = 0

for i in range(5):
    velocidad = int(input("Ingrese una velocidad en Km/h:"))
    velocidades.append(velocidad)
    promvel += velocidad/5
    if velocidad > velmax:
        velmax = velocidad
    
for vel in velocidades:
    if vel < 20:
        print(f"¡PELIGRO! LA {velocidades.index(vel)+1}° VELOCIDAD REGISTRADA ES DEMASIADO BAJA. PUEDE CAUSAR UN ACCIDENTE")
    elif vel > 140:
        print(f"¡PELIGRO! LA {velocidades.index(vel)+1}° VELOCIDAD REGISTRADA ES DEMASIADO ALTA. PUEDE CAUSAR UN ACCIDENTE")
    elif vel < 60 or vel > 120:
        print(f"La {velocidades.index(vel)+1}° velocidad registrada está fuera del rango permitido")

print(f"Promedio de velocidades registradas: {round(promvel, 1)}")
print(f"Velocidad máxima registrada: {velmax}")