from src.bloom_filter import get_fingerprint
from src.similarity import jaccard_similarity, dice_similarity, cosine_similarity

L = 1000
K = 20

SIMILAR_PAIRS = [
    ("password1", "Password1!"),
    ("letmein", "LetMein123"),
    ("qwerty", "qwerty123"),
    ("iloveyou", "IloveYou1"),
    ("dragon", "dragon123"),
]

UNRELATED_PAIRS = [
    ("password1", "sunshine"),
    ("letmein", "basketball"),
    ("qwerty", "chocolate"),
    ("iloveyou", "mountain"),
    ("dragon", "umbrella"),
]


def average_max_score(pairs: list[tuple[str, str]]) -> float:
    scores = []
    for a, b in pairs:
        fp_a = get_fingerprint(a, L, K)
        fp_b = get_fingerprint(b, L, K)
        max_score = max(
            jaccard_similarity(fp_a, fp_b),
            dice_similarity(fp_a, fp_b),
            cosine_similarity(fp_a, fp_b),
        )
        scores.append(max_score)
        print(f"{a!r} vs {b!r}: {max_score:.3f}")
    return sum(scores) / len(scores)


if __name__ == "__main__":
    print("=== Similar pairs ===")
    similar_avg = average_max_score(SIMILAR_PAIRS)
    print(f"Average: {similar_avg:.3f}\n")

    print("=== Unrelated pairs ===")
    unrelated_avg = average_max_score(UNRELATED_PAIRS)
    print(f"Average: {unrelated_avg:.3f}\n")

    suggested_threshold = (similar_avg + unrelated_avg) / 2
    print(f"Suggested threshold (midpoint): {suggested_threshold:.3f}")