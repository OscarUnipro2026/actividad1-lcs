
def lcs_dinamica(a, b):

    m = len(a)
    n = len(b)

    # Creamos una tabla llena de ceros
    tabla = [[0] * (n + 1) for i in range(m + 1)]

    # Rellenamos la tabla
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if a[i - 1] == b[j - 1]:
                tabla[i][j] = tabla[i - 1][j - 1] + 1
            else:
                tabla[i][j] = max(tabla[i - 1][j], tabla[i][j - 1])

    # Recuperamos la subsecuencia
    resultado = ""
    i = m
    j = n

    while i > 0 and j > 0:

        if a[i - 1] == b[j - 1]:
            resultado = a[i - 1] + resultado
            i -= 1
            j -= 1

        elif tabla[i - 1][j] >= tabla[i][j - 1]:
            i -= 1

        else:
            j -= 1

    return resultado


# Prueba del algoritmo
if __name__ == "__main__":

    cadena1 = "ABCDE"
    cadena2 = "ACE"

    resultado = lcs_dinamica(cadena1, cadena2)

    print("Subsecuencia:", resultado)
    print("Longitud:", len(resultado))
