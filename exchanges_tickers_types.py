import os
import json
from dotenv import load_dotenv
import polygon

load_dotenv()

POLYGON_API_KEY = os.getenv("POLYGON_API_KEY")
if not POLYGON_API_KEY:
    raise ValueError("POLYGON_API_KEY is not set")

exchanges = ["XNYS", "XNAS"]

EXCHANGE_TICKERS_FILE = "exchange_tickers.json"
TICKERS_WITH_TYPE_FILE = "tickers_with_type.json"

polygon_client = polygon.RESTClient(POLYGON_API_KEY)

# Get tickers by exchange
exchange_tickers, tickers_with_type = {}, {}
for exchange in exchanges:
    print(f"Processing {exchange} exchange...")
    exchange_tickers[exchange] = []
    tickers = list(
        polygon_client.list_tickers(
            active=True,
            market="stocks",
            limit=1000,
            exchange=exchange,
        )
    )
    [exchange_tickers[exchange].append(ticker.ticker) for ticker in tickers]
    print(f"Found {len(tickers)} tickers for {exchange}")


with open(EXCHANGE_TICKERS_FILE, "w") as f:
    json.dump(exchange_tickers, f)
print(f"Saving {len(exchange_tickers)} exchange tickers to {EXCHANGE_TICKERS_FILE} \n")

# Get tickers with type
types_tickers = {}

print("Getting tickers with type...\n")
for exchange, ticker_list in exchange_tickers.items():
    print(f"Processing tickers from {exchange}...")
    for ticker in ticker_list:
        ticker_details = polygon_client.get_ticker_details(ticker)
        ticker_type = ticker_details.type
        tickers_with_type[ticker] = ticker_type
        print(".", end="", flush=True)
        if types_tickers.get(ticker_type):
            types_tickers[ticker_type].append(ticker)
        else:
            types_tickers[ticker_type] = [ticker]
    print(f"\nCompleted {len(ticker_list)} tickers from {exchange}")

with open(TICKERS_WITH_TYPE_FILE, "w") as f:
    json.dump(tickers_with_type, f)
print(f"\nSaved {len(tickers_with_type)} tickers with type to {TICKERS_WITH_TYPE_FILE}")

for ticker_type, tickers in types_tickers.items():
    with open(f"{ticker_type}.json", "w") as f:
        json.dump(tickers, f)
    print(f"\nSaved {len(tickers)} tickers of type {ticker_type} to {ticker_type}.json")
