jobs = [
    {"customer": "James K", "profit":4200},
    {"customer": "Mike L", "profit": 5100},
    {"customer": "Jennifer G", "profit": 2600},
    {"customer": "Chris T", "profit": 3800},
]

highest_profit = 0
top_customer = ""

for job in jobs:
    if job["profit"] > highest_profit:
        highest_profit = job["profit"]
        top_customer = job["customer"]

print(f"Top Job: {top_customer} with a profit of ${highest_profit:,.2f}")
print(f"Highest Profit: ${highest_profit:,.2f}")
