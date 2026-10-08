import time


def benchmark_algorithm(sort_function, data):

    start_time = time.perf_counter()

    sorted_data, comparisons, swaps = sort_function(data)

    end_time = time.perf_counter()

    execution_time = (end_time - start_time) * 1000

    return {
        "time": execution_time,
        "comparisons": comparisons,
        "swaps": swaps,
        "sorted_data": sorted_data
    }