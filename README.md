# Password Similarity Checker

![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.13-blue.svg)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)

**A password strength checker that catches structurally similar passwords, not just exact matches.**

Password blocklists typically reject a password only if it exactly matches a known weak password — so a user can bypass the check with a trivial edit, like turning `password123` into `Password123!`. This tool instead measures structural similarity between a candidate password and a dataset of common weak passwords, catching tweaked variants that exact-match systems miss.

---

## Features

- **Bigram-based structural comparison** — passwords are broken into overlapping 2-character chunks so similar passwords remain detectable even after small edits.
- **Bloom filter fingerprinting** — each password is converted into a fixed-length bit array using SHA-256/MD5 double hashing, used here as a structural fingerprint.
- **Three similarity metrics (Jaccard, Dice, Cosine)** — each candidate is scored against the dataset using all three, taking the maximum as the decision signal.
- **Evidence-based threshold** — the accept/reject threshold was derived from measuring real similar-pair vs. unrelated-pair score distributions, not guessed.

---

## Architecture

password-similarity-checker/
├── README.md
├── LICENSE
├── .gitignore
│
├── data/
│ ├── passlist.txt
│ ├── filter_dataset.py
│ └── SOURCE.md
│
├── src/
│ ├── init.py
│ ├── bigrams.py
│ ├── bloom_filter.py
│ ├── similarity.py
│ ├── dataset.py
│ └── main.py
│
├── tests/
│ ├── test_bigrams.py
│ ├── test_bloom_filter.py
│ ├── test_similarity.py
│ ├── test_dataset.py
│ └── test_main.py
│
├── experiments.py
└── docs/
├── DEVELOPMENT_LOG.md
└── DESIGN_DECISIONS.md


- **`src/bigrams.py`** — generates padded, overlapping 2-character bigrams from a password.
- **`src/bloom_filter.py`** — builds a 1000-bit fingerprint per password using SHA-256/MD5 double hashing.
- **`src/similarity.py`** — Jaccard, Dice, and Cosine similarity for comparing two fingerprints.
- **`src/dataset.py`** — loads the password dataset, precomputes fingerprints, finds the closest match for a candidate.
- **`src/main.py`** — CLI entry point wiring validation, fingerprinting, comparison, and the accept/reject decision together.
- **`experiments.py`** — measures similarity scores for known similar vs. unrelated password pairs to derive the decision threshold.

---

## How It Works

### 1. Bigrams
Each password is padded with a space on each side (`"cat"` → `" cat "`), then split into overlapping 2-character windows: `[' c', 'ca', 'at', 't ']`. This captures both the characters and their position near word boundaries. Two passwords that differ by a small edit (e.g. `password1` vs `Password1!`) still share most of their bigrams, which is what makes structural similarity detection possible.

### 2. Bloom Filter Fingerprint
Each bigram is inserted into a shared 1000-bit array by setting several bit positions to 1. Combining every bigram's positions for a password produces a single bit-array "fingerprint." This project uses the Bloom filter's fixed-length bit array as a structural fingerprint for comparison, rather than for its traditional probabilistic membership-testing purpose — this is an experimental, educational application, not a standard password-security technique.

### 3. Hashing (SHA-256 + MD5)
Each bigram is hashed with SHA-256 and MD5 to produce two large integers. These hashes are not used for any security or password-storage purpose — MD5 in particular is cryptographically broken and unsuitable for protecting real secrets. Here, both hash functions only serve as reliable, deterministic number generators used to pick bit positions.

### 4. Double Hashing
K bit positions are generated per bigram using:

position_i = (h1 + i × h2) mod L for i = 0 .. K-1

where `h1` comes from SHA-256, `h2` from MD5, and `L` is the bit array length. This produces K different positions from only two hash calls instead of hashing K separate times.

### 5. Similarity Metrics
Given two fingerprints (bit arrays), similarity is measured three ways:
- **Jaccard** = intersection / union of set bits
- **Dice** = 2 × intersection / (size A + size B)
- **Cosine** = dot product / (magnitude A × magnitude B)

