from ai_signal import generate_signal
from execute_trader import execute_order

# توليد توصية الذكاء الاصطناعي (BUY أو SELL)
signal = generate_signal()
print(f"🔍 توصية الذكاء الاصطناعي: {signal}")

# تنفيذ الصفقة على cTrader
execute_order(signal)
