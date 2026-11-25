
import random
import time
import tracemalloc
import multiprocessing
import sys

from lcs_recursiva import lcs_recursiva
from lcs_hirschberg import lcs_hirschberg
from lcs_dinamica import lcs_dinamica


# Ejecutamos el algoritmo seleccionado
def ejecutar(version, a, b):
    if version == "A":
        return lcs_recursiva(a, b, len(a), len(b))

    if version == "B":
        return lcs_hirschberg(a, b)

    return lcs_dinamica(a, b)


# Medimos el tiempo de CPU y la memoria
def medir(version, a, b):
    sys.setrecursionlimit(3000)

    inicio = time.process_time()
    resultado = ejecutar(version, a, b)
    tiempo = time.process_time() - inicio

    tracemalloc.start()
    ejecutar(version, a, b)
    memoria = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()

    return resultado, tiempo, memoria / 1024


# Comprobamos que el resultado es una subsecuencia
def es_subsecuencia(resultado, cadena):
    posicion = 0

    for letra in cadena:
        if posicion < len(resultado) and letra == resultado[posicion]:
            posicion += 1

    return posicion == len(resultado)


def main():
    random.seed(42)
    tamanos = [5, 10, 15, 100, 500, 1000]

    print("Tamano | Version | LCS | CPU (s) | Memoria (KiB)", flush=True)

    for n in tamanos:

        # Generamos las dos cadenas
        a = "".join(random.choices("ABCD", k=n))
        b = "".join(random.choices("ABCD", k=n))

        longitudes = []

        for version in ["A", "B", "C"]:

            try:
                with multiprocessing.Pool(1) as proceso:
                    tarea = proceso.apply_async(medir, (version, a, b))
                    limite = 5 if version == "A" else 60
                    resultado, tiempo, memoria = tarea.get(timeout=limite)

            except multiprocessing.TimeoutError:
                print(f"{n} | {version} | - | - | - (limite {limite} s)", flush=True)
                continue

            # Comprobamos el resultado
            assert es_subsecuencia(resultado, a)
            assert es_subsecuencia(resultado, b)
            longitudes.append(len(resultado))

            print(f"{n} | {version} | {len(resultado)} | {tiempo:.6f} | {memoria:.2f}", flush=True)

        # Comprobamos que las longitudes coinciden
        assert len(set(longitudes)) == 1


if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()
