def jaccard_similarity(a: list[int], b: list[int]) -> float:
    intersection = 0
    union = 0
    for i in range(len(a)):
        if a[i] == 1 and b[i] == 1:
            intersection += 1
        if a[i] == 1 or b[i] == 1:
            union += 1

    if union == 0:
        return 1.0

    return intersection / union


def dice_similarity(a: list[int], b: list[int]) -> float:
    intersection = 0
    size_a = 0
    size_b = 0
    for i in range(len(a)):
        if a[i] == 1 and b[i] == 1:
            intersection += 1
        if a[i] == 1:
            size_a += 1
        if b[i] == 1:
            size_b += 1

    if size_a + size_b == 0:
        return 1.0

    return (2 * intersection) / (size_a + size_b)


if __name__ == "__main__":
    a = [1, 1, 0, 0]
    b = [1, 0, 1, 0]
    print(jaccard_similarity(a, b))
    print(dice_similarity(a, b))