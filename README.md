# International Standard Atmosphere (ISA) Temperature Model

A Python-based simulation to calculate and visualize the temperature profile of Earth's atmosphere from sea level to the Mesopause (90km).

## 🌍 Project Overview
This project implements the International Standard Atmosphere (ISA) model. It uses specific lapse rates to calculate how temperature changes across different atmospheric layers, including the unique temperature inversion found in the Stratosphere.

## 🚀 Key Features
* **Multi-Layer Logic**: Accurately models the Troposphere, Stratosphere, and Mesosphere.
* **Data Visualization**: Generates a professional vertical profile plot using Matplotlib.
* **Interactive Element**: Allows users to input a specific altitude to see the exact temperature highlighted on the graph.
* **Precision Math**: Uses NumPy for high-resolution data generation.

## 📉 Atmospheric Layers Modeled
1. **Troposphere (0-11km)**: Standard cooling rate of -6.5°C/km.
2. **Stratosphere (11-47km)**: Includes the warming effect where temperatures rise to -2.5°C.
3. **Mesosphere (51-84.85km)**: Captures the drop toward the coldest part of the atmosphere.

## 🛠️ Tech Stack
* **Language**: Python
* **Libraries**: NumPy, Matplotlib

## 📊 Sample Result
Below is a visualization of the atmosphere with a test point at **45 km**:

![Atmosphere Graph](https://github.com/iamtanmay37/Atmospheric-Temp-Profile/blob/main/Graph.png)
