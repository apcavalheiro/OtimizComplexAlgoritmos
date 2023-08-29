import timeit

# Algoritmo A: Bubble Sort
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

# Algoritmo B: Quick Sort
def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivot = lista[len(lista) // 2]
    left = [x for x in lista if x < pivot]
    middle = [x for x in lista if x == pivot]
    right = [x for x in lista if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def measure_execution_time(algorithm, lista):
    start_time = timeit.default_timer()
    algorithm(lista)
    end_time = timeit.default_timer()
    return end_time - start_time

lista = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print(f"Tempo de execução do Bubble Sort: {measure_execution_time(bubble_sort, lista):.5f} segundos")
print(f"Tempo de execução do Quick Sort: {measure_execution_time(quick_sort, lista):.5f} segundos")
