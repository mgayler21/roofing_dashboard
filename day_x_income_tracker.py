import csv

def export_csv():
    jobs = load_jobs()

    if not jobs:
        print("No jobs to export.")
        return

    filename = "jobs_export.csv"

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Client", "Description", "Amount"])  # header row

        for job in jobs:
            writer.writerow([job["name"], job["description"], job["amount"]])

    print(f"Exported {len(jobs)} jobs to {filename}")

from datetime import datetime


def add_job():
    name = input("Client name: ")
    description = input("Job description: ")
    amount_str = input("Job amount: ")

    cleaned = amount_str.replace("$", "").replace(",", "").strip()

    try:
        amount = float(cleaned)
    except ValueError:
        print("Invalid amount.")
        return

    today = datetime.now().strftime("%Y-%m-%d")

    with open("jobs.txt", "a") as file:
        file.write(f"{today}|{name}|{description}|{amount}\n")

    print(f"Job saved on {today}!")

def load_jobs():
    jobs = []

    try:
        with open("jobs.txt", "r") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                date, name, desc, amount = line.split("|")

                jobs.append({
                    "date": date,
                    "name": name,
                    "description": desc,
                    "amount": float(amount)
                })

    except FileNotFoundError:
        pass

    return jobs


def view_jobs():
    jobs = load_jobs()

    if not jobs:
        print("No jobs found.")
        return

    print("\n--- Jobs ---")

    for i, job in enumerate(jobs, start=1):
        print(
            f"{i}) {job['date']} | {job['name']} | "
            f"{job['description']} | ${job['amount']:,.2f}"
        )

def total_income():
    jobs = load_jobs()

    if not jobs:
        print("No jobs found yet.")
        return

    total = sum(job["amount"] for job in jobs)
    print(f"\nTotal income: ${total:,.2f}")


def best_job():
    jobs = load_jobs()

    if not jobs:
        print("No jobs found yet.")
        return

    top = max(jobs, key=lambda j: j["amount"])
    print("\n--- Best Job ---")
    print(f"{top['name']} - {top['description']} - ${top['amount']:,.2f}")

def save_jobs(jobs):
    with open("jobs.txt", "w") as file:
        for job in jobs:
            file.write(f"{job['name']}|{job['description']}|{job['amount']}\n")


def delete_job():
    jobs = load_jobs()

    if not jobs:
        print("No jobs to delete.")
        return

    # Show jobs with numbers
    print("\n--- Jobs ---")
    for i, job in enumerate(jobs, start=1):
        print(f"{i}) {job['name']} - {job['description']} - ${job['amount']:,.2f}")

    choice = input("Enter the job number to delete (or press Enter to cancel): ").strip()
    if choice == "":
        print("Cancelled.")
        return

    if not choice.isdigit():
        print("Please enter a valid number.")
        return

    idx = int(choice)
    if idx < 1 or idx > len(jobs):
        print("That number is out of range.")
        return

    removed = jobs.pop(idx - 1)
    save_jobs(jobs)

    print(f"Deleted: {removed['name']} - {removed['description']} - ${removed['amount']:,.2f}")

def monthly_report():
    jobs = load_jobs()

    if not jobs:
        print("No jobs found.")
        return

    report = {}

    for job in jobs:
        month = job["date"][:7]  # YYYY-MM

        if month not in report:
            report[month] = 0

        report[month] += job["amount"]

    print("\n--- Monthly Report ---")

    for month in sorted(report):
        print(f"{month}: ${report[month]:,.2f}")

def search_jobs():
    jobs = load_jobs()

    if not jobs:
        print("No jobs found.")
        return

    term = input("Search by client name or keyword: ").lower().strip()

    if not term:
        print("Search cancelled.")
        return

    matches = []

    for job in jobs:
        text = f"{job['name']} {job['description']}".lower()

        if term in text:
            matches.append(job)

    if not matches:
        print("No matching jobs found.")
        return

    print("\n--- Search Results ---")

    for i, job in enumerate(matches, start=1):
        print(
            f"{i}) {job['date']} | {job['name']} | "
            f"{job['description']} | ${job['amount']:,.2f}"
        )

from datetime import datetime, timedelta

def dashboard():
    jobs = load_jobs()

    if not jobs:
        print("No jobs found.")
        return

    total_jobs = len(jobs)
    total_income = sum(j["amount"] for j in jobs)
    avg_income = total_income / total_jobs

    best = max(jobs, key=lambda j: j["amount"])

    # Top 3 jobs
    top3 = sorted(jobs, key=lambda j: j["amount"], reverse=True)[:3]

    # Best month
    month_totals = {}
    for j in jobs:
        month = j["date"][:7]  # YYYY-MM
        month_totals[month] = month_totals.get(month, 0) + j["amount"]

    best_month = max(month_totals, key=month_totals.get)
    best_month_total = month_totals[best_month]

    # Last 30 days income
    cutoff = datetime.now() - timedelta(days=30)
    last30_total = 0

    for j in jobs:
        try:
            job_date = datetime.strptime(j["date"], "%Y-%m-%d")
            if job_date >= cutoff:
                last30_total += j["amount"]
        except ValueError:
            # Skip lines with bad dates (shouldn't happen if add_job uses today's date)
            pass
    
    print("\nTop 3 Jobs:")
    for i, j in enumerate(top3, start=1):
        print(f"{i}) {j['date']} | {j['name']} - {j['description']} - ${j['amount']:,.2f}")    

    print("\n=== Dashboard ===")
    print(f"Total Jobs: {total_jobs}")
    print(f"Total Income: ${total_income:,.2f}")
    print(f"Average Job: ${avg_income:,.2f}")
    print(f"Best Job: {best['name']} - {best['description']} - ${best['amount']:,.2f}")
    print(f"Best Month: {best_month} - ${best_month_total:,.2f}")
    print(f"Last 30 Days: ${last30_total:,.2f}")               

def main():
    while True:
        print("\n=== Income Tracker +++")
        print("1) Add Job")
        print("2) View Jobs")
        print("3) Total Income")
        print("4) Best Job")
        print("5) Exit")
        print("6) Delete Job") 
        print("7) Export to CSV")
        print("8) Monthly Report")
        print("9) Search Jobs")
        print("10) Dashboard")

        choice = input("Choose an option: ")

        if choice == "1":
            add_job()
        elif choice == "2":
            view_jobs()
        elif choice == "3":
            total_income()
        elif choice == "4":
            best_job()
        elif choice == "5":
            print("Goodbye!")
            break
        elif choice == "6":
            delete_job()   
        elif choice == "7":
            export_csv()   
        elif choice == "8":
            monthly_report()  
        elif choice == "9":
            search_jobs()  
        elif choice == "10":
            dashboard()          
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

                        