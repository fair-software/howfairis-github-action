"""

Attempts to infer whether a license is present in a
directory and, if so, if the license is open-source

Thin wrapper around ruby library licensee
https://github.com/licensee/licensee 

"""

import argparse

import subprocess
import json

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('repo')
    args = parser.parse_args()

    found_licenses = guess_license(args.repo)
    oss_status = [is_oss(l) for l in found_licenses]
    all_oss = all(oss_status)

    print(found_licenses, oss_status, all_oss)
    return

def guess_license(dir):
    """Parses output of licensee for the SPDX license ids"""
    res = subprocess.check_output(['licensee', 'detect', '--json', dir])
    res = json.loads(res)
    lic_abbrs = [l['spdx_id'] for l in res["licenses"]]
    return lic_abbrs

# Loads reference set of SPDX licenses with OSI/FSF status
with open("spdx_licenses.json", "r") as fh:
    spdx = json.load(fh)

def is_oss(abbr):
    """Determines if the license provided is open-source or not"""
    if abbr in spdx.keys():
        return spdx[abbr]['is_fsf'] or spdx[abbr]['is_osf']
    return False

if __name__ == '__main__':
    main()

