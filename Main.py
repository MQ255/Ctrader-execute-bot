import requests
import random

# بيانات الاتصال الخاصة بك
BOT_TOKEN = "8067398934:AAGvw2oAS-0Y5zgDD-1QUI8EbZppWJIb_NQ"
CHAT_ID = "5956821181"
SPOTWARE_ACCESS_TOKEN = "aeb_Sz7NOg_dGtjwV9hfEf2jazhk10kGPKyApuXmE5w"
ACCOUNT_ID = "5217824"

# توليد توصية BUY أو SELL عشوائية لغرض الاختبار فقط
signal = random.choice(["BUY", "SELL"])
symbol = "BTCUSD"

# إعداد نقاط الهدف والستوب
entry_price = 0  # سيتم الحصول عليه من API
pip_size = 0.01  # حسب نوع الرمز
tp_pips = 40
sl_pips = 20
lot_size = 0.03  # لكل 100$

# جلب السعر الحقيقي من Spotware
def get_symbol_price():
    url = f"https://api.spotware.com/connect/trading/accounts/{ACCOUNT_ID}/symbols/{symbol}/price"
    headers = {
        "Authorization": f"Bearer {SPOTWARE_ACCESS_TOKEN}"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return float(data["ask"]) if signal == "BUY" else float(data["bid"])

# تنفيذ الصفقة
def execute_trade():
    global entry_price
    entry_price = get_symbol_price()
    sl = entry_price - sl_pips * pip_size if signal == "BUY" else entry_price + sl_pips * pip_size
    tp = entry_price + tp_pips * pip_size if signal == "BUY" else entry_price - tp_pips * pip_size

    payload = {
        "accountId": ACCOUNT_ID,
        "symbol": symbol,
        "type": "MARKET",
        "side": signal,
        "volume": int(lot_size * 100000),  # حسب حجم اللوت
        "stopLoss": round(sl, 2),
        "takeProfit": round(tp, 2),
        "label": "AI Scalping Bot"
    }

    url = "https://api.spotware.com/connect/trading/orders"
    headers = {
        "Authorization": f"Bearer {SPOTWARE_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

# إرسال التوصية إلى Telegram
def send_telegram_signal(entry, sl, tp):
    message = f"🚨 توصية سكالبينغ تلقائية:\n\nزوج: {symbol}\nاتجاه: {signal}\nسعر الدخول: {entry}\nالهدف 🎯: {tp}\nوقف الخسارة ❌: {sl}"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message
    }
    requests.post(url, data=data)

# تنفيذ العملية
if __name__ == "__main__":
    result = execute_trade()
    if "errorCode" not in result:
        send_telegram_signal(entry_price, result["stopLoss"], result["takeProfit"])
    else:
        print("فشل تنفيذ الصفقة:", result)
