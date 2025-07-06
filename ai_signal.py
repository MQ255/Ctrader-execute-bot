import random

def generate_ai_signal():
    direction = random.choice(["BUY", "SELL"])
    return {
        "symbol": "BTCUSD",
        "direction": direction,
        "volume": 0.03,
        "sl_pips": 20,
        "tp_pips": 40
    }
