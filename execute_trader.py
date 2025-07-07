import requests

ACCESS_TOKEN = "aeb_Sz7NOg_dGtjwV9hfEf2jazhk10kGPKyApuXmE5w"
ACCOUNT_ID = "5217824"

def place_order(symbol, side, volume, sl_pips, tp_pips):
    url = "https://api.spotware.com/connect/trading/orders"
    
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    data = {
        "accountId": ACCOUNT_ID,
        "symbol": symbol,
        "orderType": "MARKET",
        "side": side,
        "volume": volume,
        "stopLoss": sl_pips,
        "takeProfit": tp_pips
    }

    response = requests.post(url, json=data, headers=headers)
    return response.json()
