import sqlite3
import pyowm
from jsonstreamer import JSONStreamer
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk


class Weather:

    def __init__(self, conf):

        loc_table = "Locations"
        loc_cols = ["id", "name", "country", "lat", "lon"]
        day_table = "Days"
        loc_create = "create table if not exists {0} ({1}, {2}, {3}, {4}, {5})"

        self.owm = pyowm.OWM(conf["api_key"])  # you MUST provide a valid API key

        self.db = sqlite3.connect('weather.db')
        cursor = self.db.cursor()

        cursor.execute(loc_create.format(loc_table, *loc_cols))

        cursor.execute("Select count(*) from %s" % loc_table)
        if cursor.fetchone()[0] == 0:
            self.populate_db()

    def populate_db(self):
        print("opening json")
        streamer = JSONStreamer()
        i = 0
        with open("city.list.json") as file:
            for line in file:
                # streamer.add_catch_all_listener(_catch_all)
                streamer.consume(line)
                i += 1
            streamer.close()
        print(i)
        print(streamer)
