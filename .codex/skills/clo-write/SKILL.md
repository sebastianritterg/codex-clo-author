---
name: clo-write
description: Draft economics paper sections with review. Adapted from the Clo-Author workflow for Codex. Use when this specific phase of the research pipeline is the main task.
---

# Clo Write

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

# Write

Draft paper sections or apply humanizer pass by dispatching the **Writer** agent.

**Input:** `$ARGUMENTS` - section name or mode, optionally followed by file path.

---

## Modes

### `$clo-write [section]` - Draft Paper Section
Draft a specific section: `intro`, `strategy`, `results`, `conclusion`, `abstract`, or `full`.

**Agent:** Writer
**Output:** LaTeX section file in paper/sections/

Workflow:

#### 1. Context Gathering

Before drafting, read all available context:
1. Read existing paper draft in `paper/` (if it exists)
2. Read `master_supporting_docs/` for notes, outlines, research specs
3. Read most recent `quality_reports/research_spec_*.md` or `quality_reports/lit_review_*.md`
4. Read `~/.codex/skills/clo-workflow/references/domain-profile.md ` for field conventions
5. Check `Bibliography_base.bib` for available citations
6. Scan `paper/tables/` and `paper/figures/` for generated output
7. Read `quality_reports/results_summary.md` if it exists (from Coder)

#### 2. Section Routing

Based on `$ARGUMENTS`:
- **`full`**: Draft all sections in sequence, pausing between major sections for user feedback
- **`intro`**: Draft introduction (most common request)
- **`strategy`**: Draft identification and estimation section
- **`results`**: Draft results from available output
- **`conclusion`**: Draft conclusion
- **`abstract`**: Draft abstract (must have other sections first)
- **No argument**: Ask user which section to draft

#### 3. Dispatch Writer

Dispatch Writer with section standards, notation protocol, and anti-hedging rules. Humanizer pass runs automatically before finalizing. Save to `paper/sections/[section].tex`.

#### 4. Quality Self-Check

Before presenting the draft:
- [ ] Every displayed equation is numbered (`\label{eq:...}`)
- [ ] All `\cite{}` keys exist in `Bibliography_base.bib`
- [ ] Introduction contribution paragraph names specific papers
- [ ] Effect sizes stated with units
- [ ] No banned hedging phrases
- [ ] Notation consistent throughout
- [ ] All tables/figures referenced actually exist in `paper/tables/` or `paper/figures/`

#### 5. Present to User

Present each section for feedback. Flag items that need attention:
- **TBD items:** Where empirical results are needed but not yet available
- **VERIFY items:** Citations that need user confirmation
- **PLACEHOLDER items:** Effect sizes awaiting final estimates

### `$clo-write humanize [file]` - Humanizer Pass Only
Strip AI writing patterns from existing text without rewriting content.

**Agent:** Writer (humanizer mode)
**Output:** Edited file with AI patterns removed

Strips 24 patterns across 4 categories:
- Structural: forced narrative arcs, artificial progression
- Lexical: "delve,leverage,nuanced,robust"
- Rhetorical: rule-of-three, negative parallelisms, em dash overuse
- Formatting: excessive bullet points, promotional language

---

## Section Standards

| Section | Length | Key Requirements |
|---------|--------|-----------------|
| Introduction | 1000-1500 words | Hook -> question -> method -> finding -> contribution -> roadmap |
| Strategy | 800-1200 words | Formal assumption, numbered equation, threats addressed |
| Results | 800-1500 words | Main spec, effect sizes in economic terms, heterogeneity |
| Conclusion | 500-700 words | Restate with effect size, policy, limitations, future |
| Abstract | 100-150 words | Question, method, finding with magnitude, implication |

---

## LaTeX Conventions

- `\citet{}` for textual citations ("Smith (2024) shows...")
- `\citep{}` for parenthetical citations ("...is well documented (Smith, 2024)")
- `booktabs` rules (`\toprule`, `\midrule`, `\bottomrule`) - never `\hline`
- Notation protocol: `Y_{it}`, `D_{it}`, `\gamma_i`, `\delta_t`, `\varepsilon_{it}`

---

## Principles
- **This is the user's paper, not Codex's.** Match their voice and style.
- **Never fabricate results.** Use TBD placeholders.
- **Citations must be verifiable.** Only cite confirmed papers.
- **Humanizer is automatic.** Every draft gets de-AI-ified.




