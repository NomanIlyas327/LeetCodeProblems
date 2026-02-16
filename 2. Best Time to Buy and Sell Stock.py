def max_profit(prices):
   min_price = float('inf')
   max_profit = 0
   for price in prices:
    if price < min_price:
        min_price = price
    elif price - min_price > max_profit:
        max_profit = price - min_price

   return max_profit
   
stock_prices = [20 , 18, 14, 17, 22, 25]
profit = max_profit(stock_prices)
print(f"Maximum profit from stock prices: {profit}")
