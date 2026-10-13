#!/usr/bin/env python3
"""Refresh the site's copy of the OT/ICS resources catalog from its canonical repository.

    python3 scripts/refresh_resources.py              # latest main of okieotsec/ot-ics-resources
    python3 scripts/refresh_resources.py --ref <sha>  # a specific commit
    python3 scripts/refresh_resources.py --verify     # no network: check the local copy against its record

The copy in _data/resources.json is a generated derivative: never edit it by hand. Edit resources.json in the
resources repository, merge that, and run this script. It records the exact commit and the SHA-256 of the file in
_data/resources_source.json, which the Resources page shows.
"""
import argparse
import datetime
import hashlib
import json
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

REPO = "okieotsec/ot-ics-resources"
ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "_data" / "resources.json"
SIDECAR = ROOT / "_data" / "resources_source.json"
ALLOWED_HOSTS = {"api.github.com", "raw.githubusercontent.com"}
MAX_BYTES = 5 * 1024 * 1024
SHA_RE = re.compile(r"[0-9a-f]{40}")


def fetch(url):
    parts = urllib.parse.urlsplit(url)
    if parts.scheme != "https" or parts.hostname not in ALLOWED_HOSTS:
        raise SystemExit(f"refusing to fetch {url}")
    request = urllib.request.Request(url, headers={"User-Agent": "okieotsec-site-refresh", "Accept": "application/vnd.github+json"})
    with urllib.request.urlopen(request, timeout=30) as response:  # noqa: S310 - https and host checked above
        data = response.read(MAX_BYTES + 1)
    if len(data) > MAX_BYTES:
        raise SystemExit("the download is larger than expected")
    return data


def check(data):
    """The catalog must be the schema this page understands, with counts that match its records."""
    if data.get("schema_version") != 2:
        raise SystemExit("unsupported catalog schema_version")
    rows = data.get("resources")
    if not isinstance(rows, list) or not rows:
        raise SystemExit("the catalog has no resources")
    counts = {"free": sum(r.get("cost_group") == "free" for r in rows), "paid": sum(r.get("cost_group") == "paid" for r in rows), "total": len(rows)}
    if data.get("counts") != counts:
        raise SystemExit(f"the catalog counts do not match its records: {counts}")
    return counts


def verify():
    record = json.loads(SIDECAR.read_text(encoding="utf-8"))
    actual = hashlib.sha256(DATA.read_bytes()).hexdigest()
    if actual != record["sha256"]:
        print(f"MISMATCH: _data/resources.json is {actual}, the record says {record['sha256']}", file=sys.stderr)
        return 1
    check(json.loads(DATA.read_text(encoding="utf-8")))
    print(f"OK: resources.json matches {record['source_repository']}@{record['source_commit'][:12]} ({record['sha256'][:12]}...)")
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--ref", default="main", help="branch, tag or commit of the resources repository")
    parser.add_argument("--verify", action="store_true", help="check the local copy against its record, without the network")
    args = parser.parse_args()
    if args.verify:
        return verify()
    commit = json.loads(fetch(f"https://api.github.com/repos/{REPO}/commits/{urllib.parse.quote(args.ref, safe='')}"))["sha"]
    if not SHA_RE.fullmatch(commit):
        raise SystemExit("unexpected commit id from GitHub")
    raw = fetch(f"https://raw.githubusercontent.com/{REPO}/{commit}/resources.json")
    counts = check(json.loads(raw.decode("utf-8")))
    DATA.write_bytes(raw)
    record = {"source_repository": REPO, "source_url": f"https://github.com/{REPO}/tree/{commit}", "source_commit": commit,
              "source_file": "resources.json", "sha256": hashlib.sha256(raw).hexdigest(), "counts": counts,
              "retrieved": datetime.datetime.now(datetime.timezone.utc).date().isoformat(),
              "refresh": "python3 scripts/refresh_resources.py"}
    SIDECAR.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    print(f"Refreshed from {REPO}@{commit[:12]}: {counts}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
