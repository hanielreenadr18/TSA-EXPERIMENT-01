import pandas as pd
import matplotlib.pyplot as plt

# Annual population data (2015–2025), in millions
year = list(range(2015, 2026))
population = [90, 93, 96, 98, 100, 103, 106, 110, 114, 118, 123]

data = pd.DataFrame({"Year": year, "Population": population})
print(data)

plt.plot(data["Year"], data["Population"], marker="o")
plt.title("Annual Population 2015–2025")
plt.xlabel("Year")
plt.ylabel("Population (Millions)")
plt.grid(True)
plt.tight_layout()
plt.savefig("output/population_graph.png", dpi=300)
plt.show()
