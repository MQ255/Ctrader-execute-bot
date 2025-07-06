from ai_signal import get_ai_signal
from execute_trader import place_order
import requests

BOT_TOKEN = "8067398934:AAGvw2oAS-0Y5zgDD-1QUI8EbZppWJIb_NQ"
CHAT_ID = "5956821181"

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

def main():
    signal = get_ai_signal()
    msg = f"""📡 توصية سكالبينغ تلقائية 🔥

🔹 الزوج: {signal['symbol']}
🔹 الاتجاه: {signal['signal']}
🔹 الهدف: {signal['take_profit']} نقطة
🔹 وقف الخسارة: {signal['stop_loss']} نقطة
🔹 الحجم: {signal['lot_size']} لوت

🚀 تنفيذ مباشر الآن...
"""
    send_telegram(msg)
    result = place_order(
        symbol=signal['symbol'],
        side=signal['signal'],
        volume=signal['lot_size'],
        sl_pips=signal['stop_loss'],
        tp_pips=signal['take_profit']
    )
    send_telegram(f"✅ تنفيذ الصفقة: {result}")

if __name__ == "__main__":
    main()
