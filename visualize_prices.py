import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Nat_Gas.csv")
df.columns = ["date", "price"]
df["date"] = pd.to_datetime(df["date"])

plt.figure(figsize=(10, 5))
plt.plot(df["date"], df["price"], marker="o")
plt.title("Monthly Natural Gas Prices")
plt.xlabel("Date")
plt.ylabel("Price")
plt.grid(True)
plt.show()
