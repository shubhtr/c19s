###################################################################
#
# Copyright (C) 2020 Shubhrendu Tripathi
#
# GPL v3 License
#
###################################################################

#!/usr/bin/env python3

from download import Download

url_c19s = "https://api.covid19india.org/csv/latest/state_wise.csv"

if __name__ == "__main__":
    Download.download(url_c19s)


