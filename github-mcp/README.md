# GitHub MCP with FLUJO

Validated 2026-09-08 UTC with FLUJO 3.45.2 and Node.js 22.22.0 on an isolated Debian cloud machine. The public npm runtime was reused with fresh FLUJO data and browser profile.

## Authentication scope

This test supplied an existing, user-authorized GitHub CLI OAuth access token as a secret Authorization Bearer header. It did not exercise FLUJO's interactive OAuth flow, client registration, or PAT creation. It must not be cited as a PAT-specific test.

Only GitHub's hosted repository read-only toolset was used: https://api.githubcopilot.com/mcp/x/repos/readonly. The secret was masked in FLUJO and was never included in screenshots, published files or command output.

## Actual UI workflow

1. Connected Apps > Connect App > I have connection details > At a remote URL; enter the read-only endpoint and Connect.
2. Continue to setup. The automatic unauthenticated test correctly requested authentication.
3. Under Custom HTTP headers, Add header, enter Authorization, enable Secret, then enter the Bearer value.
4. Run 3) Test run again. The handshake passed and discovered 13 tools. Update server saved the connection.
5. Open Tools and choose get_file_contents. Set owner=flujo-app, repo=flujo-mcp-client-validation and path=fastmcp/server.py, then Test tool.

The tool returned the exact public fixture text and file SHA 001aeee5bc27d6f0bd225cf15e1adc4a9b02510d. No repository mutation or private content was requested.

Unedited screenshots: [handshake](connection.jpg), [tool inputs](file-inputs.jpg), [returned file](file-result.jpg). FLUJO's periodic tool-list refresh briefly clears the picker while retaining the result; that real UI state is visible in the result screenshot.

This verifies one authenticated remote read. Local transport, interactive OAuth, PAT-specific behavior, other toolsets and write operations remain untested.

[Guide PR #3248](https://github.com/github/github-mcp-server/pull/3248), following [scenario issue #3247](https://github.com/github/github-mcp-server/issues/3247).


## Repository validation

All requested checks passed on PR head f3a794f727637086939f1e3742c5f3b3c1201eb8 in an isolated Debian cloud machine with Go 1.25.12:

- go test -v ./...
- script/test, which runs go test -race ./... (CGO_ENABLED=1)
- script/lint, including pinned golangci-lint 2.9.0: zero issues
- UPDATE_TOOLSNAPS=true go test ./...
- script/generate-docs: no generated Markdown changes
- git diff --check

The snapshot-update command removed only a final newline from an existing unrelated tool snapshot. That formatting change was restored; final git status is clean. The PR contains only its 31 Markdown insertions.
