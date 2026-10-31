# Portable plugin package

Source: `mcp/plugin/`. Build from the repository root:

```sh
python3 scripts/build_mcp_plugin.py
```

Output: `mcp/dist/eremos-thai-bible-1.0.0.zip` an OpenAI-specific `eremos-thai-bible-1.0.0-openai.zip`, and `SHA256SUMS`. The site build publishes the same ZIPs under `/ai/`.

The archive has `plugin.json`, `mcp.json`, and `skills/` at its root. It contains no executable hooks, credentials, or private data. `mcp.json` declares Streamable HTTP without credentials; presentation metadata declares Read capability. The OpenAI ZIP additionally declares `extensions.com.openai.auth.type: none` on the MCP server. Tool-level read-only hints come from the hosted server, not a fabricated manifest permission field.

The portable ZIP validates against the official [plugin](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json) and [MCP](https://agent-plugins.org/schemas/1.0.0/mcp.schema.json) schemas. This checks portable structure, not directory acceptance or installed-client behavior. See [OpenAI packaging documentation](https://developers.openai.com/plugins/build/plugins).

To use with a supported local Codex marketplace, extract the archive into a plugin folder and point a marketplace entry at it. Merge into an existing marketplace rather than replacing its other entries. No local installation is necessary to use the hosted URL directly in a compatible client.

## Schema compatibility note (October 31, 2026)

OpenAI documents the per-server `extensions.com.openai.auth` object, but the published Agent Plugins 1.0.0 MCP schema currently rejects all per-server extension fields. Therefore the default ZIP follows that schema exactly; the `-openai.zip` adds the documented host extension. Its portable core is schema-validated after removing only that extension, and the extension is checked explicitly. Do not describe the extended file as passing the unmodified portable schema. OpenAI portal acceptance and end-to-end installed-client behavior remain to be verified.

The public directory submission still needs verified publisher identity and accurate publisher-approved privacy/terms URLs. Those are intentionally not invented in the package.
