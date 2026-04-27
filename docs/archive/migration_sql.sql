-- Eremos Translation: additive migration
-- Safe to run against production. Adds 2 new tables, modifies nothing.
-- Zero risk to existing user data.

CREATE TABLE IF NOT EXISTS "eremos_translation_verses" (
    "id" serial PRIMARY KEY NOT NULL,
    "book" varchar NOT NULL,
    "chapter" integer NOT NULL,
    "verse" integer NOT NULL,
    "thai" text NOT NULL,
    "thai_literal" text,
    "key_decisions" jsonb,
    "notes" text
);

CREATE INDEX IF NOT EXISTS "idx_eremos_translation_book_chapter"
    ON "eremos_translation_verses" ("book", "chapter");

CREATE TABLE IF NOT EXISTS "translation_feedback" (
    "id" serial PRIMARY KEY NOT NULL,
    "user_id" varchar NOT NULL,
    "book" varchar NOT NULL,
    "chapter" integer NOT NULL,
    "verse" integer NOT NULL,
    "message" text,
    "created_at" timestamp DEFAULT now()
);

CREATE INDEX IF NOT EXISTS "idx_translation_feedback_created"
    ON "translation_feedback" ("created_at");
