#!/usr/bin/env python3
"""
Hot Tub Evaporation Model

Estimates daily water loss from an outdoor hot tub based on:
- Physical dimensions
- Water and air temperatures
- Humidity
- Wind conditions
- Surface agitation from jets
"""

import math

def vapor_pressure_mmhg(temp_f):
    """
    Calculate saturated vapor pressure using Antoine equation.

    Args:
        temp_f: Temperature in Fahrenheit

    Returns:
        Vapor pressure in mmHg
    """
    # Convert to Celsius
    temp_c = (temp_f - 32) * 5/9

    # Antoine equation for water (valid 1-100°C)
    # log10(P) = A - B/(C + T)
    A, B, C = 8.07131, 1730.63, 233.426

    log_p = A - (B / (C + temp_c))
    pressure_mmhg = 10 ** log_p

    return pressure_mmhg

def calculate_evaporation_rate(
    water_temp_f,
    air_temp_f,
    relative_humidity_percent,
    wind_speed_mph,
    surface_area_sqft,
    churn_area_percent,
    exposure_hours_per_day
):
    """
    Calculate hot tub evaporation using modified pool evaporation formulas.

    The model uses:
    1. Vapor pressure gradient (water vs air)
    2. Wind factor (increases boundary layer removal)
    3. Agitation factor (jets churning increases effective evaporation)
    4. Exposure time (covered vs uncovered)

    Returns:
        Dictionary with evaporation estimates in gallons/day
    """

    # Calculate vapor pressures
    pw_water = vapor_pressure_mmhg(water_temp_f)  # Saturated VP at water surface
    pw_air = vapor_pressure_mmhg(air_temp_f)       # Saturated VP at air temp

    # Actual vapor pressure in air (accounting for humidity)
    pa_air = pw_air * (relative_humidity_percent / 100)

    # Vapor pressure deficit (driving force for evaporation)
    vp_deficit = pw_water - pa_air  # mmHg

    print(f"\n--- Vapor Pressure Analysis ---")
    print(f"Saturated VP at water surface ({water_temp_f}°F): {pw_water:.1f} mmHg")
    print(f"Saturated VP in air ({air_temp_f}°F): {pw_air:.1f} mmHg")
    print(f"Actual VP in air ({relative_humidity_percent}% RH): {pa_air:.1f} mmHg")
    print(f"Vapor pressure deficit: {vp_deficit:.1f} mmHg")

    # Base evaporation rate (still water, no wind)
    # Using empirical formula: E = k × (Pw - Pa)
    # where k ≈ 0.001 to 0.002 inches/day per mmHg for pools
    # For hot water, using k = 0.0018
    k_base = 0.0018  # inches per day per mmHg

    base_evap_inches_per_day = k_base * vp_deficit

    # Wind factor - increases evaporation by removing humid boundary layer
    # Multiplier = 1 + (wind_speed_mph × 0.04)
    # This means 5 mph wind increases evaporation by ~20%, 10 mph by ~40%
    wind_multiplier = 1 + (wind_speed_mph * 0.04)

    # Agitation factor - jets churning the water
    # Split surface into churned and still portions
    churn_fraction = churn_area_percent / 100
    still_fraction = 1 - churn_fraction

    # Churned water evaporates 1.8-2.5x faster (using 2.0x)
    # This accounts for: increased surface area from bubbles,
    # faster water turnover, disrupted boundary layer
    churn_multiplier = 2.0

    # Effective evaporation multiplier (weighted average)
    agitation_multiplier = (still_fraction * 1.0) + (churn_fraction * churn_multiplier)

    # Combined evaporation rate (24-hour basis)
    evap_rate_full_day = (base_evap_inches_per_day *
                          wind_multiplier *
                          agitation_multiplier)

    # Adjust for actual exposure time
    exposure_fraction = exposure_hours_per_day / 24
    evap_rate_actual = evap_rate_full_day * exposure_fraction

    # Convert to volume loss
    # Volume = area × depth
    volume_cubic_feet = surface_area_sqft * (evap_rate_actual / 12)  # inches to feet
    volume_gallons = volume_cubic_feet * 7.48  # cubic feet to gallons

    # Alternative high-estimate using industry rule of thumb
    # Hot tubs: 0.25-0.5 inches/day base × multipliers
    industry_base = 0.35  # inches/day for hot tub
    industry_estimate = (industry_base * wind_multiplier * agitation_multiplier *
                        exposure_fraction * surface_area_sqft / 12 * 7.48)

    return {
        'evap_inches_per_day': evap_rate_actual,
        'evap_gallons_per_day': volume_gallons,
        'industry_estimate_gallons': industry_estimate,
        'base_rate': base_evap_inches_per_day,
        'wind_multiplier': wind_multiplier,
        'agitation_multiplier': agitation_multiplier,
        'exposure_fraction': exposure_fraction,
        'vp_deficit_mmhg': vp_deficit
    }

