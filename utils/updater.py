from configparser import ConfigParser

class New():
    global user = ''
    global db = ''

    def __init__(self):
        self.config = ConfigParser()

    def read_old(self):
        pass

    def new_data(self):
        new = {
            "user": user,
            "db": db
        }
        return new

    def parse_new_data(self):
        old = self.read_old()
        new = self.new_data()
        up_to_date = str(old) + '\n' + str(new)
        return up_to_date

    def update(self):
        new_data = self.parse_new_data()
        with open("config.ini", "w") as f:
            self.config.write(f)
