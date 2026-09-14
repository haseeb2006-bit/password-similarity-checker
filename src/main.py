from src.bloom_filter import get_fingerprint
from src.dataset import load_passwords, precompute_fingerprints, find_closest_match

L = 1000
K = 20
THRESHOLD = 0.4


def validate_password(password: str) -> bool:
    if len(password) < 4:
        return False
    return True


def make_decision(max_score: float, threshold: float) -> str:
    if max_score >= threshold:
        return "REJECTED"
    return "ACCEPTED"


def explain_decision(result: dict, decision: str, threshold: float) -> str:
    closest = result["closest_password"]
    score = result["max_score"]
    if decision == "REJECTED":
        return (f"REJECTED: This password is too similar to a known weak "
                f"password ('{closest}'). Similarity score: {score:.3f} "
                f"(threshold: {threshold}).")
    return (f"ACCEPTED: This password is sufficiently different from known "
            f"weak passwords. Closest match: '{closest}' "
            f"(similarity: {score:.3f}, threshold: {threshold}).")


def main():
    print("Loading password dataset...")
    passwords = load_passwords("data/passlist.txt")
    fingerprints = precompute_fingerprints(passwords, L, K)
    print(f"Loaded {len(passwords)} passwords.\n")

    while True:
        password = input("Enter a password to check (or 'quit' to exit): ")
        if password.lower() == "quit":
            break

        if not validate_password(password):
            print("Password too short (minimum 4 characters). Try again.\n")
            continue

        candidate_fingerprint = get_fingerprint(password, L, K)
        result = find_closest_match(candidate_fingerprint, passwords, fingerprints)
        decision = make_decision(result["max_score"], THRESHOLD)
        print(explain_decision(result, decision, THRESHOLD))
        print()


if __name__ == "__main__":
    main()