import hashlib
from src.bigrams import get_bigrams


def get_hash_positions(bigram: str, L: int, K: int) -> list[int]:
    h1 = int(hashlib.sha256(bigram.encode()).hexdigest(), 16)
    h2 = int(hashlib.md5(bigram.encode()).hexdigest(), 16)

    positions = []
    for i in range(K):
        position = (h1 + i * h2) % L
        positions.append(position)
    return positions


def insert_bigram(bit_array: list[int], bigram: str, L: int, K: int) -> None:
    positions = get_hash_positions(bigram, L, K)
    for position in positions:
        bit_array[position] = 1


def get_fingerprint(password: str, L: int, K: int) -> list[int]:
    bit_array = [0] * L
    bigrams = get_bigrams(password)
    for bigram in bigrams:
        insert_bigram(bit_array, bigram, L, K)
    return bit_array


if __name__ == "__main__":
    fingerprint = get_fingerprint("cat", L=1000, K=20)
    print(sum(fingerprint))