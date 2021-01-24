from binance.client import Client
import time
print("Введите ваш публичный API-ключ: ")
api_key = input()
print("Введите ваш приватный API-ключ: ")
api_secret = input()
print("Введите актив для трейдинга: ")
trading_asset = input()
print("Введите объём актива для трейдинга")
trading_value = input()
client = Client(api_key, api_secret)
while True:
    buy_order_limit = client.create_order(
        symbol=trading_asset,
        side='BUY',
        type='MARKET',
        quantity=trading_value)
    print(buy_order_limit)
    time.sleep(300)
    sell_order_limit = client.create_order(
        symbol=trading_asset,
        side='SELL',
        type='MARKET',
        quantity=trading_value)
    print(sell_order_limit)
    time.sleep(3600)
