# Field Catalog

## Top-level normalized schema

- `schema_version`
- `server_identity`
  - `hostname`, `fqdn`, `domain`, `ips`, `platform`
- `metadata`
  - `environment`, `app`, `owner`, `datacenter`, `support_group`, `patch_group`
- `compute`
  - `cpu_count`, `memory_mb`, `uptime_seconds`
- `storage`
  - `disks`, `mounts`
- `network`
  - `listeners`, `established`
- `os_config`
  - `os_name`, `os_version`, `os_build`, `kernel`, `firewall`, `winrm_status`, `ssh_summary`
- `patch`
  - `pending_reboot`, `hotfix_summary`, `pending_updates`
- `software`
  - `installed`
- `services`
  - `running`, `scheduled`
- `security`
  - `local_users`, `local_admins`
- `certificates`
  - `summary`
- `process_port_map`
- `process_destination_map`
- `compliance`
  - `status`, `risk_score`, `compliance_score`, `findings`
- `drift`
  - `has_drift`, `changes`
- `collection_metadata`
  - `run_id`, `collected_at`, `collector`, `unreachable`

## Compliance status values

- `compliant`
- `partially_compliant`
- `non_compliant`
- `exception_approved` (reserved for policy override integration)
- `unknown`
