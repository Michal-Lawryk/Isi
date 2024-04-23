import requests
import matplotlib.pyplot as plt

# Documentation: https://open-meteo.com/en/docs/

# Weather codes for open-meteo API (for later usage)
weather_codes = {
    (0,): "czyste niebo",
    (1,): "głównie bezchmurnie",
    (2,): "częściowo pochmurno",
    (3,): "pochmurno",
    (45,): "mgła",
    (48,): "opadająca mgła szronowa",
    (51,): "mżawka lekka",
    (53,): "mżawka umiarkowana",
    (55,): "mżawka gęsta",
    (56,): "zamrażająca mżawka: lekka",
    (57,): "zamrażająca mżawka: gęsta intensywność",
    (61,): "deszcz słaby",
    (63,): "deszcz umiarkowany",
    (65,): "deszcz intensywny",
    (66,): "marznący deszcz: intensywność lekka",
    (67,): "marznący deszcz: intensywność ciężka",
    (71,): "opady śniegu: intensywność niewielka",
    (73,): "opady śniegu: intensywność umiarkowana",
    (75,): "opady śniegu: intensywność duża",
    (77,): "ziarna śniegu",
    (80,): "przelotne opady deszczu: słabe",
    (81,): "przelotne opady deszczu: umiarkowane",
    (82,): "przelotne opady deszczu: gwałtowne",
    (85,): "opady śniegu lekkie",
    (86,): "opady śniegu intensywne",
    (95,): "burza: Słaba lub umiarkowana",
    (96,): "burza z lekkim gradem",
    (99,): "burza z silnym gradem",
}

# Coordinates for few places in the format (latitude, longitude)
coordinates = {
    "Gowino": ("54.57", "18.20"),
    "Gdynia": ("54.52", "18.53"),
    "Warszawa": ("52.237", "21.017"),
    "Tokyo": ("35.65", "139.84"),
    "Paryz": ("48.52", "2.21")
}

if __name__ == '__main__':

    for place, coords in coordinates.items():
        weather_url = (f"https://api.open-meteo.com/v1/forecast"
                       f"?latitude={coords[0]}&longitude={coords[1]}"
                       f"&daily=temperature_2m_max,&past_days=31")

        weather = requests.get(weather_url).json()

        temp = weather["daily"]["temperature_2m_max"]
        date = weather["daily"]["time"]
        date = [x[5:] for x in date]  # leave month and day only

        # print(gdynia_weather["daily"]["temperature_2m_max"])

        fig, ax = plt.subplots()

        ax.plot(date, temp, '-')
        ax.set_ylabel('temperature [C]')
        ax.set_xlabel('date')
        fig.autofmt_xdate()
        plt.grid(axis='both', alpha=0.5)
        plt.title(place)
        fig.set_size_inches(16, 12)
        plt.savefig(place + ".png")
