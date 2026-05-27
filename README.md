# 🔍 Log Analyzer v2

An advanced Python-based log analysis tool designed to simulate real-world SOC analyst workflows.

---

## 🚀 Features

- 🔐 Detects failed login attempts by IP
- 🎯 Identifies targeted usernames (root, admin, guest)
- ⚠️ Flags suspicious brute force activity
- 📊 Categorizes attack severity (HIGH / LOW)
- 📁 Generates structured JSON reports
- 💻 Clean terminal-based output

---

## 🧠 Use Case

This tool simulates real-world cybersecurity tasks:

- Auditing authentication logs
- Detecting brute force attacks
- Identifying suspicious login behavior
- Supporting incident response analysis

---

## 🛠️ Technologies Used

- Python 3
- Kali Linux
- Log Parsing Techniques

---

## ▶️ How to Run

```bash
python3 log_analyzer_v2.py

📊 Sample Output

LOG ANALYSIS REPORT

Failed Login Attempts by IP:
192.168.1.10 → 4 attempts (HIGH)
192.168.1.20 → 1 attempts (LOW)

Targeted Usernames:
root → 3 attempts
admin → 1 attempt
guest → 1 attempt

Suspicious Activity:
Possible brute force from 192.168.1.10

📁 Output File
report.json (structured SIEM-style output)

## 📸 Demo Output

![Log Analyzer Output](log_output.png)

👨‍💻 Author

Tinashe Zacariah Nyandoro
Cybersecurity Analyst (Entry-Level)

🔗 Connect with me
GitHub: https://github.com/ZacariahCyberSec
