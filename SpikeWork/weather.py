import sqlite3
import pyowm
import gi
from parser import Parser
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk


class Weather:

    def __init__(self, conf, sql):

        self.conf = conf
        self.sql = sql

        self.owm = pyowm.OWM(self.conf["api_key"])  # you MUST provide a valid API key

        self.db = sqlite3.connect('weather.db')
        cursor = self.db.cursor()

        cursor.execute(self.sql["create-location-table"])
        cursor.execute(self.sql["create-record-table"])
        cursor.execute(self.sql["create-country-table"])
        cursor.close()

    def get_count_locations(self):
        cursor = self.db.cursor()
        cursor.execute(self.sql["get-count-locations"])
        return cursor.fetchone()[0]

    def first_run_setup(self):
        self.read_cities_json()
        self.clear_db()
        self.populate_db()
        pass

    def read_cities_json(self):
        self.streamer = Parser()
        with open("temp.json") as file:
            self.streamer.parse(file)

    def clear_db(self):
        cursor = self.db.cursor()
        cursor.execute("delete from {0};".format(self.loc_table))
        cursor.execute("delete from {0};".format(self.rec_table))
        cursor.execute("delete from {0};".format(self.countries_table))
        self.db.commit()
        cursor.close()

    def populate_db(self):
        cursor = self.db.cursor()
        for country in self.streamer.country_list:
            print("insert into {0} ({1}) values ('{2}');".format(
                self.countries_table, self.countries_cols[1], country))
            cursor.execute("insert into {0} ({1}) values ('{2}');".format(
                self.countries_table, self.countries_cols[1], country))
        self.db.commit()
        cursor.close()
