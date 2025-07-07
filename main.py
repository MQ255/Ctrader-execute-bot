from ai_signal import generate_ai_signal
from execute_trader import place_order
import requests

BOT_TOKEN = "8067398934:AAGvw2oAS-0Y5zgDD-1QUI8EbZppWJIb_NQ"
CHAT_ID = "5956821181"

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

def main():
    signal = generate_ai_signal()
    msg = f"""
🎯 توصية سكالبينغ تلقائية 🔥

📊 الزوج: {signal['symbol']}
🔁 الإتجاه: {signal['direction']}
📈 الهدف: {signal['tp_pips']} نقطة
📉 وقف الخسارة: {signal['sl_pips']} نقطة
💰 الحجم: {signal['volume']} لوت
    """

    send_telegram(msg)

    place_order(
        signal['symbol'],
        signal['direction'],
        signal['volume'],
        signal['tp_pips'],
        signal['sl_pips']
    )

if __name__ == "__main__":
    main()
