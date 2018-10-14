PLSE Research Tools Index
=========================

An index database about artifacts in PLSE (Programming Languages & Software Engineering)
Research.

Goal of this project: track the progress and quality of artifacts in this
area of research better.

## Metadata and derived data

The principle of this repo is to derive data automatically as much as possible.

Metadata is tracked manually, inside `metadata.json`.

Derived data include:

- Language
- Github stars
- Latest commit time

Currently, derived data will be updated by running scripts manually and irregularly.
Before I can set up a database service that caches relevant data, please make a PR to update them.

# Contribution

Welcome to contribute through standard Github PR:

1. Add/delete/update an entry in `metadata.json`.
2. Run `python3 generate.py` to update `docs/data.json` with `metadata.json`.
3. Commit changes to both JSON files

# Disclaimer

This repo is only for your reference and doesn't claim its accuracy, completeness, or up-to-dateness.
