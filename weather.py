import sqlite3
import pyowm
import gi
from parser import Parser
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk


class Weather:

    def __init__(self, conf):

        self.loc_table = "Locations"
        self.loc_cols = ["id", "name", "country", "lat", "lon"]
        self.day_table = "Days"

        loc_create = "create table if not exists {0} ({1}, {2}, {3}, {4}, {5})"

        self.owm = pyowm.OWM(conf["api_key"])  # you MUST provide a valid API key

        self.db = sqlite3.connect('weather.db')
        cursor = self.db.cursor()

        cursor.execute(loc_create.format(self.loc_table, *self.loc_cols))

        print(self.get_count_locations())

    def get_count_locations(self):
        cursor = self.db.cursor()
        cursor.execute("Select count(*) from %s" % self.loc_table)
        return cursor.fetchone()[0]

    def populate_db(self):

        print("count lines")
        num_lines = sum(1 for line in open('city.list.json'))
        # percent_lines = int(num_lines / 10)
        print(num_lines)
        print("opening json")
        streamer = Parser()
        i = 0
        with open("city.list.json") as file:
            for line in file:
                #print("---->")
                #print(line, end="")
                streamer.parse(line)
                #print("----<\n")
                i += 1
                # if (i % percent_lines == 0):
                # yield(i)
            streamer.close()
        # for item in streamer.list:
            # print(item)
        for item in streamer.country_list:
            print(item)
        print(len(streamer.country_list))
        print(len(streamer.location_list))
