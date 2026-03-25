---
name: clo-research-tools
description: Run clo-author utility and maintenance workflows. Adapted from the Clo-Author workflow for Codex. Use when this specific phase of the research pipeline is the main task.
---

# Clo Research Tools

Adapt the Clo-Author workflow to Codex.

1. Start by inspecting the repo's AGENTS files, README.md, and current folder layout.
2. Use the repository's actual manuscript, output, and docs directories instead of assuming Clo-Author defaults.
3. Use the main Codex session as the orchestrator. Delegate focused work to the matching Codex subagents when that improves quality or speed.
4. Preserve worker-critic separation: creators produce artifacts, critics, editors, and referees review without editing.
5. If a repo already has paper-specific rules or skills, treat them as higher-priority than the generic Clo-Author defaults.
6. Read `references/source-skill.md` only when you need the original upstream command details or argument structure.

## Codex Notes

- Original slash commands are exposed here as explicit `$clo-*` skills.
- Hidden hooks are not ported. Use explicit verification, snapshot, upgrade, and review steps instead.
- Use the active `clo-workflow` references for domain and journal calibration: ~/.codex/skills/clo-workflow/references/domain-profile.md and ~/.codex/skills/clo-workflow/references/journal-profiles.md.
- Treat `explorations/` as the repo-level sandbox for experimental work. If exploratory work is needed and the folder is missing, scaffold it from ~/.codex/skills/clo-workflow/references/explorations.md.
- Read source mirrors only when provenance matters: ~/.codex/skills/clo-workflow/references/source-rules and ~/.codex/skills/clo-workflow/references/source-references.
- For repo-specific path conventions and field rules, prefer local `.agents/skills` and `AGENTS.override.md`.

## Source Workflow

# Tools

Utility subcommands for project maintenance and infrastructure.

**Input:** `$ARGUMENTS` - subcommand followed by any arguments.

---

## Subcommands

### `$clo-research-tools commit [message]` - Git Commit
Stage changes, create commit, optionally create PR and merge.
- Run git status to identify changes
- Stage relevant files (never stage.env or credentials)
- Create commit with descriptive message
- If quality score available and >= 80, note in commit

### `$clo-research-tools compile [file]` - LaTeX Compilation
3-pass XeLaTeX + bibtex compilation.

For papers:
```bash
cd Paper && TEXINPUTS=../Preambles:$TEXINPUTS xelatex -interaction=nonstopmode [file]
BIBINPUTS=..:$BIBINPUTS bibtex [file_base]
TEXINPUTS=../Preambles:$TEXINPUTS xelatex -interaction=nonstopmode [file]
TEXINPUTS=../Preambles:$TEXINPUTS xelatex -interaction=nonstopmode [file]
```

For talks:
```bash
cd Talks && TEXINPUTS=../Preambles:$TEXINPUTS xelatex -interaction=nonstopmode [file]
```

### `$clo-research-tools validate-bib` - Bibliography Validation
Cross-reference all \cite{} keys in paper and talk files against Bibliography_base.bib.
Report: missing entries, unused entries, duplicate keys.

### `$clo-research-tools journal` - Research Journal
Regenerate the research journal timeline from quality reports and git history.
Shows chronological record of agent actions, phase transitions, scores, decisions.

### `$clo-research-tools context` - Context Status
Show current context status and session health.
Check context usage, whether auto-compact is approaching, what state will be preserved.

### `$clo-research-tools deploy` - Deploy Guide Site
Render Quarto guide site and publish to GitHub Pages.
```bash
cd guide && quarto publish gh-pages --no-browser
```

### `$clo-research-tools learn` - Extract Learnings
Extract reusable knowledge from the current session. Auto-memory handles corrections automatically; this is for multi-step workflows worth turning into a full skill.

### `$clo-research-tools upgrade` - Upgrade Clo-Author Codex Infrastructure
Upgrade an existing Codex port to the latest clo-author source architecture.

**What it does:**
1. Clone the latest clo-author release into a temp directory
2. Refresh the upstream Clo-Author source snapshot used by the Codex port generator
3. Regenerate the managed Codex skills and subagents
4. Replace managed `clo-*` skills under `~/.agents/skills`, mirror them to `~/.codex/skills`, and refresh managed subagents under `~/.codex/agents`
5. Preserve repo-local overlays such as `.agents/skills`, `AGENTS.override.md`, `~/.codex/AGENTS.md`, and `~/.codex/config.toml`
6. Report what changed

**Workflow:**
```text
Step 1: DOWNLOAD
  - Clone latest clo-author into a temp directory

Step 2: PRESERVE LOCAL CUSTOMIZATIONS
  - Keep repo-local `.agents/skills` customizations
  - Keep `AGENTS.override.md`
  - Keep `~/.codex/AGENTS.md` and `~/.codex/config.toml`
  - Keep non-clo skills and non-managed custom agents

Step 3: REGENERATE
  - Refresh the upstream source snapshot
  - Run the Codex port generator
  - Review the staged output for new agents, skills, and references

Step 4: SYNC MANAGED INSTALLS
  - Replace managed `clo-*` skills in `~/.agents/skills`
  - Mirror those skills to `~/.codex/skills`
  - Replace managed custom subagents in `~/.codex/agents`

Step 5: DO NOT TOUCH
  - paper, scripts, data, notes, and other repo content
  - repo-specific overlays outside the managed Clo-Author Codex port

Step 6: REPORT
  - List what was updated
  - List what was preserved
  - Clean up temp files
```

---

## Principles
- **Each subcommand is lightweight.** No multi-agent orchestration needed.
- **Compile always uses 3-pass.** Ensures references and citations resolve.
- **validate-bib catches drift.** Run before commits to catch broken citations.
- **Upgrade preserves content.** Infrastructure changes, your paper doesn't.




