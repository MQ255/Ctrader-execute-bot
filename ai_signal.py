import random

def generate_ai_signal():
    symbol = "BTCUSD"
    direction = random.choice(["BUY", "SELL"])
    volume = 0.03  # ثابت لكل 100$
    tp_pips = 40
    sl_pips = 20

    return {
        "symbol": symbol,
        "direction": direction,
        "volume": volume,
        "tp_pips": tp_pips,
        "sl_pips": sl_pips
    }
