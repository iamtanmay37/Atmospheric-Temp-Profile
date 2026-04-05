import numpy as np
import matplotlib.pyplot as plt

def get_temp(y):
    if 0 <= y <= 11:
        return 15 - 6.5 * y
    elif 11 < y <= 20:
        return -56.5
    elif 20 < y <= 32:
        return -56.5 + 1.0 * (y - 20)
    elif 32 < y <= 47:
        return -44.5 + 2.8 * (y - 32)
    elif 47 < y <= 51:
        return -2.5
    elif 51 < y <= 71:
        return -2.5 - 2.8 * (y - 51)
    elif 71 < y <= 84.85:
        return -58.5 - 2.0 * (y - 71)
    else:
        return -86.2

y_val = float(input("Enter height (km): "))
x_val = get_temp(y_val)

y_pts = np.linspace(0, 90, 500)
x_pts = [get_temp(i) for i in y_pts]

plt.figure(figsize=(6, 8))
plt.plot(x_pts, y_pts, color='blue')
plt.scatter(x_val, y_val, color='red', s=100, zorder=5)

plt.text(x_val + 2, y_val, f"({x_val:.1f}C, {y_val}km)", color='red', fontweight='bold')

plt.title("Temperature (x) vs Altitude (y)")
plt.xlabel("Temperature (°C)")
plt.ylabel("Altitude (km)")
plt.grid(True)
plt.show()

