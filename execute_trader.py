import requests

ACCESS_TOKEN = "aeb_Sz7NOg_dGtjwV9hfEf2jazhk10kGPKyApuXmE5w"
ACCOUNT_ID = 5217824
API_URL = "https://api.ctrader.com/connect/trading-api/rest/order"  # ✅ عدل حسب عنوان Spotware الرسمي الصحيح

def place_order(symbol, direction, volume, tp_pips, sl_pips):
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    # مثال افتراضي: تحويل الاتجاه إلى نوع أمر
    order_type = "BUY" if direction == "BUY" else "SELL"

    payload = {
        "accountId": ACCOUNT_ID,
        "symbol": symbol,
        "orderType": order_type,
        "volume": volume,
        "takeProfit": tp_pips,
        "stopLoss": sl_pips
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()

        print("✅ Order placed successfully:", response.json())
    except requests.exceptions.RequestException as e:
        print("❌ Order failed:", e)
        print("Response content:", response.text)
