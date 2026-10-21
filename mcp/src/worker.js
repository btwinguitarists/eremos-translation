// Eremos Translation MCP server: lets AI assistants quote the Thai text word for word.
//
// Remote MCP over Streamable HTTP, stateless (no sessions, no streaming): each POST to
// /mcp carries one JSON-RPC message or a batch and gets a JSON reply. Text comes from the
// static verse API on bible.eremosapp.com (cached at the edge); search loads the
// whole-Bible JSON once per isolate. No dependencies.
import { BOOKS, ALIAS } from "./books.js";

const SITE = "https://bible.eremosapp.com";
const RAW = "https://raw.githubusercontent.com/btwinguitarists/eremos-translation/main/output/translations";
const PROTOCOL_VERSIONS = ["2025-06-18", "2025-03-26", "2024-11-05"];
const SERVER_INFO = { name: "eremos-bible", title: "Eremos Thai Bible", version: "1.0.0" };
const BY_CODE = Object.fromEntries(BOOKS.map((b) => [b.usfm, b]));
const NOTICE =
  "Eremos Translation (Thai), CC0 public domain: quote word for word, no permission needed. " +
  "A complete draft translated from the Hebrew and Greek with AI, machine-checked; Thai review is beginning.";

const INSTRUCTIONS =
  "Use these tools when a user wants Thai Bible text. Quote the returned Thai exactly; do not " +
  "paraphrase it and present the result as Scripture. Name the source as the Eremos Translation " +
  "and mention it is a draft under review. Verse numbers follow English (BSB) numbering.";

const TOOLS = [
  {
    name: "get_passage",
    title: "Get a Thai Bible passage",
    description:
      "Return the Eremos Translation (Thai) text of a Bible reference, word for word, with verse numbers and a link. " +
      "Accepts English or Thai book names, abbreviations or USFM codes: 'John 3:16', 'Jn 3:16-18', 'Psalm 23', " +
      "'1 Cor 13:4-7', 'ยอห์น 3:16', 'JHN 3'. One chapter or a verse range within one chapter.",
    inputSchema: {
      type: "object",
      properties: { reference: { type: "string", description: "A Bible reference, e.g. 'John 3:16' or 'สดุดี 23'" } },
      required: ["reference"],
    },
    annotations: { readOnlyHint: true, openWorldHint: false },
  },
  {
    name: "search_text",
    title: "Search the Thai text",
    description:
      "Find verses in the Eremos Translation whose Thai text contains the given words (all words must appear). " +
      "Optionally limit to one book. Returns up to `limit` verses with references.",
    inputSchema: {
      type: "object",
      properties: {
        query: { type: "string", description: "Thai words or phrase, e.g. 'ความรักมั่นคง'" },
        book: { type: "string", description: "Optional book name or code to search within" },
        limit: { type: "integer", minimum: 1, maximum: 50, default: 15 },
      },
      required: ["query"],
    },
    annotations: { readOnlyHint: true, openWorldHint: false },
  },
  {
    name: "get_translation_notes",
    title: "Why a verse was translated this way",
    description:
      "Return the published decision record for one verse: the Hebrew or Greek words, the Thai chosen, and the " +
      "translator's reason, plus any notes. Useful when a user asks why the Thai reads as it does.",
    inputSchema: {
      type: "object",
      properties: { reference: { type: "string", description: "A single verse, e.g. 'Mark 1:35'" } },
      required: ["reference"],
    },
    annotations: { readOnlyHint: true, openWorldHint: false },
  },
  {
    name: "list_books",
    title: "List the books",
    description: "List all 66 books with English and Thai names, USFM codes and chapter counts.",
    inputSchema: { type: "object", properties: {} },
    annotations: { readOnlyHint: true, openWorldHint: false },
  },
];

// ---------- references ----------

function findBook(name) {
  const key = String(name || "").toLowerCase().replace(/[\s.]+/g, "");
  return ALIAS[key] ? BY_CODE[ALIAS[key]] : null;
}

// "John 3:16-18", "ยอห์น 3:16", "1 Cor 13", "Ps 23:1-3", "JHN 3:16–4:2" is NOT supported (one chapter only).
function parseReference(ref) {
  const s = String(ref || "").trim().replace(/[–—]/g, "-");
  const m = s.match(/^(.+?)\s*(\d+)(?:\s*:\s*(\d+)(?:\s*-\s*(\d+))?)?\s*$/);
  if (!m) return { error: `Couldn't read "${ref}". Try a form like "John 3:16" or "ยอห์น 3".` };
  const book = findBook(m[1]);
  if (!book) return { error: `Unknown book "${m[1].trim()}". Call list_books for names.` };
  const chapter = Number(m[2]);
  if (chapter < 1 || chapter > book.chapters) return { error: `${book.name_en} has ${book.chapters} chapters.` };
  const from = m[3] ? Number(m[3]) : null;
  const to = m[4] ? Number(m[4]) : from;
  if (from && to < from) return { error: "The verse range runs backwards." };
  return { book, chapter, from, to };
}

