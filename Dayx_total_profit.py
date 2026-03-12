jobs = [
    {"customer": "James K", "profit": 10200},
    {"customer": "Mike L", "profit": 18700},
    {"customer": "JenniferG", "profit": 3200},
    {"customer": "Sarah M", "profit": 4500},
]

grand_total = 0

for job in jobs:
    grand_total += job["profit"]

number_of_jobs = len(jobs)
average_profit = grand_total / number_of_jobs

print(f"Total Profit: ${grand_total:,.2f}")
print(f"Total Jobs: {number_of_jobs}")
print(f"Average Profit: ${average_profit:,.2f}")
