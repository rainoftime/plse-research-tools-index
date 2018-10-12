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
- Latest update time

Currently, derived data will be updated manually and irregularly. Before I can set up a database the cache relevant data,
please make a PR to update them.

# Contribution

Welcome to contribute through standard Github PR: add/delete an entry to `metadata.json` or update any entry.

Run `python3 generate.py` to update `docs/data.json` with `metadata.json`.

# Disclaimer

This repo is only for your reference and don't claim its accuracy, completeness, or up-to-dateness.
