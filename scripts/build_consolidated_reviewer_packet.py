#!/usr/bin/env python3
"""
Build a consolidated multi-book reviewer packet.

Two flavors:
- `--lang en`: Comprehensive English packet for theological/Greek scholars and
  AI reviewers. Self-contained: project overview + confessional position +
  philosophy + source discipline + standard key-term locks + index of all
  locked decisions + per-book end-of-book audit summaries.
- `--lang th`: Thai believer FAQ stub for native-speaker review. Questions a
  Thai reader might ask, with stub answers in Thai. **Marked DRAFT** — needs
  the maintainer's editorial pass before sharing.

Usage:
  python3 scripts/build_consolidated_reviewer_packet.py BOOKS --lang LANG [--out PATH]

  BOOKS    space-separated 3-letter book codes (e.g., MAT MRK LUK ACT)
  --lang   en | th
  --out    output path; default docs/reviewer_packet_<LANG>_<DATE>.md

Example:
  python3 scripts/build_consolidated_reviewer_packet.py MAT MRK LUK ACT --lang en
"""
import argparse
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
TRANSLATOR_DECISIONS = DOCS / "translator_decisions"
TRANSLATIONS = ROOT / "output" / "translations"

BOOKS = {
    "MAT": ("matthew", "Matthew"),
    "MRK": ("mark", "Mark"),
    "LUK": ("luke", "Luke"),
    "JHN": ("john", "John"),
    "ACT": ("acts", "Acts"),
    "ROM": ("romans", "Romans"),
    "1CO": ("1corinthians", "1 Corinthians"),
    "2CO": ("2corinthians", "2 Corinthians"),
    "GAL": ("galatians", "Galatians"),
    "EPH": ("ephesians", "Ephesians"),
    "PHP": ("philippians", "Philippians"),
    "COL": ("colossians", "Colossians"),
    "1TH": ("1thessalonians", "1 Thessalonians"),
    "2TH": ("2thessalonians", "2 Thessalonians"),
    "1TI": ("1timothy", "1 Timothy"),
    "2TI": ("2timothy", "2 Timothy"),
    "TIT": ("titus", "Titus"),
    "PHM": ("philemon", "Philemon"),
    "HEB": ("hebrews", "Hebrews"),
    "JAS": ("james", "James"),
    "1PE": ("1peter", "1 Peter"),
    "2PE": ("2peter", "2 Peter"),
    "1JN": ("1john", "1 John"),
    "2JN": ("2john", "2 John"),
    "3JN": ("3john", "3 John"),
    "JUD": ("jude", "Jude"),
    "REV": ("revelation", "Revelation"),
}


def find_audit(book_code):
    """Return (Path, summary_text) for a book's end-of-book audit, or (None, None)."""
    matches = sorted(DOCS.glob(f"end_of_book/*/{book_code}_END_OF_BOOK_REVIEW_*.md"), reverse=True)
    if not matches:
        # Fallback to legacy flat docs/ layout for any pre-reorg audits.
        matches = sorted(DOCS.glob(f"{book_code}_END_OF_BOOK_REVIEW_*.md"), reverse=True)
    if not matches:
        return None, None
    audit_path = matches[0]
    text = audit_path.read_text()
    m = re.search(r"## Summary\s*\n(.+?)(?=\n##\s)", text, re.DOTALL)
    summary = m.group(1).strip() if m else "(summary section not found)"
    return audit_path, summary


def book_metadata(book_code):
    if book_code not in BOOKS:
        sys.exit(f"Unknown book code: {book_code}. Known: {sorted(BOOKS)}")
    slug, name = BOOKS[book_code]
    chapters = sorted(TRANSLATIONS.glob(f"{slug}_*.json"))
    return slug, name, len(chapters)


