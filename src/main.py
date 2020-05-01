######################################################
#
# GPL v3 License
#
# Copyright (c) 2020 Shubhrendu Tripathi
#
######################################################

#!/usr/bin/env python3

from requests import get
import csv

url_c19s = "https://api.covid19india.org/csv/latest/state_wise.csv"
state_csv = "state_wise.csv"


def download(url, file_name):
    # open in binary mode
    with open(file_name, "wb"):
        # get request
        response = get(url)
        # write to file
        open(file_name, "wb").write(response.content)


if __name__ == "__main__":
    print("Hello, world!")
    download(url_c19s, state_csv)

    with open(state_csv, newline='\n') as csvfile:
        state_reader = csv.reader(csvfile, delimiter=",")
        for row in state_reader:
            print(','.join(row))

