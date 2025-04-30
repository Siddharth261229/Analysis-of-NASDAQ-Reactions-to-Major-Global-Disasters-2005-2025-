# Analysis-of-NASDAQ-Reactions-to-Major-Global-Disasters-2005-2025-
This project investigates how the **NASDAQ Composite Index (^IXIC)** responded to major global disasters over the past two decades. It applies an **event study methodology** to compute **abnormal returns** and **cumulative abnormal returns (CAR)** for each event.
---

## 📌 Objective

To quantitatively analyze how the NASDAQ deviated from expected performance in response to:

- Natural disasters (hurricanes, earthquakes, pandemics)
- Terrorist attacks
- Geopolitical crises (wars, referendums)

---

## 🧪 Methodology

### Event Study Framework

For each event:
1. **Estimate Expected Return**  
   Using a **market model**:  
   \[
   \mathbb{E}[R_{\text{NASDAQ}}] = \alpha + \beta \cdot R_{\text{S&P 500}}
   \]  
   where α and β are obtained via linear regression over a **1-year estimation window** ending 30 days before the event.

2. **Compute Abnormal Return (AR)**  
   \[
   AR_t = R_{\text{NASDAQ}, t} - \mathbb{E}[R_{\text{NASDAQ}, t}]
   \]

3. **Compute Cumulative Abnormal Return (CAR)**  
   Summed over an event window of ±30 trading days.

---

## 🗓️ Global Disaster Events Analyzed

| Event                             | Date         | Category             |
|----------------------------------|--------------|----------------------|
| Hurricane Katrina                | 2005-08-29   | Natural Disaster     |
| 7/7 London Bombings              | 2005-07-07   | Terrorist Attack     |
| Mumbai Attacks                   | 2008-11-26   | Terrorist Attack     |
| H1N1 Pandemic                    | 2009-06-11   | Health Crisis        |
| Haiti Earthquake                 | 2010-01-12   | Natural Disaster     |
| Eyjafjallajökull Eruption        | 2010-04-14   | Natural Disaster     |
| Japan Earthquake & Tsunami      | 2011-03-11   | Natural Disaster     |
| Hurricane Sandy                  | 2012-10-29   | Natural Disaster     |
| Boston Marathon Bombing          | 2013-04-15   | Terrorist Attack     |
| Ebola Outbreak Declared PHEIC    | 2014-08-08   | Health Crisis        |
| Paris Terror Attacks             | 2015-11-13   | Terrorist Attack     |
| Brexit Referendum                | 2016-06-23   | Geopolitical Shock   |
| COVID-19 Pandemic Declared       | 2020-03-11   | Health Crisis        |
| Russia–Ukraine War Begins        | 2022-02-24   | Geopolitical Crisis  |

---

## 🧰 Tools & Libraries

- **Python 3.9+**
- `yfinance` – for stock data retrieval
- `pandas` – for data manipulation
- `numpy` – for numerical operations
- `matplotlib`, `seaborn` – for visualization
- `statsmodels` – for linear regression

---

## 📊 Outputs

- **Cumulative Abnormal Return (CAR) Plots** for each event.


---

## 📊 Interpretation of Results (from CAR Plot)

The CAR plot (Figure 1) reveals several important market patterns in response to global disasters:

### ✅ 1. **Severe Global Crises Cause Deep Market Reactions**
- The **COVID-19 pandemic** led to the **largest negative CAR** in the dataset, with the market sharply declining in the first few weeks. This reflects panic selling and extreme uncertainty during global lockdowns.
- The **Russia–Ukraine War** also triggered a clear negative CAR, though recovery was faster, suggesting markets adjusted expectations once initial fears were priced in.

### 🌐 2. **Geopolitical Events Have Varied Impact**
- The **Brexit referendum** caused a brief but sharp dip in CAR, recovering slightly as markets adapted.
- **Terrorist attacks** such as the **Paris Attacks** and **Mumbai Attacks** showed **short-term declines**, but **relatively fast recoveries**, suggesting that unless economic infrastructure is affected, markets are resilient to isolated acts of violence.

### 🌊 3. **Natural Disasters Affect Markets Selectively**
- Events like **Hurricane Katrina**, **Haiti Earthquake**, and the **Japan Earthquake/Tsunami** showed moderate negative CARs, especially when infrastructure damage was significant.
- However, **Eyjafjallajökull** (volcano eruption) and **Hurricane Sandy** had **limited long-term effects**, likely because their impacts were regional and temporary.

### 🦠 4. **Health Crises Show Unique Patterns**
- The **H1N1 pandemic** and **Ebola outbreak** resulted in **slightly negative to neutral CARs**, indicating that markets didn’t perceive them as threats to the global economic system—unlike COVID-19.
- COVID-19 was a **systemic shock** due to global interconnectivity and lockdowns, while earlier health crises were more localized.

### 🔁 5. **Recovery Time Differs by Event Type**
- **Pandemics and wars** tend to have **longer recovery arcs**.
- **Terror attacks** and **volcanic/natural events** tend to show **quick rebounds**, implying short-lived shocks.

---

## 🧰 Tools & Libraries Used

- `yfinance` for historical market data
- `pandas`, `numpy` for data wrangling
- `matplotlib`, `seaborn` for visualization
- `statsmodels` for regression modeling

---



## 📌 Key Takeaways

- The NASDAQ reacts **rationally yet sensitively** to systemic global events.
- **Crisis severity, geographic scope, and economic relevance** determine the depth and duration of market impact.
- Event studies like this provide quantitative tools for **risk analysis**, **policy guidance**, and **portfolio stress testing**.

---

## 📬 Contact

Developed by **Siddharth Shekhawat** as part of an academic project on event-driven financial analytics.  
For queries or collaborations: `sidshekhawat26@gmail.com` (replace with actual address).
