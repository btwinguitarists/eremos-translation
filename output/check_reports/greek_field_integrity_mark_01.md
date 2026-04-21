# Greek-field integrity check — mark ch. 1

- key_decisions entries scanned: **78**
- Hard fails: **1**
- Warnings: 3

## ❌ Hard fails

### Mark 1:10  (THAI_IN_GREEK)
- `greek` field: `εἶδεν + ทอดพระเนตร`
- `thai` field: `ทอดพระเนตรเห็น`
- Why flagged: Thai characters in the key_decisions[].greek slot — schema violation.

## ⚠ Warnings (non-blocking)

- **Mark 1:24** (ASCII_LABEL): `Speaker: unclean spirit to Jesus` → `ข้า...ท่าน`
- **Mark 1:27** (ASCII_LABEL): `Punctuation ambiguity` → `คำสอนใหม่ที่มีสิทธิอำนาจ!`
- **Mark 1:40** (ASCII_LABEL): `leper addressing Jesus` → `ข้าพระองค์...พระองค์`
