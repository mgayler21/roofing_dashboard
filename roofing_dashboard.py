import csv
import matplotlib.pyplot as plt


def load_jobs(filename="roofing_jobs.csv"):
    jobs = []

    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            job = {
                "customer": row["customer"],
                "job_type": row["job_type"],
                "revenue": float(row["revenue"]),
                "cost": float(row["cost"]),
                "month": row["month"]
            }
            jobs.append(job)

    return jobs


def calculate_dashboard(jobs):
    total_revenue = 0
    total_cost = 0
    total_profit = 0

    best_job = None
    worst_job = None
    monthly_profit = {}

    for job in jobs:
        profit = job["revenue"] - job["cost"]
        job["profit"] = profit

        total_revenue += job["revenue"]
        total_cost += job["cost"]
        total_profit += profit

        if best_job is None or job["profit"] > best_job["profit"]:
            best_job = job

        if worst_job is None or job["profit"] < worst_job["profit"]:
            worst_job = job

        month = job["month"]
        if month not in monthly_profit:
            monthly_profit[month] = 0

        monthly_profit[month] += profit

    return total_revenue, total_cost, total_profit, best_job, worst_job, monthly_profit


def print_dashboard(jobs):
    if len(jobs) == 0:
        print("\nNo jobs available.")
        return

    total_revenue, total_cost, total_profit, best_job, worst_job, monthly_profit = calculate_dashboard(jobs)

    print("\n=== Roofing Sales Dashboard ===")
    print(f"Total Jobs: {len(jobs)}")
    print(f"Total Revenue: ${total_revenue:,.2f}")
    print(f"Total Cost: ${total_cost:,.2f}")
    print(f"Total Profit: ${total_profit:,.2f}")
    print(f"Average Profit Per Job: ${total_profit / len(jobs):,.2f}")

    print("\n=== Best Job ===")
    print(f"Customer: {best_job['customer']}")
    print(f"Job Type: {best_job['job_type']}")
    print(f"Profit: ${best_job['profit']:,.2f}")

    print("\n=== Worst Job ===")
    print(f"Customer: {worst_job['customer']}")
    print(f"Job Type: {worst_job['job_type']}")
    print(f"Profit: ${worst_job['profit']:,.2f}")

    print("\n=== Monthly Profit Totals ===")
    for month, profit in monthly_profit.items():
        print(f"{month}: ${profit:,.2f}")


def view_all_jobs(jobs):
    if len(jobs) == 0:
        print("\nNo jobs available.")
        return

    print("\n=== All Roofing Jobs ===")
    for i, job in enumerate(jobs, start=1):
        profit = job["revenue"] - job["cost"]
        print(f"\nJob #{i}")
        print(f"Customer: {job['customer']}")
        print(f"Job Type: {job['job_type']}")
        print(f"Revenue: ${job['revenue']:,.2f}")
        print(f"Cost: ${job['cost']:,.2f}")
        print(f"Profit: ${profit:,.2f}")
        print(f"Month: {job['month']}")


def add_job(jobs):
    print("\n=== Add New Job ===")

    customer = input("Customer name: ")
    job_type = input("Job type: ")
    revenue = float(input("Revenue: "))
    cost = float(input("Cost: "))
    month = input("Month (YYYY-MM): ")

    new_job = {
        "customer": customer,
        "job_type": job_type,
        "revenue": revenue,
        "cost": cost,
        "month": month
    }

    jobs.append(new_job)
    print("\nJob added successfully.")


def export_report(jobs, filename="roofing_jobs_report.csv"):
    if len(jobs) == 0:
        print("\nNo jobs to export.")
        return

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Customer", "Job Type", "Revenue", "Cost", "Profit", "Month"])

        for job in jobs:
            profit = job["revenue"] - job["cost"]
            writer.writerow([
                job["customer"],
                job["job_type"],
                job["revenue"],
                job["cost"],
                profit,
                job["month"]
            ])

    print(f"\nReport exported to {filename}")


def plot_monthly_profit(jobs):
    if len(jobs) == 0:
        print("\nNo jobs available.")
        return

    _, _, _, _, _, monthly_profit = calculate_dashboard(jobs)

    months = list(monthly_profit.keys())
    profits = list(monthly_profit.values())

    plt.figure(figsize=(8, 5))
    plt.bar(months, profits)
    plt.title("Monthly Roofing Profit")
    plt.xlabel("Month")
    plt.ylabel("Profit")
    plt.tight_layout()
    plt.show()


def save_jobs(jobs, filename="roofing_jobs.csv"):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["customer", "job_type", "revenue", "cost", "month"])

        for job in jobs:
            writer.writerow([
                job["customer"],
                job["job_type"],
                job["revenue"],
                job["cost"],
                job["month"]
            ])


def main():
    jobs = load_jobs()

    while True:
        print("\n=== Roofing Analytics Menu ===")
        print("1) View Dashboard")
        print("2) View All Jobs")
        print("3) Add Job")
        print("4) Export Report")
        print("5) Show Monthly Chart")
        print("6) Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print_dashboard(jobs)

        elif choice == "2":
            view_all_jobs(jobs)

        elif choice == "3":
            add_job(jobs)
            save_jobs(jobs)

        elif choice == "4":
            export_report(jobs)

        elif choice == "5":
            plot_monthly_profit(jobs)

        elif choice == "6":
            print("\nGoodbye.")
            break

        else:
            print("\nInvalid choice. Please select 1-6.")


main()
