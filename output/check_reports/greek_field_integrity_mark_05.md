# Greek-field integrity check — mark ch. 5

- key_decisions entries scanned: **155**
- Hard fails: **1**
- Warnings: 5

## ❌ Hard fails

### Mark 5:22  (GREEK_NOT_IN_VERSE)
- `greek` field: `ἰδοὺ (implicit in some readings)`
- `thai` field: `ดูเถิด`
- Greek tokens checked: ['ἰδοὺ']
- Why flagged: Greek token(s) not in the verse's source text (normalized for case/accents), and rationale doesn't flag it as variant/classical/LXX/hapax/morphological.

## ⚠ Warnings (non-blocking)

- **Mark 5:1** (ASCII_LABEL): `Greek text variant` → `(see notes)`
- **Mark 5:7** (ASCII_LABEL): `Speaker: unclean spirit to Jesus` → `ข้า...ท่าน`
- **Mark 5:34** (ASCII_LABEL): `Jesus addressing the woman` → `เจ้า (intimate-affectionate, paternal-like)`
- **Mark 5:41** (ASCII_LABEL): `Aramaic transliteration` → `ทาลิธา คูม`
- **Mark 5:42** (ASCII_LABEL): `Cognate accusative pattern` → `ตกตะลึงด้วยความอัศจรรย์ใจอย่างยิ่ง`
