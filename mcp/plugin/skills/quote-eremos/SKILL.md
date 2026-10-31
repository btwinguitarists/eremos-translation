---
name: quote-eremos
description: Retrieve exact Eremos Thai Bible passages, search the published Thai draft, or explain its published translation decisions when the user requests Eremos or Thai Bible text.
---

Use the connected Eremos Bible MCP tools for the requested passage or search.

- `get_passage`: one chapter or a verse range within one chapter; English or Thai book names and USFM codes are accepted. Split cross-chapter requests into separate calls.
- `search_text`: Thai words, with an optional book and result limit. This is text matching, not a semantic concordance.
- `get_translation_notes`: the published decisions for one verse. Keep these notes separate from Scripture and from your own interpretation.
- `list_books`: available books, names, codes, and chapter counts.

Quote returned Thai word for word, preserving verse numbers and punctuation. Identify it as the Eremos Translation (Thai), CC0 public domain, and disclose that it is a complete AI-assisted draft under review. Include the returned source link. Attribution identifies the text; CC0 does not make attribution a licensing condition. Numbering follows English/BSB versification.

Label any requested explanation or paraphrase separately. Never invent a passage or decision note, silently substitute another translation, or present generated Thai as retrieved Scripture. If the connector fails, explain the failure and offer the public reader at https://bible.eremosapp.com. Retrieval is not proof of an interpretation or of completed human review.

These tools only read public translation data. They cannot edit verses, access private accounts, or submit review feedback. Follow the user's requested translation if it differs from Eremos.
