import pandas as pd

data = pd.read_csv("countries_by_area.txt")
data["density"] = data["population_2013"] / data["area_sqkm"]
data = data.sort_values(by="density", ascending=False)

for _, row in data[:5].iterrows():
    print(row["country"])
