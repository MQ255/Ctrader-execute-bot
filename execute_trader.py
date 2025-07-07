# execute_trader.py

import requests

ACCESS_TOKEN = "aeb_Sz7NOg_dGtjwV9hfEf2jazhk10kGPKyApuXmE5w"
ACCOUNT_ID = "5217824"

def place_order(signal):
    url = "https://live.ctraderapi.com/v1/accounts/{}/orders/market".format(ACCOUNT_ID)
    
    data = {
        "symbol": signal["symbol"],
        "volume": int(signal["volume"] * 100000),  # تحويل الحجم إلى وحدة السيرفر
        "side": "BUY" if signal["direction"] == "BUY" else "SELL",
        "takeProfitInPips": signal["tp_pips"],
        "stopLossInPips": signal["sl_pips"]
    }

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=data, headers=headers)
    print("Order response:", response.text)
