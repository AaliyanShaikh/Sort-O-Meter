def quick_sort(arr):
    arr = arr.copy()

    comparisons = [0]
    swaps = [0]

    def partition(low, high):
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            comparisons[0] += 1

            if arr[j] <= pivot:
                i += 1

                if i != j:
                    arr[i], arr[j] = arr[j], arr[i]
                    swaps[0] += 1

        if i + 1 != high:
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            swaps[0] += 1

        return i + 1

    def quicksort(low, high):
        if low < high:
            pivot_index = partition(low, high)

            quicksort(low, pivot_index - 1)
            quicksort(pivot_index + 1, high)

    quicksort(0, len(arr) - 1)

    return arr, comparisons[0], swaps[0]