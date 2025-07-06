import requests

ACCESS_TOKEN = "aeb_Sz7NOg_dGtjwV9hfEf2jazhk10kGPKyApuXmE5w"
ACCOUNT_ID = "5217824"

def place_order(symbol, side, volume, sl_pips, tp_pips):
    base_url = "https://api.spotware.com/connect/trading"
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}

    market_price_url = f"https://api.spotware.com/connect/prices?symbolName={symbol}&accountId={ACCOUNT_ID}"
    price_res = requests.get(market_price_url, headers=headers).json()
    price = float(price_res["ask"]) if side == "BUY" else float(price_res["bid"])

    sl = price - sl_pips * 0.0001 if side == "BUY" else price + sl_pips * 0.0001
    tp = price + tp_pips * 0.0001 if side == "BUY" else price - tp_pips * 0.0001

    order_data = {
        "accountId": ACCOUNT_ID,
        "symbolName": symbol,
        "orderType": "MARKET",
        "side": side,
        "volume": int(volume * 100000),
        "takeProfit": {"price": round(tp, 5)},
        "stopLoss": {"price": round(sl, 5)}
    }

    res = requests.post(base_url, headers=headers, json=order_data)
    return res.json()
