
# Calculamos las longitudes utilizando dos filas
def calcular_fila(a, b):
    anterior = [0] * (len(b) + 1)

    for letra in a:
        actual = [0] * (len(b) + 1)

        for j in range(1, len(b) + 1):
            if letra == b[j - 1]:
                actual[j] = anterior[j - 1] + 1
            else:
                actual[j] = max(anterior[j], actual[j - 1])

        anterior = actual

    return anterior


def lcs_hirschberg(a, b):

    # Casos base
    if len(a) == 0 or len(b) == 0:
        return ""

    if len(a) == 1:
        if a in b:
            return a
        else:
            return ""

    # Dividimos la primera cadena por la mitad
    mitad = len(a) // 2

    # Calculamos las longitudes en ambos sentidos
    izquierda = calcular_fila(a[:mitad], b)
    derecha = calcular_fila(a[mitad:][::-1], b[::-1])

    # Buscamos el mejor punto de corte
    corte = 0
    mejor = -1

    for j in range(len(b) + 1):
        suma = izquierda[j] + derecha[len(b) - j]

        if suma > mejor:
            mejor = suma
            corte = j

    # Liberamos las filas antes de continuar
    del izquierda
    del derecha

    # Resolvemos cada parte y unimos los resultados
    return lcs_hirschberg(a[:mitad], b[:corte]) + lcs_hirschberg(a[mitad:], b[corte:])


# Prueba del algoritmo
if __name__ == "__main__":

    cadena1 = "ABCDE"
    cadena2 = "ACE"

    resultado = lcs_hirschberg(cadena1, cadena2)

    print("Subsecuencia:", resultado)
    print("Longitud:", len(resultado))
