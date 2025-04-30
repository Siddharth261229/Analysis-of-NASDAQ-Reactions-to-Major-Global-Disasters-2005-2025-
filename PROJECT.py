from fredapi import Fred
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from datetime import timedelta

# Initialize FRED
fred = Fred(api_key="6acc5c11cf0da04a7a72ec1ac8a0bd7e")  # Replace with your FRED API key

# Define date range
start_date = "2005-01-01"
end_date = "2024-12-31"

# Download NASDAQ 100 and S&P 500 data
nasdaq_df = fred.get_series('NASDAQCOM', start_date, end_date).to_frame(name='Close')
sp500_df = fred.get_series('SP500', start_date, end_date).to_frame(name='Close')

# Convert index to datetime and compute returns
nasdaq_df.index = pd.to_datetime(nasdaq_df.index)
sp500_df.index = pd.to_datetime(sp500_df.index)

nasdaq_df['Return'] = nasdaq_df['Close'].pct_change()
sp500_df['Return'] = sp500_df['Close'].pct_change()

# Drop NA values
nasdaq_df.dropna(inplace=True)
sp500_df.dropna(inplace=True)

events = [
    ("COVID-19 Pandemic", "2020-03-11"),
    ("Russia-Ukraine War", "2022-02-24"),
    ("Brexit Referendum", "2016-06-23"),
    ("US-China Trade War", "2018-03-22"),
    ("US 2016 Presidential Election", "2016-11-08"),
    ("US 2020 Presidential Election", "2020-11-03")
]

def compute_event_abnormal(event_date, window=10, est_days=60):
    ev_date = pd.to_datetime(event_date)
    
    est_end = ev_date - timedelta(days=5)
    est_start = est_end - timedelta(days=est_days)

    est_data = nasdaq_df.loc[est_start:est_end].join(
        sp500_df['Return'], how='inner', lsuffix='_nasdaq', rsuffix='_sp'
    ).dropna()
    
    if len(est_data) < 10:
        raise ValueError("Not enough data in estimation window.")

    # Linear regression
    X = sm.add_constant(est_data['Return_sp'])
    y = est_data['Return_nasdaq']
    res = sm.OLS(y, X).fit()
    alpha, beta = res.params.const, res.params.Return_sp

    # Event window
    window_start = ev_date - timedelta(days=window)
    window_end = ev_date + timedelta(days=window)

    win_data = nasdaq_df.loc[window_start:window_end].join(
        sp500_df['Return'], how='inner', lsuffix='_nasdaq', rsuffix='_sp'
    ).dropna()

    win_data['Expected'] = alpha + beta * win_data['Return_sp']
    win_data['Abnormal'] = win_data['Return_nasdaq'] - win_data['Expected']
    win_data['CAR'] = win_data['Abnormal'].cumsum()
    win_data['DaysFromEvent'] = (win_data.index - ev_date).days

    return win_data

event_results = {}
for name, date in events:
    try:
        event_results[name] = compute_event_abnormal(date)
        print(f"{name} processed.")
    except Exception as e:
        print(f"Skipping {name}: {e}")

selected = ["COVID-19 Pandemic", "Russia-Ukraine War", "Brexit Referendum", "US-China Trade War", 
            "US 2016 Presidential Election", "US 2020 Presidential Election"]

fig, axes = plt.subplots(len(selected), 1, figsize=(8, 3 * len(selected)), sharex=True)

for ax, name in zip(axes, selected):
    if name not in event_results:
        continue
    df = event_results[name]
    ax.plot(df['DaysFromEvent'], df['CAR'], marker='o')
    ax.axvline(0, color='red', linestyle='--', label='Event Date')
    ax.set_title(f"{name}: Cumulative Abnormal Return")
    ax.set_ylabel("CAR")
    ax.legend()

plt.xlabel("Days from event")
plt.tight_layout()
plt.show()