def main():
    print("=" * 60)
    print("HOT TUB EVAPORATION CALCULATOR")
    print("=" * 60)

    # Get inputs from user
    print("\n--- Hot Tub Specifications ---")
    diameter_ft = float(input("Hot tub diameter (feet) [default: 12]: ") or "12")
    water_temp = float(input("Water temperature (°F) [default: 102]: ") or "102")
    exposure_hours = float(input("Hours exposed per day [default: 14]: ") or "14")

    print("\n--- Environmental Conditions ---")
    air_temp = float(input("Average air temperature (°F) [default: 70]: ") or "70")
    humidity = float(input("Relative humidity (%) [default: 35]: ") or "35")
    wind_speed = float(input("Average wind speed (mph) [default: 5]: ") or "5")

    print("\n--- Jets/Agitation ---")
    churn_percent = float(input("Percentage of surface area being churned by jets (0-100%) [default: 25]: ") or "25")

    # Calculate surface area
    radius_ft = diameter_ft / 2
    surface_area = math.pi * radius_ft ** 2

    print(f"\n--- Calculated Surface Area ---")
    print(f"Surface area: {surface_area:.1f} square feet")

    # Run the model
    results = calculate_evaporation_rate(
        water_temp_f=water_temp,
        air_temp_f=air_temp,
        relative_humidity_percent=humidity,
        wind_speed_mph=wind_speed,
        surface_area_sqft=surface_area,
        churn_area_percent=churn_percent,
        exposure_hours_per_day=exposure_hours
    )

    # Display results
    print("\n" + "=" * 60)
    print("EVAPORATION MODEL RESULTS")
    print("=" * 60)

    print(f"\n--- Multipliers ---")
    print(f"Wind multiplier: {results['wind_multiplier']:.2f}x")
    print(f"Agitation multiplier: {results['agitation_multiplier']:.2f}x")
    print(f"Exposure time factor: {results['exposure_fraction']:.2f}x ({exposure_hours} hrs/day)")

    print(f"\n--- Water Loss Estimates ---")
    print(f"Base evaporation rate: {results['base_rate']:.3f} inches/day")
    print(f"Actual evaporation rate: {results['evap_inches_per_day']:.3f} inches/day")
    print(f"\n💧 ESTIMATED DAILY WATER LOSS: {results['evap_gallons_per_day']:.1f} gallons/day")
    print(f"   (Industry rule-of-thumb estimate: {results['industry_estimate_gallons']:.1f} gallons/day)")

    # Additional insights
    print(f"\n--- Additional Insights ---")
    weekly_loss = results['evap_gallons_per_day'] * 7
    monthly_loss = results['evap_gallons_per_day'] * 30
    print(f"Weekly water loss: ~{weekly_loss:.0f} gallons")
    print(f"Monthly water loss: ~{monthly_loss:.0f} gallons")

    # Calculate water depth loss
    depth_loss_per_day = results['evap_inches_per_day']
    days_to_lose_one_inch = 1 / depth_loss_per_day if depth_loss_per_day > 0 else float('inf')
    print(f"Water level drops {depth_loss_per_day:.3f} inches per day ({days_to_lose_one_inch:.1f} days per inch)")

    print("\n" + "=" * 60)
    print("SENSITIVITY NOTES:")
    print("- Doubling wind speed increases loss by ~20-40%")
    print("- Each 10°F increase in water temp adds ~15-25% loss")
    print("- Each 10% drop in humidity adds ~10-15% loss")
    print("- Aggressive jets (50% churn) can add 25-50% to loss")
    print("=" * 60)

if __name__ == "__main__":
    main()
