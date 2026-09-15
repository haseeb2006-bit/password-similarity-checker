# Password Similarity Checker

![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.13-blue.svg)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)

**A password strength checker that catches structurally similar passwords, not just exact matches.**

Password blocklists typically reject a password only if it exactly matches a known weak password — so a user can bypass the check with a trivial edit, like turning `password123` into `Password123!`. This tool instead measures structural similarity between a candidate password and a dataset of common weak passwords, catching tweaked variants that exact-match systems miss.

---

## Features

- **Bigram-based structural comparison** — (one sentence)
- **Bloom filter fingerprinting** — (one sentence)
- **Three similarity metrics (Jaccard, Dice, Cosine)** — (one sentence)
- **Evidence-based threshold** — (one sentence, reference your experiment)

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


- **`src/bigrams.py`** — (one line)
- **`src/bloom_filter.py`** — (one line)
- **`src/similarity.py`** — (one line)
- **`src/dataset.py`** — (one line)
- **`src/main.py`** — (one line)
- **`experiments.py`** — (one line)

---

## How It Works

### 1. Bigrams
(your explanation)

### 2. Bloom Filter Fingerprint
(your explanation — flag as experimental fingerprint use)

### 3. Hashing (SHA-256 + MD5)
(your explanation — explicit note MD5 isn't used for security here)

### 4. Double Hashing
(your explanation of the formula)

### 5. Similarity Metrics
(Jaccard/Dice/Cosine explanations)

### 6. Decision Logic
(threshold explanation, link to Experimental Results section)

---

## Dataset

(source, license, filtering, reproducibility — your words)

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

(paste a real REJECTED example from your terminal)
(paste a real ACCEPTED example from your terminal)


---

## Experimental Results

(your experiments.py output + the 0.7 → 0.4 threshold story)

---

## Testing

```bash
python -m unittest discover tests
```

(test count, what's covered)

---

## Limitations

(your honest list — dataset coverage, small sample, experimental Bloom filter use, L/K not tuned)

---

## Security Considerations

(no logging/persistence, MD5's role, not an auth system, not a bcrypt/Argon2 replacement)

---

## Future Work

(larger threshold validation, L/K tuning, optional complexity layer, dataset expansion)

---

## License

MIT — see [LICENSE](LICENSE)

## Attribution

Dataset: [SecLists](https://github.com/danielmiessler/SecLists) (danielmiessler/SecLists), MIT License

## Author

(your name / GitHub handle)