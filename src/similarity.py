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


if __name__ == "__main__":
    a = [1, 1, 0, 0]
    b = [1, 0, 1, 0]
    print(jaccard_similarity(a, b))