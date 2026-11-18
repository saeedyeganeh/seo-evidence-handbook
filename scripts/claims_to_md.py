"""Render sources/claims.yml as a Markdown table for the published site."""
import sys

import yaml

rows = yaml.safe_load(open(sys.argv[1], encoding="utf-8")) or []
print("# Claim ledger\n")
print("Every factual claim in the handbook, the kind of evidence behind it, and when it was last checked.\n")
print("| ID | Ch. | Claim | Label | Source | Locator | Checked |")
print("|---|---|---|---|---|---|---|")
for r in rows:
    cells = [
        r.get("id", ""),
        str(r.get("chapter", "")),
        r.get("claim", "").replace("|", "\\|"),
        f"`{r.get('label', '')}`",
        f"[link]({r.get('source', '')})",
        str(r.get("locator", "")).replace("|", "\\|"),
        str(r.get("checked", "")),
    ]
    print("| " + " | ".join(cells) + " |")
