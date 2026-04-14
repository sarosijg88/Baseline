#!/usr/bin/env python3
"""Render CSV and HTML outputs from normalized baseline JSON."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape


def load_servers(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8"))


def write_csv_summary(servers: list[dict], output_csv: Path) -> None:
    output_csv.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "hostname",
        "fqdn",
        "platform",
        "os_name",
        "os_version",
        "ip_count",
        "compliance_status",
        "compliance_score",
        "risk_score",
        "environment",
        "app",
        "owner",
        "datacenter",
        "support_group",
        "patch_group",
    ]
    with output_csv.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        for s in servers:
            writer.writerow(
                {
                    "hostname": s.get("server_identity", {}).get("hostname", ""),
                    "fqdn": s.get("server_identity", {}).get("fqdn", ""),
                    "platform": s.get("server_identity", {}).get("platform", ""),
                    "os_name": s.get("os_config", {}).get("os_name", ""),
                    "os_version": s.get("os_config", {}).get("os_version", ""),
                    "ip_count": len(s.get("server_identity", {}).get("ips", [])),
                    "compliance_status": s.get("compliance", {}).get("status", "unknown"),
                    "compliance_score": s.get("compliance", {}).get("compliance_score", 0),
                    "risk_score": s.get("compliance", {}).get("risk_score", 0),
                    "environment": s.get("metadata", {}).get("environment", ""),
                    "app": s.get("metadata", {}).get("app", ""),
                    "owner": s.get("metadata", {}).get("owner", ""),
                    "datacenter": s.get("metadata", {}).get("datacenter", ""),
                    "support_group": s.get("metadata", {}).get("support_group", ""),
                    "patch_group": s.get("metadata", {}).get("patch_group", ""),
                }
            )


def render_html(servers: list[dict], output_root: Path) -> None:
    templates_dir = Path(__file__).resolve().parent.parent / "templates"
    env = Environment(
        loader=FileSystemLoader(str(templates_dir)),
        autoescape=select_autoescape(["html", "xml"]),
    )

    html_dir = output_root / "html"
    html_dir.mkdir(parents=True, exist_ok=True)

    dashboard = env.get_template("dashboard.html.j2").render(servers=servers)
    (html_dir / "dashboard.html").write_text(dashboard, encoding="utf-8")

    detail_template = env.get_template("server_detail.html.j2")
    for s in servers:
        host = s.get("server_identity", {}).get("hostname", "unknown")
        detail = detail_template.render(server=s)
        (html_dir / f"server_{host}.html").write_text(detail, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output-root", required=True)
    args = parser.parse_args()

    input_path = Path(args.input)
    output_root = Path(args.output_root)
    servers = load_servers(input_path)

    write_csv_summary(servers, output_root / "csv" / "servers_summary.csv")
    render_html(servers, output_root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
