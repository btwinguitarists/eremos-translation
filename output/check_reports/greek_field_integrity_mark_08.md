# Greek-field integrity check — mark ch. 8

- key_decisions entries scanned: **167**
- Hard fails: **1**
- Warnings: 3

## ❌ Hard fails

### Mark 8:2  (THAI_IN_GREEK)
- `greek` field: `Self-reference 'เรา'`
- `thai` field: `เรา (royal first-person)`
- Why flagged: Thai characters in the key_decisions[].greek slot — schema violation.

## ⚠ Warnings (non-blocking)

- **Mark 8:24** (ASCII_LABEL): `Self-reference` → `ข้า`
- **Mark 8:27** (ASCII_LABEL): `Self-ref` → `เรา`
- **Mark 8:33** (ASCII_LABEL): `Self-ref / address-to-Peter` → `เรา / เจ้า`
