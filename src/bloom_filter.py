import hashlib


def get_hash_positions(bigram: str, L: int, K: int) -> list[int]:
    h1 = int(hashlib.sha256(bigram.encode()).hexdigest(), 16)
    h2 = int(hashlib.md5(bigram.encode()).hexdigest(), 16)

    positions = []
    for i in range(K):
        position = (h1 + i * h2) % L
        positions.append(position)
    return positions


if __name__ == "__main__":
    print(get_hash_positions("ca", L=1000, K=20))