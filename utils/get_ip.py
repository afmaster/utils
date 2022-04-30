import requests

def ip() -> dict:
    r = requests.get('https://httpbin.org/ip')
    response = r.json()
    return response

if __name__ == "__main__":
    IP = ip()
    print(type(IP))