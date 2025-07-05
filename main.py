import requests
import random
import time

# توصية الذكاء الاصطناعي (BUY أو SELL)
ai_signal = random.choice(["BUY", "SELL"])

# معلومات الحساب
ACCOUNT_ID = "5217824"
ACCESS_TOKEN = "aeb_Sz7NOg_dGtjwV9hfEf2jazhk10kGPKyApuXmE5w"

# إعدادات الصفقة
SYMBOL = "BTCUSD"
VOLUME_PER_100 = 0.03  # 0.03 لوت لكل 100$
STOP_LOSS_PIPS = 20
TAKE_PROFIT_PIPS = 40

# احصل على سعر السوق الحالي من Spotware OpenAPI
def get_market_price():
    url = f"https://api.spotware.com/connect/trading/accounts/{ACCOUNT_ID}/symbols/{SYMBOL}/price"
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    response = requests.get(url, headers=headers)
    data = response.json()
    return float(data["ask"]) if ai_signal == "BUY" else float(data["bid"])

# تنفيذ الصفقة
def execute_trade():
    price = get_market_price()
    volume = int(100000 * VOLUME_PER_100)  # حجم اللوت

    sl = price - STOP_LOSS_PIPS * 0.1 if ai_signal == "BUY" else price + STOP_LOSS_PIPS * 0.1
    tp = price + TAKE_PROFIT_PIPS * 0.1 if ai_signal == "BUY" else price - TAKE_PROFIT_PIPS * 0.1

    order_data = {
        "accountId": ACCOUNT_ID,
        "symbol": SYMBOL,
        "volume": volume,
        "type": "MARKET",
        "side": ai_signal,
        "stopLoss": round(sl, 2),
        "takeProfit": round(tp, 2),
        "label": "AI Scalping Bot"
    }

    url = f"https://api.spotware.com/connect/trading/orders"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=order_data, headers=headers)
    print("تم إرسال الصفقة:", response.status_code, response.text)

# تشغيل البوت
print("توصية الذكاء الاصطناعي:", ai_signal)
execute_trade()
