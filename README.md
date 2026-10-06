# Weather Simulator 🌦️

A Python-based **weather application** that provides real-time weather information, forecasts, geographical data and weather visualizations for cities around the world.

The original application is built with **Tkinter** as a desktop graphical interface and retrieves weather data using the **OpenWeatherMap API**.

The project can also be extended into a web application using **Streamlit**.

---

## About the Project

**Weather Simulator** is an interactive weather application developed in Python.

The application allows users to search for a city and retrieve weather-related information such as:

- Temperature
- Humidity
- Atmospheric pressure
- Wind speed
- Weather conditions
- Multi-day forecasts
- Sunrise and sunset times
- Local time
- Geographic location

The project combines graphical interface development, API integration, geolocation and weather-data visualization.

---

## Features

### 🌤️ Current Weather

Retrieve weather information for a selected city, including:

- Temperature
- Humidity
- Atmospheric pressure
- Wind speed
- Weather description
- Weather icons

---

### 📅 Weather Forecast

The application retrieves weather forecasts from the **OpenWeatherMap API**.

It can display temperatures for multiple days and distinguish between daytime and nighttime temperatures.

---

### 🌅 Sunrise & Sunset

Search for a city and retrieve:

- Sunrise time
- Sunset time

The information is calculated using weather and geographical data.

---

### 🌍 Geolocation

The project uses geographical services to retrieve:

- Latitude
- Longitude
- City location
- Time zone

Geolocation is handled using libraries such as:

- `geopy`
- `timezonefinder`

---

### 🕐 Local Time

Based on the geographical coordinates of a searched city, the application determines its time zone and displays the local time.

---

### 🗺️ Weather Map

The project includes map functionality using:

```text
tkintermapview
```

This allows geographical information to be displayed directly inside the desktop interface.

---

### 📊 Weather Visualization

The application contains dedicated functionality for graphical weather analysis using:

- Matplotlib
- NumPy

Weather information can therefore be represented visually rather than only as text.

---

### 🌙 Dark / Light Mode

The desktop interface includes a theme switch allowing users to switch between:

- Light mode
- Dark mode

---

### ⌨️ Virtual Keyboard

A virtual keyboard is available for entering city names directly from the graphical interface.

---

