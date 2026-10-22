# Contributing to bo6-external

bo6-external is an educational research project exploring external process
memory reading, overlay rendering and signature scanning against Black Ops 6
on Windows. Contributions are welcome as long as they stay within the
research/education scope of the repository.

## Ground rules

- This repo is **for educational purposes only**. Do not submit anything
  intended for use in live multiplayer matches.
- Only target the offline/custom-game / private-match environment when
  testing. Never submit code that auto-joins public lobbies.
- Every PR that touches `src/offsets/` must include the game build number
  the offsets were verified against in the PR description.
- Keep modules small and testable. New features go in `src/plugins/` as a
  plugin implementing the contract in `src/contracts/plugin_api.py`.

## Workflow

1. Fork the repo and create a feature branch.
2. Run `python -m pytest tests/` before opening a PR.
3. Keep commits scoped — one feature per PR.
4. Update `docs/plugin_authoring.md` if you add a new plugin type.

## Code style

- Python 3.11+, type hints everywhere.
- Black + isort formatting.
- No global mutable state outside `src/host/registry.py`.

## Reporting bugs

Open an issue with the game build, the module you were using, and the
traceback. Do **not** attach memory dumps that may contain personal data.