import requests
import random
from datetime import datetime

# بيانات البوت
TELEGRAM_TOKEN = '8067398934:AAGaxKaM0nr85x7YEM6Mu9B7TFuvCDS1h04'
TELEGRAM_CHAT_ID = '8067398934'

# رمز الذهب على Binance
SYMBOL = "XAUUSDT"

def get_price(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    response = requests.get(url)
    data = response.json()
    return float(data["price"])

def generate_ai_signal():
    return random.choice(["BUY", "SELL"])

def calculate_levels(entry_price, direction):
    point = 0.1
    sl = entry_price - 3 * point if direction == "BUY" else entry_price + 3 * point
    tp1 = entry_price + 2 * point if direction == "BUY" else entry_price - 2 * point
    tp2 = entry_price + 4 * point if direction == "BUY" else entry_price - 4 * point
    tp3 = entry_price + 6 * point if direction == "BUY" else entry_price - 6 * point
    return round(sl, 2), round(tp1, 2), round(tp2, 2), round(tp3, 2)

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    requests.post(url, data=data)

def run():
    price = get_price(SYMBOL)
    signal = generate_ai_signal()
    sl, tp1, tp2, tp3 = calculate_levels(price, signal)
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    msg = (
        f"توصية سكالبينغ على الذهب ({SYMBOL})\\n"
        f"نوع التوصية: {signal}\\n"
        f"سعر الدخول: {price}\\n"
        f"TP1: {tp1}\\nTP2: {tp2}\\nTP3: {tp3}\\n"
        f"SL: {sl}\\n"
        f"الوقت: {now}\\n"
        "#سكالبينغ #الذهب"
    )
    send_telegram(msg)

run()
