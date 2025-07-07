import random

def generate_ai_signal():
    symbol = "BTCUSD"
    direction = random.choice(["BUY", "SELL"])
    tp_pips = 40
    sl_pips = 20
    volume = 0.03

    return {
        "symbol": symbol,
        "direction": direction,
        "tp_pips": tp_pips,
        "sl_pips": sl_pips,
        "volume": volume
    }
