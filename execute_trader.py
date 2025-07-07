# execute_trader.py

import requests

ACCESS_TOKEN = "aeb_Sz7NOg_dGtjwV9hfEf2jazhk10kGPKyApuXmE5w"
ACCOUNT_ID = "5217824"

def place_order(symbol, direction, volume, tp_pips, sl_pips):
    url = f"https://live.ctraderapi.com/v1/accounts/{ACCOUNT_ID}/orders/market"
    
    data = {
        "symbol": symbol,
        "volume": int(volume * 100000),
        "side": "BUY" if direction == "BUY" else "SELL",
        "takeProfitInPips": tp_pips,
        "stopLossInPips": sl_pips
    }

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=data, headers=headers)
    print("Order response:", response.text)