// ---------- data ----------

async function cachedJson(url, ctx, ttl = 3600) {
  const cache = caches.default;
  const req = new Request(url);
  let res = await cache.match(req);
  if (!res) {
    const fresh = await fetch(url, { cf: { cacheTtl: ttl } });
    if (!fresh.ok) throw new Error(`fetch ${url}: ${fresh.status}`);
    res = new Response(fresh.body, fresh);
    res.headers.set("Cache-Control", `public, max-age=${ttl}`);
    ctx.waitUntil(cache.put(req, res.clone()));
  }
  return res.json();
}

const chapterJson = (code, ch, ctx) => cachedJson(`${SITE}/api/v1/${code}/${ch}.json`, ctx);

let BUNDLE = null; // whole Bible, loaded on first search in this isolate
async function bundle(ctx) {
  if (!BUNDLE) BUNDLE = await cachedJson(`${SITE}/data/eremos-thai.json`, ctx, 21600);
  return BUNDLE;
}

// ---------- tools ----------

const text = (t, isError = false) => ({ content: [{ type: "text", text: t }], ...(isError ? { isError: true } : {}) });

async function getPassage({ reference }, ctx) {
  const r = parseReference(reference);
  if (r.error) return text(r.error, true);
  const ch = await chapterJson(r.book.usfm, r.chapter, ctx);
  const verses = ch.verses.filter((v) => {
    const n = Number(String(v.verse).split("-")[0]);
    return !r.from || (n >= r.from && n <= r.to);
  });
  if (!verses.length) return text(`${r.book.name_en} ${r.chapter} has no verse ${r.from}.`, true);
  const label = `${r.book.name_th} ${r.chapter}${r.from ? `:${r.from}${r.to !== r.from ? `-${r.to}` : ""}` : ""}`;
  const labelEn = `${r.book.name_en} ${r.chapter}${r.from ? `:${r.from}${r.to !== r.from ? `-${r.to}` : ""}` : ""}`;
  const lines = [];
  if (!r.from && ch.title) lines.push(`(${ch.title})`);
  for (const v of verses) lines.push(`${v.verse} ${v.text}`);
  const link = `${SITE}/th/${r.book.slug}/${r.chapter}.html${r.from ? `#v${r.from}` : ""}`;
  return text(`${label} (${labelEn}), Eremos Translation\n\n${lines.join("\n")}\n\n${link}\n${NOTICE}`);
}

async function searchText({ query, book, limit = 15 }, ctx) {
  const words = String(query || "").split(/\s+/).filter(Boolean);
  if (!words.length) return text("Give some Thai words to search for.", true);
  let only = null;
  if (book) {
    only = findBook(book);
    if (!only) return text(`Unknown book "${book}". Call list_books for names.`, true);
  }
  const max = Math.min(Math.max(Number(limit) || 15, 1), 50);
  const b = await bundle(ctx);
  const hits = [];
  let total = 0;
  for (const bk of b.books) {
    if (only && bk.usfm !== only.usfm) continue;
    for (const c of bk.chapters) {
      for (const v of c.verses) {
        if (words.every((w) => v.text.includes(w))) {
          total++;
          if (hits.length < max) hits.push(`${bk.name_th} ${c.chapter}:${v.verse} (${bk.name_en}) ${v.text}`);
        }
      }
    }
  }
  if (!total) return text(`No verses contain: ${words.join(" ")}`);
  return text(`${total} verse(s) contain "${words.join(" ")}"${total > hits.length ? `; first ${hits.length}` : ""}:\n\n${hits.join("\n\n")}\n\n${NOTICE}`);
}

