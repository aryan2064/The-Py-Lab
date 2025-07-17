import requests

API_KEY = "YOUR_API_KEY"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city_name):
    url = f"{BASE_URL}?q={city_name}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            city = data["name"]
            temp = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            condition = data["weather"][0]["main"]
            humidity = data["main"]["humidity"]

            print("\n" + "=" * 35)
            print(f"  Weather for {city}")
            print("=" * 35)
            print(f"  Temperature : {temp}°C")
            print(f"  Feels Like  : {feels_like}°C")
            print(f"  Condition   : {condition}")
            print(f"  Humidity    : {humidity}%")
            print("=" * 35)
        elif response.status_code == 404:
            print("\nCity not found. Please check the spelling and try again.")
        else:
            print(f"\nError: {data.get('message', 'Something went wrong')}")

    except requests.exceptions.ConnectionError:
        print("\nFailed to fetch data. Please check your internet connection.")
    except requests.exceptions.RequestException:
        print("\nFailed to fetch data. Please try again later.")


def main():
    print("=" * 35)
    print("       WEATHER APP (CLI)")
    print("=" * 35)

    while True:
        city = input("\nEnter city name (or 'exit' to quit): ").strip()

        if city.lower() == "exit":
            print("\nGoodbye!")
            break

        if city == "":
            print("City name cannot be empty. Please try again.")
            continue

        get_weather(city)


if __name__ == "__main__":
    main()