"""
Rename images in ./images/ into clean sequential order (1.jpg, 2.jpg, …)

Rules:
  8_.jpg   → treated as 8   (strip trailing underscore)
  136.jpg  → 136            (base)
  136(1).jpg → 136 + 0.5    (inserted right after 136, before 137)
  139(1).jpg → 139 + 0.5
  166(1).jpg → 166 + 0.5

Files are sorted by their sort-key, then renamed 1, 2, 3, …

Run with --dry-run first to preview, then without to apply.
"""

import os
import re
import sys

IMG_DIR = "images"

def sort_key(name):
    """Return (base_number, variant_order) for sorting."""
    base = name.replace(".jpg", "")
    # strip trailing underscore(s): "8_" -> "8"
    base = base.rstrip("_")
    # check for (N) suffix: "136(1)" -> base=136, variant=1
    m = re.match(r"^(\d+)\((\d+)\)$", base)
    if m:
        return (int(m.group(1)), int(m.group(2)))
    # plain number
    if base.isdigit():
        return (int(base), 0)
    raise ValueError(f"Cannot parse filename: {name}")

def main():
    dry_run = "--dry-run" in sys.argv

    files = [f for f in os.listdir(IMG_DIR) if f.lower().endswith(".jpg")]
    files_sorted = sorted(files, key=sort_key)

    print(f"Found {len(files_sorted)} images.\n")
    print(f"{'Old name':<25}  {'New name'}")
    print("-" * 45)

    # First pass: rename to temp names to avoid collisions (e.g. 136.jpg -> 137.jpg)
    temp_names = {}
    for i, old_name in enumerate(files_sorted, start=1):
        new_name = f"{i}.jpg"
        temp_name = f"__temp_{i}__.jpg"
        print(f"{old_name:<25}  →  {new_name}")
        temp_names[temp_name] = new_name
        if not dry_run:
            os.rename(
                os.path.join(IMG_DIR, old_name),
                os.path.join(IMG_DIR, temp_name)
            )

    if not dry_run:
        # Second pass: rename temp names to final names
        for temp_name, new_name in temp_names.items():
            os.rename(
                os.path.join(IMG_DIR, temp_name),
                os.path.join(IMG_DIR, new_name)
            )
        print(f"\n✅ Done! Renamed {len(files_sorted)} files.")
    else:
        print(f"\n[DRY RUN] No files were changed. Remove --dry-run to apply.")

if __name__ == "__main__":
    main()