async function getNotes({ reference }, ctx) {
  const r = parseReference(reference);
  if (r.error) return text(r.error, true);
  if (!r.from || r.to !== r.from) return text("Give one verse, e.g. 'Mark 1:35'.", true);
  // Decision records live in per-chapter source files in Hebrew/Greek (MT) numbering.
  // Look in the same chapter number and its neighbours for the verse whose English
  // reference matches; most books share numbering, so it is usually the same verse.
  const want = `${r.book.name_en} ${r.chapter}:${r.from}`.toLowerCase();
  for (const c of [r.chapter, r.chapter + 1, r.chapter - 1]) {
    if (c < 1) continue;
    let rows;
    try {
      rows = await cachedJson(`${RAW}/${r.book.slug}_${String(c).padStart(2, "0")}.json`, ctx);
    } catch {
      continue;
    }
    const v = rows.find((x) => {
      const eng = x.versification?.english_ref;
      if (eng) return eng.toLowerCase().replace(/^psalm /, "psalms ") === want.replace(/^psalm /, "psalms ");
      return c === r.chapter && x.verse === r.from;
    });
    if (!v) continue;
    const t = v.translation || {};
    const out = [`${r.book.name_th} ${r.chapter}:${r.from} (${r.book.name_en}), Eremos Translation`, "", t.thai || ""];
    const src = v.greek || v.hebrew;
    if (src) out.push("", `Source text: ${typeof src === "string" ? src : JSON.stringify(src)}`);
    if (t.key_decisions?.length) {
      out.push("", "Translation decisions:");
      for (const d of t.key_decisions) {
        out.push(`- ${d.greek || d.hebrew || d.source || ""} → ${d.thai || ""}: ${d.rationale || ""}`);
      }
    }
    if (t.notes) out.push("", `Notes: ${t.notes}`);
    out.push("", `Record: https://github.com/btwinguitarists/eremos-translation/blob/main/output/translations/${r.book.slug}_${String(c).padStart(2, "0")}.json`);
    return text(out.join("\n"));
  }
  return text(`No decision record found for ${r.book.name_en} ${r.chapter}:${r.from}.`, true);
}

function listBooks() {
  return text(BOOKS.map((b) => `${b.usfm}  ${b.name_en} · ${b.name_th} (${b.chapters} chapters)`).join("\n"));
}

const HANDLERS = { get_passage: getPassage, search_text: searchText, get_translation_notes: getNotes, list_books: listBooks };

// ---------- JSON-RPC / MCP ----------

async function handleMessage(msg, ctx) {
  const { id, method, params } = msg || {};
  const isNotification = id === undefined || id === null;
  const ok = (result) => ({ jsonrpc: "2.0", id, result });
  const err = (code, message) => ({ jsonrpc: "2.0", id: id ?? null, error: { code, message } });
  if (!msg || msg.jsonrpc !== "2.0" || typeof method !== "string") return err(-32600, "Invalid Request");
  if (isNotification) return null; // notifications/initialized and friends need no reply
  try {
    switch (method) {
      case "initialize": {
        const asked = params?.protocolVersion;
        return ok({
          protocolVersion: PROTOCOL_VERSIONS.includes(asked) ? asked : PROTOCOL_VERSIONS[0],
          capabilities: { tools: { listChanged: false } },
          serverInfo: SERVER_INFO,
          instructions: INSTRUCTIONS,
        });
      }
      case "ping":
        return ok({});
      case "tools/list":
        return ok({ tools: TOOLS });
      case "tools/call": {
        const fn = HANDLERS[params?.name];
        if (!fn) return err(-32602, `Unknown tool: ${params?.name}`);
        return ok(await fn(params.arguments || {}, ctx));
      }
      default:
        return err(-32601, `Method not found: ${method}`);
    }
  } catch (e) {
    return ok(text(`Something went wrong: ${e.message}`, true));
  }
}

const CORS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type, Accept, Mcp-Session-Id, Mcp-Protocol-Version, Authorization",
};

const ABOUT = `Eremos Thai Bible MCP server

Connect an AI assistant to https://mcp.eremosapp.com/mcp (Streamable HTTP, no sign-in)
so it can quote the Eremos Translation (Thai) word for word.

Tools: get_passage, search_text, get_translation_notes, list_books.
Text: CC0 public domain. A complete draft, translated from the Hebrew and Greek with AI;
Thai review is beginning. More: ${SITE}/llms.txt
Source: https://github.com/btwinguitarists/eremos-translation/tree/main/mcp
`;

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    if (request.method === "OPTIONS") return new Response(null, { status: 204, headers: CORS });
    if (url.pathname === "/" || url.pathname === "/llms.txt") {
      return new Response(ABOUT, { headers: { "Content-Type": "text/plain; charset=utf-8", ...CORS } });
    }
    if (url.pathname !== "/mcp") return new Response("Not found", { status: 404, headers: CORS });
    if (request.method === "GET") {
      // No server-initiated stream: this server only answers requests.
      return new Response("Method Not Allowed", { status: 405, headers: { Allow: "POST", ...CORS } });
    }
    if (request.method === "DELETE") return new Response(null, { status: 405, headers: CORS });
    if (request.method !== "POST") return new Response("Method Not Allowed", { status: 405, headers: CORS });

    let body;
    try {
      body = await request.json();
    } catch {
      return Response.json({ jsonrpc: "2.0", id: null, error: { code: -32700, message: "Parse error" } }, { status: 400, headers: CORS });
    }
    const batch = Array.isArray(body);
    const replies = (await Promise.all((batch ? body : [body]).map((m) => handleMessage(m, ctx)))).filter(Boolean);
    if (!replies.length) return new Response(null, { status: 202, headers: CORS });
    return Response.json(batch ? replies : replies[0], { headers: CORS });
  },
};
