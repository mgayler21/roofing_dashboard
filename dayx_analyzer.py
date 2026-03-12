def load_jobs():
    jobs = []

    FILENAME = "jobs_clean.txt"
    with open(FILENAME, "r") as file:
        for line in file:
            name, profit = line.strip().split(",")
            jobs.append((name, float(profit)))

    return jobs


from datetime import datetime

def show_stats(jobs):
    total = sum(job[1] for job in jobs)
    average = total / len(jobs)

    best = max(jobs, key=lambda x: x[1])
    worst = min(jobs, key=lambda x: x[1])

    lines = []
    lines.append("=== Roofing Job Stats ===")
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"Total Jobs: {len(jobs)}")
    lines.append(f"Total Profit: ${total:,.2f}")
    lines.append(f"Average Profit: ${average:,.2f}")
    lines.append("")
    lines.append(f"Best Job: {best[0]} - ${best[1]:,.2f}")
    lines.append(f"Worst Job: {worst[0]} - ${worst[1]:,.2f}")
     # Sort jobs by profit (highest first)
    sorted_jobs = sorted(jobs, key=lambda x: x[1], reverse=True)

    lines.append("")
    lines.append("Top 3 Jobs:")

    for i, job in enumerate(sorted_jobs[:3], start=1):
        lines.append(f"{i}. {job[0]} - ${job[1]:,.2f}")
        
    # Print to terminal
    print("\n" + "\n".join(lines))

    # Save to report.txt
    with open("report.txt", "w") as f:
        f.write("\n".join(lines) + "\n")

    print("\nSaved report to: report.txt")
    

def main():
    jobs = load_jobs()
    show_stats(jobs)

if __name__ == "__main__":
    main()
