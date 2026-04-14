# Server Baseline Collection and Searchable Operations Dashboard (Ansible)

Enterprise-ready Ansible framework to collect Windows and Unix/Linux baselines, normalize into a common schema, score compliance/risk, compare drift vs previous snapshots, and generate searchable HTML/JSON/CSV reporting.

## Repository layout

- `inventory/` sample inventory and group variables.
- `playbooks/` collection, report build, and historical comparison playbooks.
- `roles/` modular collection/normalize/compliance/drift/report roles.
- `templates/` dashboard and detail HTML templates.
- `scripts/` lightweight Python renderer for combined dashboard artifacts.
- `output/` current and historical machine-readable outputs.
- `docs/` architecture, field catalog, runbook.

## Prerequisites

- Ansible Core 2.15+ (2.16+ recommended)
- Python 3.10+
- Collections:
  - `ansible.windows`
  - `community.windows`
  - `community.general`
  - `ansible.posix`

Install collections:

```bash
ansible-galaxy collection install -r requirements.yml
```

## Quick start

1. Update inventory and credentials in `inventory/hosts.ini` and `inventory/group_vars/*.yml`.
2. Run baseline collection:

```bash
ansible-playbook -i inventory/hosts.ini playbooks/baseline_collect.yml
```

3. Build dashboard/report artifacts on localhost:

```bash
ansible-playbook -i inventory/hosts.ini playbooks/baseline_report.yml
```

4. Compare current run to previous snapshot:

```bash
ansible-playbook -i inventory/hosts.ini playbooks/baseline_compare.yml
```

## Outputs

- Per-host normalized JSON: `output/current/<run_id>/json/<host>.json`
- Aggregate JSON: `output/current/<run_id>/json/servers.json`
- CSV summary: `output/current/<run_id>/csv/servers_summary.csv`
- Dashboard: `output/current/<run_id>/html/dashboard.html`
- Server details: `output/current/<run_id>/html/server_<host>.html`
- Comparison: `output/current/<run_id>/html/compare.html`

## Scheduler usage (AWX / AAP / Semaphore)

- Use `playbooks/baseline_collect.yml` as the primary scheduled job.
- Chain `baseline_report.yml` and `baseline_compare.yml` after collection.
- Set host/group vars for policy thresholds and approved listeners/destinations.

## Environment-specific customization required

- Ownership metadata placeholders (`app`, `owner`, `datacenter`, `support_group`, `patch_group`).
- Approved listener/destination policy lists.
- Agent signatures and compliance thresholds.
- Connection/auth settings and privilege escalation model.

See `docs/runbook.md` for full operational details.
