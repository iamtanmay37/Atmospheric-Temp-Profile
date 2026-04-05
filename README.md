# International Standard Atmosphere (ISA) Temperature Model

This Python project simulates the temperature variations in the Earth's atmosphere from sea level to the Mesopause (90km).

## 🌍 How it Works
The script uses standard lapse rates to calculate temperatures across different atmospheric layers:
* [cite_start]**Troposphere**: 0 - 11 km [cite: 12, 93]
* [cite_start]**Stratosphere**: 11 - 47 km (including the Ozone layer warming effect) [cite: 16, 24, 95, 99]
* [cite_start]**Mesosphere**: 51 - 84.85 km [cite: 32, 37, 103, 105]

## 📈 Visualization
The program generates a vertical profile plot and highlights a user-defined altitude with its specific coordinates.

![Temperature Graph](./your_graph_image.png)

## 🛠️ Tech Stack
* [cite_start]**Python** [cite: 2]
* [cite_start]**NumPy** (Numerical range generation) [cite: 7, 90]
* [cite_start]**Matplotlib** (Data visualization) [cite: 8, 91]
