from ai_signal import get_ai_signal
from execute_trader import execute_trade

# 1. احصل على توصية الذكاء الاصطناعي (BUY أو SELL)
signal = get_ai_signal()
print(f"🔍 توصية الذكاء الاصطناعي: {signal}")

# 2. نفّذ الصفقة تلقائيًا
execute_trade(signal)
