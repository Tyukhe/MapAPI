import requests

def image(lon, lat, delta):
    api_server = "http://static-maps.yandex.ru/1.x/"

    params = {
        "ll": ",".join([lon, lat]),
        "spn": ",".join([delta, delta]),
        "l": "map"
    }
    response = requests.get(api_server, params=params)

    if not response:
        return response.status_code, response.reason

    map_file = "data\map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
        return map_file