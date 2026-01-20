import pandas as pd

# -----------------------------
# Load and prepare data
# -----------------------------
df = pd.read_csv("Nat_Gas.csv")

# Rename columns if needed (safe step)
df.columns = ["date", "price"]

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"], format="%m/%d/%y")

# Sort by date
df = df.sort_values("date").reset_index(drop=True)

# -----------------------------
# Create daily interpolation
# -----------------------------
daily_dates = pd.date_range(start=df["date"].min(), end=df["date"].max(), freq="D")

daily_df = pd.DataFrame({"date": daily_dates})

# Merge and interpolate
daily_df = daily_df.merge(df, on="date", how="left")
daily_df["price"] = daily_df["price"].interpolate(method="linear")

# -----------------------------
# Monthly seasonality pattern
# -----------------------------
daily_df["month"] = daily_df["date"].dt.month
monthly_avg = daily_df.groupby("month")["price"].mean()


# -----------------------------
# Price estimation function
# -----------------------------
def estimate_gas_price(input_date):
    """
    Takes a date (YYYY-MM-DD or datetime) and returns
    an estimated natural gas price.
    """

    input_date = pd.to_datetime(input_date)

    # If date exists in historical range
    if input_date <= daily_df["date"].max():
        return float(daily_df.loc[daily_df["date"] == input_date, "price"].values[0])

    # Future extrapolation (up to 1 year)
    last_price = daily_df["price"].iloc[-1]
    target_month = input_date.month

    seasonal_adjustment = monthly_avg[target_month] - monthly_avg.mean()

    return float(last_price + seasonal_adjustment)


# -----------------------------
# Example test
# -----------------------------
if __name__ == "__main__":
    print("Price on 2022-02-15:", estimate_gas_price("2022-02-15"))
    print("Price on 2025-01-10:", estimate_gas_price("2025-01-10"))
