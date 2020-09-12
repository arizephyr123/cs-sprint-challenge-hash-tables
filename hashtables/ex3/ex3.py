def intersection(arrays):
    in_all = {}
    for n in arrays[0]:
        in_all[n] = 1

    for array in arrays[1:]:
        for n in array:
            try:
                if in_all[n]:
                    in_all[n] += 1
            except:
                pass

    result = []
    for (k, v) in in_all.items():
        if v == len(arrays):
            result.append(k)
        
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

    