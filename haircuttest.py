hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

for num in prices:
  total_price += num
price_num = len(prices)
average_price = total_price / price_num
print("Average Haircut Price: " + str(average_price))
new_prices = [x - 5 for x in prices]
print(new_prices)
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i]*last_week[i]
print("Total Revenue: " + str(total_revenue))
money_made = sum(x * y for x, y in zip(prices, last_week))
print(money_made)