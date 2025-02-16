# Observation Table and Performance Calculation for Francis Turbine

## Overview
This Python program takes user inputs for various readings related to a Venturimeter experiment and generates observation tables. It also calculates key performance metrics such as discharge, head, pressure difference, power, and efficiency. The program utilizes the `PrettyTable` library to format and display the collected data in a structured manner.

## Features
- Accepts input readings for Inlet Pressure, Venturimeter Readings (P1 & P2), Speed, Hanger Weight, Spring Balance, and Vacuum Pressure.
- Generates formatted tables for observation data.
- Calculates performance characteristics like net weight, discharge, head, pressure difference, input power, output power, efficiency, and unit parameters.
- Displays results in a tabular format for better readability.

## Requirements
Ensure you have Python installed along with the required dependencies:
```sh
pip install prettytable
```

## Usage
Run the script and provide the required inputs when prompted.
```sh
python script.py
```

### Input:
The user needs to provide:
1. Number of input readings.
2. Speed value (for operating characteristics) or Inlet Pressure and Venturimeter Readings (for main characteristics).
3. Individual readings for Hanger Weight, Spring Balance, and Vacuum Pressure.

### Output:
- Two observation tables (Operating and Main characteristics).
- Calculated values including discharge, power, and efficiency.
- Final formatted tables displaying results.

## Functions
### `operating(number_of_inputs)`
Takes user input readings and returns a list of observation values.

### `main_characteristics(number_of_inputs)`
Collects the main characteristic readings.

### `calculation(number_of_inputs, inlet_pressure, P1, P2, Speed, Hanger_weight, Spring_balance)`
Calculates the required performance metrics.

### `operating_table(net_wt, discharge, head, dh, out_power, in_power, efficiency)`
Displays the calculated values for operating characteristics.

### `main_table(net_wt, discharge, head, dh, out_power, in_power, unit_power, unit_speed, unit_discharge, efficiency)`
Displays the calculated values for main characteristics.

## Example Output
```
+----------------------+-----------+-----------+------------+---------------+---------------+----------------+
| Inlet Pressure Kg/cm2 |   P1 (m)  |   P2 (m)  | Speed (rpm) | Hanger Weight | Spring Balance | Vacuum Pressure |
+----------------------+-----------+-----------+------------+---------------+---------------+----------------+
|        1.2         |     2.4   |    1.8    |     1000    |       5       |       3       |      0.9       |
+----------------------+-----------+-----------+------------+---------------+---------------+----------------+
```
