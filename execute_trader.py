import requests

ACCESS_TOKEN = "aeb_Sz7NOg_dGtjwV9hfEf2jazhk10kGPKyApuXmE5w"
ACCOUNT_ID = "5217824"

def place_order(symbol, direction, volume, tp_pips, sl_pips):
    url = "https://api.spotware.com/connect/trading/accounts/{}/orders".format(ACCOUNT_ID)
    
    side = "BUY" if direction == "BUY" else "SELL"

    order_data = {
        "accountId": int(ACCOUNT_ID),
        "symbolName": symbol,
        "orderType": "MARKET",
        "side": side,
        "volume": int(volume * 100000),  # حسب منصة cTrader
        "takeProfitInPips": tp_pips,
        "stopLossInPips": sl_pips
    }

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=order_data, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return f"❌ فشل في تنفيذ الصفقة: {response.status_code}, {response.text}"
