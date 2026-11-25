
def lcs_recursiva(a, b, i, j):

    # Si alguna cadena esta vacia, no hay coincidencias
    if i == 0 or j == 0:
        return ""

    # Si los caracteres coinciden, guardamos el caracter
    if a[i - 1] == b[j - 1]:
        return lcs_recursiva(a, b, i - 1, j - 1) + a[i - 1]

    # Si no coinciden, probamos las dos posibilidades
    resultado1 = lcs_recursiva(a, b, i - 1, j)
    resultado2 = lcs_recursiva(a, b, i, j - 1)

    # Nos quedamos con el resultado mas largo
    if len(resultado1) >= len(resultado2):
        return resultado1
    else:
        return resultado2


# Prueba del algoritmo
if __name__ == "__main__":

    cadena1 = "ABCDE"
    cadena2 = "ACE"

    resultado = lcs_recursiva(cadena1, cadena2, len(cadena1), len(cadena2))

    print("Subsecuencia:", resultado)
    print("Longitud:", len(resultado))
