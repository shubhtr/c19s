###################################################################
#
# Copyright (C) 2020 Shubhrendu Tripathi
#
# GPL v3 License
#
###################################################################

#!/usr/bin/env python3

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from download import Download
from ui import UI

url_c19s = "https://api.covid19india.org/csv/latest/state_wise.csv"

if __name__ == "__main__":
    """Covid-19 Statistics"""
    window = UI()
    Gtk.main()

    Download.download(url_c19s)


