import pandas as pd
import matplotlib.pyplot as plt

# Monthly commodity market price data
month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
         "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
price = [4200, 4350, 4280, 4500, 4650, 4800,
         4700, 4900, 5000, 5150, 5250, 5400]

data = pd.DataFrame({"Month": month, "Price": price})
print(data)

plt.plot(data["Month"], data["Price"], marker="o")
plt.title("Monthly Commodity Market Price")
plt.xlabel("Month")
plt.ylabel("Price")
plt.grid(True)
plt.tight_layout()
plt.savefig("output/commodity_price_graph.png", dpi=300)
plt.show()
