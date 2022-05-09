from datetime import datetime, timezone, timedelta
import requests
from geopy.geocoders import Nominatim  # pip install geopy

class Open_Weather:
    def __init__(self, city):
        self.city = city
        self.res = self.fetch_open_weather()


    @property
    def day(self):
        return self._day


    @day.setter
    def day(self, value):
        self._day = value


    @property
    def hour(self):
        return self._hour


    @hour.setter
    def hour(self, value):
        self._hour = value


    def segment_of_the_day(self):
        #day, night, eve, morning
        h = int(str(self.formate_hour_string(self.hour)).replace(":", ""))
        if h > 2200 or h < 600:
            return 'night'
        if h > 600 and h < 1200:
            return 'morning'
        if h > 1200 and h < 1800:
            return 'day'
        if h > 1800 and h < 2200:
            return 'eve'

    def city_coordinate(self):
        geolocator = Nominatim(user_agent="Your_Name")
        location = geolocator.geocode(self.city)
        return location.latitude, location.longitude


    def unix_to_dt(self, unix):
        from datetime import datetime
        ts1 = int(unix)
        return datetime.utcfromtimestamp(ts1).strftime('%d/%m/%Y %H:%M')


    def formate_hour_string(self):
        if len(self.hour) == 5:
            if ":" in self.hour:
                return self.hour
        if len(self.hour)==4:
            if self.hour[0] == 0 or self.hour[0] == 1:
                return f'{self.hour[0]}{self.hour[1]}:{self.hour[2]}{self.hour[3]}'
        if len(self.hour) == 3:
            return f'0{self.hour[0]}:{self.hour[1]}{self.hour[2]}'


    def time_parse(self):
        def today():
            timezone_offset = -3.0
            tzinfo = timezone(timedelta(hours=timezone_offset))
            data = datetime.strptime(datetime.now(tzinfo).strftime('%d/%m/%Y %H:%M'), '%d/%m/%Y %H:%M')
            return data
        def intended_day():
            timezone_offset = -3.0
            tzinfo = timezone(timedelta(hours=timezone_offset))
            cdate = (datetime.now(tzinfo) + timedelta(days=self.day)).strftime('%d/%m/%Y')
            data = datetime.strptime(cdate, '%d/%m/%Y')
            data = data.strftime('%d/%m/%Y')
            return data
        dt = datetime.strptime(f'{intended_day()} {self.formate_hour_string(self.hour)}', '%d/%m/%Y %H:%M')
        return dt - today()

    def fetch_open_weather(self):
        from conf import api_key
        part0 = 'minutely'
        part1 = 'hourly'
        part2 = 'alerts'
        part = part0 + ',' + part2
        lat, lon = self.city_coordinate()
        url = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&units=metric&lang=pt_br&appid={api_key}'
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT x.y; Win64; x64; rv:10.0) Gecko/20100101 Firefox/10.0 '}
        response = requests.get(url, headers=header)
        res = response.json()
        return res


    def min_temp(self) -> float:
        return self.res.get('daily')[self.day].get('temp').get('min')


    def max_temp(self) -> float:
        return self.res.get('daily')[self.day].get('temp').get('max')


    def mean_temperature(self) -> float:
        return self.res.get('daily')[self.day].get('temp').get('day')


    def termic_sensation(self) -> float:  # section referes to the section of the day (day, night, eve, morning)
        section = self.segment_of_the_day()
        return self.res.get('daily')[self.day].get('feels_like').get(section)


    def wind_speed(self) -> float:
        return self.res.get("daily")[self.day].get("wind_speed")


    def wind_direction(self) -> int:
        return self.res.get("daily")[self.day].get("wind_deg")


    def weather_description(self) -> str:
        return self.res.get("daily")[self.day].get("weather")[0].get('description')


    def hourly_temperature(self) -> float:
        t = int(str(self.time_parse(self.day, self.hour)).split(':')[0])
        return self.res.get("hourly")[t].get("temp")


    def humidity(self) -> int:
        return self.res.get('daily')[self.day].get('humidity')


    def chance_of_rain(self) -> int:
        return self.res.get('daily')[self.day].get('pop')


    def moon_fase(self) -> float:
        return self.res.get('daily')[0].get("moon_phase")


    def sun_time(self) -> dict:
        sunrise = self.unix_to_dt(self.res.get('daily')[self.day].get("sunrise"))
        sunset = self.unix_to_dt(self.res.get('daily')[self.day].get("sunset"))
        return {"sunrise": sunrise, "sunset": sunset}
