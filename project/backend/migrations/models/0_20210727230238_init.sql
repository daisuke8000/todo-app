-- upgrade --
CREATE TABLE IF NOT EXISTS "todosummary" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "todo" VARCHAR(10) NOT NULL,
    "limit" DATE NOT NULL,
    "summary" TEXT NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(20) NOT NULL,
    "content" JSONB NOT NULL
);
