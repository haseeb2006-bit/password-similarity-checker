# Development Log

## Session 1 — Foundation & Bigrams
- Cloned repo, confirmed Python 3.13.2 environment
- Implemented `get_bigrams()` with space-padding, handled empty/single-char edge cases
- Added `tests/test_bigrams.py` (3 tests, all passing)

## Session 2 — Bloom Filter
- Implemented `get_hash_positions()` using SHA-256 + MD5 double hashing: `(h1 + i×h2) mod L`
- Implemented `insert_bigram()` and `get_fingerprint()` to build full password fingerprints
- Added `tests/test_bloom_filter.py` (5 tests, all passing)
- Learned: `python -m module.path` is required (not direct file execution) for internal package imports to resolve

## Session 3 — Similarity Metrics
- Implemented Jaccard, Dice, and Cosine similarity for binary bit-array fingerprints
- Explicitly fixed a zero-vector division-by-zero edge case (a known bug in a reference implementation) by treating both-empty vectors as identical (1.0) and one-empty as completely dissimilar (0.0)
- Hand-verified similarity values against manually calculated examples before writing tests
- Added `tests/test_similarity.py` (4 tests, all passing)

## Session 4 — Dataset & Comparison Engine
- Verified SecLists MIT license before using its `10k-most-common.txt`
- Built `data/filter_dataset.py` to dedupe and filter the raw ~10k list down to 800 entries
- Implemented `load_passwords()`, `precompute_fingerprints()`, `find_closest_match()` in `src/dataset.py`
- Added `tests/test_dataset.py` (4 tests, all passing)

## Session 5 — CLI, Decision Logic, Experiments
- Implemented `src/main.py`: validation, decision threshold logic, human-readable explanation
- Initial threshold (0.7, placeholder) found too permissive during manual testing (e.g. `P@ssw0rd1` incorrectly accepted)
- Lowered dataset minimum password length from 6 to 4 characters to catch short common passwords (e.g. `exit`, `pass`)
- Built `experiments.py` to measure similarity scores across similar vs. unrelated password pairs
- Updated threshold to 0.4 based on measured data (similar-pair avg 0.619, unrelated-pair avg 0.178)
- Verified the updated threshold correctly rejects multiple realistic weak/tweaked passwords
- Added `tests/test_main.py` (4 tests, all passing) covering validation, decision logic, and full pipeline integration

## Session 6 — Documentation
- Wrote full README (architecture, how-it-works, dataset, usage, experimental results, limitations, security)
- Documented development log and design decisions