###################################################################
#
# Copyright (C) 2020 Shubhrendu Tripathi
#
# GPL v3 License
#
###################################################################

#!/usr/bin/env python3

from requests import get
import csv

state_csv = "state_wise.csv"

class Download:
    """Download the csv file"""
    def __init__(self):
        pass

    def download(url):
        """do the actual download"""
        # open in binary mode
        with open(state_csv, "wb"):
            # get request
            response = get(url)
            # write to file
            open(state_csv, "wb").write(response.content)

            with open(state_csv, newline='\n') as csvfile:
                state_reader = csv.reader(csvfile, delimiter=",")
                for row in state_reader:
                    print(','.join(row))
