def bubble_sort(arr):
    arr = arr.copy()
    comparisons = 0
    swaps = 0

    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            comparisons += 1

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True

        if not swapped:
            break

    return arr, comparisons, swaps