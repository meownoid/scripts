#!/usr/bin/env python

import sys
import os
import re
import urllib.request


def main():
    if len(sys.argv) < 2:
        print("Please provide css file as only argument")

    filename = sys.argv[1]

    with open(filename, "r") as f:
        data = f.read()

    urls = re.findall(
        r"https?://[^\s\(\)]+",
        data,
    )

    os.makedirs("webfonts", exist_ok=True)
    for url in urls:
        local = os.path.join("webfonts", os.path.basename(url))
        print(f'Downloading {url} to {local}')
        urllib.request.urlretrieve(url, local)
        data = data.replace(url, local)

    name, ext = os.path.splitext(filename)
    new_filename = f"{name}-local{ext}"
    with open(new_filename, 'w') as f:
        f.write(data)


if __name__ == "__main__":
    main()
