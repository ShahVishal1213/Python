import matplotlib.pyplot as plt

# Sample data
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
temperature = [22, 25, 24, 23, 26]

# Line plot
plt.figure(figsize=(10, 5))
plt.plot(days, temperature, marker='o', color='blue', label="Temp (°C)")
plt.title("Temperature Over the Week")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.legend()
plt.show()

# Bar Chart
plt.bar(days, temperature, color='orange')
plt.title("Bar Chart - Temperature")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.show()

# Histogram
plt.hist(temperature, bins=5, color='green', edgecolor='black')
plt.title("Histogram of Temperatures")
plt.xlabel("Temperature")
plt.ylabel("Frequency")
plt.show()