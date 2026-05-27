import re
import json
from collections import defaultdict

log_file = "sample.log"

failed_attempts_ip = defaultdict(int)
failed_attempts_user = defaultdict(int)
successful_logins = []

# Read log file
with open(log_file, "r") as file:
    for line in file:

        # Failed login detection
        if "Failed password" in line:
            ip_match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)
            user_match = re.search(r'for (\w+)', line)

            if ip_match:
                ip = ip_match.group(1)
                failed_attempts_ip[ip] += 1

            if user_match:
                user = user_match.group(1)
                failed_attempts_user[user] += 1

        # Successful login detection
        if "Accepted password" in line:
            successful_logins.append(line.strip())

# Severity function
def get_severity(count):
    if count >= 4:
        return "HIGH 🔥"
    elif count == 3:
        return "MEDIUM ⚠️"
    else:
        return "LOW"

# Print report
print("\n🔍 LOG ANALYSIS REPORT\n")

print("🚨 Failed Login Attempts by IP:")
for ip, count in failed_attempts_ip.items():
    print(f"{ip} → {count} attempts ({get_severity(count)})")

print("\n👤 Targeted Usernames:")
for user, count in failed_attempts_user.items():
    print(f"{user} → {count} attempts")

print("\n✅ Successful Logins:")
for login in successful_logins:
    print(login)

print("\n⚠️ Suspicious Activity:")
suspicious = {}
for ip, count in failed_attempts_ip.items():
    if count >= 3:
        print(f"🔥 Possible brute force from {ip} ({count} attempts)")
        suspicious[ip] = count

# Export JSON report
report = {
    "failed_attempts_by_ip": dict(failed_attempts_ip),
    "failed_attempts_by_user": dict(failed_attempts_user),
    "successful_logins": successful_logins,
    "suspicious_ips": suspicious
}

with open("report.json", "w") as json_file:
    json.dump(report, json_file, indent=4)

print("\n📁 JSON report saved as report.json")
