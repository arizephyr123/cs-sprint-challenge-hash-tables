def has_negatives(a):
    num_dict = {}
    result = []
    for num in a:
        if num_dict.get(num *-1):
            if num >= 0:
                result.append(num)
            else:
                result.append(num *-1)
        else:
            num_dict[num] = num

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
