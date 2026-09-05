import hashlib


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


if __name__ == "__main__":
    bit_array = [0] * 1000
    insert_bigram(bit_array, "ca", L=1000, K=20)
    print(sum(bit_array))