# Directory submission packet

Prepared October 31, 2026. This packet is not evidence of submission or approval.

## Shared public listing copy

- **Name:** Eremos Thai Bible
- **One-liner:** Retrieve exact Thai Bible passages, search the published text, and explore translation notes. Read-only, no sign-in; AI-assisted draft under review.
- **Description:** Eremos Thai Bible connects assistants to the published Eremos Translation (Thai), a complete AI-assisted draft under review released under CC0. Retrieve a passage with verse numbers and a source link, search Thai words, list the 66 books, or inspect published translation decisions for a verse. Quoted text should preserve the returned wording and identify the translation and draft status. Commentary and paraphrases should remain separate. The service reads public translation data; it does not edit Scripture, access private accounts, or submit review feedback.
- **Endpoint:** https://mcp.eremosapp.com/mcp
- **Transport:** Streamable HTTP
- **Authentication:** None; no test credentials are needed to retrieve this public data.
- **Website / documentation:** https://bible.eremosapp.com/ai/
- **Support URL:** https://github.com/btwinguitarists/eremos-translation/issues
- **Repository:** https://github.com/btwinguitarists/eremos-translation
- **Icon:** `mcp/plugin/assets/icon.png` (original book glyph).
- **Read / write:** Read only; all four live tools provide titles and `readOnlyHint: true`.
- **Primary use cases:** Exact Thai passage quotation; Thai text lookup; inspecting published translation rationale.
- **Requirements:** A client supporting remote MCP and permission to add a custom connector. No Eremos subscription or account.

## Reviewer test inputs

| Tool | Arguments | Expected result |
| --- | --- | --- |
| `get_passage` | `{"reference":"John 3:16-18"}` | Three numbered Thai verses, draft disclosure, reader source link |
| `search_text` | `{"query":"ความรัก","limit":5}` | At most five matching Thai verses |
| `get_translation_notes` | `{"reference":"John 3:16"}` | Published notes, separate from Scripture |
| `list_books` | `{}` | 66 books with names and chapter counts |
| `get_passage` | `{"reference":"John 999:1"}` | Actionable invalid-chapter error |

Model prompt: “Use Eremos Thai Bible to retrieve John 3:16–18. Quote the returned Thai exactly, name the translation, include the source link, and mention its draft-under-review status.” Compare to https://bible.eremosapp.com/th/john/3.html#v16.

Do not attest to installed-client testing based only on protocol tests. No personal AI account was configured as part of this publication task.

## OpenAI

Portal: https://platform.openai.com/plugins . Use the `-openai.zip` build, which includes the documented no-auth extension; see [schema compatibility note](PACKAGE.md).

Required before public review: verified publisher identity, accurate privacy policy and terms URLs, and any required review materials. Do not substitute the discipleship app's policies without confirming they cover this public MCP service. The package includes the public website, support URL, and icon, but does not invent legal URLs or publisher/contact information.

Official references: [submission](https://developers.openai.com/plugins/deploy/submission), [package format](https://developers.openai.com/plugins/build/plugins).

## Claude

Portal: https://claude.ai/directory/manage . Choose **MCP connector**. The inspected portal displayed zero existing submissions. Its Connection step requires **Add custom connector** and says that the connector remains in Settings → Connectors. That step was not taken because this task excludes installing in the owner's personal AI accounts.

Have the publisher/company identity, review contact, support contact, privacy URL, and chosen categories confirmed before filling them. Use the public listing copy above. Do not invent an account or credentials for this unauthenticated service.

The final flow includes directory terms and seven compliance acknowledgments. Those representations require an informed publisher decision; no agreements or attestations have been accepted here.

Official references: [submission](https://claude.com/docs/connectors/building/submission), [review criteria](https://claude.com/docs/connectors/building/review-criteria).

## Existing registry entries

The official MCP Registry already lists `com.eremosapp/bible` version `1.0.0`; MCPRush also lists the service. This publication does not create duplicate entries or change the server version.
