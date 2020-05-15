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
from datetime import datetime
import os

class UI:
	file_ui = "c19s.glade"
	currFldr = os.path.dirname(os.path.abspath(__file__))
	file_ui_path = os.path.join(currFldr, file_ui)

	def __init__(self):
		self.createWindow()

	def createWindow(self):
		builder = Gtk.Builder()
		builder.add_from_file(self.file_ui_path)

		window = builder.get_object("winMain")
		window.connect("delete-event", Gtk.main_quit)
		window.show_all()

		return window

