import pandas as pd
import matplotlib.pyplot as plt

confirmed = pd.read_csv(r"D:\PYTHONCLASS\Projects\finalproject\time_series_covid19_confirmed_global.csv")
recovered = pd.read_csv(r"D:\PYTHONCLASS\Projects\finalproject\time_series_covid19_recovered_global.csv")
deaths = pd.read_csv(r"D:\PYTHONCLASS\Projects\finalproject\time_series_covid19_deaths_global.csv")

confirmed_global = confirmed.iloc[:, 4:].sum()
recovered_global = recovered.iloc[:, 4:].sum()
deaths_global = deaths.iloc[:, 4:].sum()

print("1. Global COVID-19 Spread Over Time")
print("2. Trends: Confirmed vs Recovered")
print("3. Deaths Comparison Across Countries")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    confirmed_global.plot(kind='line', figsize=(10,5), title="Global COVID-19 Spread")
    plt.xlabel("Date")
    plt.ylabel("Confirmed Cases")
    plt.show()

elif choice == 2:
    df = pd.DataFrame({
        "Confirmed": confirmed_global,
        "Recovered": recovered_global
    })
    df.plot(kind='line', figsize=(10,5), title="Confirmed vs Recovered")
    plt.xlabel("Date")
    plt.ylabel("Cases")
    plt.show()

elif choice == 3:
    country_deaths = deaths.groupby("Country/Region").sum().iloc[:, 4:].iloc[:, -1]
    top10 = country_deaths.sort_values(ascending=False).head(10)
    top10.plot(kind='bar', figsize=(10,5), title="Top 10 Countries by Deaths")
    plt.xlabel("Country")
    plt.ylabel("Deaths(in millions)")
    plt.show()

else:
    print("Invalid choice")