def list_decision_docs():
    """Return list of (filename, title, oneline) tuples from translator_decisions/."""
    docs = []
    for p in sorted(TRANSLATOR_DECISIONS.glob("*.md")):
        if p.name == "README.md":
            continue
        text = p.read_text()
        title_match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
        scope_match = re.search(r"\*\*Scope:\*\*\s*(.+?)(?=\n\*\*|\n\n)", text, re.DOTALL)
        title = title_match.group(1).strip() if title_match else p.stem
        scope = scope_match.group(1).strip().replace("\n", " ") if scope_match else ""
        if len(scope) > 200:
            scope = scope[:197] + "..."
        docs.append((p.name, title, scope))
    return docs


def build_english(book_codes):
    today = date.today().isoformat()
    book_names = ", ".join(BOOKS[c][1] for c in book_codes)
    book_list = " + ".join(BOOKS[c][1] for c in book_codes)

    chapter_lines = []
    for code in book_codes:
        slug, name, ch_count = book_metadata(code)
        chapter_lines.append(f"- **{name}**: {ch_count} chapters — `output/reader/{slug}.md` (Thai-only continuous-reading), per-chapter JSONs at `output/translations/{slug}_*.json`, per-chapter check reports at `output/check_reports/{slug}_*_review.md`")

    decision_docs = list_decision_docs()
    decision_lines = []
    for fname, title, scope in decision_docs:
        decision_lines.append(f"- **[{title}](translator_decisions/{fname})** — {scope}")

    audit_sections = []
    for code in book_codes:
        slug, name, _ = book_metadata(code)
        audit_path, summary = find_audit(code)
        if audit_path:
            rel_path = audit_path.relative_to(DOCS)
            audit_sections.append(
                f"### {name}\n\n"
                f"Full audit: [{audit_path.name}]({rel_path})\n\n"
                f"{summary}\n"
            )
        else:
            audit_sections.append(
                f"### {name}\n\n"
                f"No end-of-book audit on file. {name} predates the End-of-Book Checklist process or is awaiting backfill.\n"
            )

    return f"""# Eremos Translation — Consolidated Reviewer Packet
**Date assembled: {today}**
**Books covered: {book_names}**

This packet consolidates everything a Greek scholar, theological reviewer, or AI reviewer needs to evaluate the {book_list} translation. The translation itself lives in `output/reader/<slug>.md` (full Thai text) and `output/translations/<slug>_*.json` (per-verse Greek + Thai + rationale + notes). This packet documents the decisions behind those files.

For an external AI sanity-check (Grok / ChatGPT / Gemini scale), see the per-book `docs/end_of_book/<book>/external_review_packet_<BOOK>_*.md` files — those are scoped and sized for free-tier AI ceilings. **This packet is full-content for human reviewers.**

---

## 1. What this translation is

**Eremos Translation** is a CC0, AI-assisted Thai New Testament translated directly from the SBLGNT Greek critical text. Translation philosophy is **optimal equivalence** — faithful to Greek grammar AND natural in modern Thai. The methodology follows SIL / Wycliffe / UBS standards (Larson's meaning-based approach, Beekman & Callow's principles, Paratext's check framework), adapted for AI-assisted draft generation with extensive automated and human verification.

**Status as of this packet:**

{chr(10).join(chapter_lines)}

The full repository (CC0): https://github.com/{{maintainer}}/thai-bible-ai (path adjust as needed for the maintainer's GitHub username).

---

## 2. Confessional position

Eremos Translation is **evangelical Protestant**. Source-text family: SBLGNT (Alexandrian-leaning critical text, same scholarly base as ESV / NIV / NASB / CSB / BSB). Canon: 27-book NT (no deuterocanonicals).

**Editorial decisions on contested verses follow what major evangelical Protestant translations do.** When manuscript evidence is split, we prefer the editorial choice that aligns with the modern evangelical critical-text consensus (NA28-aligned, where SBLGNT and NA28 agree); when SBLGNT and NA28 disagree, we follow SBLGNT but document the divergence.

**License vs. theology:** CC0 means anyone of any tradition may use the translation, but the *editorial decisions* are evangelical Protestant — not ecumenical-syncretist or doctrinally neutral. The license is open; the translator's editorial frame is not.

---

## 3. Translation philosophy (summary)

**Optimal equivalence**, BSB family. Faithful to Greek grammar, syntax, and semantic range AND natural in modern Thai. When the four pillars (Larson's accuracy / clarity / naturalness / acceptability) conflict, **accuracy wins**, with naturalness documented as a tradeoff.

What this means in practice:
- Greek tense / mood / aspect distinctions are preserved when meaningful, naturalized when not (e.g., historic-present always rendered Thai past — see `historic_present_2026-04.md`).
- Greek word order is rearranged for Thai naturalness; semantic load preserved.
- Idioms are rendered to a Thai equivalent where one exists; otherwise rendered literally with a `notes` entry explaining the original idiom.
- Aramaic embeds (Talitha cumi, Ephphatha, Abba) preserve transliteration AND Mark's own Greek translation — matching Mark's "transliterate then translate" rhetorical move.

---

## 4. Source discipline (strict)

**During translation**, the AI may read only:

- The Greek text (SBLGNT) with MACULA morphological analysis
- The Berean Standard Bible English (CC0) — sanity check ONLY, never as a source to copy
- `RULES.md` — the canonical rules
- `glossary.json` — the persistent key-term ledger
- Prior chapters of Eremos's own output (for consistency)
- unfoldingWord Book Introduction (CC-BY-SA, read-for-context-not-copy)
- unfoldingWord Translation Notes (CC-BY-SA, read-for-context-not-copy)

**Never read during translation:**

- Any copyrighted Thai translation (THSV, NTV, ERV Thai, TNCV)
- TNBT (CC-BY-SA — used post-draft for structural comparison only, never read for wording)
- Any copyrighted commentary

**Why the strictness:** this preserves the "independent creation" copyright defense. Output is produced by independent analysis of the public-domain original languages. After drafting, comparison against other translations identifies divergences to justify, never to copy.

---

## 5. Register & honorifics

- **Divine subjects** (God, Christ, Spirit) always use ราชาศัพท์ (royal register): ทรง / เสด็จ / ตรัส / ทอดพระเนตร / พระหัตถ์ / พระบาท / พระเจ้า / พระเยซู.
- **Humans addressing Christ/God** use lowest humble register: ข้าพระองค์ / พระองค์.
- **God addressing the Son** acceptably uses เจ้า (intimate Father-Son) or พระองค์ (high reverence) — documented per choice.
- **Demons / adversaries** use neutral / distancing register, never honorifics.
- **Inter-human dialogue** matches the social relationship.
- **Non-divine human authorities** (Herod, Pilate, Felix, Festus, centurions, priests) use plain Thai register, NOT ราชาศัพท์ — see `translator_decisions/honorifics_non_divine_authorities_2026-04.md`.
- **Parable characters representing God** (fathers, kings, masters, judges) use human register, never ราชาศัพท์ — see `translator_decisions/parabolic_god_figures_human_register_2026-04.md`.
- **Pagan deities** use เทพ / เทพี / เทพเจ้า — NEVER พระเจ้า, which is reserved for the biblical God.

---

## 6. Standard key-term locks

Non-negotiable (`RULES.md` §4):

| Greek | Thai | Notes |
|-------|------|-------|
| εὐαγγέλιον | ข่าวประเสริฐ | Never พระกิตติคุณ unless explicitly noted |
| χριστός | พระคริสต์ | Title, not a proper name |
| Ἰησοῦς | พระเยซู | The พระ prefix is the divine honorific |
| σατανᾶς | ซาตาน | Transliteration, standard |
| πνεῦμα ἅγιον | พระวิญญาณบริสุทธิ์ | |
| βαπτίζω / βάπτισμα | บัพติศมา | Transliteration, standard in Thai Christianity |
| ἔρημος (wilderness) | ถิ่นทุรกันดาร | "Wilderness/desert region" |
| ἔρημος τόπος | ที่เปลี่ยว | "Solitary place" |
| κύριος (= YHWH) | องค์พระผู้เป็นเจ้า | OT citations + narrator-Lord-as-Jesus in Luke-Acts |
| κύριος (Jesus / human master, vocative) | context-dependent, documented | See vocative_kyrie_didaskale doc |
| συναγωγή | ธรรมศาลา | |
| μετανοέω | กลับใจ | |
| βασιλεία τοῦ θεοῦ | อาณาจักรของพระเจ้า | Mark/Luke/Acts uniform; Matthew adds the τῶν οὐρανῶν → อาณาจักรสวรรค์ split |
| ἁμαρτία | บาป | |
| ἄφεσις (ἁμαρτιῶν) | การยกโทษ(บาป) | Locked 2026-04 |
| ἀγαπητός | ที่รัก | "Beloved" — or "ที่รักยิ่ง" for intensification |

For proper nouns (persons, places), transliteration follows established Thai Christian practice (Ἰωάννης → ยอห์น, Ἠσαΐας → อิสยาห์, etc.).

---

## 7. Locked corpus-level decisions

Each linked doc records: scope, evidence base, the rule, alternatives considered, when to revisit, and cross-references. **These decisions are LOCKED — re-litigation requires an explicit corpus revision.**

{chr(10).join(decision_lines)}

For a topic-organized index, see [translator_decisions/README.md](translator_decisions/README.md).

---

## 8. Per-book end-of-book audit summaries

Each completed book gets an end-of-book audit (per `END_OF_BOOK_CHECKLIST.md`) recording: mechanical-gate status, cross-cutting items reviewed, items locked / stable / under-review, and any new translator_decisions docs written.

{chr(10).join(audit_sections)}

---

## 9. How to access the translation

- **Read the full Thai text:** `output/reader/<slug>.md` (one file per book, continuous-reading format with chapter+verse markers and any chapter-footer textual-variant notes).
- **Read the per-verse rationale:** `output/translations/<slug>_NN.json` — each verse has `greek`, `bsb_english`, `translation.thai`, `translation.thai_literal`, `translation.thai_summary` (Thai context summary), `translation.key_decisions` (rationale ledger), `translation.notes` (textual-variant + scholarly notes).
- **Read the per-chapter check report:** `output/check_reports/<slug>_NN_review.md` — automated checks across 8 dimensions.
- **Read the corpus rules:** `RULES.md`.
- **Browse decisions:** `docs/translator_decisions/` (start with `README.md`).
- **Browse end-of-book audits:** `docs/end_of_book/<book>/<BOOK>_END_OF_BOOK_REVIEW_*.md`.

---

## 10. How to give feedback

If you find a passage that you believe is mistranslated, register-inappropriate, or theologically off, please:

1. Identify the verse(s) — book, chapter, verse.
2. Cite the Greek lemma or phrase you're concerned about.
3. State the issue (mistranslation / register / theology / clarity / Thai naturalness).
4. Suggest an alternative if you have one.
5. Cite any source supporting your alternative (a published translation, a lexicon, a commentary).

Submit via:
- GitHub issue on the repo (preferred for trackability), OR
- Direct contact with the maintainer (Ben Van Scyoc — benvanscyoc@gmail.com).

For Thai naturalness feedback specifically, native-speaker corrections are weighted heavily. The maintainer is not a native Thai speaker; the AI-generated draft may carry subtle register or idiom errors that an educated native ear catches.

For theological / editorial feedback, please indicate your tradition (evangelical Protestant / Catholic / Orthodox / academic) so the maintainer can weigh the feedback against the project's evangelical-Protestant editorial frame (§2). The license is CC0 and welcomes use in any tradition; the editorial decisions are not ecumenical and won't be adjusted for tradition-fit.

---

**End of packet.** This packet is regenerable from the repo at any time via `scripts/build_consolidated_reviewer_packet.py`. If something here is out of date relative to the actual repo state, the repo wins — regenerate the packet.
"""


