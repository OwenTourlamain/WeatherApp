from jsonstreamer import JSONStreamer


class Parser:

    def __init__(self):
        self._obj_streamer = JSONStreamer()  # same for JSONStreamer

        # this automatically finds listeners in this class and attaches them if they are named
        # using the following convention '_on_eventname'. Note method names in this class
        self._obj_streamer.auto_listen(self)
        self.location_list = []
        self.country_list = []
        self.current_obj = {}
        self.current_key = None

    def _on_object_end(self):
        if self.current_obj != {}:
            self.location_list.append(self.current_obj.copy())
            self.current_obj = {}
            self.current_key = None

    def _on_key(self, key):
        self.current_key = key

    def _on_value(self, value):
        if self.current_key == "country":
            if value not in self.country_list:
                self.country_list.append(value)
        self.current_obj[self.current_key] = value

    def consume(self, data):
        self._obj_streamer.consume(data)

    def parse(self, file):
        i = 0
        for line in file:
            self.consume(line)
            i += 1
        self.close()
        return i

    def close(self):
        self._obj_streamer.close()
