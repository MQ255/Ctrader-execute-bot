import random

def get_ai_signal():
    direction = random.choice(["BUY", "SELL"])
    return {
        "symbol": "BTCUSD",         # زوج التداول
        "signal": direction,        # اتجاه الصفقة
        "lot_size": 0.03,           # حجم اللوت
        "stop_loss": 20,            # وقف الخسارة بالنقاط
        "take_profit": 40           # الهدف بالنقاط
    }
