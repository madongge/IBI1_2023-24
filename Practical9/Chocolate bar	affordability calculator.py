def calculate_chocolate_bars(total_money, price_per_bar):
    num_bars = total_money // price_per_bar
    change = total_money % price_per_bar
    return num_bars, change

# Example
total_money = 100
price_per_bar = 7
bars, change = calculate_chocolate_bars(total_money, price_per_bar)
print(f"With {total_money} money, you can buy {bars} chocolate bars and have {change} left over.")
