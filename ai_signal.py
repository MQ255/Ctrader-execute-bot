import random

def get_ai_signal():
    # توليد إشارة عشوائية لغرض الاختبار (BUY أو SELL)
    return random.choice(["BUY", "SELL"])
