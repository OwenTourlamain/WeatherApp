import yaml
import gi
import weather
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk


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


with open("conf.yaml") as conf_file:
    conf = yaml.load(conf_file, Loader=yaml.Loader)

weather = weather(conf)

# Have a pro subscription? Then use:
# owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

# Search for current weather in London (Great Britain)
observation = owm.weather_at_place('London,GB')
w = observation.get_weather()
print(w)                      # <Weather - reference time=2013-12-18 09:20,
                              # status=Clouds>

# Weather details
w.get_wind()                  # {'speed': 4.6, 'deg': 330}
w.get_humidity()              # 87
w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

# Search current weather observations in the surroundings of
# lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
observation_list = owm.weather_around_coords(-22.57, -43.12)


window = WeatherAppWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
