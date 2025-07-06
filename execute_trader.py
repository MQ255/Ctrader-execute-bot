import requests
import json

# بيانات الحساب والتوكن
access_token = "aeb_Sz7NOg_dGtjwV9hfEf2jazhk10kGPKyApuXmE5w"
account_id = 5217824
symbol = "BTCUSD"

# رأس الطلب
headers = {
    "Authorization": f"Bearer {access_token}",
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# رابط سعر السوق من Spotware Open API (حسب معرف الحساب والمعرف الرمزي للسوق)
market_price_url = f"https://api.spotware.com/connect/trading/accounts/{account_id}/symbols/{symbol}/price"

# رابط تنفيذ الأمر
order_url = "https://api.spotware.com/connect/trading/accounts/{}/orders".format(account_id)


def place_order(direction: str, volume: float, stop_loss_pips: int, take_profit_pips: int):
    # احصل على السعر الحالي
    response = requests.get(market_price_url, headers=headers)

    if response.status_code == 200 and response.text.strip():
        price_res = response.json()
    else:
        raise ValueError(f"Invalid response from market price URL: {response.status_code}, content: {response.text}")

    bid = float(price_res["bid"])
    ask = float(price_res["ask"])
    price = ask if direction.upper() == "BUY" else bid

    # احسب SL و TP كنقاط
    point = 0.01  # على حسب الدقة (BTCUSD غالبًا 0.01 أو 0.1)
    sl = price - stop_loss_pips * point if direction.upper() == "BUY" else price + stop_loss_pips * point
    tp = price + take_profit_pips * point if direction.upper() == "BUY" else price - take_profit_pips * point

    payload = {
        "symbol": symbol,
        "volume": volume,
        "type": "MARKET",
        "direction": direction.upper(),
        "price": price,
        "stopLoss": round(sl, 2),
        "takeProfit": round(tp, 2)
    }

    response = requests.post(order_url, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError(f"Failed to place order: {response.status_code}, content: {response.text}")
