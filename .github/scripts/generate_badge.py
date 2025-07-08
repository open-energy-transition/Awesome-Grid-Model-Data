# SPDX-FileCopyrightText: 2025 Open Energy Transition (OET)
#
# SPDX-License-Identifier: MIT

"""
Generate a Shields.io-compatible JSON badge from lychee link check output.

This script reads `lychee.json` (in --format json format), calculates the
percentage of successful links, and creates `link-status.json` for use in
dynamic Shields.io badges.

---

🔧 Requirements:
- Rust (https://www.rust-lang.org/)
- lychee (a fast link checker written in Rust)

To install:

1. Install Rust:
   curl https://sh.rustup.rs -sSf | sh
   (Press '1' for default installation)

2. Install lychee:
   cargo install lychee

3. Generate link check output:
   lychee --no-progress --format json README.md > lychee.json

Then run this script:
   python .github/scripts/generate_badge.py

Output:
- link-status.json (for badge display)
"""

import json

with open("lychee.json") as f:
    data = json.load(f)

total = data.get("total", 0)
ok = data.get("successful", 0)
percent = round((ok / total) * 100) if total else 0

color = "green" if percent > 90 else "orange" if percent > 70 else "red"

badge = {
    "schemaVersion": 1,
    "label": "links passing",
    "message": f"{percent}%",
    "color": color
}

with open("link-status.json", "w") as out:
    json.dump(badge, out, indent=2)
