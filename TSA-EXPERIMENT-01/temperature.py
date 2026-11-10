import pandas as pd
import matplotlib.pyplot as plt

# Monthly temperature data in degrees Celsius
month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
         "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
temperature = [25, 27, 30, 33, 35, 34, 32, 31, 30, 29, 27, 25]

data = pd.DataFrame({"Month": month, "Temperature": temperature})
print(data)

plt.plot(data["Month"], data["Temperature"], marker="o")
plt.title("Monthly Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.tight_layout()
plt.savefig("output/temperature_graph.png", dpi=300)
plt.show()