For binary vectors, intersection means positions where both arrays have a 1, and magnitude is the square root of the count of 1s. Zero-vector cases (comparing two all-empty fingerprints) are handled explicitly to avoid division-by-zero — both-empty is treated as identical (1.0), while one-empty-one-not is treated as completely dissimilar (0.0).

### 6. Decision Logic
A candidate password is compared against all 800 dataset entries using all three metrics; the maximum score against any single entry is used as the decision signal. If that score meets or exceeds the threshold, the password is REJECTED as too similar to a known weak password. The threshold (0.4) was derived experimentally — see Experimental Results below — rather than chosen arbitrarily.

---

## Dataset

The dataset is derived from [SecLists](https://github.com/danielmiessler/SecLists)' `Passwords/Common-Credentials/10k-most-common.txt`, licensed under MIT. The original file (~10,000 entries) is filtered down to 800 entries: deduplicated, and restricted to passwords between 4 and 16 characters. The filtering script (`data/filter_dataset.py`) is included so the dataset is fully reproducible from the original source.

---

## Installation

```bash
git clone https://github.com/haseeb2006-bit/password-similarity-checker
cd password-similarity-checker
```

No external dependencies — Python 3.10+ standard library only.

---

## Usage

```bash
python -m src.main
```

Example output:

Enter a password to check (or 'quit' to exit): password1
REJECTED: This password is too similar to a known weak password ('password1'). Similarity score: 1.000 (threshold: 0.4).

Enter a password to check (or 'quit' to exit): pwaswrd1
REJECTED: This password is too similar to a known weak password ('password1'). Similarity score: 0.675 (threshold: 0.4).


---

## Experimental Results

The decision threshold was derived by measuring similarity scores for two groups of password pairs using `experiments.py`:

| Pair type | Example | Max score |
|---|---|---|
| Similar | `password1` vs `Password1!` | 0.700 |
| Similar | `qwerty` vs `qwerty123` | 0.740 |
| Unrelated | `password1` vs `sunshine` | 0.160 |
| Unrelated | `letmein` vs `basketball` | 0.220 |

- Similar-pair average: **0.619**
- Unrelated-pair average: **0.178**
- Midpoint threshold: **0.399** (rounded to **0.4**)

This replaced an initial placeholder threshold of 0.7, which was too permissive — e.g. `P@ssw0rd1` scored 0.594 and was incorrectly accepted at 0.7, but is correctly rejected at 0.4.

---

## Testing

```bash
python -m unittest discover tests
```

The suite covers bigram generation (padding, empty/short-string edge cases), Bloom filter hashing (determinism, position range, insertion), similarity metrics (identical, opposite, partial-overlap hand-verified, and zero-vector cases), dataset loading/comparison, and full end-to-end pipeline integration.

---

## Limitations

- The tool only detects similarity to passwords **present in the dataset** — a weak password structurally unlike anything in the 800-entry list will not be flagged.
- The threshold was derived from a small sample (5 similar + 5 unrelated pairs); it is a reasonable evidence-based starting point, not a statistically validated value.
- The Bloom filter's bit array is used here as a structural fingerprint for comparison — an experimental, educational design choice, not a standard password-security technique.
- Bloom filter parameters (L=1000, K=20) were not independently benchmarked against dataset size or false-positive behavior.

---

## Security Considerations

- Passwords entered by the user are not logged, persisted, or written to disk.
- MD5 is used only as a hash-position generator for the Bloom filter; it is never used to store or protect passwords.
- This is a password **similarity analysis** tool, not a password storage or authentication system.
- This project is not a replacement for secure password hashing algorithms such as bcrypt, Argon2, or scrypt.

---

## Future Work

- Larger-scale threshold validation with a bigger set of similar/unrelated pairs.
- Independent experimentation on Bloom filter parameters (L, K) against dataset size and false-positive rate.
- Optional secondary complexity-rule layer (character diversity checks) as an additional, independent signal.
- Expanding the dataset beyond the current SecLists-derived subset.

---

## License

MIT — see [LICENSE](LICENSE)

## Attribution

Dataset: [SecLists](https://github.com/danielmiessler/SecLists) (danielmiessler/SecLists), MIT License

## Author

haseeb2006-bit