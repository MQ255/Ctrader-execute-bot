import requests

ACCESS_TOKEN = "nChAqN5ZNQzd7BsSPKZLW8xXWONFJVhAzPH6LxmJF6c"
ACCOUNT_ID = 5217824
SYMBOL = "XAUUSD"
LOT_SIZE_PER_100 = 0.03
BALANCE = 659.92
STOP_LOSS_PIPS = 20
TAKE_PROFIT_PIPS = 40

def get_current_price():
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    url = f"https://api.ctrader.com/connect/trading-accounts/{ACCOUNT_ID}/symbols/{SYMBOL}"

    response = requests.get(url, headers=headers)

    if response.status_code == 200 and response.text.strip():
        try:
            data = response.json()
            bid = float(data["symbol"]["bid"])
            ask = float(data["symbol"]["ask"])
            return bid, ask
        except Exception as e:
            raise Exception(f"❌ فشل في قراءة السعر من JSON: {str(e)}")
    else:
        raise Exception(f"❌ فشل الحصول على السعر. Status Code: {response.status_code}, Response: {response.text}")

def execute_trade(signal):
    try:
        bid, ask = get_current_price()
        entry_price = ask if signal == "BUY" else bid
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

        order_url = "https://api.ctrader.com/connect/trading-api/rest/order"
        response = requests.post(order_url, json=order_data, headers=headers)

        if response.status_code == 200:
            print("✅ تم تنفيذ الصفقة بنجاح.")
        else:
            print("❌ فشل تنفيذ الصفقة:", response.status_code, response.text)

    except Exception as e:
        print("⚠️ خطأ أثناء تنفيذ الصفقة:", str(e))
