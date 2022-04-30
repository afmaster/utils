from configparser import ConfigParser


config_dic = {
        'my_email': 'testtesttest@gtest.com',
        'password': '123456'
    }

def set_config():
    config = ConfigParser()
    config["DEFAULT"] = config_dic
    with open("config.ini", "w") as f:
        config.write(f)

def import_config(section, parameter):
    config = ConfigParser()
    config.read("config.ini")
    config_data = config[section]
    search_variable = config_data[parameter]
    return search_variable


if __name__ == "__main__":
    set_config()
    print(import_config('DEFAULT', 'my_email'))