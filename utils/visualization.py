import time


# ============================================================
# BUBBLE SORT VISUALIZATION
# ============================================================

def bubble_sort_steps(arr):
    arr = arr.copy()
    steps = []

    steps.append({
        "array": arr.copy(),
        "message": "Starting Bubble Sort"
    })

    n = len(arr)

    for i in range(n):

        swapped = False

        for j in range(0, n - i - 1):

            steps.append({
                "array": arr.copy(),
                "message": (
                    f"Comparing {arr[j]} and {arr[j + 1]}"
                )
            })

            if arr[j] > arr[j + 1]:

                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                swapped = True

                steps.append({
                    "array": arr.copy(),
                    "message": (
                        f"Swapped {arr[j + 1]} and {arr[j]}"
                    )
                })

        if not swapped:
            break

    steps.append({
        "array": arr.copy(),
        "message": "Bubble Sort completed!"
    })

    return steps


# ============================================================
# SELECTION SORT VISUALIZATION
# ============================================================

def selection_sort_steps(arr):

    arr = arr.copy()
    steps = []

    steps.append({
        "array": arr.copy(),
        "message": "Starting Selection Sort"
    })

    n = len(arr)

    for i in range(n):

        min_index = i

        steps.append({
            "array": arr.copy(),
            "message": (
                f"Finding minimum from position {i}"
            )
        })

        for j in range(i + 1, n):

            steps.append({
                "array": arr.copy(),
                "message": (
                    f"Comparing {arr[j]} with "
                    f"current minimum {arr[min_index]}"
                )
            })

            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:

            arr[i], arr[min_index] = (
                arr[min_index],
                arr[i]
            )

            steps.append({
                "array": arr.copy(),
                "message": (
                    f"Placed {arr[i]} at position {i}"
                )
            })

    steps.append({
        "array": arr.copy(),
        "message": "Selection Sort completed!"
    })

    return steps


# ============================================================
# INSERTION SORT VISUALIZATION
# ============================================================

def insertion_sort_steps(arr):

    arr = arr.copy()
    steps = []

    steps.append({
        "array": arr.copy(),
        "message": "Starting Insertion Sort"
    })

    for i in range(1, len(arr)):

        key = arr[i]
        j = i - 1

        steps.append({
            "array": arr.copy(),
            "message": (
                f"Taking {key} as the current key"
            )
        })

        while j >= 0 and arr[j] > key:

            steps.append({
                "array": arr.copy(),
                "message": (
                    f"Moving {arr[j]} one position right"
                )
            })

            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

        steps.append({
            "array": arr.copy(),
            "message": (
                f"Inserted {key} into its correct position"
            )
        })

    steps.append({
        "array": arr.copy(),
        "message": "Insertion Sort completed!"
    })

    return steps


# ============================================================
# MERGE SORT VISUALIZATION
# ============================================================

def merge_sort_steps(arr):

    arr = arr.copy()
    steps = []

    steps.append({
        "array": arr.copy(),
        "message": "Starting Merge Sort"
    })

    def merge(left, right):

        result = []

        i = 0
        j = 0

        while i < len(left) and j < len(right):

            if left[i] <= right[j]:

                result.append(left[i])
                i += 1

            else:

                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result

    def divide(array):

        if len(array) <= 1:
            return array

        mid = len(array) // 2

        left = array[:mid]
        right = array[mid:]

        steps.append({
            "array": array.copy(),
            "message": (
                f"Dividing into {left} and {right}"
            )
        })

        left = divide(left)
        right = divide(right)

        merged = merge(left, right)

        steps.append({
            "array": merged.copy(),
            "message": (
                f"Merging {left} and {right}"
            )
        })

        return merged

    sorted_array = divide(arr)

    steps.append({
        "array": sorted_array.copy(),
        "message": "Merge Sort completed!"
    })

    return steps


# ============================================================
# QUICK SORT VISUALIZATION
# ============================================================

def quick_sort_steps(arr):

    arr = arr.copy()
    steps = []

    steps.append({
        "array": arr.copy(),
        "message": "Starting Quick Sort"
    })

    def partition(low, high):

        pivot = arr[high]

        steps.append({
            "array": arr.copy(),
            "message": f"Pivot selected: {pivot}"
        })

        i = low - 1

        for j in range(low, high):

            steps.append({
                "array": arr.copy(),
                "message": (
                    f"Comparing {arr[j]} with pivot {pivot}"
                )
            })

            if arr[j] <= pivot:

                i += 1

                if i != j:

                    arr[i], arr[j] = (
                        arr[j],
                        arr[i]
                    )

                    steps.append({
                        "array": arr.copy(),
                        "message": (
                            f"Swapped {arr[i]} and {arr[j]}"
                        )
                    })

        if i + 1 != high:

            arr[i + 1], arr[high] = (
                arr[high],
                arr[i + 1]
            )

            steps.append({
                "array": arr.copy(),
                "message": (
                    f"Placed pivot {pivot} "
                    f"at position {i + 1}"
                )
            })

        return i + 1

    def quicksort(low, high):

        if low < high:

            pivot_index = partition(
                low,
                high
            )

            quicksort(
                low,
                pivot_index - 1
            )

            quicksort(
                pivot_index + 1,
                high
            )

    quicksort(
        0,
        len(arr) - 1
    )

    steps.append({
        "array": arr.copy(),
        "message": "Quick Sort completed!"
    })

    return steps


# ============================================================
# GET STEPS FOR ANY ALGORITHM
# ============================================================

visualization_functions = {

    "Bubble Sort": bubble_sort_steps,
    "Selection Sort": selection_sort_steps,
    "Insertion Sort": insertion_sort_steps,
    "Merge Sort": merge_sort_steps,
    "Quick Sort": quick_sort_steps
}


def get_sorting_steps(algorithm_name, data):

    if algorithm_name not in visualization_functions:
        return []

    return visualization_functions[
        algorithm_name
    ](data)