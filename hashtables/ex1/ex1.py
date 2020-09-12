

def get_indices_of_item_weights(weights, length, limit):
    # {'limit - item weight' : index}
    weight_dict = {}
    idx_1 = -1
    idx_2 = -1

    for (idx, weight) in enumerate(weights):
        if str(weight) in weight_dict:
            idx_1 = idx
            idx_2 = weight_dict[str(weight)]
            return (idx_1, idx_2)
        elif weight > limit:
            pass
        else:
            weight_dict[str(limit - weight)] = idx

    return None