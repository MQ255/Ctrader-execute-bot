import requests

# بيانات الاتصال مع Spotware Open API
ACCESS_TOKEN = "nChAqN5ZNQzd7BsSPKZLW8xXWONFJVhAzPH6LxmJF6c"
ACCOUNT_ID = 5217824
SYMBOL = "XAUUSD"
LOT_SIZE_PER_100 = 0.03
BALANCE = 659.92  # الرصيد الحالي
STOP_LOSS_PIPS = 20
TAKE_PROFIT_PIPS = 40

def get_current_price():
    url = f"https://api.spotware.com/connect/trading-accounts/{ACCOUNT_ID}/orders"
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    symbol_url = f"https://api.spotware.com/connect/trading-accounts/{ACCOUNT_ID}/symbols/{SYMBOL}"
    response = requests.get(symbol_url, headers=headers)
    data = response.json()
    return float(data["symbol"]["bid"]), float(data["symbol"]["ask"])

def execute_trade(signal):
    try:
        price_bid, price_ask = get_current_price()
        entry_price = price_ask if signal == "BUY" else price_bid
        volume = int((LOT_SIZE_PER_100 * (BALANCE / 100)) * 100000)

        sl_price = entry_price - STOP_LOSS_PIPS * 0.1 if signal == "BUY" else entry_price + STOP_LOSS_PIPS * 0.1
        tp_price = entry_price + TAKE_PROFIT_PIPS * 0.1 if signal == "BUY" else entry_price - TAKE_PROFIT_PIPS * 0.1

        order_data = {
            "accountId": ACCOUNT_ID,
            "symbolName": SYMBOL,
            "orderType": "MARKET",
            "tradeSide": signal,
            "volume": volume,
            "stopLoss": round(sl_price, 2),
            "takeProfit": round(tp_price, 2),
        }

        headers = {
            "Authorization": f"Bearer {ACCESS_TOKEN}",
            "Content-Type": "application/json"
        }

        response = requests.post("https://api.spotware.com/connect/trading-api/rest/order",
                                 json=order_data, headers=headers)

        if response.status_code == 200:
            print("✅ تم تنفيذ الصفقة بنجاح.")
        else:
            print("❌ فشل تنفيذ الصفقة:", response.text)

    except Exception as e:
        print("⚠️ خطأ أثناء تنفيذ الصفقة:", str(e))
