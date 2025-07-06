import random

def get_ai_signal():
    signal = random.choice(["BUY", "SELL"])
    return {
        "symbol": "BTCUSD",
        "signal": signal,
        "lot_size": 0.03,
        "take_profit": 40,
        "stop_loss": 20
    }
