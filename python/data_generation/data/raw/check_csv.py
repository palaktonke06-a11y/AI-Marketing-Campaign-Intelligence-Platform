import pandas as pd

files = [
"customers.csv",
"products.csv",
"locations.csv",
"campaigns.csv",
"campaign_performance.csv",
"customer_journey.csv",
"transactions.csv"
]

path = "../data/raw/"

for f in files:
    df = pd.read_csv(path+f)
    print(f, df.columns.tolist())