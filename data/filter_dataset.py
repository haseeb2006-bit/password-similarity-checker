def filter_dataset(input_path: str, output_path: str, target_count: int = 800, min_len: int = 6, max_len: int = 16) -> None:
    seen = set()
    filtered = []

    with open(input_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            password = line.strip()
            if not password:
                continue
            if password in seen:
                continue
            if not (min_len <= len(password) <= max_len):
                continue
            seen.add(password)
            filtered.append(password)
            if len(filtered) >= target_count:
                break

    with open(output_path, "w", encoding="utf-8") as f:
        for password in filtered:
            f.write(password + "\n")

    print(f"Wrote {len(filtered)} passwords to {output_path}")


if __name__ == "__main__":
    filter_dataset("data/10k-most-common-RAW.txt", "data/passlist.txt")