from execute_trader import place_order

def main():
    result = place_order(
        symbol="BTCUSD",
        direction="BUY",
        volume=0.03,
        sl=20,
        tp=40
    )
    print(result)

if __name__ == "__main__":
    main()
