import requests
import random
import time

# إعدادات التليجرام
TOKEN = "8067398934:AAGaxKaM0nr85x7YEM6Mu9B7TFuvCDS1h04"
CHAT_ID = "171691712"

# جلب السعر الحالي من Binance للذهب
def get_gold_price():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=XAUUSDT"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return float(response.json()['price'])
    except Exception as e:
        print("❌ خطأ في جلب السعر:", e)
        return None

# توليد توصية سكالبينغ وهمية (بيع أو شراء)
def generate_signal():
    return random.choice(["BUY", "SELL"])

# إرسال التوصية إلى تليجرام
def send_signal_to_telegram(signal, price):
    sl = price - 3 if signal == "BUY" else price + 3
    tp1 = price + 2 if signal == "BUY" else price - 2
    tp2 = price + 4 if signal == "BUY" else price - 4
    tp3 = price + 6 if signal == "BUY" else price - 6

    msg = f"📡 توصية سكالبينغ على الذهب XAUUSD\n\n" \
          f"📊 نوع الصفقة: {signal}\n" \
          f"💰 سعر الدخول: {price:.2f}\n" \
          f"🎯 TP1: {tp1:.2f}\n" \
          f"🎯 TP2: {tp2:.2f}\n" \
          f"🎯 TP3: {tp3:.2f}\n" \
          f"⛔️ SL: {sl:.2f}"

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": msg
    }

    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()
        print("✅ تم إرسال التوصية بنجاح.")
    except Exception as e:
        print("❌ خطأ في إرسال التوصية:", e)

# تشغيل النظام
def main():
    price = get_gold_price()
    if price:
        signal = generate_signal()
        send_signal_to_telegram(signal, price)

if __name__ == "__main__":
    main()
