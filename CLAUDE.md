# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a Python practice repository containing standalone educational scripts and utilities. Each Python file is self-contained and demonstrates specific concepts or functionality.

## Environment Setup

The project uses a Python virtual environment located at `.venv/`.

### Install Dependencies

```bash
uv pip install -r requirements.txt
```

Required packages:
- `requests==2.31.0` - HTTP library for API calls
- `python-dotenv==1.0.0` - Environment variable management

### Environment Variables

API keys and credentials are stored in `.env` (not tracked in git). Use `.env.example` as a template:

```bash
cp .env.example .env
```

Required variables:
- `OPENWEATHER_API_KEY` - OpenWeatherMap API key for weather.py

## Running Scripts

All Python scripts are executable and can be run directly:

```bash
python weather.py
python hot_tub_evaporation.py
python list_comprehensions_demo.py
```

Or with the shebang:

```bash
./weather.py
```

## Project Structure

The repository contains independent Python scripts, each with a specific purpose:

### weather.py
Interactive command-line weather application using the OpenWeatherMap API. Implements a class-based architecture with `WeatherApp` handling API calls, data formatting, and the main application loop. Uses environment variables for API key management and includes error handling for network issues and invalid cities.

### hot_tub_evaporation.py
Scientific calculator for estimating hot tub water evaporation. Uses thermodynamic principles including:
- Vapor pressure calculations via Antoine equation
- Wind, agitation, and exposure time multipliers
- Interactive CLI for parameter input
- Detailed output showing intermediate calculations and sensitivity analysis

The model accounts for:
- Vapor pressure gradients between water and air
- Wind effects on boundary layer removal
- Surface agitation from jets (churned vs. still water)
- Partial day exposure (covered vs. uncovered periods)

### hot_tub_dashboard.html
Standalone HTML visualization dashboard for the hot tub evaporation model. No server required - opens directly in browser. Contains embedded JavaScript for interactive calculations and visualizations.

### list_comprehensions_demo.py
Educational script demonstrating Python list comprehension patterns with 10+ examples covering basic transformations, filtering, nested comprehensions, and comparisons with traditional loops.

## Code Patterns

### Error Handling
Scripts use specific exception handling rather than generic catches:
- `requests.exceptions.HTTPError` for API errors
- `requests.exceptions.RequestException` for network issues
- Input validation with continue/break flow control

### User Input
Interactive scripts use a consistent pattern:
- Default values in input prompts: `input("Prompt [default: X]: ") or "X"`
- Exit commands: Accept both 'quit' and 'exit'
- Input validation before processing

### API Integration
When working with external APIs (like OpenWeatherMap):
- API keys loaded from environment via `python-dotenv`
- Timeout parameters on requests (10 seconds)
- Status code checking with `raise_for_status()`
- Graceful error messages for common failures (404, network issues)
