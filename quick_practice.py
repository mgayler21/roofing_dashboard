name = input("Customer's name: ")
profit = float(input("Profit Amount: "))

if profit > 15000:
    rate = 0.12
elif profit < 5000:
    rate = 0.08
else:
    rate = 0.10

commission = profit * rate

print("\n----- Summary -----")
print(f"Name: {name}")
print(f"Profit: ${profit:,.2f}")
print(f"Commission Rate: {int(rate*100)}%")
print(f"Commission: ${commission:,.2f}")

if commission > 2000:
    print("🔥 Big job! Great close.")