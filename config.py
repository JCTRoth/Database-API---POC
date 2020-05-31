import json


class config:

    config = ""  # Config Storage

    def __init__(self):
        return

    def read_config_file(self):
        # Loads Project Config into Class Obj.
        confFile = open("config.json", "r")
        self.config = json.loads(confFile.read())
