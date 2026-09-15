# Design Decisions

## Bigrams over trigrams
**Decision:** Use 2-character bigrams for structural comparison.
**Alternatives:** Trigrams (3-character windows).
**Reason:** Bigrams produce denser overlap for short strings like passwords, giving more reliable similarity signal at typical password lengths.
**Tradeoff:** Bigrams are less specific than trigrams (more false-positive-prone in theory), but trigrams would be too sparse for short passwords to share meaningful overlap.

## Bloom filter as fingerprint, not membership structure
**Decision:** Use the Bloom filter's bit array as a structural fingerprint for similarity comparison.
**Alternatives:** Use the Bloom filter only for its standard purpose (fast membership testing); compare raw bigram sets directly without a Bloom filter at all.
**Reason:** Fixed-length bit vectors allow consistent, efficient similarity comparison across all dataset entries. Bloom filter double hashing repurposes this into a compact fingerprint.
**Tradeoff:** This is a non-standard, experimental use of Bloom filters — flagged explicitly as such rather than presented as an established technique.

## SHA-256 + MD5 for double hashing
**Decision:** Generate K bit positions per bigram using `(h1 + i×h2) mod L`, with h1 from SHA-256 and h2 from MD5.
**Alternatives:** K independent hash function calls; two SHA-256 calls with different salts.
**Reason:** Double hashing produces K positions from only two hash calls, which is cheaper than K separate hash operations.
**Tradeoff:** MD5 is cryptographically broken and unsuitable for security purposes — but here it is used only as a non-adversarial number generator, not to protect any secret, so its weaknesses don't apply to this use case.

## Zero-vector handling in similarity metrics
**Decision:** Two all-empty fingerprints are treated as identical (score 1.0); one empty and one non-empty is treated as completely dissimilar (score 0.0).
**Alternatives:** Raise an error; always return 0.0 regardless of both-empty vs one-empty.
**Reason:** Avoids a known division-by-zero bug present in a reference implementation, while giving a defensible, consistent interpretation across all three metrics.
**Evidence:** Covered explicitly in `tests/test_similarity.py`.

## Dataset: SecLists subset over custom-built list
**Decision:** Use a filtered subset of SecLists' `10k-most-common.txt`.
**Alternatives:** Manually author a custom password list; use breach data (e.g. RockYou).
**Reason:** SecLists is MIT-licensed, publicly maintained, and used in real security tooling — meaning results are grounded in realistic weak-password patterns with verifiable, legitimate sourcing.
**Tradeoff:** The tool's coverage is limited to what's in this subset; a password not similar to any dataset entry will not be flagged, regardless of its inherent weakness.

## Threshold: experimentally derived, not guessed
**Decision:** Set the accept/reject threshold to 0.4, based on measuring similar-pair vs. unrelated-pair score distributions.
**Alternatives:** Arbitrary fixed value (originally 0.7, used as a placeholder).
**Reason:** The placeholder value (0.7) was shown to be too permissive during manual testing (`P@ssw0rd1` incorrectly accepted). The midpoint between measured similar-pair average (0.619) and unrelated-pair average (0.178) gives an evidence-based value.
**Evidence:** See `experiments.py` output and the Experimental Results section of the README.
**Tradeoff:** Derived from a small sample (5 similar + 5 unrelated pairs); a larger validation set would strengthen confidence in this exact value.