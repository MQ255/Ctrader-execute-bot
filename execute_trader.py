def place_order(symbol, side, volume, sl_pips, tp_pips):
    print(f"تنفيذ صفقة: {side} على {symbol} بلوت {volume}, وقف خسارة: {sl_pips}, هدف: {tp_pips}")
    return "✅ تم التنفيذ بنجاح"
