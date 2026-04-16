# Contributing to Beyan

Thank you for your interest in improving Beyan! This document explains how to contribute effectively.

---

## Ways to Contribute

### 1. Report a Prompt Issue
If a prompt produces unclear, incomplete, or incorrect guidance:
- Open an issue using the **Bug Report** template
- Include: which prompt, what went wrong, what you expected, which LLM you used

### 2. Request a New Prompt
If you need analysis support for a project type not yet covered:
- Open an issue using the **New Prompt Request** template
- Describe the project type, what makes it different from existing prompts, and potential use cases

### 3. Submit a Translation
English translations of the Turkish prompts are in progress. To contribute:
- Pick an untranslated prompt from `en/` (marked with `<!-- TODO: translate -->`)
- Translate maintaining all structure, tables, Mermaid diagrams, and checklists
- Submit a PR with title: `[EN] Translate: [prompt name]`

### 4. Improve an Existing Prompt
- Fork the repo
- Make your changes
- Ensure the prompt still follows the [structure standard](#prompt-structure-standard)
- Update `Son Güncelleme` / `Last Updated` header field
- Submit a PR with a clear description of what was improved and why

---

## Prompt Structure Standard

Every prompt in Beyan must include these sections in order:

```
1. Title + Update tracking header
2. Role Definition
3. Descriptive/Evaluative layer table (if applicable)
4. Core Rules (placeholder ban, language standard, analysis order)
5. Phase 0: Pre-Flight Scan
6. Descriptive phases (system-specific)
7. — EVALUATIVE LAYER — section break
8. Evaluative phases (completeness audit is mandatory)
9. Output File System (with docs/[directory]/ path)
10. Quality Checklist (minimum 6 items)
```

**Mandatory output files** for every project-type prompt:
- `completeness_report.md`
- `system_taxonomy.md`
- `index.md` (always last)

**Forbidden patterns:**
- ❌ Project names, person names, or specific proprietary technology names in titles
- ❌ Placeholder content without `[fill for your system]` notes
- ❌ "Optional" label except on the final phase

---

## Pull Request Guidelines

- One prompt per PR (unless fixing a cross-cutting issue)
- PR title format: `[TYPE] Short description`
  - Types: `[FIX]`, `[IMPROVE]`, `[NEW]`, `[EN]`, `[DOCS]`
- Update the prompt's `Last Updated` / `Son Güncelleme` field
- If adding a new prompt, also update:
  - `tr/triyaj/triyaj_yonlendirme_promptu_v1.0.md` reference table
  - `en/triage/triage_routing_prompt_v1.0.md` reference table
  - `NAVIGATION_STANDARD.md`
  - `GROWTH_STRATEGY.md` active family structure

---

## Development Cycle

Beyan uses a self-referential improvement process:

1. Changes are proposed via issues or PRs
2. Major structural changes go through a Meta Audit cycle
3. Health Score is updated after significant improvement batches
4. Changelog is updated with each release

---

## Questions?

Open a Discussion on GitHub — we're happy to help.
