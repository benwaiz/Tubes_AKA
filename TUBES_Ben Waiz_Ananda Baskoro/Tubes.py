# Judul: Pencarian Linear dan Pengurutan Menggunakan Bubble Sort

import time
import matplotlib.pyplot as plt
import random
import pandas as pd
from tabulate import tabulate

# Pencarian Linear - Versi Iteratif
def linear_search_iterative(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

# Pencarian Linear - Versi Rekursif
def linear_search_recursive(arr, target, index=0):
    if index >= len(arr):
        return -1
    if arr[index] == target:
        return index
    return linear_search_recursive(arr, target, index + 1)

# Pengurutan Bubble - Versi Iteratif
def bubble_sort_iterative(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Pengurutan Bubble - Versi Rekursif
def bubble_sort_recursive(arr, n=None):
    if n is None:
        n = len(arr)
    if n == 1:
        return
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    bubble_sort_recursive(arr, n - 1)

# Analisis dan Visualisasi
input_sizes = [1, 10, 20, 50, 100, 200, 500, 1000]
performance_data_linear = []
performance_data_bubble = []

for size in input_sizes:
    arr = random.sample(range(size * 2), size)
    target = random.choice(arr)

    # Pencarian Linear Iteratif
    start_time = time.time()
    linear_search_iterative(arr, target)
    iterative_time = (time.time() - start_time)

    # Pencarian Linear Rekursif
    start_time = time.time()
    linear_search_recursive(arr, target)
    recursive_time = (time.time() - start_time)

    # Pengurutan Bubble Iteratif
    arr_copy = arr[:]
    start_time = time.time()
    bubble_sort_iterative(arr_copy)
    bubble_iterative_time = (time.time() - start_time)

    # Pengurutan Bubble Rekursif
    arr_copy = arr[:]
    start_time = time.time()
    bubble_sort_recursive(arr_copy, len(arr_copy))
    bubble_recursive_time = (time.time() - start_time)

    # Simpan data untuk tabel linear search
    performance_data_linear.append([size, round(recursive_time, 6), round(iterative_time, 6)])

    # Simpan data untuk tabel bubble sort
    performance_data_bubble.append([size, round(bubble_recursive_time, 6), round(bubble_iterative_time, 6)])

# Plotting hasil waktu eksekusi untuk Linear Search
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, [row[1] for row in performance_data_linear], label="Linear Recursive", marker="o")
plt.plot(input_sizes, [row[2] for row in performance_data_linear], label="Linear Iterative", marker="o")
plt.xlabel("Ukuran Masukan")
plt.ylabel("Waktu Eksekusi (s)")
plt.title("Perbandingan Waktu Eksekusi Pencarian Linear")
plt.legend()
plt.grid()
plt.show()

# Tabel untuk Linear Search
headers_linear = ["n", "Recursive Time (s)", "Iterative Time (s)"]
print("\nTabel Perbandingan Kinerja Linear Search:\n")
print(tabulate(performance_data_linear, headers=headers_linear, tablefmt="grid", floatfmt=".6f"))

# Plotting hasil waktu eksekusi untuk Bubble Sort
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, [row[1] for row in performance_data_bubble], label="Bubble Recursive", marker="o")
plt.plot(input_sizes, [row[2] for row in performance_data_bubble], label="Bubble Iterative", marker="o")
plt.xlabel("Ukuran Masukan")
plt.ylabel("Waktu Eksekusi (s)")
plt.title("Perbandingan Waktu Eksekusi Pengurutan Bubble")
plt.legend()
plt.grid()
plt.show()

# Tabel untuk Bubble Sort
headers_bubble = ["n", "Recursive Time (s)", "Iterative Time (s)"]
print("\nTabel Perbandingan Kinerja Bubble Sort:\n")
print(tabulate(performance_data_bubble, headers=headers_bubble, tablefmt="grid", floatfmt=".6f"))
