import numpy as np
import time

def crear_datos(num_alumnos, num_materias):
    """
    Crea una matriz de alumnos y materias con valores aleatorios.
    """
    return np.random.randint(0, 101, size=(num_alumnos, num_materias))  # calificaciones de 0 a 100


def prueba_busqueda(matriz, alumno, materia, forma=1):
    """
    Realiza una búsqueda dependiendo de la forma de la matriz:
    - forma 1: materias como filas, alumnos como columnas
    - forma 2: alumnos como filas, materias como columnas
    """
    if forma == 1:
        return matriz[materia, alumno]
    else:
        return matriz[alumno, materia]


def medir_tiempo(num_alumnos, num_materias, alumno, materia):
    """
    Mide el tiempo de acceso en ambas formas.
    """
    # Forma 1: materias como filas, alumnos como columnas
    matriz1 = np.random.randint(0, 101, size=(num_materias, num_alumnos))
    
    inicio1 = time.time()
    valor1 = prueba_busqueda(matriz1, alumno, materia, forma=1)
    fin1 = time.time()
    
    tiempo1 = (fin1 - inicio1) * 1000  # en milisegundos
    
    # Forma 2: alumnos como filas, materias como columnas
    matriz2 = np.random.randint(0, 101, size=(num_alumnos, num_materias))
    
    inicio2 = time.time()
    valor2 = prueba_busqueda(matriz2, alumno, materia, forma=2)
    fin2 = time.time()
    
    tiempo2 = (fin2 - inicio2) * 1000  # en milisegundos
    
    return tiempo1, tiempo2, valor1, valor2


if __name__ == "__main__":
    # Ejemplo inicial con 500 alumnos y 6 materias
    alumnos, materias = 500, 6
    alumno_objetivo, materia_objetivo = 320, 4  # en Python el índice inicia en 0
    
    t1, t2, v1, v2 = medir_tiempo(alumnos, materias, alumno_objetivo, materia_objetivo)
    
    print(f"Ejemplo con {alumnos} alumnos y {materias} materias:")
    print(f" Forma 1 (materias como filas): valor={v1}, tiempo={t1:.6f} ms")
    print(f" Forma 2 (alumnos como filas): valor={v2}, tiempo={t2:.6f} ms")
    
    # Pruebas con diferentes tamaños
    escenarios = [
        (1000, 100),
        (10000, 500),
        (100000, 10000),
    ]
    
    for alumnos, materias in escenarios:
        alumno_objetivo = np.random.randint(0, alumnos)
        materia_objetivo = np.random.randint(0, materias)
        
        t1, t2, _, _ = medir_tiempo(alumnos, materias, alumno_objetivo, materia_objetivo)
        print(f"\nEscenario con {alumnos} alumnos y {materias} materias:")
        print(f" Forma 1 -> {t1:.6f} ms")
        print(f" Forma 2 -> {t2:.6f} ms")
