# Runbook

## 1. Configure inventory and vars

- Edit `inventory/hosts.ini`.
- Replace placeholder credentials in `inventory/group_vars/windows.yml`.
- Configure policy thresholds, agent signatures, and allow-lists in `inventory/group_vars/all.yml`.

## 2. Install dependencies

```bash
python3 -m pip install jinja2
ansible-galaxy collection install -r requirements.yml
```

## 3. Execute baseline workflow

```bash
ansible-playbook -i inventory/hosts.ini playbooks/baseline_collect.yml
ansible-playbook -i inventory/hosts.ini playbooks/baseline_report.yml
ansible-playbook -i inventory/hosts.ini playbooks/baseline_compare.yml
```

## 4. Validate generated artifacts

- Open `output/current/<run_id>/html/dashboard.html`.
- Review `output/current/<run_id>/json/drift_summary.json`.
- Consume `output/current/<run_id>/csv/servers_summary.csv` in SIEM/BI pipeline.

## Troubleshooting

- If host data is incomplete, review connectivity and privilege boundaries.
- Collection tasks use `failed_when: false` for best-effort fields.
- For Linux network mapping, ensure `ss` or `netstat` is available.
- For Windows commands, ensure required PowerShell cmdlets are available.
