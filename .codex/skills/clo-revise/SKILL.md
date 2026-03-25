---
name: clo-revise
description: Structure an R-and-R response cycle. Adapted from the Clo-Author workflow for Codex. Use when this specific phase of the research pipeline is the main task.
---

# Clo Revise

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

# Revise

Structure point-by-point referee responses with classification, agent routing per revision protocol, and diplomatic drafting.

**Input:** `$ARGUMENTS` - path to referee report file(s), optionally followed by paper path.

---

## Workflow

### Step 1: Parse Inputs
1. Read referee report(s) from `$ARGUMENTS`
2. Read the paper (Paper/main.tex or specified path)
3. Read revision protocol from rules
4. Read existing scripts to know what analyses already exist

### Step 2: Classify Every Comment

| Class | Routing | Action |
|-------|---------|--------|
| **NEW ANALYSIS** | -> Coder agent | Flag for user, create analysis task |
| **CLARIFICATION** | -> Writer agent | Draft rewritten section |
| **REWRITE** | -> Writer agent | Draft structural revision |
| **DISAGREE** | -> User (mandatory) | Draft diplomatic pushback, flag for review |
| **MINOR** | -> Writer agent | Draft fix directly |

### Step 3: Build Tracking Document
Save to `quality_reports/referee_response_tracker.md` with:
- Summary counts per referee
- Action items by priority (HIGH: new analysis, MEDIUM: clarification, FLAGGED: disagreements, LOW: minor)

### Step 4: Dispatch Agents
- CLARIFICATION/REWRITE -> dispatch Writer with specific instructions
- NEW ANALYSIS -> flag for user approval before dispatching Coder
- DISAGREE -> draft diplomatic response, flag prominently for user

### Step 5: Draft Response Letter
Generate LaTeX response letter with:
- Summary of major changes
- Point-by-point responses with exact referee quotes
- Color-coded responses
- Page/section references for each change

### Step 6: Diplomatic Disagreement Protocol
When DISAGREE: open with acknowledgment, provide evidence, offer partial concession, NEVER say "the referee is wrong." FLAG for user review.

### Step 7: Save Outputs
1. Tracker: `quality_reports/referee_response_tracker.md`
2. Response letter: `quality_reports/referee_response_[journal]_[date].tex`
3. Revised sections: `Paper/sections/` (for CLARIFICATION/REWRITE items)

---

## Principles
- **The response letter is the user's voice.** Match their tone.
- **Never fabricate results.** Mark NEW ANALYSIS items as TBD.
- **Flag all DISAGREE items.** These need human judgment.
- **Track everything.** Every comment appears in both tracker and response letter.




