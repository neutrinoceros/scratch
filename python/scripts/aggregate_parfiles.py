# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "yt>=4.0.0",
# ]
# ///
"""Merge parfiles using AMRVAC's logic (based on yt.frontend api)

usage

$ aggregate_parfiles.py model.par mod.par mod2.par > merger.par
"""
from yt.frontends.amrvac import read_amrvac_namelist
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("parfiles", type=str, nargs="+", help="parfiles to aggregate")
    args = parser.parse_args()
    print(read_amrvac_namelist(args.parfiles))
    print(f"! aggregated files: {', '.join(args.parfiles)}\n")
