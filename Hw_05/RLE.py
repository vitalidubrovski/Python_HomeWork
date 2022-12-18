# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def main():
    rle = "11111 22222 WWWWW BBB 3333333 5555 66666 777 xxxxx sssss"
    encoded = encode(rle)
    decoded = decode(encoded)

    print("Исходные данные: " + rle)

    print("Сжатие: " + format_output(encoded))

    print("Восстановление: " + decoded)


def encode(sequence):
    count = 1
    result = []

    for x, item in enumerate(sequence):
        if x == 0:
            continue
        elif item == sequence[x - 1]:
            count += 1
        else:
            result.append((sequence[x - 1], count))
            count = 1

    result.append((sequence[len(sequence) - 1], count))

    return result


def decode(sequence):
    result = []

    for item in sequence:
        result.append(item[0] * item[1])

    return "".join(result)


def format_output(sequence):
    result = []

    for item in sequence:
        if item[1] == 1:
            result.append(item[0])
        else:
            result.append(str(item[1]) + ':' + item[0])

    return "".join(result)


if __name__ == "__main__":
    main()
