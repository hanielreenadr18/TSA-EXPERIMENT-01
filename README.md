# Experiment 01 – Plot a Time Series Data

## NAME: HANIEL REENA D R
## REGISTER NO: 2305001008

## Aim

To develop Python programs to plot and visualize time-series data such as population, commodity market price, or temperature using Pandas and Matplotlib.

## Software Requirements

- Python 3
- Pandas
- Matplotlib

## Algorithm

1. Start the program.
2. Import the required libraries, Pandas and Matplotlib.
3. Create the time-series data using Year or Month and the corresponding values.
4. Store the data in a Pandas DataFrame.
5. Select the time column and value column.
6. Plot the data using a line graph.
7. Add a suitable title and labels for the X-axis and Y-axis.
8. Display the graph.
9. Observe the graph and identify the trend.
10. Stop the program.

---

## Programs

### 1. Plot annual population for 2015–2025

**Program:**

```python
import pandas as pd
import matplotlib.pyplot as plt

year = list(range(2015, 2026))
population = [90, 93, 96, 98, 100, 103, 106, 110, 114, 118, 123]

data = pd.DataFrame({
    "Year": year,
    "Population": population
})

print(data)

plt.plot(data["Year"], data["Population"], marker="o")
plt.title("Annual Population 2015–2025")
plt.xlabel("Year")
plt.ylabel("Population (Millions)")
plt.grid(True)
plt.tight_layout()
plt.show()
```

**Output:**

<img width="2400" height="1500" alt="image" src="https://github.com/user-attachments/assets/07b99adc-573c-421a-b0e5-d07ee9d68dc7" />


**Observation:** The time series shows an increasing trend.

---

### 2. Plot monthly temperature for 12 months

**Program:**

```python
import pandas as pd
import matplotlib.pyplot as plt

month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
         "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
temperature = [25, 27, 30, 33, 35, 34, 32, 31, 30, 29, 27, 25]

data = pd.DataFrame({
    "Month": month,
    "Temperature": temperature
})

print(data)

plt.plot(data["Month"], data["Temperature"], marker="o")
plt.title("Monthly Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.tight_layout()
plt.show()
```

**Output:**

<img width="2400" height="1500" alt="image" src="https://github.com/user-attachments/assets/cdb840e9-739b-4248-9b3a-c7ea0876f6ea" />


**Observation:** The time series shows a seasonal pattern.

---

### 3. Plot monthly commodity price for 12 months

**Program:**

```python
import pandas as pd
import matplotlib.pyplot as plt

month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
         "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
price = [4200, 4350, 4280, 4500, 4650, 4800,
         4700, 4900, 5000, 5150, 5250, 5400]

data = pd.DataFrame({
    "Month": month,
    "Price": price
})

print(data)

plt.plot(data["Month"], data["Price"], marker="o")
plt.title("Monthly Commodity Market Price")
plt.xlabel("Month")
plt.ylabel("Price")
plt.grid(True)
plt.tight_layout()
plt.show()
```

**Output:**

<img width="2400" height="1500" alt="image" src="https://github.com/user-attachments/assets/49d9a068-a330-4dfb-a46d-a878603da15e" />


**Observation:** The time series shows an increasing trend.

---

## Installation

Install the required libraries using:

```bash
pip install -r requirements.txt
```

## Result

Thus, the given time-series data were successfully plotted using Python, Pandas, and Matplotlib, and the trends were identified.
