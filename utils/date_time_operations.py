from datetime import datetime, timezone, timedelta, date

def today():
    timezone_offset = -3.0
    tzinfo = timezone(timedelta(hours=timezone_offset))
    data = str(datetime.now(tzinfo).strftime("%d/%m/%Y"))
    return data

def now():
    timezone_offset = -3.0
    tzinfo = timezone(timedelta(hours=timezone_offset))
    data = str(datetime.now(tzinfo).strftime("%d/%m/%Y - %H:%M:%S"))
    return data

def now_simple():
    timezone_offset = -3.0
    tzinfo = timezone(timedelta(hours=timezone_offset))
    data = str(datetime.now(tzinfo).strftime("%d/%m/%Y - %H:%M"))
    return data

def hour():
    timezone_offset = -3.0
    tzinfo = timezone(timedelta(hours=timezone_offset))
    data = str(datetime.now(tzinfo).strftime("%H:%M"))
    return data

def week_day():
    dia = datetime.now().strftime("%d")
    dia = int(dia)
    mes = datetime.now().strftime("%m")
    mes = int(mes)
    ano = datetime.now().strftime("%Y")
    ano = int(ano)
    data = date(year=ano, month=mes, day=dia)
    week_day = data.isoweekday()
    return week_day

def change_day(days):
    return (datetime.now() + timedelta(days=days)).strftime('%d/%m/%Y')