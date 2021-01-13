#!/usr/bin/python3

import csv
import sys
from os.path import expanduser

logins = []

cache_file_addr = expanduser("~") + "/.cache/passws"
try:
    cache_file = open(cache_file_addr)
except FileNotFoundError:
    print("No cache file found. Generating...")
    # Read from original file
    with open(expanduser("~") + "/logins.csv") as logins_file:
        reader = csv.reader(logins_file)
        for row in reader:
            logins.append(row)

    # Write to cache file:
    with open(cache_file_addr, "w") as cache_file:
        writer = csv.writer(cache_file)
        for login in logins:
            writer.writerow([login[5], login[0], login[1], login[2]])
finally:
    cache_file.close()


def read_cache_file():
    cached_data = []

    with open(cache_file_addr) as cache_file:
        reader = csv.reader(cache_file)
        for row in reader:
            cached_data.append(row)
    
    return cached_data


def search(input):
    data = read_cache_file()
    matches = [x for x in data if sys.argv[1] in x[1]]

    return matches


if sys.argv[1] == "add":
    pass
else:
    # search for site
    matches = search(sys.argv[1])
    
    for row in matches:
        print("> " + row[1].split("/")[2])
        print("\t" + (row[2] if row[1] != "" else "N/A"))
        print("\t" + row[3])
        print()
