# Photography Coach Rename Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rename the skill and public repository from `photo-reference-coach` to `photography-coach`.

**Architecture:** Rename the skill folder and identity while preserving behavior. Update every active invocation, installation path, test, UI label, repository URL, and installed copy.

**Tech Stack:** Markdown, YAML, Python unittest, Git, GitHub

---

### Task 1: Rename And Verify

**Files:**
- Rename: `photo-reference-coach/` to `photography-coach/`
- Modify: `photography-coach/SKILL.md`
- Modify: `photography-coach/agents/openai.yaml`
- Modify: `README.md`
- Modify: `tests/test_skill_contract.py`

- [ ] Rename the directory and identifiers.
- [ ] Replace old invocation and installation paths.
- [ ] Run contract tests and skill validation.
- [ ] Sync the installed skill and remove the superseded installation.
- [ ] Rename the GitHub repository and verify its About panel.
