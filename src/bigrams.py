def get_bigrams(password: str) -> list[str]:
    password = " " + password + " "
    bigrams = []
    for i in range(len(password) - 1):
        bigrams.append(password[i] + password[i + 1])
    return bigrams


if __name__ == "__main__":
    print(get_bigrams("cat"))