def build_thai(book_codes):
    today = date.today().isoformat()
    book_names = ", ".join(BOOKS[c][1] for c in book_codes)
    decision_docs = list_decision_docs()

    return f"""# คำถามที่พบบ่อยสำหรับผู้อ่านชาวไทย — Eremos Translation
**วันที่จัดทำ: {today}**
**หนังสือที่ครอบคลุม: {book_names}**

> ⚠️ **เอกสารนี้เป็นฉบับร่าง (DRAFT)** — สร้างโดย AI เพื่อเป็นจุดเริ่มต้น คำตอบในเอกสารนี้ต้องผ่านการตรวจสอบและแก้ไขโดยผู้ดูแลโครงการก่อนนำไปเผยแพร่ ผู้ตรวจทานชาวไทยที่ได้รับเอกสารนี้กรุณาช่วยปรับสำนวน ภาษา และเนื้อหาให้เหมาะสมกับผู้อ่านชาวไทย

---

## คำนำ

Eremos Translation เป็นพระคัมภีร์ภาคพันธสัญญาใหม่ภาษาไทย ที่แปลตรงจากภาษากรีกฉบับ SBLGNT (ฉบับวิจารณ์ของ Society of Biblical Literature) เผยแพร่ภายใต้ใบอนุญาต CC0 (ไม่สงวนลิขสิทธิ์ ใครจะนำไปใช้ก็ได้)

โครงการนี้ใช้ AI ช่วยในการแปล แต่ผ่านการตรวจสอบหลายชั้น ทั้งโดยอัตโนมัติและโดยผู้ดูแลโครงการ ปัจจุบันยังต้องการคำติชมจากผู้อ่านชาวไทย โดยเฉพาะในเรื่องความเป็นธรรมชาติของภาษาไทย และการเลือกคำที่เหมาะสมในบริบทของผู้อ่านชาวไทย

เอกสารชุดนี้รวบรวมคำถามที่ผู้อ่านชาวไทยอาจมี เพื่อช่วยให้ผู้ตรวจทานทราบว่าโครงการได้ตัดสินใจอะไรไว้บ้าง และเปิดให้ท้วงติงในจุดที่อาจไม่เหมาะสม

---

## คำถามทั่วไปเกี่ยวกับโครงการ

### ทำไมถึงต้องมีพระคัมภีร์ฉบับใหม่ภาษาไทยอีก?

(ผู้ดูแลโครงการกรุณายืนยันคำตอบ) ฉบับแปลภาษาไทยที่ใช้กันอยู่ในปัจจุบัน (เช่น THSV, NTV, ERV Thai, TNCV) ล้วนสงวนลิขสิทธิ์ ไม่สามารถใช้ในแอปพลิเคชัน, เว็บไซต์ หรือสื่อใดๆ ได้โดยอิสระ Eremos Translation มุ่งสร้างฉบับ CC0 ที่ใครๆ ก็นำไปใช้ได้

### ฉบับนี้แปลจากภาษาอะไร?

แปลตรงจากภาษากรีกต้นฉบับ (SBLGNT) ไม่ได้แปลผ่านภาษาอังกฤษ ใช้ฐานข้อมูลภาษาศาสตร์ MACULA สำหรับการวิเคราะห์รูปคำ และอ้างอิง Berean Standard Bible (BSB) เพียงเป็นการตรวจทาน ไม่ใช่ต้นฉบับในการแปล

### โครงการนี้ใช้ AI แปลทั้งหมดเลยหรือ?

AI สร้างฉบับร่างขั้นต้น แต่ทุกบทผ่านการตรวจสอบอัตโนมัติ 8 ชั้น (ความสม่ำเสมอของศัพท์, การแปลกลับเป็นอังกฤษเปรียบเทียบกับ BSB, การอ้างอิง OT, การอัตลักษณ์ของฟิลด์ภาษากรีก, ฯลฯ) และผู้ดูแลโครงการตรวจทานทุกบท นอกจากนั้นยังมีการตรวจสอบโดย AI ภายนอก (Grok / ChatGPT / Gemini) ในจุดสิ้นสุดของแต่ละเล่ม

### จุดยืนทางเทววิทยาของฉบับนี้คืออะไร?

โครงการนี้เป็น Evangelical Protestant ใช้ฐานต้นฉบับ Alexandrian (SBLGNT, NA28) เช่นเดียวกับ ESV / NIV / NASB / CSB / BSB ใบอนุญาต CC0 ไม่ได้แปลว่าฉบับนี้เป็น "กลางๆ ทางเทววิทยา" — แต่เป็น "ใครก็เอาไปใช้ได้ฟรี" การตัดสินใจในข้อที่มีปัญหาทางพระคัมภีร์ (textual variants) จะตามแนวทาง Evangelical Protestant ที่กระแสหลักใช้

---

## คำถามเกี่ยวกับการเลือกคำสำคัญ

### ทำไมเลือก "คริสตจักร" ไม่ใช่ "ที่ประชุม" สำหรับคำว่า ἐκκλησία?

(ผู้ดูแลโครงการกรุณายืนยันคำตอบ) คำว่า "คริสตจักร" เป็นศัพท์มาตรฐานในภาษาไทยตั้งแต่ยุคมิชชันนารีในศตวรรษที่ 19 ผู้อ่านชาวไทยทุกนิกาย (คาทอลิก เพรสไบทีเรียน เพ็นเทคอสต์ ฯลฯ) เข้าใจคำนี้ว่าหมายถึงอะไร เราคิดว่า "ที่ประชุม" จะทำให้ผู้อ่านสับสน

ข้อยกเว้น: เมื่อ ἐκκλησία หมายถึงการชุมนุมแบบฆราวาส (เช่น ที่กิจการ 19:32, 19:39 — ม็อบในเมืองเอเฟซัส) เราใช้ "ที่ประชุม" หรือ "การชุมนุม" พร้อมหมายเหตุอธิบาย

ดูรายละเอียดเพิ่มเติม: `docs/translator_decisions/ekklesia_2026-04.md`

### ทำไม "องค์พระผู้เป็นเจ้า" ในพระกิตติคุณลูกาและกิจการ ไม่เป็น "พระเยซู"?

(ผู้ดูแลโครงการกรุณายืนยันคำตอบ) ในต้นฉบับภาษากรีก ลูกา (และพระธรรมกิจการ) มีลักษณะพิเศษคือ ผู้บรรยาย (ไม่ใช่ตัวละครในเรื่อง) เรียกพระเยซูว่า "องค์พระผู้เป็นเจ้า" (ὁ κύριος) ในรูปบุคคลที่สาม มาระโกและมัทธิวไม่ทำเช่นนี้ การแปลของเรารักษาลักษณะพิเศษนี้ไว้ เพราะมันเป็นเครื่องหมายทางเทววิทยาของลูกา-กิจการ

### ทำไม "อาณาจักรของพระเจ้า" ในมาระโก/ลูกา/กิจการ แต่ "อาณาจักรสวรรค์" ในมัทธิว?

(ผู้ดูแลโครงการกรุณายืนยันคำตอบ) เพราะภาษากรีกเขียนแตกต่างกัน มัทธิวใช้ βασιλεία τῶν οὐρανῶν (อาณาจักรของฟ้าสวรรค์) เป็นการอ้อมเพื่อเลี่ยงการเอ่ยพระนามพระเจ้า — เป็นลักษณะเฉพาะของมัทธิว ส่วนมาระโก ลูกา และกิจการใช้ βασιλεία τοῦ θεοῦ (อาณาจักรของพระเจ้า) ตรงๆ การแปลของเรารักษาความแตกต่างนี้ไว้แทนที่จะรวมเป็นรูปเดียวกันทั้งหมด

### ทำไม μετανοέω กับ μεταμέλομαι แปลต่างกัน?

(ผู้ดูแลโครงการกรุณายืนยันคำตอบ) สองคำนี้มีความหมายต่างกันในภาษากรีก:
- μετανοέω = "กลับใจ" — มีนัยถึงการเปลี่ยนแปลงในใจที่นำไปสู่ความรอด (เช่น คำเทศน์ของยอห์นผู้ให้รับบัพติศมา)
- μεταμέลομαι = "เปลี่ยนใจ" — เพียงเปลี่ยนความคิดเห็น ไม่จำเป็นต้องเกี่ยวกับความรอด (เช่น ยูดาสที่เสียใจหลังทรยศ)

ใน 2 โครินธ์ 7:10 เปาโลใช้ทั้งสองคำในข้อเดียว และแยกแยะอย่างชัดเจน ฉบับแปลของเรารักษาความแตกต่างนี้ไว้เพื่อไม่ให้ความหมายที่เปาโลตั้งใจหายไป

---

## คำถามเกี่ยวกับการใช้คำราชาศัพท์

### เมื่อไหร่ใช้ราชาศัพท์ (ทรง, เสด็จ, ตรัส, พระ-)?

(ผู้ดูแลโครงการกรุณายืนยันคำตอบ) ราชาศัพท์ใช้กับพระเจ้า, พระเยซู, และพระวิญญาณบริสุทธิ์ เสมอ — ทั้งในคำบรรยายของผู้บันทึก และเมื่อมนุษย์พูดกับพระองค์

ไม่ใช้ราชาศัพท์กับ:
- กษัตริย์เฮโรด, ปีลาท, ผู้ว่าราชการเฟลิกซ์, เฟสทัส, นายร้อย, มหาปุโรหิต — ใช้ภาษาธรรมดา
- ตัวละครในอุปมา (พ่อ, กษัตริย์, นายชาย) ที่เป็นภาพแทนพระเจ้า — ใช้ภาษามนุษย์ปกติ ไม่ใช้ราชาศัพท์
- ปีศาจ, มาร, ฝ่ายปฏิปักษ์ — ใช้ภาษาห่างเหิน ไม่ใช้คำสุภาพ
- เทพเจ้าของพวกนอกรีต (Zeus, Artemis ฯลฯ) — ใช้ "เทพ", "เทพี", "เทพเจ้า" ไม่ใช้ "พระเจ้า" ที่สงวนไว้สำหรับพระเจ้าของพระคัมภีร์

### มัทธิว 25:31-46 (พระบุตรมนุษย์เสด็จมา) ใช้ราชาศัพท์ใช่หรือไม่?

(ผู้ดูแลโครงการกรุณายืนยันคำตอบ) ใช่ เพราะข้อ 25:31 อ้างถึงพระบุตรมนุษย์ในการเสด็จมาในศักดิ์ศรี — เป็นการกล่าวตรงๆ ถึงพระเยซู ไม่ใช่ตัวละครในอุปมา ส่วนตัวละครในอุปมาอื่นๆ (เช่น ในมัทธิว 18:23-35, 20:1-16) ใช้ภาษามนุษย์ปกติ

---

## คำถามเกี่ยวกับการใช้และเข้าถึง

### ฉันจะอ่านได้ที่ไหน?

อ่านได้ที่:
- ไฟล์ `output/reader/<ชื่อหนังสือ>.md` — ฉบับเต็มภาษาไทย จัดรูปแบบสำหรับการอ่านต่อเนื่อง (เช่น `output/reader/luke.md`)
- บนเว็บที่ {{the maintainer's app URL}} (ผู้ดูแลโครงการกรุณาเติม)

### ฉันสามารถนำไปใช้ในแอปของฉัน / โบสถ์ของฉัน / หนังสือของฉัน ได้หรือไม่?

ได้ ใบอนุญาต CC0 หมายความว่าใครก็ใช้ได้ ทำสำเนาได้ ดัดแปลงได้ และจำหน่ายได้ ไม่ต้องขออนุญาต ไม่ต้องจ่ายค่าธรรมเนียม ไม่ต้องระบุที่มา (แต่การอ้างอิงที่มาก็จะดีต่อชุมชน)

### ถ้าพบข้อผิดพลาดล่ะ?

กรุณาแจ้งทาง:
- GitHub issue บนคลังโค้ดของโครงการ (วิธีที่แนะนำ — ติดตามได้)
- ส่งอีเมลถึงผู้ดูแลโครงการที่ benvanscyoc@gmail.com

ระบุ: หนังสือ บท ข้อ คำกรีกที่กังวล ปัญหาที่พบ และข้อเสนอแนะ (ถ้ามี)

---

## คำถามทางเทววิทยา

### ฉบับนี้เปลี่ยนคำแปลตามนิกายของคนที่ใช้หรือไม่?

(ผู้ดูแลโครงการกรุณายืนยันคำตอบ) ไม่ การตัดสินใจในข้อที่มีปัญหาทางพระคัมภีร์ตามแนวทาง Evangelical Protestant กระแสหลัก ใบอนุญาต CC0 หมายความว่าใครก็ใช้ได้ แต่การตัดสินใจในการแปลไม่ปรับเปลี่ยนเพื่อให้ถูกใจกับนิกายอื่นๆ การตัดสินใจในข้อที่ขัดแย้งกัน (เช่น มาระโก 16:9-20) จะตามที่ ESV / NIV / NASB / CSB / BSB ทำ

### ทำไมบางข้อมีวงเล็บ [...] หรือ ⟦...⟧?

(ผู้ดูแลโครงการกรุณายืนยันคำตอบ) วงเล็บทั้งสองแบบบ่งชี้ข้อความที่อยู่ในต้นฉบับบางสาย แต่ไม่อยู่ในสายอื่น:
- `[...]` หมายถึง วลีสั้นๆ ที่ต้นฉบับฝ่าย Alexandrian (SBLGNT/NA28) ละไว้ แต่ฝ่าย Byzantine (เสียงข้างมาก/TR) มีอยู่ — เราใส่วลีนั้นในวงเล็บเพื่อรักษาความเป็นธรรมต่อผู้อ่านที่คุ้นเคยกับข้อความฉบับเก่า
- `⟦...⟧` หมายถึง ส่วนข้อความขนาดใหญ่ที่ทั้งสองฝ่ายโต้เถียงกัน (เช่น มาระโก 16:9-20, ยอห์น 7:53-8:11)
- ข้อที่ตกหายทั้งข้อ จะปรากฏเป็นหมายเหตุท้ายบท ไม่อยู่ในเนื้อหาหลัก

วิธีนี้เหมือนที่ ESV / NIV / NASB / CSB / BSB ใช้ ดูรายละเอียด: `docs/translator_decisions/inclusion_variants_absent_verses_2026-04.md`

---

## รายการการตัดสินใจทั้งหมด

ลิงก์ไปยังเอกสารทุกการตัดสินใจระดับองค์กร (ภาษาอังกฤษทั้งหมด):

{chr(10).join(f'- [{title}](translator_decisions/{fname})' for fname, title, _ in decision_docs)}

ดูสารบัญแบบจัดหมวดหมู่: [translator_decisions/README.md](translator_decisions/README.md)

---

**เอกสารนี้สร้างจาก:** `scripts/build_consolidated_reviewer_packet.py --lang th`
**สร้างใหม่ได้ทุกเมื่อ** หากเนื้อหาในเอกสารนี้ขัดแย้งกับสถานะปัจจุบันของคลังโค้ด ให้ถือว่าคลังโค้ดถูกต้อง — ให้สร้างเอกสารใหม่
"""


def main():
    parser = argparse.ArgumentParser(
        description="Build a consolidated multi-book reviewer packet."
    )
    parser.add_argument("books", nargs="+", help="3-letter book codes")
    parser.add_argument(
        "--lang",
        required=True,
        choices=["en", "th"],
        help="output language (en = English scholarly packet; th = Thai believer FAQ stub)",
    )
    parser.add_argument("--out", help="output path")
    args = parser.parse_args()

    book_codes = [b.upper() for b in args.books]
    for code in book_codes:
        if code not in BOOKS:
            sys.exit(f"Unknown book code: {code}. Known: {sorted(BOOKS)}")

    if args.lang == "en":
        text = build_english(book_codes)
    else:
        text = build_thai(book_codes)

    if args.out:
        out_path = Path(args.out)
    else:
        out_path = DOCS / f"reviewer_packet_{args.lang}_{date.today().isoformat()}.md"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text)

    char_count = len(text)
    line_count = text.count("\n") + 1
    print(f"Wrote {out_path}")
    print(f"  {char_count:,} chars / {line_count:,} lines / lang={args.lang}")
    if args.lang == "th":
        print(f"  ⚠️  DRAFT — needs maintainer's editorial pass before sharing.")


if __name__ == "__main__":
    main()
