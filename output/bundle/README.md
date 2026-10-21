# Eremos Translation: whole Bible in one file

`eremos-thai.json` is the complete Eremos Translation (Thai): 66 books, every chapter and verse,
English (BSB) verse numbering, psalm titles as `title`. Public domain (CC0 1.0). It is a draft:
drafted with AI from the Hebrew and Greek, machine-checked, with Thai review beginning.

Also at https://bible.eremosapp.com/data/eremos-thai.json, and chapter by chapter at
https://bible.eremosapp.com/api/v1/JHN/1.json (USFM book codes).

## Is my copy genuine?

Anyone may copy and change this text; that is what CC0 means. What these files prove is which
text is the original, so a changed copy can always be told apart.

1. **Fingerprints.** `SHA256SUMS` lists the SHA-256 of this JSON and of every USFM and
   projection file. From the repository root:
   `shasum -a 256 -c output/bundle/SHA256SUMS`
2. **Signature.** `SHA256SUMS.asc` is the maintainer's OpenPGP signature of that list
   (key fingerprint `91CC 37AF FDD9 469E B1B5 5A2A E5ED 8377 74A2 7153`):
   `gpg --verify SHA256SUMS.asc SHA256SUMS`
3. **Timestamp.** `SHA256SUMS.ots` is an OpenTimestamps proof anchoring the list in the
   Bitcoin blockchain, so anyone can confirm this exact text existed on that date. No tokens,
   no cost, nothing sold. `ots verify SHA256SUMS.ots`

The file is deterministic: the same text always produces the same bytes. Regenerate after any
text change with `python3 scripts/export_bundle.py`, then re-sign and re-stamp.
