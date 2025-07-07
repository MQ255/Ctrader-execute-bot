import requests

ACCESS_TOKEN = "nChAqN5ZNQzd7BsSPKZLW8xXWONFJVhAzPH6LxmJF6c"
ACCOUNT_ID = "5217824"

SYMBOL = "XAUUSD"
VOLUME = 3000  # حجم 0.03
SL_PIPS = 20
TP_PIPS = 40

def get_market_price():
    # سعر تجريبي لأن cTrader API لا توفر سعر مباشر عبر HTTP (يُستبدل لاحقًا بـ WebSocket)
    return 2350.00

def execute_order(signal):
    price = get_market_price()
    sl = price - SL_PIPS * 0.1 if signal == "BUY" else price + SL_PIPS * 0.1
    tp = price + TP_PIPS * 0.1 if signal == "BUY" else price - TP_PIPS * 0.1
    side = "BUY" if signal == "BUY" else "SELL"

    url = f"https://api.spotware.com/connect/open-api/v1/accounts/{ACCOUNT_ID}/orders"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "accountId": ACCOUNT_ID,
        "symbol": SYMBOL,
        "volume": VOLUME,
        "side": side,
        "type": "MARKET",
        "stopLoss": round(sl, 2),
        "takeProfit": round(tp, 2)
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print("✅ تم تنفيذ الصفقة بنجاح")
    else:
        print(f"❌ فشل تنفيذ الصفقة: {response.text}")
