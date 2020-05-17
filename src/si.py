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
from gi.repository import Gtk, Gdk, GdkPixbuf
import os

class SI():
    file_icon = "science-medical-virus-biology-bacteria_108620.png"
    currFldr = os.path.dirname(os.path.abspath(__file__))
    file_icon_path = os.path.join(currFldr, file_icon)

    def __init__(self):
        self.createStatusIcon()

    def createStatusIcon(self):
        self.statusIcon = Gtk.StatusIcon()
        self.statusIcon.set_from_file(self.file_icon_path)
        self.statusIcon.connect("popup-menu", self.si_right_click)

    #TODO: si_left_click - hides the window

    def si_right_click(self, icon, button, time):
        self.menu = Gtk.Menu()

        about = Gtk.MenuItem()
        about.set_label("About")
        quit = Gtk.MenuItem()
        quit.set_label("Quit")

        about.connect("activate", self.show_about)
        quit.connect("activate", Gtk.main_quit)

        self.menu.append(about)
        self.menu.append(quit)

        self.menu.show_all()

        def pos(menu, icon):
            return Gtk.StatusIcon.position_menu(menu, icon)

        self.menu.popup(None, None, None, self.statusIcon, button, time)

    def show_about(self, widget):
        about = Gtk.AboutDialog()

        authors = ["Shubhrendu Tripathi"]

        about.set_destroy_with_parent(True)
        about.set_name("Covid-19 Statistics")
        about.set_version("1.0")
        about.set_program_name("Covid-19 Statistics")
        about.set_copyright("Copyright \xa9 2020 Shubhrendu Tripathi")
        about.set_authors(authors)
        about.set_website("http://www.github.com/shubhtr")
        about.set_website_label("http://www.github.com/shubhtr")
        about.set_license_type(Gtk.License.GPL_3_0)
        about.set_icon_from_file(self.file_icon_path)
        about.set_default_icon_from_file(self.file_icon_path)
        about.set_logo(GdkPixbuf.Pixbuf.new_from_file_at_scale(self.file_icon_path, 256, 256, True))

        about.run()
        about.destroy()
