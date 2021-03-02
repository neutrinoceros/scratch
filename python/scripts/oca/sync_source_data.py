#!/usr/bin/env python
"""Update data directory from origin with rsync.

This requires that at least "runs_data.json" file was already fetched from source.

Only works if target dir contains a "runs_data.json" file
with a "origin" key pointing to a remote disk location.
The remote server needs to be used with ssh.
"""
import os
import json
from pathlib import Path
from shutil import copyfile
import tempfile
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        "--dir",
        "--directory",
        dest="directory",
        type=str,
        default=".",
        help="target directory (should contain a 'runs_data.json' database file)",
    )
    parser.add_argument("--dry-run", action="store_true", help="passed down to rsync")
    parser.add_argument(
        "-u",
        "--update-db",
        "--update-database",
        "--update-json",
        action="store_true",
        help="force update data base json file from origin",
    )
    args = parser.parse_args()

    local_json = Path(args.directory, "runs_data.json")
    with open(local_json) as file:
        js = json.load(file)

    print("Checking for json database update...")
    with tempfile.NamedTemporaryFile() as tmpf:
        res = os.system(f"scp {js['origin']}/runs_data.json {tmpf.name}")
        if res != 0:
            raise RuntimeError
        with open(tmpf.name) as file:
            newjs = json.load(file)
        if not newjs == js and not args.update_json:
            print("Diff report\n" "-----------")
            os.system(f"sdiff --left-column --suppress-common-lines runs_data.json {tmpf.name}")
            print()
            print(
                "remote json was changed since last update, "
                "please check diff and rerun with --update-db (or -u)"
            )
            exit(1)

    flags = ""
    if args.dry_run:
        flags += "--dry-run"
    cmd = f"rsync -a --stats --human-readable --copy-links --info=progress2 {flags} {js['origin']}/ {Path(args.directory)}"
    print(cmd)
    os.system(cmd)
