#!/usr/bin/env python3

import os
import re
import sys

import requests

from config import MAX_PADS, STORE_TO, BASE_URL


def do_export():
    print("Requesting pads...")
    result = requests.get('%s/pad-lister' % BASE_URL)

    if result.status_code != 200:
        print("Non success status code: %s" % result.status_code)
        return

    pad_name_list = re.findall(r'<td><a href="/p/([^"]+)">[^<]+</a></td>', result.text)
    download_counter = 0
    for name in pad_name_list:
        download_counter += 1
        if download_counter > MAX_PADS:
            return
        print("Downloading %s..." % name)
        pad_req = requests.get('%s/p/%s/export/txt' % (BASE_URL, name))
        if pad_req.status_code != 200:
            print("Non success status code for pad: %s" % pad_req.status_code)
            continue

        save_name = re.subn(r'[^a-z\-_0-9]', '_', name, flags=re.IGNORECASE)[0]
        filename = '%s/%s' % (STORE_TO, save_name)
        print("Saving to %s" % filename)
        with open(filename, "w+") as f:
            f.write(pad_req.text)


def update_repo():
    os.chdir(STORE_TO)
    if os.system("git status") != 0:
        if os.system("git init") != 0:
            return

    if os.system("git add -A .") != 0:
        return
    if os.system("git commit -m 'daily backup'") != 0:
        return


if __name__ == '__main__':
    do_export()
    sys.stdout.flush()
    update_repo()
