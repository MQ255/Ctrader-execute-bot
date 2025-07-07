import requests

ACCESS_TOKEN = "aeb_Sz7NOg_dGtjwV9hfEf2jazhk10kGPKyApuXmE5w"
ACCOUNT_ID = "5217824"

def place_order(symbol, direction, volume, tp_pips, sl_pips):
    url = "https://api.spotware.com/connect/trading/accounts/{}/orders/market".format(ACCOUNT_ID)
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    data = {
        "symbol": symbol,
        "direction": direction,
        "volume": volume,
        "tp_pips": tp_pips,
        "sl_pips": sl_pips
    }

    response = requests.post(url, headers=headers, json=data)
    print("Order Response:", response.text)
