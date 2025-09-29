import tkinter as tk
from tkinter import simpledialog, messagebox

# Inicializamos la pila
pila = ["a", "b", "c"]

# Función para actualizar el gráfico
def actualizar_pila():
    canvas.delete("all")
    x0, y0, x1, y1 = 50, 250, 150, 300
    for elemento in reversed(pila):  # Mostrar de abajo hacia arriba
        canvas.create_rectangle(x0, y0, x1, y1, fill="lightblue", outline="black")
        canvas.create_text((x0 + x1) // 2, (y0 + y1) // 2, text=elemento, font=("Arial", 14))
        y0 -= 50
        y1 -= 50

# Apilar
def apilar():
    nuevo = simpledialog.askstring("Apilar", "Ingresa un valor:")
    if nuevo:
        pila.append(nuevo)
        actualizar_pila()

# Desapilar
def desapilar():
    if pila:
        elemento = pila.pop()
        messagebox.showinfo("Desapilado", f"Se sacó: {elemento}")
        actualizar_pila()
    else:
        messagebox.showwarning("Error", "La pila está vacía")

# Ventana principal
ventana = tk.Tk()
ventana.title("Simulación de Pila con Tkinter")

canvas = tk.Canvas(ventana, width=200, height=300, bg="white")
canvas.pack(pady=20)

frame = tk.Frame(ventana)
frame.pack()

btn_apilar = tk.Button(frame, text="Apilar", command=apilar, width=10)
btn_apilar.grid(row=0, column=0, padx=5)

btn_desapilar = tk.Button(frame, text="Desapilar", command=desapilar, width=10)
btn_desapilar.grid(row=0, column=1, padx=5)

# Dibujar pila inicial
actualizar_pila()

ventana.mainloop()
