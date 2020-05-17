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
from gi.repository import Gtk, Gdk
from datetime import datetime
import os

class UI(Gtk.Window):
	file_ui = "c19s.glade"
	file_style = "style.css"
	file_icon = "science-medical-virus-biology-bacteria_108620.png"

	currFldr = os.path.dirname(os.path.abspath(__file__))

	file_ui_path = os.path.join(currFldr, file_ui)
	file_style_path = os.path.join(currFldr, file_style)
	file_icon_path = os.path.join(currFldr, file_icon)

	def __init__(self):
		Gtk.Window.__init__(self)
		self.createWindow()

	def createWindow(self):
		builder = Gtk.Builder()
		builder.add_from_file(self.file_ui_path)

		window = builder.get_object("winMain")

		cssP = Gtk.CssProvider()
		cssP.load_from_path(self.file_style_path)
		screen = Gdk.Screen.get_default()
		styleContext = Gtk.StyleContext()
		styleContext.add_provider_for_screen(screen, cssP, Gtk.STYLE_PROVIDER_PRIORITY_USER)

		self.set_icon_from_file(self.file_icon_path)

		window.connect("delete-event", Gtk.main_quit)
		window.show_all()

		return window

