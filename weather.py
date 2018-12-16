import sqlite3
import pyowm


class Weather:

    db = sqlite3.connect('weather.db')
    print (db)

    def __init__(self, conf):
        self.owm = pyowm.OWM(conf["api_key"])  # You MUST provide a valid API key
