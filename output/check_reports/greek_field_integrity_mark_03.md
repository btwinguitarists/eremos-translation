# Greek-field integrity check — mark ch. 3

- key_decisions entries scanned: **141**
- Hard fails: **1**
- Warnings: 5

## ❌ Hard fails

### Mark 3:26  (GREEK_NOT_IN_VERSE)
- `greek` field: `εἰ + aor. ind. (switched from ἐάν)`
- `thai` field: `ถ้า`
- Greek tokens checked: ['ἐάν']
- Why flagged: Greek token(s) not in the verse's source text (normalized for case/accents), and rationale doesn't flag it as variant/classical/LXX/hapax/morphological.

## ⚠ Warnings (non-blocking)

- **Mark 3:2** (ASCII_LABEL): `implicit subject (Pharisees)` → `พวกเขา`
- **Mark 3:4** (ASCII_LABEL): `Jesus to Pharisees (confrontational)` → `พวกเขา (in narrator frame); zero 2nd-person in direct speech`
- **Mark 3:22** (ASCII_LABEL): `Scribes' direct speech about Jesus` → `เขา (dismissive)`
- **Mark 3:30** (ASCII_LABEL): `Narrator bridge (not in Greek)` → `(พระองค์ตรัสเช่นนี้)`
- **Mark 3:33** (ASCII_LABEL): `Jesus' self-reference` → `เรา`
