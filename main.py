from ai_signal import generate_ai_signal
from execute_trader import place_order
import requests

BOT_TOKEN = "8067398934:AAGvw2oAS-0Y5zgDD-..."
CHAT_ID = "5956821181"

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

def main():
    signal = generate_ai_signal()
    msg = f"""🔥 توصية سكالبينغ تلقائية 🧠

📘 الزوج: {signal['symbol']}
📘 الإتجاه: {signal['direction']}
📘 نقطة الهدف: {signal['tp_pips']}
📘 وقف الخسارة: {signal['sl_pips']}
📘 حجم اللوت: {signal['volume']}

🚀 تنفيذ مباشر الآن..
"""
    send_telegram(msg)

    result = place_order(
        symbol=signal['symbol'],
        side=signal['direction'],
        volume=signal['volume'],
        sl_pips=signal['sl_pips'],
        tp_pips=signal['tp_pips']
    )

    send_telegram(f"تنفيذ الصفقة ✅: {result}")

if __name__ == "__main__":
    main()
