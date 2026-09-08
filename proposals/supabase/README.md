# Supabase client-selector proposal — authentication untested

Prepared against Supabase commit 3418975b701a6e7a08ae340b17421b36a796c4e2 on 2026-09-08 UTC.

The [two-file draft](proposed-docs.patch) adds FLUJO to Web Clients in McpUrlBuilder/clients.data.ts and supplies one shared mdast instruction tree in clients.instructions.md.tsx. It uses the generated URL verbatim, preserving project_ref, read_only and features. No configuration-file format or one-click installer is invented.

The drafting worker passed repository-configured Prettier, patch applicability and isolated React/Markdown checks. The real adapters and instruction tree were used; UI, code-block and image components were stubbed. This was not a monorepo build/typecheck or browser/CSS test. The final draft corrects the button wording to "Save and authenticate", verified in FLUJO's rendered UI.

Hosted Supabase OAuth, authenticated tool discovery and a bounded read-only development-project call remain untested. This is a reviewable proposal, not validation evidence or a supported-client claim.

Upstream CONTRIBUTING requests a Discussion before feature PRs. The proposed next step is maintainer scope review, then a recorded OAuth connection and harmless read against an authorized development project before any PR.
