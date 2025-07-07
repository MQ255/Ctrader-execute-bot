# ai_signal.py

def generate_ai_signal():
    # توليد توصية عشوائية للتجربة
    import random
    direction = random.choice(["BUY", "SELL"])
    
    return {
        "symbol": "BTCUSD",
        "direction": direction,
        "tp_pips": 40,
        "sl_pips": 20,
        "volume": 0.03
    }
