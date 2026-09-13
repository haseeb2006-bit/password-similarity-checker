from src.bloom_filter import get_fingerprint
from src.similarity import jaccard_similarity, dice_similarity, cosine_similarity


def load_passwords(filepath: str) -> list[str]:
    passwords = []
    with open(filepath, "r") as f:
        for line in f:
            passwords.append(line.strip())
    return passwords


def precompute_fingerprints(passwords: list[str], L: int, K: int) -> list[list[int]]:
    fingerprints = []
    for password in passwords:
        fingerprint = get_fingerprint(password, L, K)
        fingerprints.append(fingerprint)
    return fingerprints


def find_closest_match(candidate_fingerprint: list[int], passwords: list[str],
                        fingerprints: list[list[int]]) -> dict:
    best_password = None
    best_jaccard = -1.0
    best_dice = -1.0
    best_cosine = -1.0
    best_max_score = -1.0

    for i in range(len(passwords)):
        j = jaccard_similarity(candidate_fingerprint, fingerprints[i])
        d = dice_similarity(candidate_fingerprint, fingerprints[i])
        c = cosine_similarity(candidate_fingerprint, fingerprints[i])
        max_score = max(j, d, c)

        if max_score > best_max_score:
            best_max_score = max_score
            best_password = passwords[i]
            best_jaccard = j
            best_dice = d
            best_cosine = c

    return {
        "closest_password": best_password,
        "jaccard": best_jaccard,
        "dice": best_dice,
        "cosine": best_cosine,
        "max_score": best_max_score,
    }


if __name__ == "__main__":
    passwords = load_passwords("data/passlist.txt")
    fingerprints = precompute_fingerprints(passwords, L=1000, K=20)

    candidate = get_fingerprint("password123", L=1000, K=20)
    result = find_closest_match(candidate, passwords, fingerprints)
    print(result)