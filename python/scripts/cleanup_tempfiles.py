#!/usr/bin/env python
"""Remove common temporary files from cwd recursively"""
import argparse
import os
from glob import glob
from typing import Iterable
import json
from pathlib import Path

conffile = Path(__file__).parent / "tempfiles_patterns.json"


def main(patterns: Iterable[str], dry_run: bool = False) -> None:
    targets = []
    for p in patterns:

        targets += sorted(glob(str(Path.cwd() / "**" / p), recursive=True))

    if dry_run:
        print("The following files would be removed")
        print("\n".join(targets))
        return

    for t in targets:
        try:
            os.remove(t)
        except Exception:
            print(f"Error while trying to remove {t}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry", "--dry-run", dest="dry_run", action="store_true")
    parser.add_argument(
        "--extra",
        nargs="+",
        help="additional filters (patterns) to remove recurcively.",
    )
    args = parser.parse_args()

    with open(conffile, mode="rt") as fileobj:
        patterns = json.load(fileobj)

    if args.extra is not None:
        patterns += args.extra

    main(patterns=patterns, dry_run=args.dry_run)
