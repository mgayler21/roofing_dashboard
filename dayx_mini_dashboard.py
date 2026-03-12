jobs = [
    {"customer": "James K", "profit": 4200},
    {"customer": "Mike L", "profit": 5100},
    {"customer": "Jennifer G", "profit": 2600},
    {"customer": "Chris T", "profit": 3800},
]

total_profit = 0
highest_profit = 0
top_customer = ""

for job in jobs:
    total_profit += job["profit"]

    if job["profit"] > highest_profit:
        highest_profit = job["profit"]
        top_customer = job["customer"]

number_of_jobs = len(jobs)
average_profit = total_profit / number_of_jobs

print("===RoofOps Summary===")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Number of Jobs: {number_of_jobs}")
print(f"Average Profit: ${average_profit:,.2f}")
print(f"Top Customer: {top_customer} (${highest_profit:,.2f})")