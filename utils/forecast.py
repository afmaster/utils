import requests
res = {}
#https://github.com/chubin/wttr.in

def fetch_weather(city='porto_alegre'):
    url = f'https://wttr.in/{city}?format=j1'
    response = requests.get(url)
    res = response.json()
    return res



def time_parse(hour):
    times = [0, 300, 600, 900, 1200, 1500, 1800, 2100]
    hour = hour.replace(":", "")
    if hour[0] == "0":
        hour = hour[1:]
    hour = int(hour)

    subtraction = []
    for item in times:
        sub = item - hour
        if sub < 0:
            sub = sub *(-1)
        subtraction.append(sub)
    match = min(subtraction)
    index = subtraction.index(match)
    return index


def data(res, day):
    return res.get("weather")[day].get("date")


def min_temp(res, day):
    return res.get("weather")[day].get("mintempC")

def max_temp(res, day):
    return res.get("weather")[day].get("maxtempC")


def wind_speed(res, day, hour):
    h = time_parse(hour)
    return res.get("weather")[day].get("hourly")[h].get("windspeedKmph")

def wind_direction(res, day, hour):
    h = time_parse(hour)
    return res.get("weather")[day].get("hourly")[h].get("winddir16Point")

def weather_description(res, day, hour):
    h = time_parse(hour)
    return res.get("weather")[day].get("hourly")[h].get("weatherDesc")

def temperature(res, day, hour):
    h = time_parse(hour)
    return res.get("weather")[day].get("hourly")[h].get("tempC")

def humidity(res, day, hour):
    h = time_parse(hour)
    return res.get("weather")[day].get("hourly")[h].get("humidity")

def chance_of_rain(res, day, hour):
    h = time_parse(hour)
    return res.get("weather")[day].get("hourly")[h].get("chanceofrain")

def termic_sensation(res, day, hour):
    h = time_parse(hour)
    return res.get("weather")[day].get("hourly")[h].get("FeelsLikeC")

def moon_fase(res):
    return res.get("weather")[0].get("astronomy")[0].get("moon_phase")

def sun_time(res):
    sunrise = res.get("weather")[0].get("astronomy")[0].get("sunrise")
    sunset = res.get("weather")[0].get("astronomy")[0].get("moon_phsunsetase")
    return {"sunrise": sunrise, "sunset": sunset}




if __name__ == "__main__":
    print(time_parse("17:20"))
