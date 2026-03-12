jobs = [
    {"customer": "James K", "profit": 1000},
    {"customer": "Sarah L", "profit": 7000},
    {"customer": "Mike M", "profit": 500},
    {"customer": "Jennifer G", "profit": 2000},
]

total_profit = 0
average_profit = 0

for job in jobs:
    total_profit += job["profit"]
    

number_of_jobs = len(jobs)
average_profit = total_profit / number_of_jobs

print(f"Total Profit: ${total_profit:,.2f}")
print(f"Total Jobs: {number_of_jobs}")
print(f"Average Profit: ${average_profit:,.2f}")
