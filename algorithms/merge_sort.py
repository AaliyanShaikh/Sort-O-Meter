def merge_sort(arr):
    comparisons = [0]
    swaps = [0]

    def merge(left, right):
        result = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            comparisons[0] += 1

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

        left = divide(array[:mid])
        right = divide(array[mid:])

        return merge(left, right)

    sorted_array = divide(arr.copy())

    return sorted_array, comparisons[0], swaps[0]