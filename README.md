# Simple Python Weather App

A command-line weather application that fetches current weather data using the OpenWeatherMap API.

## Features

- Get current weather for any city worldwide
- Display temperature, humidity, pressure, and wind speed
- Uses metric units (Celsius)
- Simple and intuitive command-line interface
- Continuous operation until user exits

## Prerequisites

- Python 3.6 or higher
- OpenWeatherMap API key (free tier available)

## Setup Instructions

### 1. Get an API Key

1. Go to [OpenWeatherMap](https://openweathermap.org/api)
2. Sign up for a free account
3. Navigate to API keys section
4. Copy your API key

### 2. Install Dependencies

```bash
uv pip install -r requirements.txt
```

### 3. Configure Environment Variables

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Edit the `.env` file and add your API key:
   ```
   OPENWEATHER_API_KEY=your_actual_api_key_here
   ```

## Usage

Run the application:

```bash
python weather.py
```

Enter a city name when prompted:

```
Welcome to the Weather App!
Type 'quit' or 'exit' to close the app.

Enter city name: London
```

The app will display current weather information:

```
==================================================
Weather in London, GB
==================================================
Time: 2025-11-11 14:30:00
Condition: Cloudy
Temperature: 15.5°C (Feels like 14.2°C)
Humidity: 72%
Pressure: 1013 hPa
Wind Speed: 5.5 m/s
==================================================
```

To exit the app, type `quit` or `exit`.

## Project Structure

```
.
├── weather.py          # Main application file
├── requirements.txt    # Python dependencies
├── .env.example       # Example environment variables
├── .env               # Your API key (create this, not tracked in git)
└── README.md          # This file
```

## Dependencies

- **requests**: For making HTTP requests to the OpenWeatherMap API
- **python-dotenv**: For loading environment variables from .env file

## Error Handling

The app handles common errors:
- City not found
- Network connection issues
- Missing API key
- Invalid API responses

## License

This project is open source and available for educational purposes.
