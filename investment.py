shares = 10
price_per_share = 150

total_investment = shares * price_per_share

print("Number of Shares:", shares)
print("Price per Share: $", price_per_share)
print("Total Investment: $", total_investment)


new_share_price = 175
current_value = shares * new_share_price
profit_or_loss = current_value - total_investment
percentage_return = (profit_or_loss / total_investment) * 100

print("New Share Price: $", new_share_price)
print("Current Investment Value: $", current_value)
print("Profit or Loss: $", profit_or_loss)
print("Percentage Return:", round(percentage_return, 2), "%")