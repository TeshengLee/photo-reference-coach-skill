# Editor-Aware Photo Coach Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make metadata extraction automatic and editing instructions specific to the user's available app.

**Architecture:** Keep routing and mandatory behavior in `SKILL.md`. Store compact Apple Photos and Instagram control mappings in an on-demand reference. Test the written contract with a small standard-library test.

**Tech Stack:** Markdown, Python `unittest`

---

### Task 1: Contract Tests

**Files:**
- Create: `tests/test_skill_contract.py`

- [ ] Add assertions for automatic metadata attempts, non-blocking fallback, editor selection, and supported-control-only guidance.
- [ ] Run `python3 -m unittest tests/test_skill_contract.py` and confirm failure.

### Task 2: Skill Rules

**Files:**
- Modify: `photo-reference-coach/SKILL.md`
- Create: `photo-reference-coach/references/editing-tools.md`
- Modify: `photo-reference-coach/scripts/extract_image_metadata.py`

- [ ] Replace optional-sounding metadata language with an automatic best-effort attempt.
- [ ] Continue visual analysis when metadata is inaccessible or absent.
- [ ] Gate detailed editing instructions on the user's chosen editor.
- [ ] Add concise Apple Photos and Instagram operation paths.
- [ ] Run the contract test and skill validator.

### Task 3: Delivery

**Files:**
- Modify: `README.md`

- [ ] Document automatic metadata attempts and editor-aware instructions.
- [ ] Sync the installed skill, verify identical files, commit, and push.
