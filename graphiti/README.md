# Graphiti with FLUJO

Validated 2026-09-08 UTC using FLUJO 3.45.2 with a fresh data directory and browser profile on an isolated Debian cloud machine. The previously installed public FLUJO runtime was reused.

Graphiti commit b943c9e8486cdc7fe6cb2f4cfe151ae53f0a884d; graphiti-core 0.30.1; Python MCP SDK 1.27.2; Python 3.10.21; Node.js 24.20.0; Chromium 152.0.7977.82. Graphiti dependencies installed with uv sync --frozen --no-dev.

## Actual validation

1. Start Graphiti's HTTP MCP server with an isolated FalkorDB database.
2. In FLUJO, select Connected Apps > Connect App > I have connection details > At a remote URL.
3. Enter http://127.0.0.1:8000/mcp/ (both applications run on the same cloud machine), then Connect.
4. The handshake passed and discovered 13 tools. Update server saved the connection.
5. In Tools, get_status returned status=ok and confirmed connection to FalkorDB.
6. get_episodes with group_ids=flujo-listing-test returned the exact harmless seeded episode.

Unedited screenshots: [connection](connection.png), [database status](status.png), [episode retrieval](episodes.png).

## Fixture and limits

The real local database used falkordb/falkordb@sha256:adbddd418916c25618564ff8597a919b08bc76452ebeb74eb985c38d7281df62, with Redis on loopback and persistence disabled. [seed-fixture.py](seed-fixture.py) saved a disposable episode directly through Graphiti core.

The server's model API URL pointed to a local endpoint returning 503 for every request, with a non-secret placeholder key. That endpoint received zero requests through startup and both tool calls.

This validates HTTP connectivity, database health and raw episode retrieval. Memory ingestion, embeddings, semantic search, OAuth, other transports and database providers remain untested. No paid model service was used.

The [13-line documentation proposal](proposed-docs.patch) passed git diff --check. Upstream requires an RFC before a new integration PR; no maintainer approval is assumed.
