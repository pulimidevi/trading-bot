import random
import logging

# setup logging
logging.basicConfig(
    filename="trading_bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

symbol = input("Enter symbol (BTCUSDT): ")
side = input("Enter side (BUY/SELL): ")
order_type = input("Enter type (MARKET/LIMIT): ")
quantity = float(input("Enter quantity: "))

price = None
if order_type == "LIMIT":
    price = float(input("Enter price: "))

try:
    order = {
        "orderId": random.randint(100000, 999999),
        "status": "FILLED" if order_type == "MARKET" else "NEW",
        "executedQty": quantity,
        "avgPrice": price if price else "market price"
    }

    # log request + response
    logging.info(f"Request: {symbol}, {side}, {order_type}, {quantity}, {price}")
    logging.info(f"Response: {order}")

    print("\n✅ SUCCESS (Simulated)")
    print("Order ID:", order["orderId"])
    print("Status:", order["status"])
    print("Executed Qty:", order["executedQty"])
    print("Avg Price:", order["avgPrice"])

except Exception as e:
    logging.error(str(e))
    print("\n❌ ERROR:", str(e))