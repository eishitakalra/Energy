import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("B7Plot.csv")
print(df.head())  # Show the first few rows
print(df.dtypes) 
df["CO2_Limit"] = pd.to_numeric(df["CO2_Limit"], errors="coerce")
df["AP_g"] = pd.to_numeric(df["AP_g"], errors="coerce")
plt.show(block=True) 
df["Generator"] = df["Generator"].str.strip()
print(df["Generator"].unique())  # List all generators
gen = df["Generator"].unique()[0]  # Pick the first generator
gen_data = df[df["Generator"] == gen]

plt.plot(gen_data["CO2_Limit"], gen_data["AP_g"], marker="o", linestyle="-", label=gen)
plt.xlabel("CO₂ Limit (Tonnes per hour)")
plt.ylabel("Average Power Output (MW)")
plt.title(f"AP_g vs CO₂ Limit for {gen}")
plt.legend()
plt.grid()
plt.show()
# Plot for each generator
plt.figure(figsize=(8, 5))
for gen in df["Generator"].unique():
    gen_data = df[df["Generator"] == gen]
    plt.plot(gen_data["CO2_Limit"], gen_data["AP_g"], marker="o", linestyle="-", label=gen)

# Formatting
plt.xlabel("CO₂ Limit (Tonnes per hour)")
plt.ylabel("Average Power Output (MW)")
plt.title("AP_g(g) vs CO₂ Limit for Each Generator")
plt.legend()
plt.grid()
plt.show()

plt.ion()  # Enable interactive mode
plt.show()
