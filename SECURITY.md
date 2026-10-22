# Security Policy

## Scope

bo6-external is a research tool for studying external memory access and
overlay rendering. It does **not** ship kernel drivers, does not bypass
anti-cheat, and does not perform injection. Any PR attempting to add
kernel-mode components or anti-cheat evasion will be closed.

## Reporting a vulnerability

If you find a security issue in the loader, the signature scanner, or the
plugin host (e.g. arbitrary code execution via a malicious plugin, path
traversal in the config loader), please email `security@bo6-external.dev`
with a description and a minimal reproduction.

Please do not open public issues for security reports.

## Supported versions

Only the latest `main` branch is supported. Tagged releases older than
90 days are considered end-of-life.

## Out of scope

- Bans from BattlEye / Ricochet — this is a research repo, not a ban
  support forum.
- Cheat detection bypasses.
- Requests to add injection or driver components.