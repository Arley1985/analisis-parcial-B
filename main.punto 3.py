def criba_eratostenes(max_num):
    es_primo = [True] * (max_num + 1)
    es_primo[0], es_primo[1] = False, False
    for i in range(2, int(max_num**0.5) + 1):
        if es_primo[i]:
            for j in range(i*i, max_num + 1, i):
                es_primo[j] = False
    return es_primo

def contar_primos_en_rangos(pares):
    # Determinar el máximo valor en todos los pares para optimizar la criba
    max_val = max(max(a, b) for a, b in pares)

    # Obtener la lista de primos hasta max_val
    es_primo = criba_eratostenes(max_val)

    # Crear un arreglo de prefijos para contar primos acumulados
    pref = [0] * (max_val + 1)
    for i in range(1, max_val + 1):
        pref[i] = pref[i-1] + (1 if es_primo[i] else 0)

    # Calcular la cantidad de primos en cada rango
    resultados = []
    for a, b in pares:
        # Asegurarse que a <= b
        if a > b:
            a, b = b, a
        count = pref[b] - pref[a-1] if a > 0 else pref[b]
        resultados.append(count)

    return resultados

# Ejemplo de uso
if __name__ == "__main__":
    N = int(input("Ingrese la cantidad de pares: "))
    pares = []
    for _ in range(N):
        a, b = map(int, input().split())
        pares.append((a, b))

    resultados = contar_primos_en_rangos(pares)
    for res in resultados:
        print(res)
