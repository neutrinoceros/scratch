# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Remove trailing whitespaces in files matching with chosen suffix"""
from pathlib import Path
from argparse import ArgumentParser


def curate_one_file(filepath: Path, dry_run: bool = False):
    if not filepath.is_file():
        return
    with open(filepath, mode="r") as fileobj:
        lines = fileobj.readlines()
        text = fileobj.read()

    striped_lines = [L.rstrip() for L in lines]
    new_text = "\n".join(striped_lines)
    if striped_lines and striped_lines[-1]:
        # Because str.join will never preserve an existing EOF newline
        # I choose to always add one for consistency
        # This is "conditional" only in that it doesn't apply to empty files
        new_text += "\n"

    if new_text != text:
        if dry_run:
            print(filepath)
            return

        with open(filepath, mode="wt") as fileobj:
            fileobj.write(new_text)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("files", nargs="+", type=str)
    parser.add_argument(
        "--dry",
        "--dry-run",
        dest="dry_run",
        action="store_true",
        help="print list of files that would be modified",
    )

    args = parser.parse_args()
    for filepath in [Path(f) for f in args.files]:
        curate_one_file(
            filepath, dry_run=args.dry_run,
        )
