# Weather App

A terminal-based weather application that fetches real-time weather data for any city using the [OpenWeatherMap API](https://openweathermap.org/api).

## Features

- Get current temperature, feels-like temp, condition, and humidity
- City-not-found error handling
- Internet connection error handling
- Loop to check multiple cities in one session

## Requirements

- Python 3.x
- `requests`

```bash
pip install requests
```

## Setup

You need an OpenWeatherMap API key. Open `weather_app.py` and replace:

```python
API_KEY = "YOUR_API_KEY"
```

with your actual API key from [openweathermap.org](https://openweathermap.org/api).

## How to Run

```bash
python weather_app.py
```

## Example Output

```
===================================
       WEATHER APP (CLI)
===================================

Enter city name (or 'exit' to quit): London

===================================
  Weather for Tamil Nadu
===================================
  Temperature : 14.2°C
  Feels Like  : 12.8°C
  Condition   : Clouds
  Humidity    : 76%
===================================
```