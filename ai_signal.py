import random

def generate_signal():
    # توليد توصية عشوائية لغرض الاختبار (BUY أو SELL)
    return random.choice(["BUY", "SELL"])
