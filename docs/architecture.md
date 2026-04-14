# Architecture

## Design principles

- Role-per-responsibility for collection, normalization, compliance, drift, reporting.
- Per-host normalized JSON as source of truth.
- Localhost-only report and drift generation for deterministic artifact creation.
- Configurable policy via inventory/group vars.

## Data flow

1. `baseline_collect.yml`
   - Gather host data (`windows_baseline` or `unix_baseline`).
   - Normalize into common schema (`common_normalize`).
   - Apply compliance/risk scoring (`compliance_checks`).
   - Write host JSON to `output/current/<run_id>/json` and snapshot to `output/history`.

2. `baseline_report.yml`
   - Read per-host JSON.
   - Build `servers.json`, CSV summary, HTML dashboard/detail pages.

3. `baseline_compare.yml`
   - Compare current host JSON vs previous run snapshots.
   - Generate drift summary JSON + HTML comparison page.

## Extensibility

- Add collectors by splitting task files in `windows_baseline` / `unix_baseline`.
- Extend schema in `common_normalize`.
- Tune policy in `inventory/group_vars/all.yml`.
- Customize templates and Python renderer output.
