#Adrián Alejandro Hernández Díaz 3SA Estrctura de Datos ADA2

#Memoria ESTÁTICA.
calificaciones = [0] * 5  

for i in range(5):
    calificaciones[i] = int(input(f"Captura la calificación {i+1}: "))

print("Las calificaciones son:", calificaciones)

#Memoria DINÁMICA.

frutas = []

frutas.append("Mango")
frutas.append("Manzana")
frutas.append("Banana")

print("Frutas iniciales:", frutas)

frutas.pop(0)  # elimina "Mango"
frutas.pop(1)  # ahora elimina "Banana" porque los índices se recorrieron

frutas.append("Sandía")

print("Frutas finales:", frutas)

