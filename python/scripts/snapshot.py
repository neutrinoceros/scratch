# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "yt>=4.0.0",
# ]
# ///
"""Produce the latest density snapshot of a 2D AMRVAC sim the output png is written to cwd,
but the simulation data can be fetch in a -d directory, absolute or relative to cwd.
"""
import argparse
import os
import yt


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", type=str, default=".")
    parser.add_argument("--log", action="store_true")
    parser.add_argument("--fields", nargs="*", type=str, default=["density"])
    args = parser.parse_args()

    ts = yt.load(os.path.join(args.directory, "*dat"), unit_system="code")
    ds = ts[-1]
    p = yt.plot_2d(ds, fields=args.fields)
    if not args.log:
        p.set_log("all", False)
    p.annotate_timestamp(draw_inset_box=True)
    p.save()
