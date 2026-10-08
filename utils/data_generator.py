import random


def generate_data(size, data_type):
    data = list(range(1, size + 1))

    if data_type == "Random":
        random.shuffle(data)

    elif data_type == "Sorted":
        pass

    elif data_type == "Reverse Sorted":
        data.reverse()

    elif data_type == "Nearly Sorted":
        swaps = max(1, size // 20)

        for _ in range(swaps):
            i = random.randint(0, size - 1)
            j = random.randint(0, size - 1)

            data[i], data[j] = data[j], data[i]

    return data