## Technologies

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![OpenWeatherMap](https://img.shields.io/badge/OpenWeatherMap-API-orange)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-FF4B4B?logo=streamlit&logoColor=white)

Main technologies and libraries used:

- **Python**
- **Tkinter**
- **OpenWeatherMap API**
- **Requests**
- **Geopy**
- **TimezoneFinder**
- **PyTZ**
- **Pillow**
- **TkinterMapView**
- **Matplotlib**
- **NumPy**

---

## How It Works

The application follows the following workflow:

```text
User enters a city
        │
        ▼
Geolocation
        │
        ▼
Latitude / Longitude
        │
        ├──────────────► Time Zone
        │
        ▼
OpenWeatherMap API
        │
        ▼
Weather Data
        │
        ├── Temperature
        ├── Humidity
        ├── Pressure
        ├── Wind
        ├── Forecast
        ├── Weather Condition
        └── Sunrise / Sunset
        │
        ▼
Graphical Interface
```

---

## Project Structure

The repository contains several Python modules and graphical assets.

```text
Weather-Simulator/
│
├── Main.py
├── pagePrincipale.py
├── graphiques.py
├── sunrise_sunset.py
├── sunsetSunrise.py
├── switch_mod.py
├── suntime.py
│
├── weather icons
│   ├── 01d@2x.png
│   ├── 01n@2x.png
│   ├── 02d@2x.png
│   ├── ...
│   └── 50n@2x.png
│
├── interface assets
│   ├── weather.png
│   ├── sunrise.png
│   ├── sunset.png
│   ├── temperature.png
│   ├── pression.png
│   ├── vent.png
│   └── ...
│
└── README.md
```

### Main files

`Main.py`

Contains a large part of the weather logic and the main weather interface.

`pagePrincipale.py`

Contains the main navigation interface, theme management and access to the different application modules.

`graphiques.py`

Handles graphical visualization of weather information.

`sunrise_sunset.py`

Provides sunrise and sunset information for a searched city.

`switch_mod.py`

Contains the light / dark mode switching functionality.

---

## API Integration

Weather data is retrieved using the **OpenWeatherMap API**.

Example endpoint:

```text
https://api.openweathermap.org/data/2.5/weather
```

Forecast information is retrieved through:

```text
https://api.openweathermap.org/data/2.5/forecast
```

The application sends the city name to the API and processes the returned JSON data.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/hanaekhayyi/Weather-Simulator.git
```

Navigate to the project:

```bash
cd Weather-Simulator
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## Requirements

A `requirements.txt` file can contain:

```text
requests
geopy
timezonefinder
pytz
Pillow
tkintermapview
matplotlib
numpy
geocoder
suntime
streamlit
```

> Tkinter is usually included with standard Python installations, but depending on your operating system it may need to be installed separately.

---

## Environment Variables

The OpenWeatherMap API key should not be stored directly inside the Python source code.

Create a `.env` file:

```env
OPENWEATHER_API_KEY=your_api_key_here
```

Then load the API key from the environment.

The `.env` file should be excluded from Git using `.gitignore`.

---

## Run the Desktop Application

Run the main application with:

```bash
python pagePrincipale.py
```

or depending on the desired entry point:

```bash
python Main.py
```

---

## Streamlit Web Version

The project can also be extended into a web-based weather dashboard using **Streamlit**.

Instead of using a Tkinter desktop interface, Streamlit can provide an application accessible directly from a browser.

The web version could include:

- City search
- Current temperature
- Humidity
- Atmospheric pressure
- Wind speed
- Weather condition
- Weather icon
- Sunrise and sunset
- Geographic coordinates
- Multi-day forecast
- Interactive weather charts
- Weather map

---

## Recommended Structure for Streamlit

```text
Weather-Simulator/
│
├── app.py
├── weather_service.py
│
├── Main.py
├── pagePrincipale.py
├── graphiques.py
├── sunrise_sunset.py
│
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
│
└── assets/
    ├── weather icons/
    └── interface images/
```

`app.py`

Contains the Streamlit web interface.

`weather_service.py`

Contains the logic used to communicate with the OpenWeatherMap API.

This separation makes the project easier to maintain because the interface and API logic are no longer mixed together.

---

## Run the Streamlit Application

Install the dependencies:

```bash
pip install -r requirements.txt
```

Then launch:

```bash
streamlit run app.py
```

The application will normally be available at:

```text
http://localhost:8501
```

---

## Project Evolution

The project demonstrates an evolution from a Python desktop application toward a modern web application.

```text
Python
  │
  ▼
Weather API Integration
  │
  ▼
Tkinter Desktop Application
  │
  ▼
Weather Visualizations
  │
  ▼
Streamlit Web Dashboard
```

This progression demonstrates several important software development skills:

- Python programming
- REST API consumption
- JSON processing
- GUI development
- Data visualization
- Geolocation
- Modular programming
- Web application development

---

## Concepts Practiced

This project demonstrates:

- Python programming
- Object and function-based application design
- REST API integration
- HTTP requests
- JSON processing
- GUI development with Tkinter
- Web application development with Streamlit
- Geolocation
- Time-zone handling
- Weather-data processing
- Data visualization
- Image handling
- External library integration
- Error handling

---

## Possible Improvements

Future improvements could include:

- Refactoring duplicated weather functions
- Moving the API key to environment variables
- Improved error handling
- Interactive weather charts
- Historical weather analysis
- Location autocomplete
- Automatic geolocation
- Improved map visualization
- Weather alerts
- Hourly forecasts
- Air-quality information
- Responsive Streamlit interface
- Cloud deployment
- Weather data caching
- Unit selection between Celsius and Fahrenheit

---

## Deployment

A Streamlit version of the project could be deployed using **Streamlit Community Cloud**.

Once deployed, users would be able to access the weather application directly from their browser.

```text
Live Demo: Coming soon
```

---

## Author

**Hanae KHAYYI**

Data & AI Engineering Student

GitHub: [@hanaekhayyi](https://github.com/hanaekhayyi)

---

⭐ If you found this project useful, feel free to star the repository.
