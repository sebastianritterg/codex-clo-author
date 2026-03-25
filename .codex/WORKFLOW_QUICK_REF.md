# Workflow Quick Reference

Model: you direct, Codex orchestrates through skills and custom subagents.

## Main Pipeline

```text
$clo-discover interview -> research spec + domain profile
    ->
$clo-discover lit -> literature synthesis
    ->
$clo-discover data -> data assessment
    ->
$clo-strategize -> strategy memo
    ->
$clo-analyze -> scripts + outputs
    ->
$clo-write -> paper sections
    ->
$clo-review -> review score + peer review
    ->
$clo-submit -> final submission gate
```

Enter at any stage. Use `$clo-new-project` when you want the full pipeline.

## Entry Points

- `$clo-new-project`
- `$clo-discover`
- `$clo-strategize`
- `$clo-analyze`
- `$clo-write`
- `$clo-review`
- `$clo-revise`
- `$clo-talk`
- `$clo-submit`
- `$clo-research-tools`

## Quality Gates

- `>= 80`: commit-ready
- `>= 90`: merge-ready
- `>= 95`: submission-ready

## Exploration Mode

For prototypes and side investigations:

- work in `explorations/`
- keep rough work outside canonical outputs
- promote only after the idea stabilizes
- archive abandoned lines under `explorations/ARCHIVE/`

