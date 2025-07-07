import random
import requests
import json
import time

# بيانات الحساب
ACCESS_TOKEN = "nChAqN5ZNQzd7BsSPKZLW8xXWONFJVhAzPH6LxmJF6c"
ACCOUNT_ID = "5217824"
SYMBOL = "XAUUSD"
VOLUME = 0.03  # 0.03 لكل 100 دولار (كما هو محدد)

# توليد توصية AI تلقائية (BUY / SELL)
def generate_ai_signal():
    return random.choice(["BUY", "SELL"])

# تنفيذ الصفقة على cTrader
def execute_order(direction):
    url = f"https://api.spotware.com/connect/trading-api/rest/order"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    # تحديد الجهة الرقمية للشراء أو البيع
    trade_side = "BUY" if direction == "BUY" else "SELL"

    # إعداد بيانات الصفقة
    data = {
        "accountId": ACCOUNT_ID,
        "symbolName": SYMBOL,
        "orderType": "MARKET",
        "tradeSide": trade_side,
        "volume": int(VOLUME * 100000),  # تحويل اللوت إلى وحدات
        "stopLossInPips": 20,
        "takeProfitInPips": 40
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        print("✅ تم تنفيذ الصفقة بنجاح.")
    else:
        print("❌ فشل تنفيذ الصفقة:", response.text)

# --- نقطة البداية ---
if __name__ == "__main__":
    signal = generate_ai_signal()
    print(f"🔍 توصية الذكاء الاصطناعي: {signal}")
    execute_order(signal)
