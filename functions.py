
import requests

API_KEY = "7e36ded011f6507a04a02c1405829767"


def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?" \
          f"q={place}&appid={API_KEY}" \
          f"&units=imperial"
    response = requests.get(url)
    data = response.json()
    filtered = data["list"]
    nr_values = 8 * forecast_days
    filtered_data1 = filtered[0:nr_values]
    return filtered_data1


if __name__ == "__main__":
    filtered_data = get_data(place="Tokyo", forecast_days=3)


