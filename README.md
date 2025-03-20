# Exchange Ticker Collector Powered by Polygon.io

A utility project for retrieving and maintaining up-to-date stock ticker lists from major exchanges (NYSE and NASDAQ) for the [Alpha is Now Powered by AI](https://alpha.isnow.ai) trading strategy platform.

## Overview

This project facilitates quick access to ticker symbols for strategies running in the iSnow.ai worker environment. It maintains JSON files containing organized lists of tickers by exchange and type, which are regularly updated through CI to account for market changes (delistings, new listings, etc.).

## Features

- Collects tickers from NYSE (XNYS) and NASDAQ (XNAS) exchanges
- Categorizes securities by type (common stocks, ETFs)
- Generates structured JSON files for easy consumption
- Updates quarterly via CI to maintain accuracy

## Setup

### Requirements

- Python 3.12+
- A Polygon.io API key

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/polygon-get-exchange-ticker.git
   cd polygon-get-exchange-ticker
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file with your Polygon.io API key:
   ```
   POLYGON_API_KEY=your_api_key_here
   ```

## Usage

Run the main script to collect ticker information:

```
python get_ticker_list_by_exchange.py
```

This will generate:
- `exchange_tickers.json` - Tickers organized by exchange
- `tickers_with_type.json` - Tickers mapped to their security types

For getting detailed ticker data including ETFs and common stocks:

```
python betting_against_beta.py
```

This generates:
- `nyse_nasdaq_tickers.json` - All tickers with detailed information
- `nyse_nasdaq_tickers_etf.json` - List of ETF tickers
- `nyse_nasdaq_tickers_cs.json` - List of common stock tickers

## Maintenance

The ticker data is automatically updated quarterly through CI workflows to ensure it reflects current market listings.

## License

This project is licensed under the MIT License. See the [MIT](https://opensource.org/licenses/MIT) file for details.

## Contributing

Contributions to improve the project are welcome. Please feel free to submit a pull request or open an issue.
