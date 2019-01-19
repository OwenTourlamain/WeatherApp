import yaml
import gi
from weather import Weather
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GLib


class WeatherAppWindow (Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Weather App")

        self.footerBar = Gtk.Box(spacing=6)

        self.mainLayout = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        self.add(self.mainLayout)
        self.mainLayout.pack_end(self.footerBar, False, True, 0)

        self.langSelector = Gtk.ComboBox()
        self.footerBar.pack_start(self.langSelector, True, True, 0)

        self.button1 = Gtk.Button(label="Refresh")
        self.button1.set_vexpand(False)
        self.button1.connect("clicked", self.on_button1_clicked)
        self.footerBar.pack_end(self.button1, True, True, 0)

        self.button2 = Gtk.Button(label="tmp")
        self.button2.set_vexpand(True)
        self.mainLayout.pack_start(self.button2, True, True, 0)

    def on_button1_clicked(self, widget):
        print("Hello")

    def on_button2_clicked(self, widget):
        print("Goodbye")


class ProgressBarWindow(Gtk.Window):

    def __init__(self, populate):
        self.populate = populate
        Gtk.Window.__init__(self, title="Setup")
        self.connect("show", self.show_bar)
        self.set_border_width(10)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        self.progressbar = Gtk.ProgressBar()
        self.progressbar.set_show_text(True)
        self.progressbar.set_text("Running first time setup...")
        vbox.pack_start(self.progressbar, True, True, 0)

        # self.timeout_id = GLib.timeout_add(50, self.on_timeout, None)
        self.activity_mode = False

    def show_bar(self, data=None):
        for chunk in self.populate():
            print(chunk)
            new_value = self.progressbar.get_fraction() + 0.1

            if new_value > 1:
                new_value = 0

            self.progressbar.set_fraction(new_value)

    def on_show_text_toggled(self, button):
        show_text = button.get_active()
        if show_text:
            text = "some text"
        else:
            text = None
        self.progressbar.set_text(text)
        self.progressbar.set_show_text(show_text)

    def on_timeout(self, user_data):
        """
        Update value on the progress bar
        """
        if self.activity_mode:
            self.progressbar.pulse()
        else:
            new_value = self.progressbar.get_fraction() + 0.01

            if new_value > 1:
                new_value = 0

            self.progressbar.set_fraction(new_value)

        # As this is a timeout function, return True so that it
        # continues to get called
        return True


with open("conf.yaml") as conf_file:
    conf = yaml.load(conf_file, Loader=yaml.Loader)



with open("sql.yaml") as sql_file:
    sql = yaml.load(sql_file, Loader=yaml.Loader)

print(sql["create-locations-table"])



#weather = Weather(conf)

#if weather.get_count_locations() == 0:
#    weather.first_run_setup()

    #progress = ProgressBarWindow(weather.populate_db)
    #progress.connect("destroy", Gtk.main_quit)
    #progress.show_all()
    #Gtk.main()
