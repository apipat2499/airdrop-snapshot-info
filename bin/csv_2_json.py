#!/usr/bin/env python
"""
Convert each CSV file to a JSON file.
"""

import json
import csv
import sys

from urllib.request import urlopen


def main():
    url_template = "https://raw.githubusercontent.com/Gelotto/airdrop-snapshot-info/main/{}.txt"
    assets = ["atom", "juno", "scrt", "neta", "osmo", "stars"]

    for asset in assets:
        json_objects = []
        csv_file_url = url_template.format(asset)
        print(f"fetching {csv_file_url}...")
        csv_lines = [line.decode() for line in urlopen(csv_file_url)]
        for addr, _, amount in csv.reader(csv_lines[1:]):
            json_objects.append({"address": addr, "amount": float(amount)})

        output_filepath = f'{asset}.json'
        print(f"writing json data to {output_filepath}...")

        with open(output_filepath, "w") as output_json_file:
            json.dump(json_objects, output_json_file)


if __name__ == "__main__":
    sys.exit(main())
