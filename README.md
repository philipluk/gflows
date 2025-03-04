# G|Flows

G|Flows, or Greek Flows, provides 15-minute updates for the SPX, NDX, and RUT indexes every Monday-Friday from 9:00am-4:30pm ET.

## Features

### Measure by date & strike price:

- Delta, gamma, vanna, and charm exposure for stocks/indexes
- Implied volatility (IV) average

### Expirations to choose:

- All expirations
- Current month
- Current monthly OPEX
- 0DTE, if available, otherwise the closest expiration

### Guide:

- Need a refresh? View the meaning behind each greek and how their flows can be interpreted

## Setup

Compatible with Python versions **>=3.9**

Install the app's required packages:

```{.sourceCode .bash}
$ pip install -r requirements.txt
```

(Recommended) To keep the package installation local/within a virtual environment, run these before the `pip` command:

```{.sourceCode .bash}
$ python -m venv venv
$ source venv/bin/activate
```

### Configuration:

Create a .env file in the project's working directory to configure the app, otherwise the app will use default values:

```dosini
# For downloading options data. If not set, the app defaults to a CBOE API — see ticker_dwn for info
API_URL=YOURAPIURL
# Auto-respond to prompt 'Download recent data? (y/n).' If not set, user input is requested
AUTO_RESPONSE=y
# Default. Choose tickers from https://finance.yahoo.com/lookup (excluding futures)
TICKERS=^SPX,^NDX,^RUT
```

`my_app.py`:

G|Flows uses a scheduler to periodically redownload options data. To disable it, comment out this code

```
"""
# schedule when to redownload data
sched = BackgroundScheduler(daemon=True)
sched.add_job(
    sensor,
    CronTrigger.from_crontab(
        "0,15,30,45 9-15 * * 0-4", timezone=timezone("America/New_York")
    ),
)
sched.add_job(
    sensor,
    CronTrigger.from_crontab(
        "0,15,30 16 * * 0-4", timezone=timezone("America/New_York")
    ),
)
sched.start()
"""
```

To analyze CSV data, change the **is_json** value to **False** within the **analyze_data** function

```
def analyze_data(ticker, expir):
    # Analyze stored data of specified ticker and expiry
    # defaults: json format, timezone 'America/New_York'
    result = get_options_data(
        ticker,
        expir,
        is_json=True,  # False for CSV
        tz="America/New_York",
    )
    ...
```

For manual updates, CSV-formatted options data can be downloaded [here](https://www.cboe.com/delayed_quotes/cboe/quote_table) then placed in the `data/csv` directory

---

Upon completion, run the Dash app (available at http://localhost:8050):

```{.sourceCode .bash}
$ python my_app.py
```
