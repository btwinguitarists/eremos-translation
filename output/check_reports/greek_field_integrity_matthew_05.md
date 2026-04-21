# Greek-field integrity check — matthew ch. 5

- key_decisions entries scanned: **134**
- Hard fails: **1**
- Warnings: 0

## ❌ Hard fails

### Matthew 5:29  (THAI_IN_GREEK)
- `greek` field: `ὁ ὀφθαλμός σου ὁ δεξιὸς σκανดαλίζει σε`
- `thai` field: `ตาขวาของท่านทำให้ท่านสะดุดหลงผิด`
- Why flagged: Thai characters in the key_decisions[].greek slot — schema violation.
